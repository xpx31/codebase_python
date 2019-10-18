"""

Script Description:

A divide and conquer stable algorithm in sorting
Divide the list in half until two units left
depends on the compare condition, move the one
to the new list

This version works with doubled circular linked list

Time: O(n log n)
Space: O(log n)

Created by Pengxiang Xu
Date: Oct/14/2019
Time: 10:18
"""

from Data_structure.LinkedList_Double_Circular import LinkedList_Double_Circular
from Data_structure.ListNode import ListNode


class Merge_Sort:
	def __init__(self, _list: LinkedList_Double_Circular):
		self.__anchor = _list.get_anchor()

	@staticmethod
	def __compare(left: ListNode, right: ListNode):
		if left == right:
			return 0
		else:
			return left > right

	def __get_mid(self, left: ListNode, right: ListNode):
		# Base case
		if left == right:
			return left

		slow = left
		fast = left

		# Iterate slow and fast pointers, speed of fast is twice as much as slow
		while fast != self.__anchor and fast.next_node != self.__anchor:
			slow = slow.next_node
			fast = fast.next_node.next_node

		return slow

	def __merge(self, left: ListNode, right: ListNode):
		if left == self.__anchor:
			return right
		if right == self.__anchor:
			return left

		# Compare two ListNodes and return the head
		choice = self.__compare(left, right)
		if choice == 0:
			next_n = self.__merge(left.next_node, right.next_node)
			left.next_node = next_n
			next_n.prev_node = left
			return left
		elif choice < 0:
			next_n = self.__merge(left.next_node, right)
			left.next_node = next_n
			next_n.prev_node = left
			return left
		else:
			next_n = self.__merge(left, right.next_node)
			right.next_node = next_n
			next_n.prev_node = right
			return right

	def merge_sort(self, _list: LinkedList_Double_Circular):
		head = self.merge_sort_(_list.head(), _list.tail())

		# Keep list integrity
		# for head
		self.__anchor.next_node = head
		head.prev_node = self.__anchor

		# for tail
		node = head
		while node.next_node != self.__anchor:
			node = node.next_node
		self.__anchor.prev_node = node

		return head

	def merge_sort_(self, left: ListNode, right: ListNode):
		# Sanity Check
		if left is None or left == right:
			return left

		# Split the list into two parts recursively
		mid = self.__get_mid(left, right)
		mid_next = mid.next_node
		mid.next_node = self.__anchor
		left = self.merge_sort_(left, mid)
		right = self.merge_sort_(mid_next, right)

		# Merge two lists recursively
		return self.__merge(left, right)