#!/usr/bin/env python3
"""Install the bundled skill locally. Never overwrites an existing installation."""
import argparse
import shutil
from pathlib import Path

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--target', choices=['codex', 'claude'], default='codex',
               help='Choose Codex or local Claude Code; does not install into Claude web/Cowork')
p.add_argument('--dest', type=Path, help='Override parent skill directory')
a = p.parse_args()
src = Path(__file__).resolve().parent/'skills'/'viral-flow-capcut'
parent = a.dest or Path.home()/('.claude' if a.target == 'claude' else '.agents')/'skills'
dst = parent.expanduser()/'viral-flow-capcut'
if dst.exists() or dst.is_symlink():
    p.error(f'Already installed: {dst}. Back it up before replacing deliberately.')
if not (src/'SKILL.md').is_file():
    p.error('The distribution is incomplete: SKILL.md is missing')
dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copytree(src, dst)
print(f'Installed: {dst}')
if a.target == 'claude':
    print('Start a new local Claude Code session and invoke /viral-flow-capcut.')
else:
    print('Start a new Codex turn and invoke $viral-flow-capcut. Restart Codex if needed.')
print('This installs instructions/helpers only, not CapCut, Whisper, or computer-control permissions.')
