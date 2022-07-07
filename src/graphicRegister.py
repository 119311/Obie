import tkinter as tk
import tkinter.font as tkFont
import sys
import datetime

from colorList import *


def RegisterData(winManager):
    print(winManager)
    regWin = tk.Tk()
    if not winManager.RegRegUp(regWin):
        regWin.destroy()
        return
    regWin.title(u"データ登録：Obie")
    regWin.geometry("640x480+0+0")
    regWin.configure(bg=appColors["lWhite"])
    regWin.resizable(width=False, height=False)

    footSize = 25
    widthLabel = 20

# ロゴ表示
    titleCanvas = tk.Canvas(regWin, width=640, height=40, bg="white")
    titleCanvas.place(x=0, y=0)
    # titleCanvas.create_image(
    #     325, 40, image=(winManager.GetLogo()), anchor=tk.CENTER)

# footer
    foot = tk.Canvas(regWin, width=660, height=footSize, bg="#083D77")
    foot.place(x=-10, y=(480-footSize))

    dt = datetime.datetime.now()

    fontTitle = tkFont.Font(
        regWin,
        family="Helve",
        size=30)
    fontLabel = tkFont.Font(
        regWin,
        family="Helve",
        size=12)

    # 変数格納
    year = tk.StringVar()
    month = tk.StringVar()
    day = tk.StringVar()
    use = tk.StringVar()
    target = tk.StringVar()
    money = tk.StringVar()
    moneyMode = tk.IntVar()
    comment = tk.StringVar()

    moneyMode.set(1)

    # ラベル
    menuTitle = tk.Label(regWin, text=u'データ登録', fg='black',
                         bg=appColors["lWhite"], font=fontTitle)
    menuTitle.place(x=230, y=50)

    lYear = tk.Label(
        regWin,
        text=u"年",
        fg="black",
        bg=appColors["lWhite"], font=fontLabel)

    lYear.place(x=100, y=120)

    iYear = tk.Entry(
        regWin,
        textvariable=year,
        font=fontLabel,
        width=widthLabel
    )
    iYear.place(x=150, y=120)
    iYear.insert(tk.END, str(dt.year))

    lMonth = tk.Label(
        regWin,
        text=u"月",
        fg="black",
        bg=appColors["lWhite"], font=fontLabel)

    lMonth.place(x=100, y=145)

    iMonth = tk.Entry(
        regWin,
        textvariable=month,
        font=fontLabel,
        width=widthLabel
    )
    iMonth.place(x=150, y=145)
    iMonth.insert(tk.END, str(dt.month))

    lDate = tk.Label(
        regWin,
        text=u"日",
        fg="black",
        bg=appColors["lWhite"], font=fontLabel)

    lDate.place(x=100, y=170)

    iDate = tk.Entry(
        regWin,
        textvariable=day,
        font=fontLabel,
        width=widthLabel
    )
    iDate.place(x=150, y=170)
    iDate.insert(tk.END, str(dt.day))

    lUse = tk.Label(
        regWin,
        text=u"用途",
        fg="black",
        bg=appColors["lWhite"], font=fontLabel)

    lUse.place(x=100, y=195)

    iUse = tk.Entry(
        regWin,
        textvariable=use,
        font=fontLabel,
        width=widthLabel
    )
    iUse.place(x=150, y=195)
    iUse.insert(tk.END, "何か")

    lTarget = tk.Label(
        regWin,
        text=u"対象",
        fg="black",
        bg=appColors["lWhite"], font=fontLabel)

    lTarget.place(x=100, y=220)

    iTarget = tk.Entry(
        regWin,
        textvariable=target,
        font=fontLabel,
        width=widthLabel
    )
    iTarget.place(x=150, y=220)
    iTarget.insert(tk.END, "母")

    lCost = tk.Label(
        regWin,
        text=u"金額",
        fg="black",
        bg=appColors["lWhite"], font=fontLabel)

    lCost.place(x=100, y=245)

    iCost = tk.Entry(
        regWin,
        textvariable=money,
        font=fontLabel,
        width=widthLabel
    )
    iCost.place(x=150, y=245)
    iCost.insert(tk.END, 33400)

    lMMode = tk.Label(
        regWin,
        text=u"収支",
        fg="black",
        bg=appColors["lWhite"], font=fontLabel)

    lMMode.place(x=100, y=270)

    rMModeA = tk.Radiobutton(
        regWin,
        text=u"収入",
        value=1,
        width=6,
        font=fontLabel,
        bg=appColors["lWhite"],
        cursor="hand2",
        variable=moneyMode)
    rMModeA.place(x=150, y=270)

    rMModeB = tk.Radiobutton(
        regWin,
        text=u"支出",
        value=2,
        width=6,
        font=fontLabel,
        bg=appColors["lWhite"],
        cursor="hand2",
        variable=moneyMode)
    rMModeB.place(x=250, y=270)

    lComment = tk.Label(
        regWin,
        text=u"ｺﾒﾝﾄ",
        fg="black",
        bg=appColors["lWhite"], font=fontLabel)

    lComment.place(x=100, y=295)

    iComment = tk.Entry(
        regWin,
        textvariable=comment,
        font=fontLabel,
        width=widthLabel
    )
    iComment.place(x=150, y=295)

    # 本登録
    bReg = tk.Button(
        regWin,
        text="入力内容を登録",
        width=widthLabel-5,
        height=3,
        bg=appColors["yellow"],
        fg="black",
        cursor="hand2",
        relief="groove",
        font=fontLabel,
        command=lambda: DataRegist(iYear.get(), iMonth.get(), iDate.get(), iUse.get(), iTarget.get(), iCost.get(), moneyMode.get(), iComment.get()))

    bReg.place(x=370, y=270)

    # CSV登録
    bCSVL = tk.Button(
        regWin,
        text="CSV読み込み/登録",
        width=widthLabel,
        height=3,
        bg=appColors["yellow"],
        relief="groove",
        font=fontLabel,
        cursor="hand2",
        fg="black")
    # command=lambda: graphicRegister.RegisterData(winManager))

    bCSVL.place(x=100, y=350)

    bCSVS = tk.Button(
        regWin,
        text="CSV書き出し",
        width=widthLabel,
        height=3,
        bg=appColors["yellow"],
        relief="groove",
        font=fontLabel,
        cursor="hand2",
        fg="black")
    # command=lambda: graphicRegister.RegisterData(winManager))

    bCSVS.place(x=350, y=350)

    bClose= tk.Button(
        regWin,
        text="閉じる",
        width=7,
        height=2,
        bg="white",
        relief="groove",
        font=fontLabel,
        cursor="hand2",
        fg="black",
        command=lambda: ClickRegClose(winManager, regWin))

    bClose.place(x=530, y=0)

    # regWin.protocol("WM_DELETE_WINDOW", ClickRegClose(winManager))
    regWin.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
    regWin.mainloop()


def DataRegist(year, month, date, use, target, cost, mode, comment):
    print([year, month, date, use, target, cost, str(mode), comment])


def ClickRegClose(winManager, win):
    winManager.RegRegDown()
