from .store import Store,Branch
from urllib.parse import urlparse,urlunparse

class ivory(Store):
	branches = [
			Branch("Eilat-Sderot Hatmarim",           (29.55520160874542, 34.95310057330349),      hebrew_names=['אילת - שדרות התמרים'],             rank=0.0),
			Branch("Eilat-Pninat Eilat",              (29.55095505554007, 34.95552529017801),      hebrew_names=['אילת - פנינת אילת'],               rank=0.0),
			Branch("Eilat-Red Compound",              (29.554087400514423, 34.961775384953214),    hebrew_names=['אילת - רד (מתחם RED)'],            rank=0.0),
			Branch("Ashdod",                          (31.793844855819117, 34.640792315344854),    hebrew_names=['אשדוד'],                           rank=0.0),
			Branch("Ashkelon",                        (31.666314712109777, 34.55823165952717),     hebrew_names=['אשקלון'],                          rank=0.0),
			Branch("Beer Sheva-Bet Noam",             (31.245910269623177, 34.80474185953371),     hebrew_names=['באר שבע - בית נועם'],              rank=0.0),
			Branch("Beer Sheva-Grand Compound",       (31.250475864760794, 34.77172879571062),     hebrew_names=['באר שבע - גרנד קניון'],            rank=0.0),
			Branch("Bat Yam",                         (32.01286231658003, 34.75192811534152),      hebrew_names=['בת ים'],                           rank=0.0),
			Branch("Hadera",                          (32.44195757914707, 34.91205821718688),      hebrew_names=['חדרה'],                            rank=0.0),
			Branch("Holon",                           (32.01596122117799, 34.80144661719382),      hebrew_names=['חולון'],                           rank=0.0),
			Branch("Haifa-Hotsot Hamefrats",          (32.80804903461783, 35.0535329245757),       hebrew_names=['חיפה - חוצות המפרץ'],              rank=0.0),
			Branch("Haifa-Atsmaot",                   (32.82103437220727, 34.99685808834461),      hebrew_names=['חיפה - עצמאות'],                   rank=0.0),
			Branch("Jerusalim-King Gorge",            (31.78275702292164, 35.217271257672955),     hebrew_names=['ירושלים - קינג ג&#39;ורג&#39;'],   rank=0.0),
			Branch("Jerusalim-Gevat Shoal",           (31.793399461764466, 35.18919355952526),     hebrew_names=['ירושלים - גבעת שאול'],             rank=0.0),
			Branch("Jerusalim-Talpiot",               (31.752199983790984, 35.208590238361715),    hebrew_names=['ירושלים - תלפיות'],                rank=0.0),
			Branch("Kfar Saba",                       (32.17385406953553, 34.92740839999455),      hebrew_names=['כפר סבא'],                         rank=0.0),
			Branch("Karmeal",                         (32.92693439936218, 35.32596912123635),      hebrew_names=['כרמיאל'],                          rank=0.0),
			Branch("Modeen",                          (31.889608169635242, 34.96254344376292),     hebrew_names=['מודיעין'],                         rank=0.0),
			Branch("Nesert Elit",                     (32.71516314612169, 35.335889055805396),     hebrew_names=['נוף הגליל (נצרת עילית)'],          rank=0.0),
			Branch("Netanya",                         (32.28882630745538, 34.861883273009134),     hebrew_names=['נתניה - פולג'],                    rank=0.0),
			Branch("Affola",                          (32.607411939475824, 35.29282507300386),     hebrew_names=['עפולה'],                           rank=0.0),
			Branch("Petah Tekvah-Sgola",              (32.1092133848328, 34.89569485952025),       hebrew_names=['פתח תקווה - סגולה'],               rank=0.0),
			Branch("Petaf Tekva-Matalon",             (32.09206570933055, 34.85705123835656),      hebrew_names=['פתח תקווה - מטלון'],               rank=0.0),
			Branch("Keryat Gat",                      (31.608852828822332, 34.77305588432741),     hebrew_names=['קרית גת'],                         rank=0.0),
			Branch("Rosh Letsion-Leshinsky",          (31.993029369594307, 34.767992217194156),    hebrew_names=['ראשל&#34;צ - לישנסקי'],            rank=0.0),
			Branch("Rosh Letsion-Rocheld Compound",   (31.96372943356719, 34.80148053068655),      hebrew_names=['ראשל&#34;צ - קניון רוטשילד'],      rank=0.0),
			Branch("Rahovot",                         (31.900311384330504, 34.80407354417924),     hebrew_names=['רחובות'],                          rank=0.0),
			Branch("Ramat Gan",                       (32.099967408785, 34.82855184999571),        hebrew_names=['רמת גן - בני ברק'],                rank=0.0),
			Branch("Rananah",                         (32.19700229084945, 34.87820564130603),      hebrew_names=['רעננה'],                           rank=0.0),
			Branch("Tel Avi-Haharots",                (32.06128791611406, 34.7913504883569),       hebrew_names=['תל אביב - החרוץ'],                 rank=0.0),
			Branch("Tel Avi-Desingov",                (32.07556436705093, 34.77542698835679),      hebrew_names=['תל אביב - דיזינגוף סנטר'],         rank=0.0)
]
	def __init__(self,url):
		self.url = self.page_getter(url).url
		self.company = "IVORY"
		self.set_company_names()

	def updated_price(self):
		url = self.url
		page = self.page_getter(url)
		tree = self.build_html_tree(page.content)
		price_tag_xpath = '//*[@id="pricetotalitemjs"]/div[1]/span[1]'
		eilat_price_tag_xpath = '//*[@id="priceforeilat"]'

		price_tag = tree.xpath(price_tag_xpath)[0]
		normal_price = int(price_tag.text.replace(',',''))
		try:
			eilat_price_tag = tree.xpath(eilat_price_tag_xpath)[0]
			eilat_price = int(eilat_price_tag.text.replace('₪','').replace(',',''))
		except:
			eilat_price = int(normal_price/1.17)

		return (normal_price,eilat_price)
	def get_available_branches(self):
		url = self.url_parser(self.url)
		page = self.page_getter(url)
		page = page.json()
		branchs = page['Data']
		res = [self.branch_from_hebrew_name(branch['branchName']) for branch in branchs if int(branch['qty']) > 0]
		return [branch for branch in res if branch != None]

	def url_parser(self,url):
		parsed = urlparse(url)
		l = parsed.query.split('&')
		f = False
		for q in l:
			if 'id' in q:
				f = True
		if not f:
			raise Exception('no id in ul')
		l += ['act=ws_check_balance']
		new_query_string = '&'.join(l)
		parsed = parsed._replace(query=new_query_string)
		return urlunparse(parsed)