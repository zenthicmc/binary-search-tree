from node import Node
from prettytable import PrettyTable

transaction_list = []

init = False
bst = None

class Transaction():
    def __init__(self):
        global init
        global bst
        
        if init == False:
            bst = Node(None)
            init = True

    def input_transaction(self):
        print("\n======= Masukkan Transaksi Baru =======")
        nama_konsumen = input("Nama Konsumen: ")
        sku = int(input("SKU: "))
        sum_beli = int(input("Jumlah Pembelian: "))
  
        product = bst.get_data_by_sku(sku)

        if product is None:
            print("Barang yang diinputkan belum terdaftar.")
            choice = input("Apakah ingin melanjutkan transaksi (Y/N)? ")
            if choice == 'y':
                self.input_transaction()
            return
         
        if sum_beli > product['stok']:
            print("Jumlah Stok No. SKU yang Anda beli tidak mencukupi.")
            choice = input("Apakah ingin melanjutkan transaksi (Y/N)? ")
            if choice == 'y':
                self.input_transaction()
            return

        subtotal = sum_beli * product['harga']

        transaction_list.append([nama_konsumen, sku, sum_beli, subtotal])
        print("Transaksi berhasil ditambahkan!")

        # cek apakah data sudah terinput
        # print(transaction_list)


    def show_transaction(self):
        print("\n======= Data Transaksi =======")
        table = PrettyTable()
        column_names = ['Nama', 'SKU','Jumlah Beli','Subtotal']
        table.field_names = column_names

        for data in transaction_list:
            table.add_row(data)
        print(table)
        return True

    def show_transaction_by_subtotal(self):
        table = PrettyTable()
        column_names = ['Nama', 'SKU','Jumlah Beli','Subtotal']
        table.field_names = column_names

        sorted_transactions = self.quicksort_transactions()
        for transaction in sorted_transactions:
            table.add_row(transaction)
        print(table)
        return True

    def quicksort_transactions(self):
        transactions = transaction_list
        if len(transactions) <= 1:
            return transactions
        else:
            # Set pivot dari subtotal
            pivot = transactions[0][3]  
            less = []
            greater = []
            equal = []
            for transaction in transaction_list:
                if transaction[3] < pivot:
                    less.append(transaction)
                elif transaction[3] > pivot:
                    greater.append(transaction)
                else:
                    equal.append(transaction)
        
            return greater + equal + less