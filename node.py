#! /usr/bin/env python3

import sys


class Node(object):
    instance_count = 0

    def __init__(self, data, left=None, right=None):
        Node.instance_count += 1
        self.data = data
        self.left = left
        self.right = right
        self.id = Node.instance_count


def insert_node(node, data):
    if not(node):
        return Node(data)

    else:
        if data <= node.data:
            node.left = insert_node(node.left, data)

        else:
            node.right = insert_node(node.right, data)

    return node


def lookup(node, target):
    if not(node):
        return False

    else:
        if target == node.data:
            return True
        elif target < node.data:
            return lookup(node.left, target)
        else:
            return lookup(node.right, target)


if len(sys.argv) < 2:
    sys.exit(1)

tree = Node(int(sys.argv[1]))

for val in sys.argv[2:]:
    insert_node(tree, int(val))

for val in sys.argv[1:]:
    print(lookup(tree, int(val)))


def print_postorder(root_node):

    if root_node.left:
        print_postorder(root_node.left)

    if root_node.right:
        print_postorder(root_node.right)

    print(root_node.id, root_node.data)

    return


def print_inorder(root_node):

    if root_node.left:
        print_inorder(root_node.left)

    print(root_node.id, root_node.data)

    if root_node.right:
        print_inorder(root_node.right)

    return


def print_preorder(root_node):

    print(root_node.id, root_node.data)

    if root_node.left:
        print_preorder(root_node.left)

    if root_node.right:
        print_preorder(root_node.right)

    return


print("preoder")
print_preorder(tree)
print("inorder")
print_inorder(tree)
print("postoder")
print_postorder(tree)