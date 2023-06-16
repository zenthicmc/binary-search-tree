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
		# modify
		if self.data is None or self.data['sku'] == val:
			return self

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
		
	def search_by_sku(self, val):
		data = self.printTree()

		if self.data and self.data['sku'] == val:
			return self.data
		if val < self.data['sku'] and self.left:
			return self.left.search_by_sku(val)
		elif val > self.data['sku'] and self.right:
			return self.right.search_by_sku(val)
		return None