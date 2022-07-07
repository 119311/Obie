from cgitb import text
import tkinter as tk
import tkinter.font as tkFont
import sys
import datetime

from colorList import *


def ListUpHistory(winManager):
    print(winManager)
    regWin = tk.Tk()
    if not winManager.RegHisUp(regWin):
        regWin.destroy()
        return
    regWin.title(u"履歴：かけいぼ")
    regWin.geometry("640x480")
    regWin.configure(bg=appColors["lWhite"])
    regWin.resizable(width=False, height=False)

    footSize = 25

# ロゴ表示
    titleCanvas = tk.Canvas(regWin, width=640, height=40, bg="white")
    titleCanvas.place(x=0, y=0)
    # imga = tk.PhotoImage(file="./logo.png", width=135, height=80)
    # titleCanvas.create_image(325, 40, image=winManager.Getlogo(), anchor=tk.CENTER)

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


    # ラベル
    menuTitle = tk.Label(regWin, text=u'履歴', fg='black',
                         bg=appColors["lWhite"], font=fontTitle)
    menuTitle.place(x=260, y=50)

    lYear = tk.Label(
        regWin,
        text=u"年",
        fg="black",
        bg=appColors["lWhite"], font=fontLabel)

    lYear.place(x=100, y=120)

    

    bCSVS = tk.Button(
        regWin,
        text="CSV書き出し",
        width=25,
        height=3,
        bg=appColors["yellow"],
        fg="black")
    # command=lambda: graphicRegister.RegisterData(winManager))

    bCSVS.place(x=350, y=350)

    regWin.protocol("WM_DELETE_WINDOW", ClickHisClose(winManager))
    regWin.mainloop()
 
def ClickHisClose(winManager):
    winManager.RegRegDown()
