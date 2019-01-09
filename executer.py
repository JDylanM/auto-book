import schedule
import time
from datetime import date, timedelta, datetime
import sys
from Booker import *
from constants import *

#TODO: Error handling
#TODO: test

class Executer:
	def __init__(self, in_date, start_time, end_time, email):
		self.__in_date = in_date
		self.__start_time = start_time
		self.__end_time = end_time
		self.__email = email

		#self.book()
		self.init_func()

	def init_func(self):
		today = str(date.today()).replace("-", "")
		tomorrow = str(date.today() + timedelta(days=1)).replace("-", "")

		if(today == in_date or tomorrow == in_date):
			print('Today/tomorrow is the same as booking date')
			self.__book()
		else:
			tmp_date = datetime.strptime(in_date, '%Y%m%d').date()
			book_day = str(tmp_date - timedelta(days=1)).replace("-", "")
			book_time = '00:01'
			print('Scheduling booking to {} {}'.format(book_day, book_time))
			schedule.every().day.at(book_time).do(self.__job, book_day)
			while True:
				schedule.run_pending()
				time.sleep(60) # wait one minute

				
	def __book(self):
		print("Signing in...")
		booker = Booker()
		booker.login(account, password)
		print("Booking...")
		book_id = booker.book(self.__in_date, self.__start_time, self.__end_time)
		print("Sending email...")
		booker.send_email(book_id, self.__email)
		print("Booking done!")	
		print("Ending program")
		sys.exit(0)

	def __job(self, book_day):
		print("Checking date...")
		today = str(date.today()).replace("-", "")
		print('comparing book_day {} and today {}'.format(book_day, today))
		if(book_day == today):
			self.__book()


if __name__ == "__main__":
	if(len(sys.argv) != 5):
		raise ValueError("Need 5 arguments, example: python3 executer.py 20190102 14 15 dylma900@student.liu.se")
		sys.exit(0)

	in_date = sys.argv[1]
	start_time = sys.argv[2]
	end_time = sys.argv[3]
	email = sys.argv[4]

	executer = Executer(in_date, start_time, end_time, email)
