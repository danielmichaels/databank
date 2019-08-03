# Questions

This is a collection of interview-like questions. Serves more as a repository of simple Python problems to think through.

## Working with directories

```python
def print_directory_contents(sPath):
    """
    This function takes the name of a directory 
    and prints out the paths files within that 
    directory as well as any files contained in 
    contained directories. 

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your 
    ability to work with nested structures. 
    """
    fill_this_in
```

## Data structure quiz

```python
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
```

## Object and data structures

What does this code output?

```python
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l) 

f(2)
f(3,[3,2,1])
f(3)
```

## Unique in multiple lists

```python
a = [1,2,3,4]
b = [1,2,5,6]

print(list(set().union(a,b)))
```

## Palidromes

```python
def palindrome(word):
  word = word.lower()
  if word[::1] == word:
    return True
  return False
```
