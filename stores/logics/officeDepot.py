from .store import Store,Branch
import re




class OfficeDepot(Store):
	branches = [

			Branch("Haifa",                           (32.81002244586955, 35.056542766601794),     hebrew_names=[2],                                 rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Grand Canyon",                    (32.79004640278555, 35.0066568018369),       hebrew_names=[18],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Nazeret",                         (32.69424338001205, 35.30501046871668),      hebrew_names=[22],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Maalot",                          (33.021822100082446, 35.280086944161),       hebrew_names=[27],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Shaar Ha Zafon",                  (32.80778689640857, 35.07717080183658),      hebrew_names=[21],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Bet Shan",                        (32.5130143799898, 35.50054095951361),       hebrew_names=[41],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Carmeal",                         (32.921630458071746, 35.30746732664099),     hebrew_names=[44],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Hadera",                          (32.435615382964414, 34.908886015334666),    hebrew_names=[46],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Yokenam",                         (32.65988669355884, 35.104992571150554),     hebrew_names=[73],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Yarka",                           (32.95585625766087, 35.181978715326146),     hebrew_names=[29],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Netanya",                         (32.27739312918459, 34.86087285951737),      hebrew_names=[19],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Er Yamim",                        (32.279501989280355, 34.84709379110714),     hebrew_names=[25],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Shfayiim",                        (32.22124535898169, 34.828552782769925),     hebrew_names=[6],                                 rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Ashkelon",                        (31.661280061827856, 34.58984457487152),     hebrew_names=[4],                                 rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Ashdod",                          (31.8184167744913, 34.6539511941453),        hebrew_names=[3],                                 rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Reshon Letzion",                  (31.98549265199514, 34.76977536664849),      hebrew_names=[5],                                 rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Nas Ziona",                       (31.921669119818755, 34.79337995235614),     hebrew_names=[12],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Bilo",                            (32.10688831534393, 34.96899845466554),      hebrew_names=[16],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Beer Sheva-mol 7",                (31.233658973409373, 34.79684254877491),     hebrew_names=[17],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Rohovot",                         (31.90955931705747, 34.80546818835939),      hebrew_names=[23],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Beer Yakov",                      (31.94283927072111, 34.83330031071737),      hebrew_names=[26],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Beer Sheva-Beer Yakuv Mall",      (31.224804204356012, 34.80086282068555),     hebrew_names=[35],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Arad",                            (31.247383548446756, 35.19766684418954),     hebrew_names=[40],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Netevot",                         (31.41757367906448, 34.59418571349834),      hebrew_names=[42],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Ramleh",                          (31.922200826021445, 34.86238170185101),     hebrew_names=[47],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Reshon Letzion-West",             (31.991674619900206, 34.764140611597405),    hebrew_names=[64],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Herzilya-Pituah",                 (32.162230439931676, 34.809686719928266),    hebrew_names=[24],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Rananah",                         (32.18161326939659, 34.871455042322395),     hebrew_names=[6],                                 rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Kfar Saba",                       (32.171412085675534, 34.928620359519144),    hebrew_names=[68],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Ramat Hahayal",                   (32.10973270865155, 34.83730192883167),      hebrew_names=[7],                                 rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Bne Brak",                        (32.094749167139966, 34.82348982883202),     hebrew_names=[8],                                 rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Tel Aviv-Igal Alon",              (32.07399967954596, 34.79543394417648),      hebrew_names=[43],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Petah Tekva-Sgola",               (32.100847752411966, 34.89379475766787),     hebrew_names=[48],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Tel Aviv-Megdal Shalom",          (32.06404659453759, 34.769333315340674),     hebrew_names=[54],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Bet Shemesh",                     (31.75606811710121, 34.98691432698488),      hebrew_names=[56],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Kiryat Uno",                      (32.0558648584285, 34.86349611904554),       hebrew_names=[58],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Modeen",                          (31.88957388124124, 34.964265598146795),     hebrew_names=[63],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Ramat Aviv",                      (32.11352819533559, 34.79735787300491),      hebrew_names=[31],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("Um Alfahem",                      (32.520997721969614, 35.153965688126476),    hebrew_names=[30],                                rank=0.0,           price=0,            company="OfficeDepot"),
			Branch("En Shemer",                       (32.46677044487621, 34.991998184980226),     hebrew_names=[32],                                rank=0.0,           price=0,            company="OfficeDepot"),
	]
	def __init__(self,url):
		uin = re.findall('/items/(\d*)',url)
		if len(uin) == 0:
			self.url = self.page_getter(url).url
		else:
			self.url = url
		self.company = "OfficeDepot"
		self.set_company_names()

	def updated_price(self):
		url = self.url
		page = self.page_getter(url)
		tree = self.build_html_tree(page.content)
		price_tag = tree.xpath('//*[@id="item_show_price"]/span[2]/span[1]')[0]
		normal_price = int(price_tag.text.replace(',','').replace('₪',''))
		return (normal_price,normal_price)


	def get_available_branches(self):
		url = self.url
		uin = re.findall('/items/(\d*)',url)
		if len(uin) == 0:
			print('item number cannot be found in url')
			return []
		uin = uin[0]
		url = f'https://www.officedepot.co.il/stocks/{uin}?method=comax'
		stock = self.page_getter(url).json()
		res  = [self.branch_from_hebrew_name(int(a)) for a in stock if stock[a]]
		return [ branch for branch in res if branch != None ]




