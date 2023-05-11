import tkinter as tk
"""Använd pack för generellare placering
place för exakt och grid ofatst!"""

window = tk.Tk()

#frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
#frame1.pack()

#frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
#frame2.pack(fill=tk.X) # fyller hela framen med färg

#frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
#frame3.pack(side=tk.LEFT) # flyttar till vänster

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()


window.mainloop()