import pandas as pd

# a.csvとb.csvを読み込む（header=Noneで1行目もデータとして扱う）
a_df = pd.read_csv('a.csv', header=None)
b_df = pd.read_csv('b.csv', header=None)

# 比較する列番号（n列目）を指定（1列目、2列目、...）
n = 1  # 比較対象の列番号
m = 2  # 出力したいm列目の番号（例えば2列目）

# 一致した行の結果を保存するリスト
output_rows = []

# 一致した行のインデックスを保存するリスト
matched_indices_b = []

# 一致した行を処理
for i, row_a in a_df.iterrows():
    for j, row_b in b_df.iterrows():
        if row_a[n-1] == row_b[n-1]:  # n列目が一致する場合
            # a.csvのn列目の文字列、a.csvのm列目の文字列、b.csvのm列目の文字列を出力
            output_rows.append([row_a[n-1], row_a[m-1], row_b[m-1]])
            matched_indices_b.append(j)  # 一致したb.csvの行インデックスを保存

            # 一致した内容を表示
            print(f"一致した行：a.csvの行{i+1}とb.csvの行{j+1}が一致")
            print(f"a.csvのn列目: {row_a[n-1]}")
            print(f"a.csvのm列目: {row_a[m-1]}")
            print(f"b.csvのm列目: {row_b[m-1]}")
            print("-" * 40)

# b.csv内の一致した行を削除
b_df = b_df.drop(index=matched_indices_b)

# 結果を新しいデータフレームとしてまとめる
output_df = pd.DataFrame(output_rows, columns=[f'a.csvのn列目', f'a.csvのm列目', f'b.csvのm列目'])

# 結果を表示
print("一致した行の結合結果：")
print(output_df)

# 結果を新しいCSVとして保存
output_df.to_csv('output.csv', index=False)

# b.csvを直接上書き保存
b_df.to_csv('b.csv', index=False, header=False)
