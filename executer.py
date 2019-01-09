import schedule
import time
from datetime import date, timedelta, datetime
import sys
from Booker import *
from constants import *

#TODO: make a class out of this...
#TODO: test all of this

class Executer:
	def __init__(self):
		self.__booker = Booker()

	def book(self, date, start_time, end_time, email):
		print("Signing in...")
		print(password)
		self.__booker.login(account, password)
		#self.__booker.get_rooms("20181222-20181222", "14:00", "15:00")
		print("Booking...")
		book_id = self.__booker.book(date, start_time, end_time)
		print("Sending email...")
		self.__booker.send_email(book_id, email)
		print("Booking done!")	
		print("Ending program")
		sys.exit(0)


def book(date, start_time, end_time, email):
	booker = Booker()
	print("Signing in...")
	booker.login(account, password)
	#booker.get_rooms("20181222-20181222", "14:00", "15:00")
	print("Booking...")
	book_id = booker.book(date, start_time, end_time)
	print("Sending verification email...")
	booker.send_email(book_id, email)
	print("Booking done! Hopefully without errors heheheuhue")	
	print("Ending program")
	sys.exit(0)

def job(in_date, start_time, end_time, email):
	print("Doing job")
	#print(in_date)
	#print(start_time)
	today = str(date.today()).replace("-", "")
	#print(today)
	print("Checking date...")
	if(in_date == today):
		book(in_date, start_time, end_time, email)



if __name__ == "__main__":
	#using dependency injection
	executer = Executer()
	executer.book('20180110', '19', '20', 'dylma900@student.liu.se')

"""
	print(type(sys.argv))
	if(len(sys.argv) != 5):
		raise ValueError("Need 5 arguments, example: python3 executer.py 20190102 14 15 dylma900@student.liu.se")
		sys.exit(0)

	today = str(date.today()).replace("-", "")

	#print(today)
	#TODO: Fix mess below
	in_date = sys.argv[1]
	start_time = sys.argv[2]
	end_time = sys.argv[3]
	email = sys.argv[4]

	tmp_date = datetime.strptime(in_date, '%Y%m%d').date()
	tomorrow = str(date.today() + timedelta(days=1)).replace("-", "")
	print(tomorrow)

	if(today == in_date or tomorrow == in_date):
		print('Today/tomorrow is the same as booking date')
		book(in_date, start_time, end_time, email)
	else:
		print('Scheduling booking to day before 00:01')
		tmp_date = datetime.strptime(in_date, '%Y%m%d').date()
		day_before = str(tmp_date - timedelta(days=1))
		#print(day_before)
		schedule.every().day.at("00:01").do(job, day_before, start_time, end_time, email)
		while True:
			schedule.run_pending()
			time.sleep(60) # wait one minute
"""