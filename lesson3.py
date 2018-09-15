# 文字列結合
# メモリ上良くない書き方
long_word = ''
for word in ['aaaaa', 'bbbbb']:
    long_word += '{} and '.format(word)

print(long_word)

# マシな書き方
long_word = []
for word in ['aaaaa', 'bbbbb']:
    long_word.append('{} and '.format(word))

new_long_word = ''.join(long_word)
print(new_long_word)



# ファイル処理は、with
# クラスはキャメルケース
# メソッドや変数はスネークケース
# グローバル変数は大文字ｘスネークケース

# 手動で virtualenvを作るとき
# 作る: virtualenv venv
# アクティブ: .\venv\Scripts\activate
# ディアクティブ: deactivate
