data = []

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def insert(self, data):
		if self.data:
			if data['sku'] < self.data['sku']:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data['sku'] > self.data['sku']:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data

	def edit(self, data):
		search = self.search(data['sku'])
		if search == False:
			return False
		else:
			search['stok'] = data['stok']
			return True
		

	def printTree(self):
		if self.left:
			self.left.printTree()
		data.append(self.data)
		if self.right:
			self.right.printTree()

		return data

	def search(self, val):
		if val < self.data['sku']:
			if self.left is None:
				return False
			return self.left.search(val)
		elif val > self.data['sku']:
			if self.right is None:
				return False
			return self.right.search(val)
		else:
			return self.data