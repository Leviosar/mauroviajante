class Person:
	def __init__(self, name, cpf):
		self.name = name
		self.cpf = cpf

	def __repr__(self):
		return f'Nome: {self.name}\nCPF: {self.cpf}'