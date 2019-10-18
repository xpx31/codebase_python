"""

Script Description:

Sort k sorted linked lists works with doubled circular linked list

Time: O(kn)
Space: O(1)

Created by Pengxiang Xu
Date: Oct/14/2019
Time: 10:18
"""


from Data_structure.LinkedList_Double_Circular import LinkedList_Double_Circular
from Data_structure.ListNode import ListNode


class merge_sort_k_way:
	def __init__(self):
		pass

	@staticmethod
	def __compare(left: ListNode, right: ListNode):
		if left == right:
			return 0
		else:
			return left > right

	def __merge_k_way(self, left: LinkedList_Double_Circular, right: LinkedList_Double_Circular):
		head = p = ListNode()

		anchor_left = left.get_anchor()
		anchor_right = right.get_anchor()
		left_n = left.head
		right_n = right.head

		# Compare the add to sorted list
		while left_n != anchor_left and right_n != anchor_right:
			choice = self.__compare(left_n, right_n)

			if choice == 0:
				p.next_node = left_n
				left_n.prev_node = p
				left_n = left_n.next_node
				right_n = right_n.next_node
			elif choice < 0:
				p.next_node = left_n
				left_n.prev_node = p
				left_n = left_n.next_node
			else:
				p.next_node = right_n
				right_n.prev_node = p
				right_n = right_n.next_node

		# Add the rest of the nodes
		if left_n != anchor_left:
			p.next_node = left_n
			left_n.prev_node = p
		else:
			p.next_node = right_n
			right_n.prev_node = p

		return head.next_node

	def merge_sort_k_way(self, lists: [LinkedList_Double_Circular]):
		head = self.merge_sort_k_way_(lists, len(lists) - 1)

		# Keep list integrity
		# for head
		list_anchor = lists[0].get_anchor
		list_anchor.next_node = head
		head.prev_node = list_anchor

		# for tail
		node = head
		while node.next_node != list_anchor:
			node = node.next_node
		list_anchor.prev_node = node

		return head

	def merge_sort_k_way_(self, lists: [LinkedList_Double_Circular], last: int):
		while last != 0:
			i = 0
			j = last

			# Sort a pair lists
			while i < j:
				ListNode(lists[0]).head = self.__merge_k_way(lists[i], lists[j])
				i += 1
				j -= 1

				# Done with one round
				if i >= j:
					last = j

		return lists[0]

