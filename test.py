#!/usr/bin/env python

import os

def add(x,y):
  """
  Adds two numbers
  """
  return x + y

def subtract(x,y):
  """
  Subtracts two numbers
  """
  try:
    z = x - y
    return z
  except TypeError:
    print "Arguments must be numbers"

print os.getcwd()
print "Hello World"
print add(3 + 4)
print subtract(x, y)
