import tkinter as tk
from tkinter import messagebox

class AplikasiKeuangan:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pencatat Keuangan")

        self.saldo = 0

        # Label dan Entry untuk jumlah
        self.label_jumlah = tk.Label(root, text="Jumlah:")
        self.label_jumlah.grid(row=0, column=0, padx=10, pady=10)
        self.entry_jumlah = tk.Entry(root)
        self.entry_jumlah.grid(row=0, column=1, padx=10, pady=10)

        # Label dan Entry untuk jenis transaksi
        self.label_jenis = tk.Label(root, text="Jenis (Pemasukan/Pengeluaran):")
        self.label_jenis.grid(row=1, column=0, padx=10, pady=10)
        self.entry_jenis = tk.Entry(root)
        self.entry_jenis.grid(row=1, column=1, padx=10, pady=10)

        # Tombol untuk menyimpan transaksi
        self.tombol_simpan = tk.Button(root, text="Simpan", command=self.simpan_transaksi)
        self.tombol_simpan.grid(row=2, column=0, columnspan=2, pady=10)

        # Label untuk menampilkan saldo
        self.label_saldo = tk.Label(root, text="Saldo: 0")
        self.label_saldo.grid(row=3, column=0, columnspan=2, pady=10)

    def simpan_transaksi(self):
        try:
            jumlah = float(self.entry_jumlah.get())
            jenis = self.entry_jenis.get().lower()

            if jenis == "pemasukan":
                self.saldo += jumlah
            elif jenis == "pengeluaran":
                self.saldo -= jumlah
            else:
                messagebox.showerror("Error", "Jenis transaksi harus 'Pemasukan' atau 'Pengeluaran'.")

            # Menampilkan saldo terbaru
            self.label_saldo.config(text=f"Saldo: {self.saldo:.2f}")

            # Mengosongkan field input setelah transaksi disimpan
            self.entry_jumlah.delete(0, tk.END)
            self.entry_jenis.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Masukkan jumlah dengan benar.")

if __name__ == "__main__":
    root = tk.Tk()
    aplikasi = AplikasiKeuangan(root)
    root.mainloop()