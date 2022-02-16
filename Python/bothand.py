# def move(a,b):
#   print("move from {} to {}".format(a,b))


# def hanoi(n,f,h,t):
  # n = number of circles
  # f = from
  # h = helper
  # t = to
  # if n == 0:
  #   pass
  # else:
  #   hanoi(n-1,f,t,h) 
  #   move(f,t)
  #   hanoi(n-1, h, f, t)


# TREE ÷
# class Expr:
#   pass

# class Times (Expr):
#   def __init__(self, l,r): 
#     self.l = l
#     self.r =r
#   def __str__(self):
#     return "(" + str(self.l) + " * " + str(self.r) + ")"
#   def eval(self,env):
#     return self.l.eval(env)  * self.r.eval(env)

# class Plus (Expr):
#   def __init__(self,l,r ):
#     self.l = l
#     self.r = r
#   def __str__(self):
#     return "(" + str(self.l)+ " + " + str(self.r) + ")"
#   def eval(self,env):
#     return self.l.eval(env) + self.r.eval(env)

# class Const (Expr):
#   def __init__(self,val):
#     self.val = val
#   def __str__(self):
#     return str(self.val)
#   def eval(self,env):
#     return self.val

# class Var (Expr):
#   def __init__(self,name):
#     self.name = name
#   def __str__(self ):
#     return self.name
#   def eval(self,env):
#     return env[self.name]



# el1 = Times(Const(3),Plus(Var("y"),Var("x"))) 
# el2 = Plus(Times(Const(3),Var("y")),Var("x"))
# env = {"x":2,"y":4}
# print(el1)
# print(el1)
# print(el1.eval(env))
# print(el2.eval(env))

# SODOKU

import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

def possible(y,x,n):
  global grid
  for i in range(0,9):
    if grid[y][i] == n:
      return False
  for i in range(0,9):
    if grid[i][x] == n:
      return False
  x0 = (x//3)*3
  y0 = (y//3)*3
  print("y0 = {}, & and x0 = {}".format(y0,x0))
  for i in range(0,3):
    for j in range(0,3):
      if grid[y0+i][x0+j] == n:
        return False
  return True


possible(4, 4, 6)

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x]= n
                        solve()
                        grid[y][x]=0
                return
    yeild np.matrix(grid)
