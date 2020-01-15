from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

CITIES = "Bangalore, Chennai, Delhi, Hyderabad, Kolkata, Mumbai, Ahmedabad, Pune, Agra, Ajmer, Aligarh, Amravati, Amritsar, Asansol, Aurangabad, Bareilly, Belgaum, Bhavnagar, Bhiwandi, Bhopal, Bhubaneswar, Bikaner, Bilaspur, Bokaro Steel City, Chandigarh, Coimbatore Nagpur, Cuttack, Dehradun, Dhanbad, Bhilai, Durgapur, Erode, Faridabad, Firozabad, Ghaziabad, Gorakhpur, Gulbarga, Guntur, Gwalior, Gurgaon, Guwahati, Hamirpur[disambiguation needed], Hubli–Dharwad, Indore, Jabalpur, Jaipur, Jalandhar, Jammu, Jamnagar, Jamshedpur, Jhansi, Jodhpur, Kakinada, Kannur, Kanpur, Kochi, Kolhapur, Kollam, Kozhikode, Kurnool, Ludhiana, Lucknow, Madurai, Malappuram, Mathura, Goa, Mangalore, Meerut, Moradabad, Mysore, Nanded, Nashik, Nellore, Noida, Patna, Pondicherry, Purulia Prayagraj, Raipur, Rajkot, Rajahmundry, Ranchi, Rourkela, Salem, Sangli, Shimla, Siliguri, Solapur, Srinagar, Thiruvananthapuram, Thrissur, Tiruchirappalli, Tiruppur, Ujjain, Bijapur, Vadodara, Varanasi, Vasai-Virar City, Vijayawada, Vellore, Warangal, Surat, Visakhapatnam".lower()
PRICE_MAP = {"mid": [300, 700], "low": [0, 300], "high": [700, 99999999999999999]}
LESS = ["less", "under", "below", "cheap", "lesser"]
MORE = ["more", "above", "higher"]
BETWEEN = ["between", "within"]

CUISINE = {'afghan': 1035,
 'african': 152,
 'american': 1,
 'andhra': 2,
 'arabian': 4,
 'armenian': 175,
 'asian': 3,
 'assamese': 165,
 'awadhi': 292,
 'bakery': 5,
 'bar food': 227,
 'bbq': 193,
 'belgian': 132,
 'bengali': 10,
 'beverages': 270,
 'bihari': 1013,
 'biryani': 7,
 'brazilian': 159,
 'british': 133,
 'bubble tea': 247,
 'burger': 168,
 'burmese': 22,
 'cafe': 30,
 'cantonese': 121,
 'charcoal chicken': 994,
 'chettinad': 18,
 'chinese': 25,
 'coffee': 1040,
 'continental': 35,
 'cuisine varies': 1014,
 'desserts': 100,
 'ethiopian': 149,
 'european': 38,
 'fast food': 40,
 'finger food': 271,
 'french': 45,
 'frozen yogurt': 501,
 'goan': 47,
 'greek': 156,
 'gujarati': 48,
 'healthy food': 143,
 'hot dogs': 1026,
 'hyderabadi': 49,
 'ice cream': 233,
 'indonesian': 114,
 'iranian': 140,
 'israeli': 218,
 'italian': 55,
 'japanese': 60,
 'juices': 164,
 'kashmiri': 65,
 'kebab': 178,
 'kerala': 62,
 'konkan': 63,
 'korean': 67,
 'lebanese': 66,
 'lucknowi': 157,
 'maharashtrian': 102,
 'malaysian': 69,
 'malwani': 71,
 'mangalorean': 72,
 'mediterranean': 70,
 'mexican': 73,
 'middle eastern': 137,
 'mishti': 1041,
 'mithai': 1015,
 'modern indian': 1018,
 'momos': 1051,
 'moroccan': 147,
 'mughlai': 75,
 'naga': 166,
 'nepalese': 117,
 'north eastern': 231,
 'north indian': 50,
 'odia': 1057,
 'paan': 1048,
 'pakistani': 139,
 'panini': 989,
 'parsi': 290,
 'pizza': 82,
 'poké': 1019,
 'portuguese': 87,
 'rajasthani': 88,
 'raw meats': 27,
 'roast chicken': 1005,
 'rolls': 1023,
 'russian': 84,
 'salad': 998,
 'sandwich': 304,
 'seafood': 83,
 'singaporean': 119,
 'south american': 972,
 'south indian': 85,
 'spanish': 89,
 'sri lankan': 86,
 'steak': 141,
 'street food': 90,
 'sushi': 177,
 'tamil': 1054,
 'tea': 163,
 'tex-mex': 150,
 'thai': 95,
 'tibetan': 93,
 'turkish': 142,
 'vietnamese': 99,
 'wraps': 1024}

def get_upper_lower_limit(price_range):
	"""
	return price range based on provided segment name.
	"""
	return PRICE_MAP.get(price_range, PRICE_MAP.get("high"))


class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine').lower()
		cus = CUISINE.get(cuisine)
		if loc not in CITIES:
			response= "We don't serve in provided city {}".format(loc)
		elif not cus:
			response= "Please provide appropriate cuisine {}".format(cuisine)
		else:
			price_range = tracker.get_slot('price_range')
			if price_range:
				price1, price2 = get_upper_lower_limit(price_range)
				comp_fn = lambda x: price1 <= x < price2
			else:
				price_comp = tracker.get_slot('price_comp')
				price1 = float(tracker.get_slot('price1'))
				price2 = float(tracker.get_slot('price2'))
				if price_comp in BETWEEN:
					comp_fn = lambda x: price1 <= x < price2
				elif price_comp in MORE:
					comp_fn = lambda x: x > price2
				else:
					comp_fn = lambda x: x < price1
			location_detail=zomato.get_location(loc, 1)
			d1 = json.loads(location_detail)
			lat=d1["location_suggestions"][0]["latitude"]
			lon=d1["location_suggestions"][0]["longitude"]
			results=zomato.restaurant_search("", lat, lon, str(cus), 20)
			d = json.loads(results)
			response = ""
			resp_counter = 0
			if d['results_found'] == 0:
				response = "no results"
			else:
				for restaurant in d['restaurants']:
					name = restaurant['restaurant']['name']
					address = restaurant['restaurant']['location']['address']
					rating = restaurant['restaurant']['user_rating']['aggregate_rating']
					cost = restaurant['restaurant']['average_cost_for_two']
					if comp_fn(float(cost)) and resp_counter < 10:
						response = response + "Found {} in {} with rating {} and avg cost for 2 {}\n".format(name, address, rating, cost)
						resp_counter += 1
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

