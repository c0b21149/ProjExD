import tkinter as tk
import maze_maker as mm #練習8

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

#練習７
def main_proc():
    global cx,cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    canv.coords("tori",cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#練習１

    #練習２
    canv = tk.Canvas(root,width=1500,height=900,bg="black")
    canv.pack()

    #練習９
    maze_lst = mm.make_maze(15,9)
    #print(maze_lst)
    mm.show_maze(canv,maze_lst)

    #練習３
    tori = tk.PhotoImage(file = "ex03/fig/5.png")
    cx, cy = 300, 400
    canv.create_image(cx,cy,image=tori,tag="tori")

    #練習４
    key = ""#現在押されているキーを表す

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    #練習７
    main_proc()

    root.mainloop()