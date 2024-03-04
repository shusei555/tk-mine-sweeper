"""
・ルール
地雷のマスを踏まないようにマスを開ける
隣接している方向に地雷があるとき地雷の数を表示する
隣り合っている地雷がないとき自動で隣接しているマスを開く
地雷ではない場所をすべて開けばクリア
・仕様
10*10
旗と探知は切り替え式
爆弾の数は10個
"""
import tkinter as tk
import random

button_list = []
def show_map(mine_map):
    for i in range(10):
        for j in range(10):
            print(mine_map[i][j],end="")
        print()
    print("-"*10)

def click_btn (x,y):
    a=int(x)
    b=int(y)
    open_block([(a+1)* 10+(b+1)],(a+1)* 10+(b+1))
    
def open_block(previous_list, current):
    global button_count
    #print(previous_list,current)
    i = current // 10 - 1
    j = current % 10 - 1
    if current % 10 == 0:#右端の時
        i = i - 1
        j = 9
    #print(i,j)
    if mine_map[i][j] == 0:
        mine_map[i][j] = "*"
        button_list[i][j].configure(bg = "green")
        full_open(previous_list,current)
    elif mine_map[i][j] != -1:
        button_list[i][j].configure(text=mine_map[i][j], bg = "green")
    else:
        button_list[i][j].configure(bg = "red")
        print("ゲームオーバー")

def full_open(previous_list,current):
    number = current - 11

    def isUpLimit():
        return number >= 10
    def isDownLimit():
        return number < 90
    def isRightLimit():
        return number % 10 != 9
    def isLeftLimit():
        return number % 10 != 0

    if isUpLimit() and isRightLimit():
        open_block(previous_list,current-9)#右上
    if isDownLimit() and isRightLimit():
        open_block(previous_list,current+11)#右下
    if isUpLimit() and isLeftLimit():
        open_block(previous_list,current-11)#左上
    if isDownLimit() and isLeftLimit():
        open_block(previous_list,current+9)#左下
    if (isUpLimit()):
        open_block(previous_list,current-10)#上
    if (isRightLimit()):
        open_block(previous_list,current+1)#右
    if (isDownLimit()):
        open_block(previous_list,current+10)#下
    if (isLeftLimit()):
        open_block(previous_list,current-1)#左

root = tk.Tk()
root.geometry("380x500")

mine_list=[]
mine_map=[]

while len(mine_list)<=9:
    mine=random.randint(0,99)
    if mine in mine_list:
        continue
    mine_list.append(mine)
# print(mine_list)
change_button = tk.Button(root,width=10,height=5,text="")
#change_button.pack()
for i in range(10):
    row = []
    brow = []
    for j in range(10):
        a_button=tk.Button(root,width=4,height=2, command=lambda x=(str(i)+","+str(j)).split(",") : click_btn(x[0], x[1]))
        a_button.grid(row=i,column=j)
        if 10*i+ j in mine_list:
            row.append(-1)
        else :
            row.append(0)
        brow.append(a_button)
    button_list.append(brow)    
    mine_map.append(row)
show_map(mine_map)

for i in range(10):
    for j in range(10):
        if mine_map[i][j]== -1:
            continue
        for y in range(-1,2):
            for x in range(-1,2):
                a = i + y
                b = j + x
                if a<0 or b<0 or a>=10 or b>=10:
                    continue
                if mine_map[a][b] == -1:
                    mine_map[i][j] = mine_map[i][j]+1
show_map(mine_map)
root.mainloop()
