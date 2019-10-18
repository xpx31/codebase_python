"""

Script Description:

List node

Created by Pengxiang Xu
Date: Oct/14/2019
Time: 10:24
"""


class ListNode:
	next_node = None
	prev_node = None

	def __init__(self, data=None):
		self.next_node = ListNode()
		self.prev_node = ListNode()
		self.__data = data

	def get_data(self):
		return self.__data

	def set_data(self, data):
		self.__data = data

