from random import *

def crypt(msg, p1=0, p2=1000):
  low,high=0,2**32
  seed_=low
  while seed_<=high:
    seed(seed_)
    for i in range(len(msg)):
      r_=randint(p1,p2)
      if chr(r_)!=msg[i]: break
      elif i==len(msg)-1: return seed_
    seed_+=1
  return None