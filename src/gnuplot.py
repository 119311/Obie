import importcsv
import numpy as np
import subprocess
import csv

csvList, file = importcsv.inputlist()
i = np.array(csvList)

forgraph = []  # 日付だけのリスト
j = []  # 各日の支出の合計金額だけのリスト
data = []  # 上記2つを結合したリスト

# 支出金額のリスト生成
for year in range(2020, 2024):
    y = str(year)
    a = importcsv.csvSort(csvList, 0, y)
    for month in range(1, 13):
        m = str(month)
        m = "{:0>2}".format(m)
        b = importcsv.csvSort(a, 1, m)
        for day in range(1, 32):
            d = str(day)
            d = "{:0>2}".format(d)
            c = importcsv.csvSort(b, 2, d)
            c = importcsv.csvSort(c, 5, "2")
            c = str(importcsv.csvCalc(c))
            j.append(c)

j = [i for i in j if i != "0"]

# 日付のリスト生成
hani = len(i)
a = "{}-{}-{}"
# リストの最初（データベースの最初が収入だったら困るから）
for x in range(10):
    result = "2" in i[x, 5]
    if result == True:
        m = "{:0>2}".format(i[x, 1])
        d = "{:0>2}".format(i[x, 2])
        f = a.format(i[x, 0], m, d)
        forgraph.append(f)
        break
# リストの続き
for x in range(1, hani):
    result = "2" in i[x, 5]
    y = i[x, 0]
    m = "{:0>2}".format(i[x, 1])
    d = "{:0>2}".format(i[x, 2])
    d1 = "{:0>2}".format(i[x - 1, 2])
    if result == True and d != d1:
        b = a.format(y, m, d)
        forgraph.append(b)
# 日付順にソート
forgraph.sort(key=lambda x: x[0])

# 日付と金額を結合
for x in range(0, 50):
    print(x)
    date = forgraph[x]
    m = j[x]
    data.append([date, m])

# グラフ用csv生成
body = data

with open("forgraph.csv", "w") as f:

    writer = csv.writer(f)
    writer.writerows(body)

f.close()

# Gnuplot呼び出し
proc = subprocess.Popen(
    ["gnuplot", "-p"],
    shell=True,
    stdin=subprocess.PIPE,
)
proc.stdin.write(b"file='forgraph.csv'\n")
proc.stdin.write(b"set grid\n")
proc.stdin.write(b'set style fill solid border lc rgb "black"/n')
proc.stdin.write(b"set boxwith/n")
proc.stdin.write(b"set xdata time\n")
proc.stdin.write(b'set timefmt "%Y-%m-%d"\n')

# 月日だけの表示にしたかったけどコマンド動かなかった
# proc.stdin.write(b'set format x "%m-%d"\n')

# 範囲指定したかったけどコマンド動かなかった
# proc.stdin.write(b'set xrange ["2021-04-01":"2021-04-30"]\n')

proc.stdin.write(b'set datafile separator ","\n')
proc.stdin.write(b"set boxwidth 0.5 relative\n")
proc.stdin.write(
    b'plot file using 0:2:xtic(1) with boxes lw 2 lc rgb "light-green" notitle\n'
)
proc.stdin.write(b"quit\n")  # close the gnuplot window
