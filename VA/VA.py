import tkinter as tk
import random
import math
from colors import is_color  # funktion för att kolla om färgen är godkänd av tkinter


class Ball:  # skapar en representation av en boll
    def __init__(self, color_list, radius):
        self.x1 = random.randint(hole_size+radius+1, width-radius-1)  # ska skapas innanför rutan (ej i svarta rutan)
        self.y1 = random.randint(hole_size+radius+1, height-radius-1)
        self.speed = [random.randint(-15, 15), random.randint(-15, 15)]  # slumpad hastighet
        self.x_speed = self.speed[0]
        self.y_speed = self.speed[1]
        self.color = random.randint(0, len(color_list)-1)  # slumpad färg


class MyCanvas:
    def __init__(self, n, update_speed, color_list, radius):
        self.update_speed = update_speed
        self.colors = color_list
        self.balls = []  # håller koll på representationen av bollarna
        self.bs = []  # håller koll på bollarna vi ser
        self.radius = radius
        for i in range(n):
            ball = Ball(color_list, self.radius)
            self.balls.append(ball)
            b = canvas.create_oval(ball.x1 - self.radius, ball.y1 - self.radius, ball.x1 + self.radius,
                                   ball.y1 + self.radius, fill=self.colors[ball.color], tags='Ball')
            self.bs.append(b)

    def move_ball(self):
        def distance(b1, b2):  # om två bollar krockar
            leftpos1, toppos1, rightpos1, bottompos1 = canvas.coords(b1)
            leftpos2, toppos2, rightpos2, bottompos2 = canvas.coords(b2)
            center1 = [rightpos1 - self.radius, bottompos1 + self.radius]
            center2 = [rightpos2 - self.radius, bottompos2 + self.radius]
            if math.sqrt(((center1[0] - center2[0]) ** 2 + (center1[1] - center2[1]) ** 2)) < self.radius*2:
                return True
            else:
                return False

        def krock(b1, ball1, b2, ball2):
            x = random.randint(0, 1)  # slumpmässigt vilken boll som färgar av sig
            if x == 0:
                canvas.itemconfig(b1, fill=self.colors[ball2.color])
                ball1.color = ball2.color
            else:
                canvas.itemconfig(b2, fill=self.colors[ball2.color])
                ball2.color = ball1.color

        b_list = list(zip(self.bs, self.balls))
        for b, ball in b_list:  # ska flytta alla bollar i listan
            canvas.move(b, ball.x_speed, ball.y_speed)

            try:
                leftpos, toppos, rightpos, bottompos = canvas.coords(b)  # bollens position
            except ValueError:  # funktionen fortsätter även när bollarna från tidigare omgångar raderats
                return

            if leftpos <= 0 or rightpos >= width:  # om bollen slår i kanten
                ball.x_speed = -ball.x_speed

            if toppos <= 0 or bottompos >= height:
                ball.y_speed = -ball.y_speed

            for i, j in b_list[b_list.index((b, ball)):]:  # bollarna ska bara krocka en gång med varandra
                if distance(b, i):
                    krock(b, ball, i, j)

            if rightpos <= hole_size and bottompos <= hole_size:  # om de ramlar ut
                canvas.delete(b)
                b_list.remove((b, ball))
                self.bs.remove(b)
                self.balls.remove(ball)

        canvas.after(self.update_speed, self.move_ball)  # uppdatera animationen


def start():
    radius = 20
    canvas.delete('Ball')
    num_b = int(num_b_entry.get())
    update_speed = int(speed_entry.get())
    color_list = colors_entry.get().split(', ')
    for c in color_list:
        if not is_color(c):  # kontrollerar input
            color_list.remove(c)
    if color_list == []:  # annars kör vi med standard listan
        color_list = ['red', 'yellow', 'blue']
    if num_b >= 0:  # vi kan inte ha negativt antal bollar
        ball = MyCanvas(num_b, update_speed, color_list, radius)
        ball.move_ball()
    else:
        raise ValueError("Negative numbers not allowed")
    num_b_entry.delete(0, tk.END)  # återställ default värden
    num_b_entry.insert(tk.END, "5")
    speed_entry.delete(0, tk.END)
    speed_entry.insert(tk.END, "40")
    colors_entry.delete(0, tk.END)
    colors_entry.insert(tk.END, "red, blue, yellow")


def stop():  # stäng programmet
    window.quit()


window = tk.Tk()
window.resizable(False, False)

"""Kod för start och stopp knapparna"""
big_frame = tk.Frame(master=window)

button_frame1 = tk.Frame(master=big_frame, relief=tk.RIDGE, borderwidth=10)
button_frame2 = tk.Frame(master=big_frame, relief=tk.RIDGE, borderwidth=10)

start_label = tk.Label(text="Klicka på START för att börja", bg='white', fg='black', master=button_frame1)
start_button = tk.Button(text="START", bg='green', fg='white', master=button_frame1, command=start)
start_label.pack()
start_button.pack()

stop_label = tk.Label(text="Klicka på STOP för att avsluta", bg='white', fg='black', master=button_frame2)
stop_button = start_button = tk.Button(text="STOP", bg='red', fg='white', master=button_frame2, command=stop)
stop_label.pack()
stop_button.pack()

button_frame1.pack()
button_frame2.pack()

"""Kod för användar input"""
num_b_frame = tk.Frame(master=big_frame, relief=tk.RIDGE, borderwidth=10)
num_b_label = tk.Label(text="Hur många bollar vill du skapa?", master=num_b_frame)
num_b_entry = tk.Entry(fg="black", master=num_b_frame)
num_b_entry.insert(tk.END, "5")
num_b_label.pack()
num_b_entry.pack()
num_b_frame.pack()

speed_entry_frame = tk.Frame(master=big_frame, relief=tk.RIDGE, borderwidth=10)
speed_entry_label = tk.Label(text="Vilken hastighet på animationen?", master=speed_entry_frame)
speed_entry = tk.Entry(fg="black", master=speed_entry_frame)
speed_entry.insert(tk.END, "40")
speed_entry_label.pack()
speed_entry.pack()
speed_entry_frame.pack()

colors_entry_frame = tk.Frame(master=big_frame, relief=tk.RIDGE, borderwidth=10)
colors_entry_label = tk.Label(text="Skriv dina färger med komma mellan", master=colors_entry_frame)
colors_entry = tk.Entry(fg="black", master=colors_entry_frame)
colors_entry.insert(tk.END, "red, blue, yellow")
colors_entry_label.pack()
colors_entry.pack()
colors_entry_frame.pack()

big_frame.pack(side=tk.LEFT)

"""Skapa spelramen"""
game_frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=10)
width = 800
height = 600
canvas = tk.Canvas(game_frame, bg='snow', width=width, height=height)
hole_size = 80
canvas.create_rectangle(0, 0, hole_size, hole_size, fill='black')
canvas.pack()

game_frame.pack(fill=tk.BOTH, expand=True)


window.mainloop()
