# tensorflow-debunked
## The formula for the divergent series '1 + 2 + 3 + 4 + 5 +..n' is n(n+1)/2 . 
## When n=5, the partial sum will be 15. Or in other words, for the given partial sum of 15, the value of n will be 5. 
## For a given partial sum, I want to find the n.
## I have two python program, one using simple formula 'simple_solution.py' and other using TensorFlow 'tf_solution.py'.
## See how TensorFlow fails for numbers like 55 and above. Also it is very slow.
