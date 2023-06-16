from prettytable import PrettyTable
from node import Node

init = False
tree = None

class Stock:
	def __init__(self):
		global init
		global tree

		if init == False:
			tree = Node(None)
			init = True

	def create(self):
		print("\n======= Tambah Data Stock =======")
		sku = input("SKU: ")
		nama = input("Nama: ")
		harga = input("Harga: ")
		stok = input("Stok: ")

		# Olah data menjadi dictionary
		data = {
			'sku': int(sku),
			'nama': nama,
			'harga': int(harga),
			'stok': int(stok),
		}

		# Input data ke tree
		tree.insert(data)
		
		print("Data berhasil ditambahkan!")
		# print(data)

		return True

	def restock(self):
		print("\n======= Restock Produk =======")
		sku = input("SKU: ")
		stok = input("Stok: ")

		# Olah data menjadi dictionary
		data = {
			'sku': int(sku),
			'stok': int(stok),
		}

		# Edit data ke tree
		tree.edit(data)
		
		print("Data berhasil diedit!")

		return True
	
	def show(self):
		data = tree.printTree()
		
		# remove duplicate data
		data = [i for n, i in enumerate(data) if i not in data[n + 1:]]

		if(data != None):
			table = PrettyTable(['SKU', 'Nama', 'Harga', 'Stok'])
			print("\n======= Tampilkan Data Stock =======")
			for item in data:
				table.add_row([item['sku'], item['nama'], item['harga'], item['stok']])
			print(table)

			return True
		else:
			print("Belum ada stock yang ditambahkan!")
			return True

		