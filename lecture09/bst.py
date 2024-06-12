#!/usr/bin/env python3

from dataclasses import dataclass
from typing      import Optional

import sys

# Classes

@dataclass
class Node:
    value:  int
    left:   Optional['Node'] = None
    right:  Optional['Node'] = None

@dataclass
class Tree:
    root:   Node = None

    def search(self, value):                # Discuss: Search
        return self.search_r(self.root, value)

    def search_r(self, node, value):        # Discuss: Recursive helper
        if node is None:
            return False

        if value == node.value:
            return True

        if value <= node.value:
            return self.search_r(node.left, value)
        else:
            return self.search_r(node.right, value)

    def insert(self, value):                # Discuss: Insertion
        self.root = self.insert_r(self.root, value)

    def insert_r(self, node, value):
        if node is None:
            return Node(value)

        if value <= node.value:
            node.left  = self.insert_r(node.left, value)
        else:
            node.right = self.insert_r(node.right, value)

        return node

    def print(self):                        # Discuss: Traversal
        self.print_r(self.root)

    def print_r(self, node):                # Discuss: In-Order Traversal
        if not node:
            return

        self.print_r(node.left)
        print(node.value)
        self.print_r(node.right)

    def nodes(self):                        # Review: Generators
        yield from self.nodes_r(self.root)

    def nodes_r(self, node):
        if not node:
            return
            
        yield from self.nodes_r(node.left)
        yield node.value
        yield from self.nodes_r(node.right)

# Main Execution

def main():
    tree = Tree()
    for number in map(int, sys.argv[1:]):
        tree.insert(number)

    for number in map(int, sys.argv[1:]):
        print(number, tree.search(number))
        print(2*number, tree.search(number*2))

    tree.print()
    print(', '.join(map(str, tree.nodes())))

if __name__ == '__main__':
    main()
