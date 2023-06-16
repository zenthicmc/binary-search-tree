from node import Node

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
        print(transaction_list)


    def show_transaction(self):
        print("\n======= Masukkan Transaksi Baru =======")
        for i in transaction_list:
            print("Nama Konsumen:", i.nama_konsumen)
            print("No. SKU barang yang dibeli:", i.sku)
            print("Jumlah Beli:", i.sum_beli)
            print("Subtotal:", i.subtotal)

    def show_transaction_by_subtotal(self):
        sorted_transactions = self.quicksort_transactions(transaction_list)
        for transaction in sorted_transactions:
            print(transaction)

    def quicksort_transactions(transactions):
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