def eratosthenes2(n):
    multiples = set()
    for i in range(2, n+2):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))

def eratosthenesFastNotReally(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i)) 
 
print(list(eratosthenes2(100)))
