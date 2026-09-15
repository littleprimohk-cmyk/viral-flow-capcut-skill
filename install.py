#!/usr/bin/env python3
"""Install the bundled skill locally. Never overwrites an existing installation."""
import argparse
import shutil
from pathlib import Path

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--dest', type=Path, default=Path.home()/'.agents'/'skills',
               help='Parent skill directory; default follows current Codex local-skill docs')
a = p.parse_args()
src = Path(__file__).resolve().parent/'skills'/'viral-flow-capcut'
dst = a.dest.expanduser()/'viral-flow-capcut'
if dst.exists() or dst.is_symlink():
    p.error(f'Already installed: {dst}. Back it up before replacing deliberately.')
if not (src/'SKILL.md').is_file():
    p.error('The distribution is incomplete: SKILL.md is missing')
dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copytree(src, dst)
print(f'Installed: {dst}')
print('Start a new Codex turn and invoke $viral-flow-capcut. Restart Codex if it does not appear.')
print('This installs instructions/helpers only, not CapCut, Whisper, or computer-control permissions.')
