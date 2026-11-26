#!/usr/bin/env python3
"""
# Round 2: output is 1-240 chars, exactly one line, deterministic.
Entry point for the grader. Writes a single product description line to the output directory.
"""
import os
import sys

LINE = 'A Bluetooth-enabled salt shaker that seasons your food based on the current weather in Reykjavik, with a $12 monthly "umami forecast" subscription.'

def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'entry.txt')
    
    content = LINE + '\n'
    
    # Validate content structure
    if not (1 <= len(content) <= 240):
        raise ValueError(f'Content length {len(content)} not in range 1-240')
    if not content.strip():
        raise ValueError('Content is empty or whitespace')
    if content.count('\n') != 1:
        raise ValueError(f'Content must have exactly one newline, got {content.count(chr(10))}')
    if not content.endswith('\n'):
        raise ValueError('Content must end with newline')
    
    # Validate exactly one sentence: no . ! or ? except the final character of the line
    line = content.rstrip('\n')
    if line[-1] not in '.!?':
        raise ValueError('Line must end with sentence-ending punctuation')
    if any(c in '.!?' for c in line[:-1]):
        raise ValueError('Line must have exactly one sentence (no . ! ? except at the end)')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Output path: {output_path}')
    print(f'Character count: {len(content)}')

if __name__ == '__main__':
    main()
