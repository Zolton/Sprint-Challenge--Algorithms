#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) It should be O(n).  The number of operations will always be equal to n.  If n is 10, the first pass will calculate 0+100=0, then 100+100=200, then 200+100 = 300, and so on, until 1000.  n is 10, it'll take 10 operations to hit 1000, therefore the number of operations required is equal to n - O(n) runtime


b)  I don't know the exact mathematical expression, but it's likely logn.  if n = 10, 3 operations will be run.  If n = 20, 4 operations will run, if n = 100, 6 operations will run.  It's basically an inverse binary search, with j doubling instead of halving.


c)  Runtime should be O(n).  If n = 3, first pass will be 2+(3-1) = 2+(2-1) = 2+(1-1) - answer is 6, but it took 3 operations to arrive at the answer, which is equal to n.  So I would say the runtime is O(n)

## Exercise II

Don't drop any eggs.  

This problem doesn't make any sense.  The pseudo code would be something like (# of floors n) = (some operation to determine # of eggs broken).  There'd be a logic if-statement to determine when the number of broken eggs rose above some arbitrary limit, and to return what # floor the function was at before it broke through the limit


