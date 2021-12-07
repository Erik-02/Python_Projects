import datetime
import time
import sqlite3


#CREATE AND OPEN THE DATABASE
#con = sqlite3.connect('Habits.db')
#c = con.cursor()

#c.execute('DROP TABLE All_Habits') 		#RE-CREATE DATABASE FROM THE START
#c.execute("""CREATE TABLE All_Habits (
#				Habit TEXT,
#				DW TEXT,
#				Start_Date TEXT,
#				CS INTEGER,
#				LS INTEGER)""")

#INSERTING THE PRE-REQUISETS
#c.execute("INSERT INTO All_Habits VALUES('8 Glasses of water', 'DAILY' , '2021-11-26 11:30:28' , 12, 19)")
#c.execute("INSERT INTO All_Habits VALUES('Jog 2 miles', 'DAILY' , '2021-11-26 14:30:28' , 1, 3)")
#c.execute("INSERT INTO All_Habits VALUES('Walk the dog', 'WEEKLY' , '2021-11-26 15:30:28' , 2, 4)")
#c.execute("INSERT INTO All_Habits VALUES('Read 5 pages', 'DAILY' , '2021-11-26 16:50:21' , 4, 5)")
#c.execute("INSERT INTO All_Habits VALUES('Review budget', 'WEEKLY' , '2021-11-26 17:27:14' , 0, 1)")


#SAVE AND CLOSE DATABASE
#con.commit()
#con.close()


#SHOW ALL RECORDS IN DATABASE
def show_all():		
	time.sleep(0.5)
	con = sqlite3.connect('Habits.db')
	c = con.cursor()

	c.execute("SELECT rowid,Habit,DW FROM All_Habits")

	items = c.fetchall()
	for item in items:
		print(item)
		time.sleep(0.8)

	con.commit()
	con.close()

#DELETE CERTAIN RECORD
def delete_one():
	id = input('\nSelect number to delete\n')

	con= sqlite3.connect('Habits.db')  #connect to databse
	c = con.cursor()					#open database
	
	c.execute("DELETE FROM All_Habits WHERE rowid=(?)", id)  #delete entry
	c.execute("SELECT * FROM All_Habits")
	items = c.fetchall()    				#COVERT REMAINING RECORDS TO LIST

	c.execute('DROP TABLE All_Habits')
	c.execute("""CREATE TABLE All_Habits (
						Habit TEXT,
						DW TEXT,
						Start_Date TEXT,
						CS INTEGER,
						LS INTEGER)""")

	for item in items:
		i0 = item[0]
		i1 = item[1]
		i2 = item[2]
		i3 = item[3]
		i4 = item[4]
		c.execute("INSERT INTO All_Habits VALUES(?,?,?,?,?)",(i0,i1,i2,i3,i4))  #RE-ENTER THE RECORDS
	
	c.execute("SELECT rowid,Habit,DW FROM All_Habits")
	print('Remaining Habits are:\n')
	items2 = c.fetchall()
	for item in items2:							#PRINT REMAINING ITEMS
		print(item)

	con.commit()
	con.close()	
	WaitToClose = input()		#Wait for user to exit the program manually, or when any input is given the program will close

#ADD NEW RECORD
def add_one():
	time.sleep(0.5)
	D_W_i = int(input('\nWill this Habit be: \n 1. Daily \n 2. Weekly?\n'))
	D_W = ''
	if D_W_i == 1:
		D_W = 'DAILY'		#SETTING IN HABIT AS DAILY

	elif D_W_i == 2:
		D_W = 'WEEKLY'	#SETTING IN HABIT AS WEEKLY

	else:
		pass

	Habit = input('\nPlease define the Habit.\n')

	from datetime import datetime
	now = datetime.now()
	dt_string = now.strftime("%y-%m-%d %H:%M:%S")

	con= sqlite3.connect('Habits.db')  #connect to databse
	c = con.cursor()					#open database
	
	c.execute("INSERT INTO All_Habits VALUES(?,?,?,?,?)",(Habit,D_W,dt_string,0,0))
	
	con.commit()
	con.close()
	WaitToClose = input()		#Wait for user to exit the program manually, or when any input is given the program will close

