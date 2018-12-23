import urllib.request, json

class Schedule:
	def __init__(self, url):
		self.__url = url
		#Schedule is an array [True, True, True, True, True, True, True, True, True]
		#                       08-09  09-10 10-11 11-12 13-14 14-15 15-16 16-17
		# True if free, false if not free
		self.__schedule = self.__init_schedule()
		self.__reservations = self.__get_reservations()
		self.__insert_reservations()
		#print(self.__schedule)

	def __get_reservations(self):
		"""
		Code for production

		with urllib.request.urlopen(self.__url) as url:
			data = json.loads(url.read().decode())
			print("Done...")
		"""

		with open('test_data.json') as f:
			data=json.load(f)
		return data["reservations"]

	def __init_schedule(self):
		schedule = []
		for i in range(9):
			schedule.append(True)
		return schedule

	def __insert_reservations(self):
		for reservation in self.__reservations:
			start_time = int(reservation["starttime"][:2])

			#TODO: Handle after schedule after 17.00
			if(start_time > 17):
				continue

			end_time = int(reservation["endtime"][:2])
			diff = end_time - start_time
			start_index = start_time - 8

			#print("array: {}".format(start_index))
			for i in range(diff):
				self.__schedule[start_index + i] = False


	def find_free(self):
		free_times = []
		found = False
		start_time = 0
		#print(self.__schedule)
		#print("len of schedule {}".format(len(self.__schedule)))
		for i, free in enumerate(self.__schedule):
			#print(i)
			if(free):
				#print("free on spot {}".format(i+8))
				#print(i)
				found = True
				start_time = i+8
			else:
				if(found):
					end_time = i+8
					free_times.append([start_time, end_time])
					found = False

			if(i+1==len(self.__schedule) and found):
				#print("true")
				end_time = i+9
				free_times.append([start_time, end_time])
				found = False

		return free_times

if __name__ == "__main__":
	url = "https://cloud.timeedit.net/liu/web/schema/ri157366X88Z59Q5Z46g7Y35y5056Y03Q09gQY5Q56777.json"
	schedule = Schedule(url)
	print(schedule.find_free())