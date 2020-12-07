from .store import Store,Branch
import re
class ksp(Store):
	branches = [
			Branch("Eilat-Tayelet",                   (29.550892133998484, 34.96076312698867),     hebrew_names=['אילת הטיילת'],                     rank=0.0),
			Branch("Eilat-Legona",                    (29.554562372574747, 34.96102175955931),     hebrew_names=['אילת לגונה'],                      rank=0.0),
			Branch("Eilat-Tourist Center",            (29.55126472896782, 34.95258642764735),      hebrew_names=['אילת מרכז התיירות'],               rank=0.0),
			Branch("Eilat-Tarshish",                  (29.551263333900607, 34.957513834254605),    hebrew_names=['אילת תרשיש'],                      rank=0.0),
			Branch("Ashdod-Center",                   (31.793083173789665, 34.639146631877175),    hebrew_names=['אשדוד מרכז'],                      rank=0.0),
			Branch("Ashdod-Ad Halom",                 (31.767283021315954, 34.665499001853455),    hebrew_names=['אשדוד עד הלום'],                   rank=0.0),
			Branch("Ashkelon",                        (31.668235982920027, 34.570179417199235),    hebrew_names=['אשקלון'],                          rank=0.0),
			Branch("Beer Sheva-East",                 (31.244599343371444, 34.80857222737552),     hebrew_names=['באר שבע מזרח'],                    rank=0.0),
			Branch("Beer Sheva-Shoael hamelekh",      (31.257863954233898, 34.76797052072991),     hebrew_names=['באר שבע שאול המלך'],               rank=0.0),
			Branch("Bilo Center",                     (31.865152043908925, 34.814249903704365),    hebrew_names=['בילו רחובות ק.עקרון'],             rank=0.0),
			Branch("Bet Shemesh",                     (31.754705023131248, 34.992691446462175),    hebrew_names=['בית שמש'],                         rank=0.0),
			Branch("Herzilya-Center",                 (32.16137567854241, 34.84277976231791),      hebrew_names=['הרצליה מרכז'],                     rank=0.0),
			Branch("Herzilya-Pituah",                 (32.1644820534152, 34.81119655886076),       hebrew_names=['הרצליה פיתוח'],                    rank=0.0),
			Branch("Hadera",                          (32.439279385066435, 34.910431586498504),    hebrew_names=['חדרה'],                            rank=0.0),
			Branch("Holon",                           (32.02338709523057, 34.774913046029695),     hebrew_names=['חולון'],                           rank=0.0),
			Branch("Haifa-Matam",                     (32.78366068041302, 34.96106510183703),      hebrew_names=['חיפה מת"מ'],                       rank=0.0),
			Branch("Haifa-Stela Maris",               (32.82032174998756, 34.97402199045964),      hebrew_names=['חיפה סטלה מאריס'],                 rank=0.0),
			Branch("Haifa-Romama",                    (32.78919344685998, 35.00079993067311),      hebrew_names=['חיפה רוממה'],                      rank=0.0),
			Branch("Tabrayia",                        (32.796254429671606, 35.52685562882065),     hebrew_names=['טבריה'],                           rank=0.0),
			Branch("Yavne",                           (31.886230946690173, 34.7339527941795),      hebrew_names=['יבנה'],                            rank=0.0),
			Branch("Jerusalim-Har Hotsvem",           (31.80056594762039, 35.21080018836109),      hebrew_names=['ירושלים חוצבים'],                  rank=0.0),
			Branch("Jerusalim-King Gorge",            (31.782673125055204, 35.21603633323959),     hebrew_names=['ירושלים מרכז'],                    rank=0.0),
			Branch("Jerusalim-Talpiot",               (31.75064163326589, 35.209052400138646),     hebrew_names=['ירושלים תלפיות'],                  rank=0.0),
			Branch("Kfar Saba-Hayeroka",              (32.19264066946644, 34.89166367301068),      hebrew_names=['כפר סבא הירוקה'],                  rank=0.0),
			Branch("Kfar Saba-Htaash",                (32.17460909196293, 34.927209992217875),     hebrew_names=['כפר סבא התעש'],                    rank=0.0),
			Branch("Karmeal",                         (32.92363220057766, 35.308059436107),        hebrew_names=['כרמיאל'],                          rank=0.0),
			Branch("Modeaen",                         (31.88702128654447, 34.96136178650748),      hebrew_names=['מודיעין'],                         rank=0.0),
			Branch("Nahariya",                        (32.99525287563224, 35.09201710778556),      hebrew_names=['נהריה'],                           rank=0.0),
			Branch("Nesert Elit",                     (32.70073774304547, 35.32040152120324),      hebrew_names=['נצרת עילית'],                      rank=0.0),
			Branch("Nesher",                          (32.775553438452, 35.04279608649299),        hebrew_names=['נשר'],                             rank=0.0),
			Branch("Netevot",                         (31.41785005484984, 34.59697622884268),      hebrew_names=['נתיבות'],                          rank=0.0),
			Branch("Netanya-Poleg",                   (32.27840053983426, 34.86107273068128),      hebrew_names=['נתניה'],                           rank=0.0),
			Branch("Netanya-Keryat Hasharon",         (32.30778490723762, 34.8754817441727),       hebrew_names=['נתניה קרית השרון'],                rank=0.0),
			Branch("Affola",                          (32.607755198553846, 35.28766504231536),     hebrew_names=['עפולה'],                           rank=0.0),
			Branch("Petah Tekva-St. Rabin",           (32.08922394471608, 34.86181320184837),      hebrew_names=['פתח תקווה דרך רבין'],              rank=0.0),
			Branch("Petah Tekva-sgola",               (32.10542932412491, 34.89297204771975),      hebrew_names=['פתח תקווה סגולה'],                 rank=0.0),
			Branch("Haifa-Hestadrot",                 (32.812639338654826, 35.07013818834466),     hebrew_names=['קריון ק.ביאליק'],                  rank=0.0),
			Branch("Kiryat Byalik",                   (32.84417003267014, 35.08984846096096),      hebrew_names=['קרית אונו'],                       rank=0.0),
			Branch("Kiryat Uno",                      (32.055797014219536, 34.863328986504754),    hebrew_names=['קרית אתא'],                        rank=0.0),
			Branch("Kiryat Hayim",                    (32.82265813332167, 35.05720404416438),      hebrew_names=['קרית חיים'],                       rank=0.0),
			Branch("Rosh Letsion-Center",             (31.9672040087461, 34.784337586506176),      hebrew_names=['ראשון לציון מרכז'],                rank=0.0),
			Branch("Rosh Letsion-Rozentski",          (31.986649183382337, 34.773178565539354),    hebrew_names=['ראשון לציון רוזינסקי'],            rank=0.0),
			Branch("Rohovot",                         (31.910115776038623, 34.807030473015125),    hebrew_names=['רחובות'],                          rank=0.0),
			Branch("Ramleh",                          (31.92529003097746, 34.86352428835904),      hebrew_names=['רמלה'],                            rank=0.0),
			Branch("Ramat Aviv",                      (32.117078946197985, 34.797246115339696),    hebrew_names=['רמת אביב'],                        rank=0.0),
			Branch("Ramat Gan",                       (32.09313371064668, 34.819808907606266),     hebrew_names=['רמת גן'],                          rank=0.0),
			Branch("Ramat Hasharon",                  (32.14484197539571, 34.8376194376549),       hebrew_names=['רמת השרון'],                       rank=0.0),
			Branch("Ranana",                          (32.18028231674193, 34.87774558835503),      hebrew_names=['רעננה'],                           rank=0.0),
			Branch("Tel Aviv-Desingov",               (32.075567840215236, 34.77540608161465),     hebrew_names=['תל אביב דיזינגוף'],                rank=0.0),
			Branch("Tel Aviv-Hahashmonaem",           (32.070801881046265, 34.7839793363747),      hebrew_names=['תל אביב החשמונאים'],               rank=0.0),
			Branch("Tel Aviv-Hamasger",               (32.06776738565907, 34.78688928650445),      hebrew_names=['תל אביב המסגר'],                   rank=0.0),
			Branch("Tel Aviv-Ramat Hahayal",          (32.106830392391515, 34.83457001533991),     hebrew_names=['תל אביב רמת החייל'],               rank=0.0)
]



	def __init__(self,url):
		self.url = url
		self.company = "KSP"
		self.set_company_names()
		url = self.url
		page = self.page_getter(url)
		tree = self.build_html_tree(page.content)
		try:

			self.name = ''.join([c for c in tree.xpath('//*[@id="itemContainer"]/div/span')[0].text if ord(c) < 128 ]).strip()
			self.image = tree.xpath('//*[@id="mainImage"]')[0].attrib['src']
		except:
			self.name = 'Not Available'
			self.image = ''		
	def get_availability_from_tag_attrib(self,attrib):
		return 0 if ('not-in-stock' in attrib['class']) else 1

	def updated_price(self):
		url = self.url
		page = self.page_getter(url)
		tree = self.build_html_tree(page.content)
		try:
			is_eilat = False
			pattern = re.compile('<span class="span-new-price-get-item"[^>]*>([0123456789,]*).*</span>')
			res = pattern.findall(page.text)
			res = [price.replace(',','') for price in res]
			res = [int(price) for price in res]
			normal_price = max(res)
			eilat_price = min(res)
			return (normal_price,eilat_price)
		except:
			return (-1,-1)

	def get_available_branches(self):
		url = self.url
		page = self.page_getter(url)
		tree = self.build_html_tree(page.content)
		elements = tree.xpath('//*[@id="wrapper_bottom"]/div[4]/div[2]/div[1]/div[2]')
		if len(elements) == 0:
			print('uin Not Found in Given Page\n')
			return []
		uin = str(elements[0].text) 
		stock_page = f'https://ksp.co.il/?get_storage_new&uinsql={uin}'

		page = self.page_getter(stock_page)
		tree = self.build_html_tree(page.content)
		element = tree.xpath('//*[@id="wrap"]/table/tbody/tr[3]/td/div[2]/ul')[0]
		childs = []
		for child in element.iterchildren():
			i_tag = child.find('li').find('table').find('tbody').find('tr').find('td').find('i')
			name_tag = child.find('li').find('table').find('tbody').find('tr').findall('td')[1]
			if self.get_availability_from_tag_attrib(i_tag.attrib):
				childs += [name_tag.text]
		res =  [self.branch_from_hebrew_name(h_name) for h_name in childs]
		return [branch for branch in res if branch != None]



