# 関数定義してからじゃないとエラーになる
# say_something()
def say_something():
    print('hi')


say_something()
print(type(say_something))
f = say_something
f()
print('###########################')


def test_func3():
    s = 'hahaha'
    return s


print(test_func3())
print('###########################')


def what_is_this(color):
    print(color)


what_is_this('red')
print('###########################')


def add_num(a: int, b: int) -> int:
    return a + b


print(add_num(1, 2))
## これはこれで動く
print(add_num('ss', 'vv'))
print('###########################')


def menu(a, b, c):
    print(a, b, c)


menu(a='1st', b='2nd', c='3rd')


def menu2(a='1', b='2', c='3'):
    print(a, b, c)


menu2()
print('###########################')


def test_func(x, l=[]):
    l.append(x)
    return l


"""
 一度定義したらその中のデフォルト引数のリストは
 使い回される。だから、二回目は[100, 100]となる
 →リストは参照渡しなので、リストをデフォルト引数にすべきじゃない
"""
print(test_func(100))
print(test_func(100))


def test_func2(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


"""
 空の辞書型やリストをデフォルト引数にするときは
 中身をNoneにして、defの中で詰め直す
"""
print(test_func2(100))
print(test_func2(100))
print('###########################')


def say_something2(word1, word2, *args):
    print(type(args))
    print(args)
    print('word1: ', word1)
    print('word2: ', word2)
    for i in args:
        print('args:', i)


say_something2('aaa', 'bbb', 'ccc', 'ddd')
t = ('foo', 'bar')
say_something2('aaa', 'bbb', *t)

print('###########################')


def menu3(**kwargs):
    print(kwargs)


menu3(a=1, b=2, c=3)
d = dict(xx=11, yy=22)
menu3(**d)
print('###########################')


def test_func4(param1, param2):
    """

    :param param1:
    :param param2:
    :return:
    """


help((test_func4))
help((test_func4.__doc__))
print('###########################')


def outer(a, b):
    def plus(c, d):
        return c + d

    r = plus(a, b)
    print(r)


outer(5, 6)
print('###########################')


# クロージャー

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area


ca1 = circle_area_func(3)
ca2 = circle_area_func(3.14)
print(ca1(10))
print(ca2(10))

print('###########################')


# デコレーター

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func: ', func.__name__)
        print('args: ', args)
        print('kwargs: ', kwargs)
        result = func(*args, **kwargs)
        print('result: ', result)
        return result

    return wrapper


def print_info(func):
    def wrapper(*args, **kwargs):
        print('-- start --')
        result = func(*args, **kwargs)
        print('-- end -- ')
        return result

    return wrapper


@print_info
@print_more
def add_num(a, b):
    return a + b


r = add_num(10, 20)
print(r)

print('###########################')
# ラムダ ...　ちょろっと関数書くイメージ
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


def change_words(words, func):
    for w in words:
        print(func(w))


change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())

print('###########################')


# ジェネレーター
def greeting():
    yield 'Good mooning'
    for i in range(50):
        print(i)
    yield 'Good afternoon'
    yield 'Good night'


def counter(num=10):
    for _ in range(num):
        yield 'run'


g = greeting()
c = counter()
print(next(g))
print(next(c))
print(next(c))
print(next(g))
print(next(c))
print(next(c))
print(next(g))

print('###########################')
# リスト包表記 ... 短いループで使える
t = (1, 2, 3, 4, 5)

r = [i for i in t if i % 2 == 0]
print(r)

# 書けるけど分かりづらい
t2 = (6, 7, 8, 9, 10)
r = [i * j for i in t for j in t2]
print(r)

print('###########################')
# 辞書包括表記
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']
d = {}
for x, y in zip(w, f):
    d[x] = y
print(d)

d = {x: y for x, y in zip(w, f)}
print(d)

print('###########################')
# 集合内表記
s = set()
s = {i for i in range(10)}
print(s)

print('###########################')


# ジェネレーター内包表記
def g():
    for i in range(10):
        yield i


g = g()
g = (i for i in range(10))
# tuple ならば、こう書け
# g = tuple(i for i in range(10))
print(type(g))
print(next(g))

print('###########################')
animal = 'cat'


def f():
    # グローバルの変数は呼び方に決まりがある
    # print(animal)
    global animal
    animal = 'dog'
    local_name = 'yuki'
    print(animal)
    print(locals())
    print(globals())


f()
