from .ivory import ivory
from .bug import bug
from .celluarStorage import celluarStorage
from .officeDepot import OfficeDepot

from lxml import html
import requests
class Zap:
	bug_store_id = 1056
	cs_store_id = 5689
	ivory_store_id = 1546
	office_depot_store_id = 493
	headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


	def __init__(self,url):
		self.url = url
		url = self.url
		page = requests.get(url,headers = Zap.headers)
		self.tree = html.fromstring(page.content)
		name_xpath = '//*[@id="sectionContent"]/div[2]/div[1]/h1/span'
		image_xpath = '//*[@id="div_MainImage"]/img'
		self.name = ''.join([c for c in self.tree.xpath(name_xpath)[0].text if ord(c) < 128 ]).strip()
		self.image = self.tree.xpath(image_xpath)[0].attrib['src']
	def get_store_from_store_id(self,url,store_id):
		if str(Zap.bug_store_id) == store_id:
			return bug(url)
		elif str(Zap.cs_store_id) == store_id:
			return celluarStorage(url)
		elif str(Zap.ivory_store_id) == store_id:
			return ivory(url)
		elif str(Zap.office_depot_store_id) == store_id:
			return OfficeDepot(url)
		else:
			return None

		
	def get_stores(self):
		try:
			tree = self.tree
			known_store_ids = [str(i) for i in [self.bug_store_id,self.cs_store_id,self.ivory_store_id,self.office_depot_store_id]]
			stores_xpath = '//*[@id="div_RegularSale"]'
			stores_tag = tree.xpath(stores_xpath)[0]
			known_stores = [child for child in stores_tag.iterchildren() if child.attrib['data-siteid'] in known_store_ids]
			res = []
			for ks in known_stores:
				suffix = ks.find('div').findall('div')[2].find('div').find('div').find('a').attrib['href']
				prefix = 'https://www.zap.co.il'
				store = self.get_store_from_store_id(f'{prefix}{suffix}',ks.attrib['data-siteid'])
				store.set_rank(float(ks.attrib['data-total-rank']))
				res.append(store)
		except:
			res = []

		return res

