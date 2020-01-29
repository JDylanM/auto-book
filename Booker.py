import requests, json, re
from constants import *

#TODO:
#1. think of way to integrate both modules
#2. error handling, logging(?)


class Booker:
	def __init__(self):
		self.__session = requests.session()

	def login(self, acc, pw):
		self.__session.get('https://cloud.timeedit.net/liu/web/timeedit/sso/?ssoserver=liu_stud_cas&entry=wr_stud&back=https%3A%2F%2Fcloud.timeedit.net%2Fliu%2Fweb%2Fwr_stud%2F')

		payload = {
			'j_username': acc,
			'j_password': pw,
			'_eventId_proceed': '',
			'AuthMethod': 'FormsAuthentication'
		}
		response = self.__session.post(
			'https://login.it.liu.se/idp/profile/cas/login?execution=e1s1',
			data=payload,
		)

	#'26.A-huset'
	def __get_rooms(self, date, starttime, endtime, acc, pw):
		payload = {
			'max': '1',
			'fr': 'f',
			'part': 't',
			'partajax': 't',
			'im': 'f',
			'step': '1',
			'sid': '4',
			'l': 'sv_SE',
			'types': '195',
			'subtypes': '230,231',
			'fe': ['26.Key', '23.Valla'],
			'dates': date,
			'starttime': starttime,
			'endtime': endtime
		}

		headers = {'user-agent': 'chrome'}

		# bokade rum här
		rooms = self.__session.get('https://cloud.timeedit.net/liu/web/wr_stud/objects.json',params=payload)
		rooms = json.loads(rooms.text)
		return rooms['objects']

	def book(self, date, starttime, endtime, acc, pw):
		rooms = self.__get_rooms(date, starttime, endtime, acc, pw)
		print(rooms)
		first_best = rooms[0]['idAndType']
		if ":" not in starttime:
			starttime = starttime + ':15'
		if ":" not in endtime:
			endtime = endtime + ':00'
		#o: '435564.184' is unique to each account?
		payload = {
			'kind': 'reserve',
			'nocache': '4',
			'l': 'sv_SE',
			'o': [first_best, '389614.184'],
			'aos': '',
			'dates': date,
			'starttime': starttime,
			'endtime': endtime,
			'url': 'https://cloud.timeedit.net/liu/web/wr_stud/ri1Q8.html',
			'fe7': '',
		}

		response = self.__session.post(
			'https://cloud.timeedit.net/liu/web/wr_stud/ri1Q8.html',
			data=payload
		)


		# use (?<=\?id=)\d* regexp to find id and send email
		match = re.search('(?<=\?id=)\d*', response.url)
		id = match.group(0)
		
		return id

	#TODO this function
	def send_email(self, id, email):
		#print ("send email {}".format(id))

		params = {
			'id': id,
			'media': 'html',
			'mailto': email,
			'dt': 't',
			'sid': '4',
			'subject': 'Bokat rum',
		}

		payload = {
			'mail': ''
		}

		response = self.__session.post(
			'https://cloud.timeedit.net/liu/web/wr_stud/ri1Q8.html',
			params = params,
			data=payload
		)


if __name__ == "__main__":
	acc = account
	pw = password
	booker = Booker()
	booker.login(acc, pw)
	#booker.get_rooms("20181222-20181222", "14:00", "15:00")
	book_id = booker.book("20181226", "14:00", "15:00")
	booker.send_email(book_id, 'dylma900@student.liu.se')
