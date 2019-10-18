"""

Script Description:.

Doubled linked list

Created by Pengxiang Xu
Date: Oct/14/2019
Time: 10:22
"""

from Data_structure.ListNode import ListNode


class LinkedList_Double:
	def __init__(self, node: ListNode):
		self.__length = 0
		self.__head = node
		self.__tail = node

	def __iter__(self):
		node = self.head()

		while node is not None:
			yield node
			node = node.next_node

	def length(self):
		return self.__length

	def head(self):
		return self.__head

	def tail(self):
		return self.__tail

	def insert_head(self, node: ListNode):
		head_o = self.head()
		node.next_node = head_o
		head_o.prev_node = node
		node.prev_node = None
		self.__head = node

		self.__length += 1

	def insert_tail(self, node: ListNode):
		tail_o = self.tail()
		node.prev_node = tail_o
		tail_o.next_node = node
		node.next_node = None
		self.__tail = node

		self.__length += 1

	def remove(self, node: ListNode):
		if node == self.head():
			self.__head = node.next_node
		if node == self.tail():
			self.__tail = node.prev_node

		prev_n = node.prev_node
		next_n = node.next_node

		prev_n.next_node = next_n
		next_n.prev_node = prev_n

		self.__length -= 1
