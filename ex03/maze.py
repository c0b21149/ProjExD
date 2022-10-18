import tkinter as tk
import maze_maker as mm #練習8

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def count_up():
    global tmr
    tmr += 1
    label["text"] = tmr
    root.after(1000,count_up)

#練習７
def main_proc():
    global cx,cy
    global mx, my
    global tori
    delta = {
        ""     :[0,0],
        "Up"   :[0,-1],
        "Down" :[0,+1],
        "Left" :[-1,0],
        "Right":[+1,0],
    }

    if maze_lst[my+delta[key][1]][mx+delta[key][0]] == 0:
        mx, my = mx+delta[key][0], my+delta[key][1]
        cx, cy = mx*100+50, my*100+50
        #画像変更
        if key == "Up" or key == "Down":
            tori = tk.PhotoImage(file = ud_png)
            canv.create_image(cx,cy,image=tori,tag="tori")
        if key == "Right":
            tori = tk.PhotoImage(file = r_png)
            canv.create_image(cx,cy,image=tori,tag="tori")
        if key == "Left":
            tori = tk.PhotoImage(file = l_png)
            canv.create_image(cx,cy,image=tori,tag="tori")
    else: #壁に向かって進もうとする場合
        tori = tk.PhotoImage(file = "ex03/fig/0.png")
        canv.create_image(cx,cy,image=tori,tag="tori")
    canv.coords("tori",cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#練習１

    ud_png = "ex03/fig/3.png"
    r_png = "ex03/fig/2.png"
    l_png = "ex03/fig/5.png"

    #カウントアップ
    tmr = 0
    label = tk.Label(root, font=(" ",40),anchor=tk.CENTER)
    label.pack()
    root.after(1000, count_up)

    #練習２
    canv = tk.Canvas(root,width=1500,height=900,bg="black")
    canv.pack()

    #練習９
    maze_lst = mm.make_maze(15,9)
    #print(maze_lst)
    mm.show_maze(canv,maze_lst)

    #練習３
    tori = tk.PhotoImage(file = "ex03/fig/5.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx,cy,image=tori,tag="tori")

    #練習４
    key = ""#現在押されているキーを表す

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    #練習７
    main_proc()

    root.mainloop()