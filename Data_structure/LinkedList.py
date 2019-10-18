"""

Script Description:

Single linked list

Created by Pengxiang Xu
Date: Oct/14/2019
Time: 10:22
"""


from Data_structure.ListNode import ListNode


class LinkedList:
	def __init__(self, node: ListNode = None):
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

	def insert_head(self, node: ListNode):
		if self.head() is None:
			self.__head = node
		else:
			head_o = self.head()
			node.next_node = head_o
			self.__head = node

		self.__length += 1

	def append(self, node: ListNode):
		self.__tail.next_node = node
		self.__tail = node

		if node is not None:
			node.next_node = None

		self.__length += 1

	def remove(self, node: ListNode):
		if node == self.head():
			self.__head = None
			self.__length -= 1
		else:
			for node_ in self:
				if node_ is not None and node_.next_node == node:
					node_next = node.next_node
					node_.next_node = node_next
					self.__length -= 1
