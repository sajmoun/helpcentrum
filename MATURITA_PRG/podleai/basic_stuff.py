import tkinter as tk
from tkinter import messagebox

class Obdelnik:
    def __init__(self, master):
        self.master = master
        master.title("Obdelník")

        self.lbl_delka = tk.Label(master, text="Délka: ")
        self.lbl_delka.grid(row=0, column=0)

        self.entry_delka = tk.Entry(master)
        self.entry_delka.grid(row=0, column=1)

        self.lbl_sirka = tk.Label(master, text="Šířka: ")
        self.lbl_sirka.grid(row=1, column=0)

        self.entry_sirka = tk.Entry(master)
        self.entry_sirka.grid(row=1, column=1)

        self.vysledek = tk.Label(master, text="", fg="blue")
        self.vysledek.grid(row=2, column=0)

        self.btn_spocitat = tk.Button(master, text="Spočítat", command=self.spocitat)
        self.btn_spocitat.grid(row=3, column=0)


    def spocitat(self):
        try:
            delka = float(self.entry_delka.get())
            sirka = float(self.entry_sirka.get())

            if sirka <= 0 or delka <= 0:
                raise ValueError("Hodnoty musí být kladné! ")
            
            obvod = 2*(delka + sirka)
            obsah = delka * sirka

            self.vysledek.config(
                text=f"Obvod: {obvod} jednotek\nObsah: {obsah} jednotek"
            )
        except ValueError as e:
            messagebox.showerror("Chyba", f"Neplatný vstup {e}")
            self.vysledek.config(text="")
            
if __name__=="__main__":
    root = tk.Tk()
    app = Obdelnik(root)
    root.mainloop()