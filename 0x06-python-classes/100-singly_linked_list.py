#!/usr/bin/python3
"""Singly Linked List Implementation"""


class Node:
    """Node of a singly linked list.

    Attributes:
        data: The data stored in the node.
        next_node: Reference to the next node in the list.

    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """Singly linked list."""

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (
                current.next_node is not None
                and current.next_node.data < value
            ):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        result = []
        while self.head:
            result.append(str(self.head.data))
            self.head = self.head.next_node
        return '\n'.join(result)
