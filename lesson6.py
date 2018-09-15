import sys

# フルパスで読み込むパターン
# import lesson_package.util
# モジュールまでインポートするパターン
from lesson_package.tools import utils

# これ↓よくない。どのモジュールのメソッドか分かりづらくなるから
# from lesson_package.utils import say_twice

# from lesson_package.talk import human
# from lesson_package.talk import animal
"""
*指定に備えて package内の__init__に__all__で
モジュールをリストで書くことができる。
あまり勧められていないので、*読み込みは避けるように！
"""
# from lesson_package.talk import *


# print(sys.argv)
# for i in sys.argv:
#     print(i)
#
# # r = lesson_package.utils.say_twice('hello')
# r = utils.say_twice('hello')
#
# print(human.cry())
# print(animal.cry())

"""
違うバージョンを使ってモジュールを使い分けたいときにこれを使う
"""
try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils

