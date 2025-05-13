import tkinter as tk
from tkinter import messagebox

class Teplota:
    def __init__(self, master):
        self.master = master
        master.title("Převod teplot CFK")

        self.jednotky = ["Celsius", "Fahrenheit", "Kelvin"]

        self.lbl_teplota = tk.Label(master, text="Zadej teplotu: ")
        self.lbl_teplota.grid(row=0, column=0)
        self.entry_teplota = tk.Entry(master)
        self.entry_teplota.grid(row=0, column=1)

        self.vstup_jednotka = tk.StringVar(master)
        self.vstup_jednotka.set(self.jednotky[1])
        self.menu_z = tk.OptionMenu(master, self.vstup_jednotka, *self.jednotky)
        self.menu_z.grid(row=0, column=2)


        self.lbl_do = tk.Label(master, text="Do jednotky: ")
        self.lbl_do.grid(row=1, column=0)
        self.lbl_vysledek = tk.Label(master, text="")
        self.lbl_vysledek.grid(row=1, column=1)

        self.vystup_jednotka = tk.StringVar(master)
        self.vystup_jednotka.set(self.jednotky[1])
        self.menu_do = tk.OptionMenu(master, self.vystup_jednotka, *self.jednotky)
        self.menu_do.grid(row=1, column=2)

        tk.Button(master, text="Převést", command=self.prevest).grid(row=2, column=0)

    def prevest_hodnotu(self, hodnota, z, do):
        if z == do:
            return hodnota
        
        # Vše na Celsia
        if z == "Fahrenheit":
            hodnota = (hodnota-32)*5/9
        elif z == "Kelvin":
            hodnota = (hodnota-273.15)

        # A z Celsia do cílové jednotky
        if do == "Fahrenheit":
            return hodnota * 9/5 + 32
        elif do == "Kelvin":
            return hodnota + 273.15
        else:
            return hodnota
        
    def prevest(self):
        try:
            vstup = float(self.entry_teplota.get())
            z = self.vstup_jednotka.get()
            do = self.vystup_jednotka.get()

            vysledek = self.prevest_hodnotu(vstup, z, do)
            self.lbl_vysledek.config(
                text=vysledek
            )
        except ValueError as e:
            messagebox.showerror("Chyba", "Zadej platnou hodnotu! ")



if __name__=="__main__":
    root = tk.Tk()
    app = Teplota(root)
    root.mainloop()