
def fib (x,y,sum):
    next = x + y
    if next % 2 == 0:
        sum += next
    print(next)
    if next < 4000000:
        fib(y,next,sum)
    else:
        print("finished sum is", sum)

fib(1,2,2)
    
    
    
