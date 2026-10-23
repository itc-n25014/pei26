# aに2を代入する
a = 2 

#空のリストを用意
result_list = []

# aを使った繰り返し処理でリストを作成
for i in range(1, 6):
    #リストの末尾にaを追加
    result_list.append(a)
    a = a * 2
    # 実行結果を表示
print(result_list)
