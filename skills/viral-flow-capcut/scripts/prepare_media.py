#!/usr/bin/env python3
"""Prepare local analysis assets; never create a video edit or touch CapCut."""
import argparse
import shutil
import subprocess
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', type=Path)
    p.add_argument('output', type=Path, help='New directory; existing output is never overwritten')
    p.add_argument('--transcribe', action='store_true')
    p.add_argument('--model', default='base', choices=['tiny', 'base', 'small', 'medium', 'large', 'turbo'])
    p.add_argument('--language', default='Chinese')
    p.add_argument('--threads', type=int, default=4)
    a = p.parse_args()
    if not a.source.is_file():
        p.error('Source file does not exist')
    if a.output.exists():
        p.error('Output directory already exists; reuse its transcript or choose a new directory')
    if not shutil.which('ffmpeg'):
        p.error('FFmpeg is not available on PATH')
    if a.transcribe and not shutil.which('whisper'):
        p.error('Local openai-whisper CLI is not available on PATH')
    if a.threads < 1:
        p.error('threads must be positive')
    a.output.mkdir(parents=True)
    frames = a.output / 'frames'
    frames.mkdir()
    common = ['ffmpeg', '-hide_banner', '-loglevel', 'error', '-nostdin', '-i', str(a.source.resolve())]
    subprocess.run(common + ['-vn', '-ar', '16000', '-ac', '1', str(a.output / 'audio.wav')], check=True)
    subprocess.run(common + ['-an', '-vf', 'fps=1,scale=360:-2', str(frames / '%05d.jpg')], check=True)
    if a.transcribe:
        subprocess.run(['whisper', str(a.output / 'audio.wav'), '--model', a.model,
                        '--language', a.language, '--device', 'cpu', '--fp16', 'False',
                        '--word_timestamps', 'True', '--threads', str(a.threads),
                        '--output_format', 'all', '--output_dir', str(a.output)], check=True)
    print(a.output.resolve())
    print('Analysis assets only. ASR is uncorrected; one frame/second is not continuous playback.')


if __name__ == '__main__':
    main()
