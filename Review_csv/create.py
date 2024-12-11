import pandas as pd

# a.csvとb.csvを読み込む
a_df = pd.read_csv('a.csv', header=None)
b_df = pd.read_csv('b.csv', header=None)

# 比較する列番号（n列目）を指定（1列目、2列目、...）
n = 1  # 比較対象の列番号
m = 2  # 出力したいm列目の番号（例えば2列目）

output_rows = []

matched_indices_b = []

for i, row_a in a_df.iterrows():
    for j, row_b in b_df.iterrows():
        if row_a[n-1] == row_b[n-1]:
            output_rows.append([row_a[n-1], row_a[m-1], row_b[m-1]])
            matched_indices_b.append(j)

            print(f"一致した行：a.csvの行{i+1}とb.csvの行{j+1}が一致")
            print(f"a.csvのn列目: {row_a[n-1]}")
            print(f"a.csvのm列目: {row_a[m-1]}")
            print(f"b.csvのm列目: {row_b[m-1]}")
            print("-" * 40)

b_df = b_df.drop(index=matched_indices_b)

output_df = pd.DataFrame(output_rows, columns=[f'a.csvのn列目', f'a.csvのm列目', f'b.csvのm列目'])

print("一致した行の結合結果：")
print(output_df)

output_df.to_csv('output.csv', index=False)

b_df.to_csv('b_updated.csv', index=False, header=False)
