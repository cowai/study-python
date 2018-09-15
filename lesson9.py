import abc


class Person(metaclass=abc.ABCMeta):
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

    @abc.abstractmethod
    def drive(self):
        pass
        # 親クラスのメソッドを子クラスで個別実装させたいとき
        # 抽象メソッド化して子クラスに実装を委ねる
        # if self.age >= 18:
        #     print('drive ok')
        # else:
        #     raise Exception('No drive')

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

    def drive(self):
        print('No drive')


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('Drive ok')


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()


print('########################')
"""
抽象クラス
@abc.abstractmethod
"""
baby = Baby()
adult = Adult()

car = Car()
car.ride(baby)
car.ride(adult)
