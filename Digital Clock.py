from tkinter import Tk, Label
import time

def get_time():
    timeVar = time.strftime("%H:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, get_time)

def update_clock_color():
    
    current_color = clock["fg"]
    next_color = colors[(colors.index(current_color) + 1) % len(colors)]
    clock.config(fg=next_color)
    master.after(1000, update_clock_color)

master = Tk()
master.title("Disha's Color Clock 🐼")
master.geometry("400x200")
master.configure(bg="black")

colors = ["cyan", "magenta", "yellow", "green", "red", "blue", "white"]  # Custom gradient colors

font_style = ("Digital-7", 80, "bold")  # Use a high-tech font style

Label(master, font=("Arial", 20, "bold"), text="Disha's Color Clock 🐼", fg="cyan", bg="black").pack(pady=10)
clock = Label(master, font=font_style, bg="black", fg="cyan")
clock.pack()

get_time()
update_clock_color()
master.mainloop()
