#!/usr/bin/env python3

# Exericse 09-C: Binary Tree Height

from dataclasses import dataclass
from typing      import Optional
import collections

# Structures

@dataclass
class Node:
    value:  int
    left:   Optional['Node']
    right:  Optional['Node']

# Functions

def height_tree(root: Optional[Node]) -> int:
    ''' Use divide and conquer to compute the height of binary tree '''
    # Base Case: Invalid node

    # Divide and Conquer: Recursively solve left and right sub-trees

    # Combine: Take maximum sub-tree height and add 1
    return 0

# Main Execution

def main() -> None:
    # Create tree
    root = Node(7,
        Node(5,
                Node(3, Node(6, None, None), None),
                None),
        Node(4,
                None,
                Node(2, None, None),
    ))

    # Compute height of tree
    print(height_tree (root))

if __name__ == '__main__':
    main()
