print('###########################')
x = 10
if x == 0:
    print('zero')
elif x < 0:
    print('negative')
else:
    print('positive')

print('###########################')
a = 1
b = 1
print(a > 0 and b > 0)
print(a > 0 or b > 0)

print('###########################')
y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

# if not a == b:
#     print('Not equal')

is_ok = True
if not is_ok:
    print('hello')

print('###########################')
# False: 0, 0.0, '', [], {}, (), set()
is_ok = ''
if is_ok:
    print('ok')
else:
    print('no')

print('###########################')
# None ... null object
is_empty = None
# print(help(is_empty))
if is_empty is not None:
    print('None!')

# value
print(1 == True)
# object
print(1 is True)
print(True == True)

print('###########################')
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('done')

count = 0
while True:
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue

    print(count)
    count += 1

print('###########################')
# while True:
#     word = input('Enter:')
#     if word == 'ok':
#         break
#     print('again...')

print('###########################')
for w in 'abcde':
    print(w)
    # break したら else にいかないよ
else:
    print('Fuck!!')

print('###########################')
for i in range(2, 10, 3):
    # 2, 5, 8
    print(i)

for _ in range(4):
    print(i)

print('###########################')
for i, f in enumerate('abcd'):
    print(i, f)

print('###########################')
days = ['mon', 'tue', 'wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'bear']

for d, f, r in zip(days, fruits, drinks):
    print(d, f, r)

print('###########################')
d = dict(x=100, y=200)
print(d.items())
for k, v in d.items():
    print(k, v)

