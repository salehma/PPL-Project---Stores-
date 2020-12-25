from django.shortcuts import render
import folium
import requests
from stores.logics1 import api
import haversine as hs


# view in the client side
# Create your views here.

# this is our starting function we the user opens the website this function will be called and it will render the Home html page
def home(request):
    return render(request, 'index.html')


# global variables
item = 'c'
address = ''
price_pr = ''
distance_pr = ''
rate_pr = ''
zap_search = []
ksp_res = []
zap_idx = 0


# this function will called when the user passed to the next page after he submitted his inputs
# it will show the suggestions from zap
def show_items_of_zap(request):
    global item
    global address
    global price_pr
    global distance_pr
    global rate_pr
    global zap_search
    items = []

    if request.method == 'POST':
        # save the inputs in the global variables
        item = request.POST.get('item')
        address = request.POST.get('location')
        price_pr = request.POST.get('price')
        distance_pr = request.POST.get('distance')
        rate_pr = request.POST.get('rate')
        # validate the inputs
        if int(price_pr) + int(distance_pr) + int(rate_pr) != 100:
            return render(request, 'index.html', {'message': 'priorities sum should be 100'})
        print(item, '  ', address, ' ', price_pr, ' ', distance_pr, ' ', rate_pr)
        # get the zap suggestions
        zap_search = api.Api().search_for(item)
        items = [(zap_search.index(i), i.name, i.image) for i in zap_search]
    items.append((len(zap_search), 'None of The Above', 'templates/pure-white-background.jpg'))
    return render(request, "items_list_zap.html", {"list": items})


# after the zap items shown this function will show the suggestions from ksp
def show_items_of_ksp(request):
    global zap_idx
    global ksp_res
    items = []
    if request.method == 'POST':
        zap_idx = request.POST.get('options')
        # get the ksp suggestions
        ksp_res = api.Api().search_for_ksp(item)
        items = [(ksp_res.index(i), i.name, i.image) for i in ksp_res if i.name != 'Not Available']
    items.append((len(ksp_res), 'None of The Above', 'templates/pure-white-background.jpg'))
    return render(request, "items_list_ksp.html", {"list": items})


# this the main function in the process it will show the final results using a list and a folium map
def show_results(request):
    if request.method == 'POST':
        ksp_idx = request.POST.get('options')
        # here we get the exact location of the user
        loc = get_lat_long_from_address(address)
        # results is the list contains the final results
        results = get_results(ksp_idx, loc['lat'], loc['lng'])
        # creation of map comes here + business logic
        m = folium.Map([loc['lat'], loc['lng']], zoom_start=10)
        # mark the user current location
        folium.CircleMarker((float(loc['lat']), float(loc['lng'])), popup='your location').add_to(m)
        list = []
        i = 1
        # mark each store location
        for result in results:
            folium.Marker((float(result['long']), float(result['lat'])), popup=i).add_to(m)
            l = str(result['company']) + " " + str(result['name']) + ' distance:' + str(
                int(result['distance'])) + 'KM rank:' + str(result['rank']) + ' price:' + str(
                result['price']) + 'NIS'
            list.append(l)
            i += 1
        m = m._repr_html_()  # updated

        context = {'my_map': m, "list": list}
        return render(request, 'map.html', context)


# here we calculate the final result and return the list contains the best 5 stores
def get_results(idx, user_lat, user_lang):
    stores = zap_search[int(zap_idx)].get_stores() if int(zap_idx) != len(zap_search) else []
    stores += [ksp_res[int(idx)]] if int(idx) != len(ksp_res) else []
    branches = []
    for store in stores:
        # branches will contain all the suggested stores
        branches += store.set_prices(store.get_available_branches())
    br = {}
    br_lst = []
    for branch in branches:
        loc1 = (user_lat, user_lang)
        loc2 = (branch.long, branch.latt)
        distance = hs.haversine(loc1, loc2)
        dist_grade = distance * 10 * (int(distance_pr) / 100)
        price_grade = branch.price * (int(price_pr) / 100)
        rank_grade = branch.rank * 1000 * (int(rate_pr) / 100)
        store_grade = rank_grade - price_grade - dist_grade
        br['name'] = branch.name
        br['rank'] = branch.rank
        br['price'] = branch.price
        br['company'] = branch.company
        br['lat'] = branch.latt
        br['long'] = branch.long
        br['distance'] = distance
        br['grade'] = store_grade

        br_lst.append(br)
        br = {}
    final = sorted(br_lst, key=lambda x: x['grade'], reverse=True)
    return final[:5]


# using google apis we calc the current location using the address
def get_lat_long_from_address(addr):
    response = requests.get(
        'https://maps.googleapis.com/maps/api/geocode/json?address=' + addr + '&key=AIzaSyCLs_mIGVefgGgw8Ea3BFgQE9LtxRZux-4')
    resp_json_payload = response.json()
    return resp_json_payload['results'][0]['geometry']['location']
