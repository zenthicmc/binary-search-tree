from stock import Stock

class Menu:
	def main(self):
		print("\n=========== Aplikasi Retail ===========")
		print("1. Kelola Stok Barang")
		print("2. Kelola Transaksi Konsumen")

		choice = input("\nPilih menu: ")

		if choice == '1':
			self.menu_stock()
		elif choice == '2':
			self.menu_transaksi()

	def menu_stock(self):
		while True:
			print("\n=========== Kelola Stock Barang ===========")
			print("1. Input Data Stok Barang")
			print("2. Restock Barang")
			print("3. Tampilkan Data Stok Barang [Tambahan]")
			print("\n0. Kembali")

			choice = input("\nPilih menu: ")

			if choice == '1':
				Stock().create()
			elif choice == '2':
				Stock().restock()
			elif choice == '3':
				Stock().show()
			elif choice == '0':
				self.main()

	def menu_transaksi(self):
		# code goes here
		pass

				
# Jalankan aplikasi
if __name__ == '__main__':
	menu = Menu()
	menu.main()
