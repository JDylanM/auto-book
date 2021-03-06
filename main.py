import schedule
import time
from datetime import date, timedelta, datetime
import sys
from Booker import *
from Schedule import *
from CalendarHandler import *
from constants import *

#TODO: Book many in a row
#TODO: Add calender for the succeeded booking
#TODO: Error handling
#TODO: test

class Executer:
	def __init__(self):
		self.__calender = CalendarHandler()
		self.__acc_nr = 0
		
	def book_one(self, in_date, start_time, end_time, email):
		self.__in_date = in_date
		self.__start_time = start_time
		self.__end_time = end_time
		self.__email = email

		today = str(date.today()).replace("-", "")
		tomorrow = str(date.today() + timedelta(days=1)).replace("-", "")
		trimorrow = str(date.today() + timedelta(days=2)).replace("-", "")

		if(today == in_date or tomorrow == in_date or trimorrow == in_date):
			self.__book()
		else:
			print("Cannot book {} yet! Exiting program".format(self.__in_date))
			sys.exit(0)
		"""
		else:
			tmp_date = datetime.strptime(in_date, '%Y%m%d').date()
			book_day = str(tmp_date - timedelta(days=2)).replace("-", "")
			book_time = '22:00'
			print("Booking {} {} {}".format(in_date, start_time, end_time))
			print('is scheduled to execute at {} {}'.format(book_day, book_time))
			schedule.every().day.at(book_time).do(self.__job, book_day)
			while True:
				schedule.run_pending()
				time.sleep(60) # wait one minute
		"""

	def book_many(self, reservations, email):
		print("Number of meetings left {}".format(len(reservations)))
		print("--------------------------------------")
		trimorrow = str(date.today() + timedelta(days=2)).replace("-", "")
		for reservation in reservations:
			start_date = reservation["startdate"].replace("-", "")
			if trimorrow != start_date:
				continue
			start_time = reservation["starttime"][:2]
			end_time = reservation["endtime"][:2]
			self.book_one(start_date, start_time, end_time, email)
			#self.book_one("20200129", "19", "20", email)
			print("--------------------------------------")
				
	def __book(self):
		booker = Booker()

		#accounts from constants.py!
		acc = accounts[self.__acc_nr]["acc"]
		pw = accounts[self.__acc_nr]["pw"]
		self.__acc_nr += 1
		if self.__acc_nr == len(accounts):
			self.__acc_nr = 0

		
		print("Signing in with account {}...".format(acc))
		booker.login(acc, pw)
		print("Booking {} {}-{}....".format(self.__in_date, self.__start_time, self.__end_time))
		book_id, location = booker.book(self.__in_date, self.__start_time, self.__end_time, acc, pw)
		print("Sending email...")
		booker.send_email(book_id, self.__email)
		print("Adding in calendar...")
		self.__calender.book(self.__in_date, self.__start_time, self.__end_time, location)
		print("Booking done!")	
		print("--------------------------------------")

	def __job(self, book_day):
		print("Checking date...")
		today = str(date.today()).replace("-", "")
		print('comparing book_day {} and today {}'.format(book_day, today))
		if(book_day == today):
			self.__book()


if __name__ == "__main__":
	executer = Executer()
	if(len(sys.argv) == 5):
		in_date = sys.argv[1]
		start_time = sys.argv[2]
		end_time = sys.argv[3]
		email = sys.argv[4]
		executer.book_one(in_date, start_time, end_time, email)
	else:
		s = Schedule("https://cloud.timeedit.net/liu/web/schema/ri17Z036X45Z04Q6Z86g2Y90yQ046Y55x06gQY6Q557950g077Y5065y9Q9Zy6Qo.json")
		reservations = s.get_reservations()
		email = "dylma900@student.liu.se"
		executer.book_many(reservations, email)
