class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('person run')


class Car(object):
    def run(self):
        print('run')

    def run(self):
        print('car run')


class PersonCarRobot(Car, Person):
    def fly(self):
        print('fly')


pcr = PersonCarRobot()
pcr.talk()
pcr.fly()
# run は両クラスにいるけど、このとき
# 引数の順に探して利用される
# L17: Car → Person だから Car の run が呼ばれる
pcr.run()

