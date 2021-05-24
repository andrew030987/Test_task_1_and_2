
def first_rep(arr):
    s = set()
    for i in arr:
        if i in s:
            return i
        else:
            s.add(i)
 

lst1 = ['a', 'b', 'c', 'c', 'a']
lst2 = ['e', 'a', 'b', 'b', 'c', 'c', 'd', 'a', 'b']
lst3 = ['a', 'c', 'a', 'c', 'e', 'a']

assert first_rep(lst1) == 'c'
assert first_rep(lst2) == 'b'
assert first_rep(lst3) == 'a'
