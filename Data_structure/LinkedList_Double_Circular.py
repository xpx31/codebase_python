"""

Script Description:

Created by Pengxiang Xu
Date: Oct/14/2019
Time: 10:22
"""

from Data_structure.ListNode import ListNode


class LinkedList_Double_Circular:
	def __init__(self):
		self.__anchor = ListNode()
		self.__anchor.next_node = self.__anchor
		self.__anchor.prev_node = self.__anchor
		self.__length = 0

	def __iter__(self):
		node = self.head()

		while node != self.__anchor:
			yield node
			node = node.next_node

	def length(self):
		return self.__length

	def head(self):
		return self.__anchor.next_node

	def tail(self):
		return self.__anchor.prev_node

	def insert_head(self, node: ListNode):
		head_o = self.head()
		self.__anchor.next_node = node
		node.next_node = head_o
		head_o.prev_node = node
		node.prev_node = self.__anchor

		self.__length += 1

	def insert_tail(self, node: ListNode):
		tail_o = self.tail()
		self.__anchor.prev_node = node
		node.prev_node = tail_o
		tail_o.next_node = node
		node.next_node = self.__anchor

		self.__length += 1

	def remove(self, node: ListNode):
		prev_n = node.prev_node
		next_n = node.next_node

		prev_n.next_node = next_n
		next_n.prev_node = prev_n

		self.__length -= 1

	def get_anchor(self):
		return self.__anchor


