from stores.logics.api import Api

_api = Api()
search_string = 'iphone x'
zap_res = _api.search_for(search_string)
ksp_res = _api.search_for_ksp(search_string)

print(zap_res)

print('################')
for i in range(len(zap_res)):
	print(f'{i}) {zap_res[i].name}')
print(f'{len(zap_res)}) Nothing')
idx = input("please choose product for zap:")
stores = zap_res[int(idx)].get_stores() if int(idx) != len(zap_res) else []
print(stores)
# for i in range(len(ksp_res)):
# 	print(f'{i}) {ksp_res[i].name}')
# print(f'{len(ksp_res)}) Nohing')
# idx = input("please choose product for ksp:")
# stores += [ksp_res[int(idx)]] if int(idx) != len(ksp_res) else []

branches = []
for store in stores:
	branches += store.set_prices(store.get_available_branches())

for branch in branches:
	print(str(branch))



"""
1. search_for
	from this you will get a list of objets.
	every object represents a product in zap
	every object have the property name  and image
	    name: string that specfies the product name
	    image:  a url to the image of the product

2. get_stores:
	after the user chooses the product call get_stores()
	it returns the list of known stores that contain the product
	known products (ksp, bug, ivory, celluar store, office depot)


3. get:
	when we have a list of stores, call on every store the function get, that returns the list of branches.

"""