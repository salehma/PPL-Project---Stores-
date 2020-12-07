from lxml import html
import requests

class SubClassResponsibilty(Exception):
	pass

class Branch():
	def __init__(self,name,location,hebrew_names=[],rank = 0, price = 0, company = ''):
		self.company = company
		self.name = name
		self.long = location[0]
		self.latt = location[1]
		self.hebrew_names = hebrew_names
		self.rank = rank
		self.price = 0

	def __str__(self):
		location = f'({self.long}, {self.latt})'
		s = '\t\t\tBranch("'
		s += self.name
		s += '",'
		s += ' '*(45 - len(s))
		s += location
		s += ','
		s += ' '*(90 - len(s))
		s += f'hebrew_names={self.hebrew_names},'	
		s += ' '*(140 - len(s))
		s += f'rank={self.rank},'
		s += ' '*(160 - len(s))
		s += f'price={self.price},'
		s += ' '*(180 - len(s))
		s += f'company="{self.company}")'
		return s
	def set_rank(self,rank):
		self.rank = rank
	def copy(self):
		return Branch(self.name, (self.long, self.latt), hebrew_names=[s for s in self.hebrew_names], rank=self.rank,price=self.price, company = self.company)


class Store():
	branches = []
	def page_getter(self,url):
		if url == []:
			raise Exception
		return requests.get(url,headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'})     #Delegation DP
	def build_html_tree(self,page):
		return  html.fromstring(page)   #Delegation DP
	def updated_price(self):
		raise SubClassResponsibilty('Abstract Class.')
	def get_available_branches(self):
		raise SubClassResponsibilty('Abstract Class.')
	def get(self):
		pass
	def set_rank(self,rank):
		for b in self.branches:
			b.set_rank(rank)
	def set_prices(self,branches):
		normal_price,eilat_price = self.updated_price()
		for b in branches:
			if 'Eilat' in b.name:
				b.price = eilat_price
			else:
				b.price = normal_price
		return branches 
	def set_company_names(self):
		for b in self.branches:
			b.company = self.company



	"""
	every subclass of Store ingerits the global property barnches.
	its sub-class responsibility to implement it, the following function 
	returns an object that correspond to the Branch with the given name
	"""
	def branch_from_hebrew_name(self,name,comparator=lambda x,y: y in x):
		res = [branch for  branch in self.branches if comparator(branch.hebrew_names,name)]
		return res[0] if len(res) > 0 else None 




