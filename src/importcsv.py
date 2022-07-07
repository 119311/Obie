import csv
import tkinter
from tkinter import filedialog

idir = 'r119312@c-19:\\D4\\kakeibo\\'
file_path = tkinter.filedialog.askopenfilename(initialdir = idir)

def inputlist():
	with open(file_path, mode='r', encoding='utf-8-sig') as f:
		list = [row for row in csv.reader(f)]
	return list

def listappend(a):
	x = ['2022', '4', '1', '学費', '19550', '2', '長男', '高専学費月額']	#imputには日付等の入力データの配列が入る
	a.append(x)
	return a

def outputlist(a):
	with open('./test.csv', mode='w',newline='') as f:
		writer = csv.writer(f)
		writer.writerows(a)

i = inputlist()
list = listappend(i)

print(i)
print(list)
outputlist(list)