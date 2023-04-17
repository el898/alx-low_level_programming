#!/usr/bin/python3
"""define class of a singly linked list"""
class Node:
    """ A node in singly linked list"""
    def __init__(self, data, next_node=None):
        """
        intialize the Node object.

        Args:
        data(int): The data value of the Node.
        next_node (Node): The reference to the next Node,Defaults to None.
        """

        self.__data = data
        self.next__node = next_node

    @property
    def data(self):
        """Getter: get the data current value"""
        return(self.__data)

    @data.setter
    def data(self, value):
        """set the data of the Node."""

        if not isinstance(value,int):
            raise TypeError("data must be an integer")
        self._data = value


    @property
    def next_node(self):
        """retrieve the reference to the next Node."""
        return self.__next_node





class SinglyLinkedList:
    def __init__(self):
        """initialize an empty SinglyLinkedList object."""
        self._head = None

    def sorted_insert(self, value):
        """
        inserts a new Node in increasing order
        Args:
            value (int): data value of the new Node.
        """
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
        elif value < self._head.data:
            new_node.next_node = self._head
            self._head = new_node
        else:
            current = self._head
            while current.next_node is not None and current.next_node.data < value:

                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Method to generate a string representation of the SinglyLinkedList object.

        Returns:
            str: A string representation of the list with one node number per line.
        """
        nodes = []
        current = self._head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
