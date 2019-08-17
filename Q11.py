def fib(n):
    a = 1 
    b = 1
    for i in range(2,n):
      c = a+b
      a = b
      b = c
      if c % 2  == 0:
        print (c)
        
fib(37)