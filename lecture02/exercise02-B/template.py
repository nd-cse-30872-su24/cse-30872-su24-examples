#!/usr/bin/env python3

# Exericse 02-B: PBB-matched

import sys

# Functions

LEFT_PBB  = ('(', '[', '{')
RIGHT_PBB = (')', ']', '}')

def is_pbbmatched(s: str) -> bool:
    # TODO: Process string s using a stack to determine if the symbols are balanced 
    return False

# Main execution

def main():
    for line in sys.stdin:
        line   = line.rstrip()
        result = 'Yes' if is_pbbmatched(line) else 'No'
        print('{:>10}: {}'.format(line, result))

if __name__ == '__main__':
    main()
