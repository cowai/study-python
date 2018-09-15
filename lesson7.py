import collections
import os
import sys

import termcolor

import config
import lesson_package


def main():
    print('test')
    print(termcolor.colored('test', 'red'))

    """
    import したパッケージを 
    右クリック→Go to→declarationすれば場所がわかる
    
    importしたパッケージの記述を
    整理整頓するなら Ctrl + Alt + O
    ルールに則って並べてくれる
    """
    print(collections.__file__)
    print(termcolor.__file__)
    print(lesson_package.__file__)
    print(config.__file__)
    # print(sys.__file__)
    print(os.__file__)

    print(sys.path)

    print('#######################')
    """
    __name__ 
    コマンドラインからファイルしてした実行したPythonファイルは
    __main__ という名前のモジュールとしてPythonに読み込まれる。
    実行中スクリプトのモジュールの名前は、
    __name__ という変数に設定されるため
    この値を参照して、ファイルがコマンドラインから実行されたのか
    import文で読み込まれたのかを識別できる
    """
    print('lesson7: ', __name__)


if __name__ == '__main__':
    main()
