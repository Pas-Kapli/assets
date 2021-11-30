#!/usr/bin/python3

import numpy as np
import scipy
import math
import sys
from scipy import linalg

# define the two types of branch lengths
t1 = 0.1
t2 = 0.2

# k parameter (alpha/beta) for the K80 model
# d is adjusted such that the rows of Q-matrix sum to 0
k = 2
d = k+2

# equilibrium base frequencies
pi = [0.25,0.25,0.25,0.25]

# Instantaneous rate matrix.
#              T  C  A  G
Q = np.array([[-d,  k,  1,  1],     # T
              [ k, -d,  1,  1],     # C
              [ 1,  1, -d,  k],     # A
              [ 1,  1,  k, -d]])    # G

# We divide all elements of the matrix by d (in this case 4).
# This is to scale the rate of change (sum of off-diagonal elements in each row, or d) to 1 to reflect 1 substitution / site.
Q = Q / d

def partial(vec1, vec2, t1, t2):
  # calculate the transition probability matrices P(t1) and P(t2)
  Pt1 = scipy.linalg.expm(Q*t1)
  Pt2 = scipy.linalg.expm(Q*t2)

  # Pt1@vec1 means: dot product of P(t1) dot vec1
  # multiplication * means pairwise product
  return ((Pt1@vec1)*(Pt2@vec2))

if __name__ == "__main__":
  
  # set the tip vector probabilities
  v1 = np.array([0,0,1,0])
  v2 = np.array([0,0,0,1])
  v3 = np.array([1,1,0,0])
  v4 = np.array([0,0,0,1])

  # calculate vector for node 5
  print("Conditional likelihood vector for node 5:")
  v5 = partial(v3,v4,t1,t1)
  print(v5, end="\n\n")

  # calculate vector for node 6
  print("Conditional likelihood vector for node 6:")
  v6 = partial(v1,v2,t1,t1)
  print(v6, end="\n\n")

  # calculate vector for node 7
  print("Conditional likelihood vector for node 7:")
  v7 = partial(v5,v6,t2,t2)
  print(v7, end="\n\n")

  L = sum(v7*pi)
  logL = math.log(L)
  print("log-Likelihood:")
  print(logL)
#  print(np.around(v0,8))
