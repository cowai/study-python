class Person(object):
    """
    Python2の名残からobjectを書いたほうがいいらしい。
    継承のときにも活きる
    """

    def __init__(self, name='Taro', age=1):
        self.name = name
        print(self.name)
        self.age = age
        # self は自分自身
        # print(self)

    def drive(self):
        if self.age >= 18:
            print('drive ok')
        else:
            raise Exception('No drive')

    def say(self):
        print('I am {}, hello'.format(self.name))
        self.run()

    def run(self):
        print('run')

    def __del__(self):
        print('Good bye')


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError


baby = Baby()
adult = Adult()

# p = Person()
p = Person('Mike')
p.say()

"""
 __del__ はでコンストラクタ
 終わったときに呼ばれる。
 意図的に終わらすなら del object名
"""
del p
print('########################')


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()


class ToyotaCar(Car):
    def run(self):
        print('fast')


class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        # self.model = model 親クラスのinitを呼んで設定できる
        super().__init__(model)
        # _を付けると外から見られたり、書き換えられたりできないようになる
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        # property は getter
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable

    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')


c = Car()
c.run()
tc = ToyotaCar('Lexus')
print(tc.model)
tc.run()
ts = TeslaCar('Model S')
print(tc.model)
ts.run()
ts.auto_run()

# ts.enable_auto_run = True
# オブジェクトのプロパティは好き勝手書き換えられたら嫌
# なので、 プロパティに _ を付ける

# ts.enable_auto_run() = True .. property はクラス変数なので()付けない
# ts.enable_auto_run = True .. property は書き込み出来ない
print(ts.enable_auto_run)

# setter があれば、setできる
ts.enable_auto_run = True
print(ts.enable_auto_run)

"""
 __ はインスタンス内からしかアクセスできない
  _ はインスタンス外からでもアクセスできる
    だけど、書き込みはできない。
    
 _ __ がついていると
 foo = 'xx' 入らない
 だけど、↓は再定義はできちゃう
 _foo = 'xx'
 __foo = 'xx'
"""

print('########################')
car = Car()
car.ride(baby)
car.ride(adult)


print('########################')
"""
抽象クラス
"""
