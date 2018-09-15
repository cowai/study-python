from collections import defaultdict

ranking = dict(A=100, B=85, C=95)

print(sorted(ranking))
print(sorted(ranking, key=ranking.get, reverse=True))

print('#############################')
s = 'asdfasdfasdfads'
d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)

d = defaultdict(int)
for c in s:
    d[c] += 1
print(d)
