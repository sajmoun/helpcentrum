import tkinter as tk
from tkinter import ttk
import time

SECTION_TIME = 400  # 6 min 40 sec 
TOTAL_SECTIONS = 3 # 3 části

class ExamTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Časovač u zkoušek")
        self.running = False
        self.current_section = 1
        self.time_left = SECTION_TIME

        self.create_widgets()
        self.update_clock()

    def create_widgets(self):
        self.time_label = ttk.Label(self.root, text="00:00", font=("Helvetica", 48))
        self.time_label.pack(pady=10)

        self.section_label = ttk.Label(self.root, text="Část: 1 / 3", font=("Helvetica", 24))
        self.section_label.pack(pady=5)

        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate", maximum=SECTION_TIME)
        self.progress.pack(pady=10)

        self.toggle_btn = ttk.Button(self.root, text="Spustit", command=self.toggle_timer)
        self.toggle_btn.pack(pady=5)

        self.reset_btn = ttk.Button(self.root, text="Restart", command=self.reset_timer)
        self.reset_btn.pack(pady=5)

        self.clock_label = ttk.Label(self.root, text="", font=("Helvetica", 14))
        self.clock_label.pack(pady=10)

    def update_clock(self):
        self.clock_label.config(text=time.strftime("Aktuální čas: %H:%M:%S"))
        self.root.after(1000, self.update_clock)

    def toggle_timer(self):
        if not self.running:
            self.running = True
            self.toggle_btn.config(text="Pozastavit")
            self.run_timer()
        else:
            self.running = False
            self.toggle_btn.config(text="Spustit")

    def reset_timer(self):
        self.running = False
        self.current_section = 1
        self.time_left = SECTION_TIME
        self.toggle_btn.config(text="Spustit")
        self.update_display()

    def run_timer(self):
        if self.running and self.current_section <= TOTAL_SECTIONS:
            if self.time_left > 0:
                self.time_left -= 1
                self.update_display()
                self.root.after(1000, self.run_timer)
            else:
                self.current_section += 1
                if self.current_section <= TOTAL_SECTIONS:
                    self.time_left = SECTION_TIME
                    self.update_display()
                    self.root.after(1000, self.run_timer)
                else:
                    self.running = False
                    self.toggle_btn.config(text="Spustit")

    def update_display(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.time_label.config(text=f"{minutes:02}:{seconds:02}")
        self.section_label.config(text=f"Část: {self.current_section} / {TOTAL_SECTIONS}")
        self.progress["value"] = SECTION_TIME - self.time_left

if __name__ == "__main__":
    root = tk.Tk()
    app = ExamTimerApp(root)
    root.mainloop()
