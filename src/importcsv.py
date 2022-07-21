import csv
import tkinter
from tkinter import filedialog
import numpy as np

# CSV読み込み
def inputlist():  # DBを配列に格納

    idir = ".\\"
    # file_path = tkinter.filedialog.askopenfilename(initialdir = idir, filetypes = [("データファイル", "*.csv")])
    file_path = ".\\kakeibo.csv"
    with open(file_path, mode="r", encoding="utf-8-sig") as f:
        blist = [row for row in csv.reader(f)]
    return blist, file_path


# CSV行追加
def listappend(addlist, DB):  # adddata:追加データ, DB:追加先データベース
    DB.append(addlist)
    return DB


# CSV要素追加
def listinsert(x, y, addmember, DB):
    DB[x].insert(y, addmember)
    return DB


# CSV要素削除
def listpop(x, y, DB):  # x=削除したい行, y=削除したい列,
    DB[x].pop(y)
    return DB


# CSV行削除
def listclear(x, DB):  # x削除したい行,
    b = []
    DB[x].clear()

    for i in range(len(DB)):  # 空白の配列をよけて上に詰める
        d = bool(DB[i])
        print(d)
        if d == True:
            b.append(DB[i])

    return b


# CSV出力 ORDERはTrueなら降順，Falthなら昇順
def outputlist(FDB, file_path, ORDER):  # 最終編集結果をCSVに出力 FDB:FinalDataBase
    FDB = csvOrder(FDB, ORDER)

    with open(file_path, mode="w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)
        writer.writerows(FDB)


# 降順ソート
def csvOrder(DB, orderbool):
    day = 2
    month = 1
    DB = np.array(DB)
    dlist = []
    mlist = []
    alllist = []

    for i in range(len(DB)):
        if (int(DB[i][month]) < 10) == True and str(DB[i][month])[0] != "0":
            mlist.append("0" + DB[i][month])
        else:
            mlist.append(DB[i][month])
        if (int(DB[i][day]) < 10) == True and str(DB[i][day])[0] != "0":
            dlist.append("0" + DB[i][day])
        else:
            dlist.append(DB[i][day])
        alllist.append(
            [
                DB[i][0],
                mlist[i],
                dlist[i],
                DB[i][3],
                DB[i][4],
                DB[i][5],
                DB[i][6],
                DB[i][7],
            ]
        )

    orderlist = sorted(alllist, key=lambda x: (x[0], x[1], x[2]), reverse=orderbool)
    return orderlist


# 文字検索機能
def csvSort(DB, array, word):
    sortlist = []
    DB = csvOrder(DB, False)

    if array == 0:
        for i in range(len(DB)):
            if int(DB[i][0]) == word:
                sortlist.append(
                    [
                        DB[i][0],
                        DB[i][1],
                        DB[i][2],
                        DB[i][3],
                        DB[i][4],
                        DB[i][5],
                        DB[i][6],
                        DB[i][7],
                    ]
                )
    elif array == 1:
        for i in range(len(DB)):
            if int(DB[i][1]) == word:
                sortlist.append(
                    [
                        DB[i][0],
                        DB[i][1],
                        DB[i][2],
                        DB[i][3],
                        DB[i][4],
                        DB[i][5],
                        DB[i][6],
                        DB[i][7],
                    ]
                )
    elif array == 2:
        for i in range(len(DB)):
            if int(DB[i][2]) == word:
                sortlist.append(
                    [
                        DB[i][0],
                        DB[i][1],
                        DB[i][2],
                        DB[i][3],
                        DB[i][4],
                        DB[i][5],
                        DB[i][6],
                        DB[i][7],
                    ]
                )
    elif array == 3:
        for i in range(len(DB)):
            if (word in str(DB[i][3])) == True:
                sortlist.append(
                    [
                        DB[i][0],
                        DB[i][1],
                        DB[i][2],
                        DB[i][3],
                        DB[i][4],
                        DB[i][5],
                        DB[i][6],
                        DB[i][7],
                    ]
                )
    elif array == 5:
        for i in range(len(DB)):
            if int(DB[i][5]) == word:
                sortlist.append(
                    [
                        DB[i][0],
                        DB[i][1],
                        DB[i][2],
                        DB[i][3],
                        DB[i][4],
                        DB[i][5],
                        DB[i][6],
                        DB[i][7],
                    ]
                )
    elif array == 6:
        for i in range(len(DB)):
            if (word in str(DB[i][6])) == True:
                sortlist.append(
                    [
                        DB[i][0],
                        DB[i][1],
                        DB[i][2],
                        DB[i][3],
                        DB[i][4],
                        DB[i][5],
                        DB[i][6],
                        DB[i][7],
                    ]
                )
    elif array == 7:
        for i in range(len(DB)):
            if (word in str(DB[i][7])) == True:
                sortlist.append(
                    [
                        DB[i][0],
                        DB[i][1],
                        DB[i][2],
                        DB[i][3],
                        DB[i][4],
                        DB[i][5],
                        DB[i][6],
                        DB[i][7],
                    ]
                )

    print(sortlist)
    return sortlist


def csvmoneySort(DB, money, bool):
    sortlist = []
    DB = csvOrder(DB, False)

    for i in range(len(DB)):
        if bool == False and int(DB[i][4]) <= int(money):
            sortlist.append(
                [
                    DB[i][0],
                    DB[i][1],
                    DB[i][2],
                    DB[i][3],
                    DB[i][4],
                    DB[i][5],
                    DB[i][6],
                    DB[i][7],
                ]
            )
        elif bool == True and int(DB[i][4]) >= int(money):
            sortlist.append(
                [
                    DB[i][0],
                    DB[i][1],
                    DB[i][2],
                    DB[i][3],
                    DB[i][4],
                    DB[i][5],
                    DB[i][6],
                    DB[i][7],
                ]
            )

    return sortlist


# DBの値を計算
def csvCalc(DB):
    a = 0
    for i in range(len(DB)):
        a += int(DB[i][4])
    return a


"""
以下，テストモジュール
"""

"""
def outputtest(FDB,ORDER):	#最終編集結果をtest.CSVに出力 FDB:FinalDataBase
	FDB = csvOrder(FDB,ORDER)

	with open('./test.csv', mode='w',newline='',encoding='utf-8-sig') as f:

		writer = csv.writer(f)
		writer.writerows(FDB)


csvList,file = inputlist()
sort = csvmoneySort(csvList,100000,True)
outputtest(sort,False)
"""

if "__name__" == "__main__":
    list1, path = inputlist()
    list1 = listappend(
        list(("2022", "7", "16", "ユウナのガード費", "53", "収入", "ワッカ", "教えはどうなってんだ！教えは ！")),
        list1,
    )
    outputlist(list1, path, True)
