print('i don\'t know')
print('say "i don\'t know"')
print(r'C:\name\name')
print("###########")
print("""\
line1
line2
line3\
""")
print("###########")
print('HA!' * 3 + 'Mike!')
print('Py' + 'thon')
s = ('aaaaaaaaaaaaaaaaaaaaaa' \
     'bbbbbbbbbbbbbbbbbbbb')
print(s)

word = 'python'
print(word[1])
print(word[-1])
print(word[2:5])
print(word[:2])
print(word[2:])

word = 'j' + word[1:]
print(word)
print(word[:])
n = len(word)
print(n)

print('################################')

s = 'My name is Mike. Hi Mike.'
is_start = s.startswith('My')
print(is_start)

print('a is {0} {1} {2}'.format('foo', 'bar', 'goo'))

print('My name is {name} {family}'.format(name='shigeru', family='kishida'))

print('################################')
l = [1, 23, 4, 56, 7, 8]
print(l[-1])
print(l[:2])
print(list('abcdefg'))

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[0::2])
print(n[::-1])

a = list('abc')
n = [1, 2, 3]
x = [a, n]
print(x[0][-1])

print('################################')
s = list('abcdefg')
s[0] = 'x'
s[1] = 999
print(s)

s[2:5] = ['CC', 'DD', 'EE']
print(s)

s[2:5] = []
print(s)

s[:] = []
print(s)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.append(100)
print(n)
n.insert(0, 111)
print(n)
n.pop()
print(n)
n.pop(0)
print(n)
del n[0]
print(n)
n.remove(2)
print(n)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
x = a + b
print(x)
a += b
print(a)

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

x.extend(y)
print(x)

print('################################')
r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
print(r.index(3, 3))
print(r.count(3))

if 5 in r:
    print('exist')

r.sort()
print(r)

r.sort(reverse=True)
print(r)

s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)

print('################################')
i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('i = ', i)
print('j = ', j)
print(id(i))
print(id(j))

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 999
print('x = ', x)
print('y = ', y)
print(id(x))
print(id(y))

print('################################')
seat = []
min = 0
max = 5
print(min <= len(seat) < 5)
min <= len(seat) < 5

print('################################')
# tuple ... 読み込みに向いてる
t = (1, 2, 3, 4, 1, 2)
print(type(t))

print('################################')
num_tuple = (10, 20)
print(num_tuple)
x, y = num_tuple
print(x, y)

i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)
a = 100
b = 200
a, b = b, a
print(a, b)

print('################################')
chose_from_two = ('A', 'B', 'C')
ansewr = []
ansewr.append('A')
ansewr.append('C')
print(ansewr)

print('################################')
# dictionary
d = {'x': 10, 'y': 20}
d['z'] = 1000
print(d['x'])
d2 = dict(a=11, b=22)
print(d2['b'])
print(dict([('i', 111), ('j', 222)]))

d3 = {'name': 'yuki', 'age': 30}
d4 = {'sex': 'male'}
d3.update(d4)
print(d3)
print(d3.get('sex'))
print(d3.get('foo'))  # => None
del d3['sex']
print(d3)

print('################################')
# set
a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
b = {2, 3, 3, 6, 7}
print(a)
print(b)
print(type(a))

print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
print(b ^ a)

my_friends = {'A', 'C', 'D'}
a_friends = {'B', 'D', 'E', 'F'}
print(my_friends & a_friends)

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)

print('################################')
"""
multi 
line
comment
"""

s = 'aaaaaaaaaaaaaaaa' \
    + 'bbbbbbbbbbbbbbbbb'
print(s)