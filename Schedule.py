import urllib.request, json

class Schedule:
	def __init__(self, url):
		self.__url = url
		self.__reservations = self.__get_reservations()
		#self.__insert_reservations()
		#print(self.__schedule)
	
	def get_reservations(self):
		return self.__reservations

	def __get_reservations(self):
		"""
		Code for production
		"""
		with urllib.request.urlopen(self.__url) as url:
			data = json.loads(url.read().decode())

		return data["reservations"]
		
		"""
		with open('test_data.json') as f:
			data=json.load(f)
		return data["reservations"]
		"""

if __name__ == "__main__":
	url = "https://cloud.timeedit.net/liu/web/schema/ri167XQ5020Z57Qm5Z085Q56yYYg409x0Y93Y5gQ4076696Z96Z4QyyQo.json"
	schedule = Schedule(url)
	print(schedule.get_reservations())