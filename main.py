import urllib.request, json

# TODO:
# Calculate sequential times in an array[[start_time, end_time], [start_time, end_time]]
# [[08.00, 10.00], [13.00, 15.00]]
# Int or string?

def get_reservations(url):
	"""
	Code for production

	with urllib.request.urlopen(url) as url:
		data = json.loads(url.read().decode())
		print("Done...")
	"""

	with open('test_data.json') as f:
		data=json.load(f)
	return data["reservations"]

def init_schedule():
	schedule = []
	for i in range(9):
		schedule.append(True)
	return schedule

def insert_reservations(schedule, reservations):
	for reservation in reservations:
		start_time = int(reservation["starttime"][:2])

		#TODO: Handle after schedule after 17.00
		if(start_time > 17):
			continue

		end_time = int(reservation["endtime"][:2])
		diff = end_time - start_time
		start_index = start_time - 8

		#print("array: {}".format(start_index))
		for i in range(diff):
			schedule[start_index + i] = False

	return schedule


#TODO: HERE
"""def find_book_times(schedule):
	book_times = []
	found = False
	start_time = 0
	for i, free in enumerate(schedule):
		if(free):
			found = True
			start_time = i+8
			print("true")
		else:
			if(found):

			found = False:
"""

def main():
	url = "https://cloud.timeedit.net/liu/web/schema/ri157366X88Z59Q5Z46g7Y35y5056Y03Q09gQY5Q56777.json"
	reservations = get_reservations(url)
	print(reservations)

	#Will recieve an array [True, True, True, True, True, True, True, True, True]
	#                       08-09  09-10 10-11 11-12 13-14 14-15 15-16 16-17
	# True if free, false if not free
	schedule = init_schedule()
	schedule = insert_reservations(schedule, reservations)
	#book_times = find_book_times(schedule)

	print(schedule)

if __name__ == "__main__":
	print("hello")
	main()
