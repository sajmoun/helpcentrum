import tkinter as tk
from tkinter import messagebox

class Todo:
    def __init__(self, master):
        self.master = master
        self.master.title("ToDoList")

        # Label a Entry pro zadání nového úkolu
        tk.Label(master, text="Přidej název úkolu: ").grid(row=0, column=0)
        self.entry_ukol = tk.Entry(master)
        self.entry_ukol.grid(row=0, column=1)

        # Frame pro zobrazení úkolů
        self.newone = tk.Frame(self.master)
        self.newone.grid(row=1, column=0, columnspan=3)

        # Tlačítko pro přidání úkolu
        tk.Button(master, text="Přidat úkol", command=self.novy_ukol).grid(row=0, column=2)

        # Seznam pro uchování úkolů a jejich tlačítek
        self.ukoly = []

    def novy_ukol(self):
        # Ověření, že úkol není prázdný
        if self.entry_ukol.get() == "":
            messagebox.showerror("Chyba", "Špatně zadáno!")
            return
        
        # Vytvoření nového Labelu s úkolem a Buttonu pro mazání
        task_label = tk.Label(self.newone, text=self.entry_ukol.get(), bg="lightblue", width=40, anchor="w")
        task_label.pack(pady=5)

        # Oddělovací čára
        separator = tk.Canvas(self.newone, height=2, bg='black', bd=0, relief='flat')
        separator.pack(fill='x', pady=5)

        done_button = tk.Button(self.newone, text="Done", command=lambda: self.done(task_label))
        done_button.pack()

        # Vytvoření tlačítka pro smazání úkolu, přidání do seznamu úkolů
        delete_button = tk.Button(self.newone, text="Delete", command=lambda: self.delete(task_label, delete_button, separator, done_button))
        delete_button.pack(pady=5)


        # Vyprázdnění textového pole pro nový úkol
        self.entry_ukol.delete(0, tk.END)

    def delete(self, task_label, delete_button, separator, done_button):
        # Smazání úkolu, tlačítka a oddělovače
        task_label.destroy()
        delete_button.destroy()
        separator.destroy()
        done_button.destroy()
    
    def done(self, task_label):
        task_label.config(bg="green")

# Vytvoření okna aplikace
if __name__ == "__main__":
    root = tk.Tk()
    app = Todo(root)
    root.mainloop()
