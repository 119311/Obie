import tkinter as tk
import tkinter.font as tkFont
import sys
import datetime

import graphicRegister
import graphicHistory
from graphicStatus import *
from colorList import *


def main():
    root = tk.Tk()
    root.title("Obie")
    root.geometry("640x480")
    root.configure(bg=appColors["lWhite"])
    root.resizable(width=False, height=False)

    font = tkFont.Font(root, family="Helve", size=30)

    fontLabel = tkFont.Font(root, family="Helve", size=12)

    fontMonth = tkFont.Font(root, family="Helve", size=17)

    fontDate = tkFont.Font(root, family="Helve", size=24)

    winManager = WinManager()
    print(winManager)

    footSize = 25

    # ロゴ表示
    titleCanvas = tk.Canvas(root, width=640, height=80, bg="white")
    titleCanvas.place(x=0, y=0)
    img = tk.PhotoImage(file="./asset/logo.png", width=135, height=80)
    winManager.RegLogo(img)
    print(img)
    titleCanvas.create_image(325, 40, image=img, anchor=tk.CENTER)

    # footer
    foot = tk.Canvas(root, width=660, height=footSize, bg="#083D77")
    foot.place(x=-10, y=(480 - footSize))

    # ラベル
    # menuTitle = tk.Label(root, text=u'かけいぼ', fg='black',
    #                      bg=appColors["lWhite"], font=font)
    # menuTitle.place(x=250, y=100)
    welcome = tk.Label(
        root,
        text="おかえりなさい！Obieへようこそ！",
        font=fontMonth,
        fg="black",
        bg=appColors["lWhite"],
    )
    welcome.place(x=160, y=100)
    dateBoxm = tk.Label(
        root, text="Today", font=fontMonth, fg="black", bg=appColors["lWhite"]
    )
    dateBoxm.place(x=435, y=200)
    dateBoxm = tk.Label(
        root,
        text=datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=9))
        ).strftime("%b"),
        font=fontMonth,
        fg="black",
        bg=appColors["lWhite"],
    )
    dateBoxm.place(x=400, y=239)
    dateBox = tk.Label(
        root,
        text=datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=9))
        ).strftime("%d(%a)"),
        font=fontDate,
        fg="black",
        bg=appColors["lWhite"],
    )
    dateBox.place(x=440, y=230)

    menuReg = tk.Button(
        root,
        text="データ登録",
        width=25,
        height=3,
        bg=appColors["orange"],
        fg="white",
        font=fontLabel,
        relief="groove",
        cursor="hand2",
        command=lambda: graphicRegister.RegisterData(winManager),
    )

    menuReg.place(x=70, y=200)

    menuHis = tk.Button(
        root,
        text="履歴",
        width=25,
        height=3,
        bg=appColors["yellow"],
        fg="black",
        font=fontLabel,
        relief="groove",
        cursor="hand2",
        command=lambda: graphicHistory.ListUpHistory(winManager),
    )

    menuHis.place(x=70, y=300)

    menuSub = tk.Button(
        root,
        text="サブスク情報",
        width=25,
        height=3,
        bg=appColors["orange"],
        fg="white",
        font=fontLabel,
        relief="groove",
        cursor="hand2",
        command=lambda: graphicRegister.RegisterData(winManager),
    )

    menuSub.place(x=350, y=300)

    bClose = tk.Button(
        root,
        text="閉じる",
        width=7,
        height=2,
        bg="white",
        relief="groove",
        font=fontLabel,
        cursor="hand2",
        fg="black",
        command=lambda: ClickRootClose(winManager, root),
    )

    bClose.place(x=530, y=0)

    root.mainloop()


def ClickRootClose(winManager, win):
    winManager.AllClose()
    win.destroy()


if __name__ == "__main__":
    main()


"""
カラーリスト(メモ)
#083D77
#EBEBD3
#F4D35E
#EE964B
#F95738
"""
