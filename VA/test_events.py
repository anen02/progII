import tkinter as tk

window = tk.Tk()

# Assume that this list gets updated automatically
events = []

# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")

button.bind("<Button-1>", handle_click)

# Run the event loop
#while True:
    # If the event list is empty, then no events have occurred
    # and you can skip to the next iteration of the loop
    #if events == []:
    #    continue

    # If execution reaches this point, then there is at least one
    # event object in the event list
    #event = events[0]


# run the event loop
window.mainloop()