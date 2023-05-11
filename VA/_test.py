import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5) # sätt andra widgets till master = frame
frame_b = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=10)

greeting = tk.Label(text = "Skriv här", fg ="hotpink", bg ="black", width = 10, height =5, master = frame_a)

button = tk.Button(text="Klicka inte", width = 25, height =5, bg = "yellow", fg = "black", master = frame_a)
button.pack()

entry = tk.Entry(fg="white", bg = "salmon", width=50, master = frame_b)
entry.insert(0,"hej")
name = entry.get() # hämtar värdet från entry
entry.delete(0) # tar bort första i entry
greeting.pack()
entry.pack()

text_box = tk.Text(master = frame_b) # för flera rader text
text_box.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()


