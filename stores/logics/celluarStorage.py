from .store import Store,Branch

class celluarStorage(Store):
	Store.branches = [
			Branch("Tel Aviv",                         (32.07399160584907, 34.78196575971365),      hebrew_names=['מלאי סניף תל אביב '],                          rank=0.0),
			Branch("Jerusalim",                        (31.78219331317655, 35.216680699684325),     hebrew_names=['מלאי סניף ירושלים '],           rank=0.0)
			]
	def __init__(self,url):
		self.url = url
		self.company = "Celluar Store"
		self.set_company_names()
	def updated_price(self):
		url = self.url
		page = self.page_getter(url)
		tree = self.build_html_tree(page.content)
		price_tag_xpath = '//*[@id="item_show_price"]/span[2]/span'

		price_tag = tree.xpath(price_tag_xpath)[0]
		normal_price = int(price_tag.text.replace('₪','').replace(',',''))

		eilat_price = int(normal_price/1.17)

		return (normal_price,eilat_price)
		pass
	def get_available_branches(self):
		url = self.url
		page = self.page_getter(url)
		tree = self.build_html_tree(page.content)
		elements = tree.xpath('//*[@id="line_item_item_upgrade_ids_"]')
		if len(elements) == 0:
			print('line_item_item_upgrade_ids_ Div Not Found in Given Page\n')
			exit(-1)
		element = elements[0]

		res = []
		for child in element.iterchildren():
			res += [self.branch_from_hebrew_name(child.text)]
		res = [branch for branch in res if branch != None]
		return res





