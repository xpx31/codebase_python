"""

Script Description:

Viterbi Algorithm:

A dynamic programming algorithm for finding the most likely sequence of hidden states
that results in a sequence of observed events (eg. in context of Hidden Markov Models)

https://en.wikipedia.org/wiki/Viterbi_algorithm

Created by Pengxiang Xu
Date: Oct/17/2019
Time: 16:27
"""

import numpy as np


class Viterbi:
	def __init__(self, pi=None, a=None, b=None, obs=None):
		"""
		Class constructor

		:param pi: initial probability vector of emission states
		:param a: hidden state transitional probability matrix
		:param b: emission state observation probability matrix
		:param obs: observations
		"""
		if pi is None or a is None or b is None or obs is None:
			pass
		else:
			self.__pi = np.array(pi)
			self.__a = np.array(a)
			self.__b = np.array(b)
			self.__obs = np.array(obs)

	def viterbi(self, pi, a, b, obs):
		"""
		Run viterbi algorithm

		:param pi: initial probability vector of emission states
		:param a: hidden state transitional probability matrix
		:param b: emission state observation probability matrix
		:param obs: observations
		"""
		# Getting parameters
		self.__pi = np.array(pi)
		self.__a = np.array(a)
		self.__b = np.array(b)
		self.__obs = np.array(obs)

		# Get shapes
		emission_n = np.shape(b)[0]
		obs_n = np.shape(obs)[0]

		# Setting path and algorithm parameters
		# delta: highest probability of any path at state i
		# phi: time at the highest probability of each state
		path = np.zeros(obs_n)
		delta = np.zeros((emission_n, obs_n))
		phi = np.zeros((emission_n, obs_n))

		# Parameter initialization
		delta[:, 0] = pi * b[:, obs[0]]
		phi[:, 0] = 0

		# Forward algorithm
		for t in range(1, obs_n):
			for s in range(emission_n):
				delta[s, t] = np.max(delta[:, t-1] * a[:, s]) * b[s, obs[t]]
				phi[s, t] = np.argmax(delta[:, t-1] * a[:, s])

		# Backtrack
		for t in range(obs_n - 2, -1, -1):
			path[t] = phi[path[t + 1], [t + 1]]

		return path, delta, phi


