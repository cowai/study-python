# ファイル書き込み
# w:overwrite, a:append, r:read
f = open('text.txt', 'w')
f.write('Test\n')
# print('I am print', file=f)
print('My', 'name', 'is', 'Mike', sep='...', end='..!!', file=f)
f.close()

# 閉じ忘れ防止 ... with
s = """\
AAA
BBB
CCC
DDD
"""
with open('text.txt', 'w') as f:
    # f.write('using with\n')
    # print('apple', 'banana', 'citrus', sep=', ', end='!', file=f)
    f.write(s)

# 読み込み
# with open('text.txt', 'r') as f:
#     # print(f.read())
#     # 複数行ずつ
#     while True:
#         chunk = 2
#         line = f.readline(chunk)
#         print(line)
#         if not line:
#             break
#
#     # 1行ずつ
#     while True:
#         line = f.readline()
#         print(line, end='')
#         if not line:
#             break

# Seek
# with open('text.txt', 'r') as f:
#     print(f.tell())
#     print(f.read(1))
#     f.seek(5)
#     print(f.read(1))
#     f.seek(14)
#     print(f.read(1))
#     f.seek(15)
#     print(f.read(1))
#     f.seek(5)


# write -> read
s = """\
AAA
BBB
CCC
DDD
"""
# 書き込んでから読むとき
with open('text.txt', 'w+') as f:
    f.write(s)
    # 書き込んだあとは、seek で戻らないとだめ
    f.seek(0)
    print(f.read())

# read -> write
s = """\
AAA
BBB
CCC
DDD
"""
# 読んでから書き込む
with open('text.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)