#LONGEST STREAK OF ALL HABITS
def longest_streak_all_habits():
	print('\nAll habits and their longest streak :\n')
	time.sleep(1.0)

	con= sqlite3.connect('Habits.db')  #connect to databse
	c = con.cursor()	

	c.execute("SELECT rowid,Habit,DW,LS FROM All_Habits")
	items2 = c.fetchall()
	for item in items2:							
		print(item)
	con.commit()
	con.close()
	WaitToClose = input()

#LONGEST STREAK OF SELECTED HABIT
def longest_streak_selected_habit():
	print('\nPlease select the number for Habit to be checked.')
	time.sleep(1)
	show_all()
	select = input()

	con= sqlite3.connect('Habits.db')  #connect to databse
	c = con.cursor()

	c.execute("SELECT Habit,LS FROM All_Habits WHERE rowid=(?)", (select))  #RETRIEVING SELECTED DATA

	items2 = c.fetchall()
	for item in items2:							
		print(item[0] + ', Longest streak = ' + str(item[1]))

	con.commit()
	con.close()	
	WaitToClose = input()		#Wait for user to exit the program manually, or when any input is given the program will close

#LIST OF HABITS WITH SAME PERIODICITY
def same_periodicity():
	period_int = int(input('\nWould you like to see a list of :\n 1. Daily habits\n 2. Weekly habits\n'))

	con= sqlite3.connect('Habits.db')  #connect to databse
	c = con.cursor()

	if period_int == 1:
		c.execute("SELECT Habit FROM All_Habits WHERE DW='DAILY' ")
		items2 = c.fetchall()
		for item in items2:							
			print(item)

	elif period_int == 2:
		c.execute("SELECT Habit FROM All_Habits WHERE DW='WEEKLY' ")
		items2 = c.fetchall()
		for item in items2:							
			print(item)
	else:
		pass

	con.commit()
	con.close()
	WaitToClose = input()		#Wait for user to exit the program manually, or when any input is given the program will close


#START OF THE PROGRAM
print('Hi there. Welcome to your Habit tracker app.')
time.sleep(1.5)
Activity = int(input('Do you want to : \n 1. Check, Add or Delete current Habits\n 2. Update Habit progress\n 3. Check Habit analysis\n'))

if Activity == 1:  #Choosing Route 1 (CHECK FLOW-CHART.PNG)
	print('Your current habits are: \n')
	show_all()
	time.sleep(1.5)
	cchActivity_1 = int(input('\nDo you want to :\n' + '1. Add new Habit\n' + '2. Delete a Habit\n'))

	if cchActivity_1 == 1:
		add_one()

	elif cchActivity_1 == 2:
		delete_one()

if Activity == 2:  #Choosing Route 2 (CHECK FLOW-CHART.PNG)
	print('\nPlease select the Habit you wish to mark complete\n')
	time.sleep(0.5)
	show_all()
	HP_Activity = input()

	con= sqlite3.connect('Habits.db')  #connect to databse
	c = con.cursor()

	c.execute("UPDATE All_Habits SET CS = (CS + 1) WHERE rowid=(?)",HP_Activity)
	c.execute("SELECT CS,LS FROM All_Habits WHERE rowid=(?)",HP_Activity)

	items2 = c.fetchall()
	for item in items2:						
		if item[0] > item[1]:
			c.execute("UPDATE All_Habits SET LS = (CS) WHERE rowid=(?)",HP_Activity)
	con.commit()
	con.close()
	time.sleep(1.0)
	print("Habit marked complete")
	print("Program closing now...")
	time.sleep(2.0)

if Activity == 3:  #Choosing Route 3 (CHECK FLOW-CHART.PNG)
	time.sleep(0.5)
	HA_Activity = int(input('\nDo you want to : \n 1. Check Longest Streak of All Habits\n 2. Check Longest Streak of certain Habit \n 3. Check List of All Habits being tracked\n 4. Chech List of Habits with Same Periodicity ?\n'))
	time.sleep(1)

	if HA_Activity == 1:
		longest_streak_all_habits()
	elif HA_Activity == 2:
		longest_streak_selected_habit()
	elif HA_Activity == 3:
		show_all()
		WaitToClose = input()		#Wait for user to exit the program manually, or when any input is given the program will close
	elif HA_Activity == 4:
		same_periodicity()


