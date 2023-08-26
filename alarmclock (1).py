import tkinter as tk
from tkinter import messagebox
import time
import pygame

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Disha's Alarm Clock")
        self.root.configure(bg="pink")

        self.label = tk.Label(root, text="Set Alarm Time (HH:MM:SS)", font=("Helvetica", 14, "bold"), bg="pink", fg="white")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Helvetica", 12))
        self.entry.pack(pady=5)

        self.set_button = tk.Button(root, text="Set Alarm", command=self.set_alarm, font=("Helvetica", 12))
        self.set_button.pack(pady=10)

    def set_alarm(self):
        alarm_time = self.entry.get()
        try:
            alarm_hour, alarm_minute, alarm_second = map(int, alarm_time.split(':'))
            current_time = time.localtime()
            current_hour = current_time.tm_hour
            current_minute = current_time.tm_min
            current_second = current_time.tm_sec

            remaining_seconds = (alarm_hour - current_hour) * 3600 + (alarm_minute - current_minute) * 60 + 
            (alarm_second - current_second)

            if remaining_seconds <= 0:
                pygame.init()
                pygame.mixer.music.load("KrishnaFlute.mp3")  # Provide the path to your alarm sound file
                pygame.mixer.music.play()
                messagebox.showinfo("Alarm", "Wake up Disha 🐼!")
            else:
                time.sleep(remaining_seconds)
                pygame.init()
                pygame.mixer.music.load("KrishnaFlute.mp3")  # Provide the path to your alarm sound file
                pygame.mixer.music.play()
                messagebox.showinfo("Alarm", "Wake up Disha 🐼!")

        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Please use HH:MM:SS.")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="pink")
    alarm_clock = AlarmClock(root)
    root.mainloop()
