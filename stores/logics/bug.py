from .store import Store,Branch
import re
class bug(Store):

	branches = [
			Branch("Eilat-Ice Mall",                  (29.554209144115358, 34.96558484441295),     hebrew_names=['אייסמול אילת '],                   rank=0.0),
			Branch("Tel Aviv-Akhelov",                (32.08522478450344, 34.79048093802363),      hebrew_names=['איכילוב - ת"א '],                  rank=0.0),
			Branch("Ramat Gan",                       (32.101390189496314, 34.82687947505689),     hebrew_names=['אילון ר"ג '],                      rank=0.0),
			Branch("Eilat-Tayelet Shlomo",            (29.55266287707901, 34.962138630920755),     hebrew_names=['אילת טיילת המלך שלמה '],           rank=0.0),
			Branch("Lod",                             (31.986499082480073, 34.91428497215455),     hebrew_names=['אירפורט סיטי -לוד '],              rank=0.0),
			Branch("Ashdod-Big",                      (31.823312797282338, 34.6532488512815),      hebrew_names=['אשדוד ביג '],                      rank=0.0),
			Branch("Ashdod-Star",                     (31.81049993975131, 34.65568195254378),      hebrew_names=['אשדוד סטאר '],                     rank=0.0),
			Branch("Ashkilon",                        (31.664772178535557, 34.5651401443771),      hebrew_names=['אשקלון '],                         rank=0.0),
			Branch("Beer Sheva-Big",                  (31.243593110127062, 34.81099716426819),     hebrew_names=['באר שבע ביג '],                    rank=0.0),
			Branch("Beer Sheva-Grand",                (31.25048829714674, 34.771946975071735),     hebrew_names=['באר שבע גרנד '],                   rank=0.0),
			Branch("Beer Sheva-Hanegev",              (31.244170610035926, 34.79456627322047),     hebrew_names=['באר שבע הנגב - סגור זמנית '],      rank=0.0),
			Branch("Eilat-Big",                       (29.566814480556154, 34.95921135975643),     hebrew_names=['ביג אילת '],                       rank=0.0),
			Branch("Karmeal-Big",                     (32.92698979182137, 35.323358371339),        hebrew_names=['ביג כרמיאל '],                     rank=0.0),
			Branch("Bilo",                            (31.86369759838123, 34.81806078666173),      hebrew_names=['בילו '],                           rank=0.0),
			Branch("Bet Shemesh",                     (31.756408236073955, 34.99085748405389),     hebrew_names=['בית שמש - סגור זמנית '],           rank=0.0),
			Branch("Jerusalim-Ben Halal",             (31.78245982356709, 35.21730021739066),      hebrew_names=['בן הלל ירושלים '],                 rank=0.0),
			Branch("Givat Shmoal",                    (32.08224992413143, 34.85621717005453),      hebrew_names=['גבעת שמואל '],                     rank=0.0),
			Branch("Gevatayem",                       (32.06716283056236, 34.80868741738549),      hebrew_names=['גבעתיים - סגור זמנית '],           rank=0.0),
			Branch("Gan Yavne",                       (31.795533951652878, 34.70449094622644),     hebrew_names=['גן יבנה '],                        rank=0.0),
			Branch("Gan Shmoal",                      (32.45890048869952, 34.95780041752105),      hebrew_names=['גן שמואל '],                       rank=0.0),
			Branch("Netanya",                         (32.27745451982895, 34.86136904477418),      hebrew_names=['גנדן-נתניה '],                     rank=0.0),
			Branch("Haifa-Grand",                     (32.79304967799443, 35.008497100018154),     hebrew_names=['גרנד קניון - חיפה '],              rank=0.0),
			Branch("Dimona",                          (31.0601160938856, 35.02024932904402),       hebrew_names=['דימונה - סגור זמנית '],            rank=0.0),
			Branch("Jerusalim-Hadar",                 (31.753715437583047, 35.213418075649116),    hebrew_names=['הדר ירושלים '],                    rank=0.0),
			Branch("Rosh Letzion",                    (31.991574469588578, 34.7742420020433),      hebrew_names=['הזהב ראשל"צ - סגור זמנית '],       rank=0.0),
			Branch("Jerusalim-Hareal",                (31.802024857674706, 35.14879302351306),     hebrew_names=['הראל י-ם - סגור זמנית '],          rank=0.0),
			Branch("Herzilya",                        (32.16473546102087, 34.82364385296917),      hebrew_names=['הרצליה '],                         rank=0.0),
			Branch("Zechron Yakov",                   (32.569452280832905, 34.93342214833012),     hebrew_names=['זכרון יעקב '],                     rank=0.0),
			Branch("Holon",                           (32.0131291388976, 34.77851920291869),       hebrew_names=['חולון - סגור זמנית '],             rank=0.0),
			Branch("Haifa-Hotsot Hamefrats",          (32.79336957468767, 35.03731347504424),      hebrew_names=['חוצות המפרץ - חיפה '],             rank=0.0),
			Branch("Tabariya",                        (32.79103904236772, 35.53383238853657),      hebrew_names=['טבריה - סגור זמנית '],             rank=0.0),
			Branch("Yokenam",                         (32.64284656278288, 35.092991646211246),     hebrew_names=['יקנעם '],                          rank=0.0),
			Branch("Kfar Saba-G",                     (32.17116577543385, 34.927333544368274),     hebrew_names=['כפר סבא G '],                      rank=0.0),
			Branch("Karmeal",                         (32.928404907371984, 35.32538300202637),     hebrew_names=['כרמיאל - סגור זמנית '],            rank=0.0),
			Branch("Modeen",                          (31.900060567941456, 35.00831944622454),     hebrew_names=['מודיעין - סגור זמנית '],           rank=0.0),
			Branch("Hadera-Mol Ha Hof",               (32.44215090540094, 34.89538471552749),      hebrew_names=['מול החוף חדרה '],                  rank=0.0),
			Branch("Eilat-Mol Ha Yam",                (29.550211562862163, 34.95396135273972),     hebrew_names=['מול הים אילת '],                   rank=0.0),
			Branch("Jerusalim-Malha",                 (31.752271622445626, 35.18786826337644),     hebrew_names=['מלחה ירושלים '],                   rank=0.0),
			Branch("Jerusalim-Memela",                (31.777557213612965, 35.225208702047176),    hebrew_names=['ממילא י-ם '],                      rank=0.0),
			Branch("Adomem",                          (31.771732160348975, 35.29862544807818),     hebrew_names=['מעלה אדומים - סגור זמנית '],       rank=0.0),
			Branch("Nahariya",                        (33.005407313902495, 35.100450929009384),    hebrew_names=['נהריה - סגור זמנית '],             rank=0.0),
			Branch("Nas Ziona",                       (31.922333706859284, 34.793711330880456),    hebrew_names=['נס ציונה '],                       rank=0.0),
			Branch("Naseret",                         (32.696529053913295, 35.30132907451378),     hebrew_names=['נצרת '],                           rank=0.0),
			Branch("Sivionem",                        (32.03065207863545, 34.878206159714566),     hebrew_names=['סביונים '],                        rank=0.0),
			Branch("Reshon Letzion-Cinema City",      (31.984535530615744, 34.770805434049805),    hebrew_names=['סינמה סיטי ראשל"צ G '],            rank=0.0),
			Branch("Tel Aviv-Center",                 (32.07568475905736, 34.774833839375596),     hebrew_names=['סנטר תל אביב '],                   rank=0.0),
			Branch("Tel Aviv-Israeli",                (32.07651369544955, 34.79216554626244),      hebrew_names=['עזריאלי תל אביב '],                rank=0.0),
			Branch("Netanya-Aer Yamim",               (32.27960943717448, 34.846185459710014),     hebrew_names=['עיר ימים-נתניה - סגור זמנית '],    rank=0.0),
			Branch("Acre",                            (32.92323650259821, 35.08123100202656),      hebrew_names=['עכו - סגור זמנית '],               rank=0.0),
			Branch("Affola",                          (32.604300439125765, 35.293986813550106),    hebrew_names=['עפולה - סגור זמנית '],             rank=0.0),
			Branch("Affola-G",                        (32.619223439949195, 35.31256215970389),     hebrew_names=['עפולה G '],                        rank=0.0),
			Branch("Petah Tekva",                     (32.09193837283662, 34.86484039675337),      hebrew_names=['פתח תקווה '],                      rank=0.0),
			Branch("Bat Yam",                         (32.0221604202772, 34.757207782398744),      hebrew_names=['קניון בת ים - סגור זמנית '],       rank=0.0),
			Branch("Haifa",                           (32.79166924790412, 34.964970320267014),     hebrew_names=['קניון חיפה '],                     rank=0.0),
			Branch("Kastina",                         (31.72817784035746, 34.75449476765772),      hebrew_names=['קסטינה '],                         rank=0.0),
			Branch("Kirion",                          (32.85040563600576, 35.09025619470487),      hebrew_names=['קריון '],                          rank=0.0),
			Branch("Kiryat Uno",                      (32.05581520027353, 34.863404088549856),     hebrew_names=['קרית אונו '],                      rank=0.0),
			Branch("Rosh Pina",                       (32.969238499755825, 35.550267559697545),    hebrew_names=['ראש פינה '],                       rank=0.0),
			Branch("Rocheled-G",                      (31.96605384764201, 34.801395006686846),     hebrew_names=['רוטשילד G '],                      rank=0.0),
			Branch("Rhovot",                          (31.89585630929757, 34.80712693961912),      hebrew_names=['רחובות - סגור זמנית '],            rank=0.0),
			Branch("Ramat Aviv",                      (32.1125082662362, 34.795085957861595),      hebrew_names=['רמת אביב - סגור זמנית '],          rank=0.0),
			Branch("Ramat Yeshi",                     (32.707787855455784, 35.1740362845692),      hebrew_names=['רמת ישי '],                        rank=0.0),
			Branch("Rananim",                         (32.19766823295968, 34.87835324621929),      hebrew_names=['רננים '],                          rank=0.0),
			Branch("Sharonim",                        (32.133541731740586, 34.90145212549715),     hebrew_names=['שרונים  - סגור זמנית '],           rank=0.0),
			Branch("Jerusalim-Central Station",       (31.78918484786541, 35.20338179040604),      hebrew_names=['תחנה מרכזית י-ם - סגור זמנית '],   rank=0.0),
	

	]
	def __init__(self,url):
		self.url = url
		self.company = "BUG"
		self.set_company_names()
	def updated_price(self):
		url = self.url
		page = self.page_getter(url)
		tree = self.build_html_tree(page.content)
		price_tag_xpath = '//*[@id="product-price-container"]/ins'
		eilat_price_tag_xpath = '//*[@id="eilat-price-container"]/strong'

		price_tag = tree.xpath(price_tag_xpath)[0]
		normal_price = int(price_tag.text.replace('₪','').replace(',',''))
		try:
			eilat_price_tag = tree.xpath(eilat_price_tag_xpath)[0]
			eilat_price = int(eilat_price_tag.text.replace('₪','').replace(',',''))
		except:
			eilat_price = int(normal_price/1.17)

		return (normal_price,eilat_price)
		
	def get_available_branches(self):
		url = self.url
		page = self.page_getter(url)
		tree = self.build_html_tree(page.content)
		elements = tree.xpath('//*[@id="product-price-container-container"]/div[2]/span')
		if len(elements) == 0:
			print('addCart span Not Found in Given Page\n')
			exit(-1)
		product_id = str(elements[0].attrib['onclick'])
		product_id = re.findall(r'addToCart\(this,(\d*)\)',product_id)
		if len(product_id) == 0:
			print('product_id Not Found in Given Page\n')
			exit(-1)
		product_id = product_id[0]
		inventory_page = f'https://www.bug.co.il/product/check-inventory?productid={product_id}'
		page = self.page_getter(inventory_page)
		tree = self.build_html_tree( f'<div> {page.text} </div>')
		element = tree
		res = []
		for child in element.iterchildren():
			span_tag = child.find('span')
			name = child.text
			if self.get_availability_from_tag_attrib(span_tag.attrib):
				res += [self.branch_from_hebrew_name(name)]
			res = [b for b in res if b != None] 
		return res



	def get_availability_from_tag_attrib(self, attrib):
		return 0 if attrib['data-inventory'] == '0' else 1 




