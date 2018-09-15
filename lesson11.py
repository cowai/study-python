class Person(object):
    # クラス変数
    kind = 'human'

    def __init__(self, name):
        self.name = name
        self.x = 100

    def who_are_you(self):
        print(self.name, self.kind)

    @classmethod
    def what_is_your_kind(cls):
        # クラスメソッド
        return cls.kind

    @staticmethod
    def about(year):
        print('about human {}'.format(year))


a = Person('A')
b = Person('B')
a.who_are_you()
b.who_are_you()


class T(object):
    words = []

    def add_word(self, word):
        self.words.append(word)


c = T()
c.add_word('add 1')
c.add_word('add 2')

d = T()
d.add_word('add 3')
d.add_word('add 4')

# クラス変数は全てのオブジェクトで共有されるから注意
print(c.words)

print('###################')
a = Person('A')
print(a.what_is_your_kind())

# クラスメソッド
# インスタンス化してなくても、クラスメソッドは呼べる
b = Person
print(b.what_is_your_kind())
print(Person.kind)
print(Person.what_is_your_kind())

# スタティックメソッド
# クラスの外に置けるけど、意味合い的に
# クラスの中に置きたいときにこう書いてもOKよ
Person.about(1987)

print('###################')


class Word(object):
    """
    特殊メソッド
    """

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Word...'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()


w = Word('foo')
print(w)
print(len(w))

w2 = Word('bar')
print(w + w2)

w3 = Word('bar')
print(w == w3)
print(w2 == w3)
