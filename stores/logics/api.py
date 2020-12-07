from .ksp import ksp
from .zap import Zap
from lxml import html
import requests
import re



class Api():
	def _search_for_ksp(self,search_string):
		ksp_search_string = search_string + ' ksp'
		xpath = '//*[@id="rso"]'
		url = f'https://www.google.com/search?q={ksp_search_string.replace(" ","+")}'
		result = requests.get( url,headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'})
		result = html.fromstring(result.content).xpath(xpath)[0]
		pattern = re.compile('/item/(\d*)/')
		res = []
		for child in result.findall('div'):
			if child.attrib['class'] == 'g':
				href = child.find('div').findall('div')[0].find('a').attrib['href']
				if "/item/" in href:
					uid = pattern.findall(href)[0]
					res +=  [f'https://ksp.co.il/?uin={uid}']
		return [ksp(url) for url in res]
	def _search_for(self,search_string):
		zap_search_string = search_string + ' zap'
		xpath = '//*[@id="rso"]'
		url = f'https://www.google.com/search?q={zap_search_string.replace(" ","+")}'
		pattern = re.compile('modelid=(\d*)$')
		result = requests.get( url,headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'})
		result = html.fromstring(result.content).xpath(xpath)[0]
		modelids = []
		for child in result.findall('div'):
			if child.attrib['class'] == 'g':
				try:
					href = child.find('div').findall('div')[0].find('a').attrib['href']
				except:
					href = ''
				modelids += pattern.findall(href)
		urls = [f'https://www.zap.co.il/model.aspx?modelid={modelid}' for modelid in modelids]
		res = [Zap(url) for url in urls] 
		return res
	def search_for(self,search_string):
		for i in range(5):
			res = self._search_for(search_string)
			if len(res) > 0:
				return res
		return []
	def search_for_ksp(self,search_string):
		for i in range(5):
			res = self._search_for_ksp(search_string)
			if res != []:
				return res
		return []