#!/usr/bin/env python3
"""Validate a two-version source-time plan. Does not approve it or edit CapCut."""
import argparse
import json
from fractions import Fraction
from pathlib import Path


def validate(d):
    fps = Fraction(str(d['fps']))
    total = d['source_duration_frames']
    if fps <= 0 or type(total) is not int or total < 1:
        raise ValueError('Positive FPS and integer source_duration_frames are required')
    if not isinstance(d['source'], str) or not d['source'].strip():
        raise ValueError('source must be a non-empty path')
    def span(s):
        a, b = s['start_frame'], s['end_frame']
        if type(a) is not int or type(b) is not int or not 0 <= a < b <= total:
            raise ValueError(f'Invalid half-open source range: {a}–{b}')
        return a, b
    brand = span(d['brand_span'])
    versions = d['versions']
    if len(versions) != 2 or len({v['name'] for v in versions}) != 2:
        raise ValueError('Exactly two distinctly named versions are required')
    result = []
    for v in versions:
        segments = v['segments']
        if len(segments) < 3 or segments[0]['role'] != 'hook' or segments[1]['role'] != 'brand':
            raise ValueError('Each version must start with hook, then brand, then story')
        if span(segments[1]) != brand:
            raise ValueError('The second segment must preserve the entire brand-plus-English span')
        position = 0
        mapped = []
        for s in segments:
            a, b = span(s)
            if s['role'] not in {'hook', 'brand', 'body', 'payoff'}:
                raise ValueError('Unknown segment role')
            mapped.append({'role': s['role'], 'source_start_frame': a,
                           'source_end_frame': b, 'timeline_start_frame': position,
                           'duration_frames': b-a})
            position += b-a
        result.append({'name': v['name'], 'duration_seconds': float(position/fps), 'segments': mapped})
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('plan', type=Path)
    a = p.parse_args()
    try:
        result = validate(json.loads(a.plan.read_text(encoding='utf-8')))
    except (KeyError, TypeError, ValueError) as e:
        p.error(str(e))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print('Range validation only; approval and narrative quality must be checked separately.')


if __name__ == '__main__':
    main()
