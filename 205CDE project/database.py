from flask import Flask, render_template, request, session, redirect, url_for
import pymysql
import datetime
import os, sys
app = Flask(__name__)
app.secret_key = "123456"

db = pymysql.connect("localhost", "root", "49448530", "205CDE")
cursor = db.cursor()

@app.route('/login')
def login():
	return render_template("login.html")


@app.route('/member/profile')
def member_profile():
	if 'username' in session :

		info = {}
		user = session['username']
		sql = "SELECT * FROM Member WHERE Username = '" + user + "'"

		cursor.execute(sql)
		db.commit()

		results = cursor.fetchall()
		for row in results:
			info.update({"ID" : row[0]})
			info.update({"Fname" : row[1]})
			info.update({"Lname" : row[2]})
			info.update({"username" : row[3]})
			info.update({"email" : row[4]})
			info.update({"pw" : row[5]})
			info.update({"mobile" : row[6]})
		
		return render_template("member_profile.html", info = info)

	else:
		errorMessage = "Please login as member to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))


@app.route('/member_profile/edit')
def member_profile_edit():
	if 'username' in session :

		username = session['username']
		info = {}

		sqlget = "SELECT * FROM Member WHERE Username = '" + username + "'"

		cursor.execute(sqlget)
		db.commit()

		results = cursor.fetchall()
		for row in results:
			info.update({"ID" : row[0]})
			info.update({"Fname" : row[1]})
			info.update({"Lname" : row[2]})
			info.update({"username" : row[3]})
			info.update({"email" : row[4]})
			info.update({"pw" : row[5]})
			info.update({"mobile" : row[6]})

		return render_template("member_profile_edit.html", info=info)

	else:
		errorMessage = "Please login as member to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))


@app.route('/member_profile/edit/submit', methods = ['POST', 'GET'])
def member_profile_edit_submit():
	if 'username' in session :
		if request.method == "POST":
			ID = request.form["memberID"]
			Fname = request.form['firstName']
			Lname = request.form['lastName']
			email = request.form['email']
			mobile = request.form['phoneNum']
			pw = request.form['enterPassword']
			newPW = request.form['setPassword']

			sqlget = "SELECT Password FROM Member WHERE MemberID = '" + ID + "'"
			cursor.execute(sqlget)
			db.commit()

			results = cursor.fetchall()
			for row in results:
				pw_db = row[0]

			if pw == pw_db:

				if newPW != "":
					sqlupdate = "UPDATE Member SET FirstName ='"+Fname+"',LastName ='"+Lname+"',Email = '"+email+"',ContactNumber ='" + mobile + "',Password ='" + newPW + "' WHERE MemberID = "+ ID

				else:
					sqlupdate = "UPDATE Member SET FirstName ='"+Fname+"',LastName ='"+Lname+"',Email = '"+email+"',ContactNumber ='" + mobile +"' WHERE MemberID = "+ ID

				cursor.execute(sqlupdate)
				db.commit()
				return(redirect(url_for('member_profile')))

			else:
				errorMessage = "Wrong Password"
				return(render_template("error_message.html", errorMessage = errorMessage))

	else:
		errorMessage = "Please login as member to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))



@app.route('/loginsubmit/member', methods = ['POST', 'GET'])
def loginsubmit_member():

	if request.method == "POST":
		username = request.form['username']
		pw = request.form['password']

	try:

		sql = "SELECT Username, Password FROM Member WHERE Username =" + "'" + username + "'"

		cursor.execute(sql)
		db.commit()

		if cursor.rowcount > 0: #if username exists
			results = cursor.fetchall()

			for row in results:
				memberName = row[0]
				memberPW = row[1]

			if pw == memberPW:
				session['username'] = memberName
				if 'staff' in session :
					session.pop('staff', None)
				return (redirect(url_for('home')))
			else:
				errorMessage = "Wrong Password."
				return(render_template("error_message.html", errorMessage = errorMessage))

		else:
			errorMessage = "Username does not exist."
			return(render_template("error_message.html", errorMessage = errorMessage))
	except:
		db.rollback()
	

@app.route('/member/booking_history')
def member_booking_history():

	if 'username' in session :

		sqlget_memberID = "SELECT MemberID FROM Member WHERE Username = '" + session['username'] + "'"
		cursor.execute(sqlget_memberID)
		db.commit()
		resultID = cursor.fetchall()

		for row in resultID:
			memberID = row[0]

		info={"bookingID":[], "participants":[], "date":[], "start":[], "end":[], "room":[], "price":[]}

		sql = "SELECT BookingID, Participant, BookingDate, StartTime, EndTime, Room, TotalPrice FROM Reservation WHERE MemberID ='" + str(memberID) +"'"
						
		cursor.execute(sql)
		db.commit()

		record = False

		if cursor.rowcount > 0:
			record = True

			results = cursor.fetchall()
			for row in results:
				info["bookingID"].append(row[0])
				info["participants"].append(row[1])
				info["date"].append(row[2])
				info["start"].append(row[3])
				info["end"].append(row[4])
				info["room"].append(row[5])
				info["price"].append(row[6])
		

			return render_template("member_booking_history.html", info=info, record=record)

		else:
			return render_template("member_booking_history.html", record=record)

	else:
		errorMessage = "Please login as member to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))

@app.route('/member/booking_history/search', methods = ['POST', 'GET'])
def member_booking_history_search():
	if 'username' in session :
		if request.method == "POST":
			bookingID = request.form['bookingID']

			sqlget_memberID = "SELECT MemberID FROM Member WHERE Username = '" + session['username'] + "'"
			cursor.execute(sqlget_memberID)
			db.commit()
			resultID = cursor.fetchall()

			for row in resultID:
				memberID = row[0]


			sql = "SELECT * FROM Reservation WHERE BookingID = " + bookingID + " AND MemberID ='" + str(memberID) +"'"

			cursor.execute(sql)
			db.commit()
			info={}
			column = []

			record = False

			if cursor.rowcount > 0:
				record = True

				results = cursor.fetchall()

				for i in cursor.description:			
					column.append(i[0]) # get all column name from sql

						
				for x in range(len(column)):
					for row in results:
						info.update({column[x]: row[x]}) # get the key of dict from column name

				return(render_template("booking_records_record.html",column=column, info=info, record=record))

			else:
				errorMessage = "No record found."
				return(render_template("error_message.html", errorMessage = errorMessage))

	else:
		errorMessage = "Please login as member to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))




@app.route('/login/staff')
def login_staff():
	return (render_template("staff_login.html"))


@app.route('/loginsubmit/staff', methods = ['POST', 'GET'])
def loginsubmit_staff():
	

	if request.method == "POST":
		username = request.form['username']
		pw = request.form['password']

	try:

		sql = "SELECT Username, Password FROM Staff WHERE Username =" + "'" + username + "'"
		
		cursor.execute(sql)
		db.commit()


		if cursor.rowcount > 0:
			results = cursor.fetchall()
			for row in results:
				staffName = row[0]
				staffPW = row[1]

			if pw == staffPW:
				session['staff'] = staffName
				if 'username' in session :
					session.pop('username', None)
				return (redirect(url_for('home')))

			else:
				errorMessage = "Wrong Password."
				return(render_template("error_message.html", errorMessage = errorMessage))

		else:
			errorMessage = "Staff Username does not exist."
			return(render_template("error_message.html", errorMessage = errorMessage))

	except:
		db.rollback()

@app.route('/booking_records')
def booking_records():
	if 'staff' in session :

		info={"bookingID":[], "name":[], "participants":[], "date":[], "start":[], "end":[], "room":[]}

		sql = "SELECT BookingID, Name, Participant, BookingDate, StartTime, EndTime, Room FROM Reservation"

		cursor.execute(sql)
		db.commit()

		results = cursor.fetchall()
		for row in results:
			info["bookingID"].append(row[0])
			info["name"].append(row[1])
			info["participants"].append(row[2])
			info["date"].append(row[3])
			info["start"].append(row[4])
			info["end"].append(row[5])
			info["room"].append(row[6])
		
		return render_template("booking_records.html", info=info)

	else:
		errorMessage = "Please login as staff to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))

@app.route('/booking_records/filter', methods = ['POST', 'GET'])
def booking_records_filter():

	if 'staff' in session :

		if request.method == "POST":
			condition = request.form.get('condition')
			value = request.form.get('value')

			sql1 = "SELECT "


			sql_list = ["BookingID", "Name", "Participant", "BookingDate", "StartTime", "EndTime", "Room"]

			for i in sql_list:
				if condition == i:
					sql_list.remove(i)	#remove item that is == condition

			sql2 = condition

			for i in range(len(sql_list)):
				sql2 = sql2 + ", " + sql_list[i]

			sql3 = " FROM Reservation WHERE " + condition + " = '" + str(value) + "'"

			full_sql = sql1 + sql2+ sql3 #put condition to the first column

			cursor.execute(full_sql)
			db.commit()
			info={}
			column = []		

			record = False

			if cursor.rowcount > 0:
				record = True
				
				results = cursor.fetchall()

				for i in cursor.description:			
					column.append(i[0]) # get all column name from sql


				x = 0		
				for x in range(len(column)):
					for row in results:
						info.update({column[x]: []}) # get the key of dict from column name

					for row in results:
						info[column[x]].append(row[x]) # append the record to the dict's lists

				return(render_template("booking_records_filter.html",column=column,info=info, record=record))

			else:
				return(render_template("booking_records_filter.html", record=record))

		else:
			errorMessage = "Method Error"
			return(render_template("error_message.html", errorMessage = errorMessage))


	else:
		errorMessage = "Please login as staff to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))



@app.route('/booking_records/search', methods = ['POST', 'GET'])
def booking_records_search():

	if 'staff' in session :

		if request.method == "POST":
			bookingID = request.form['bookingID']

		return(redirect(url_for('booking_records_record',bookingID=bookingID)))

	else:
		errorMessage = "Please login as staff to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))



@app.route('/booking_records/<bookingID>', methods = ['POST', 'GET'])
def booking_records_record(bookingID):

	if 'staff' in session :

		sql = "SELECT * FROM Reservation WHERE BookingID = " + bookingID

		cursor.execute(sql)
		db.commit()
		info={}
		column = []

		results = cursor.fetchall()

		for i in cursor.description:			
			column.append(i[0]) # get all column name from sql

				
		for x in range(len(column)):
			for row in results:
				info.update({column[x]: row[x]}) # get the key of dict from column name


		return(render_template("booking_records_record.html",column=column, info=info))

	else:
		errorMessage = "Please login as staff to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))

@app.route('/register')
def register():
	return render_template("register.html")

@app.route('/register/success', methods = ['POST', 'GET']) #For registration
def register_success():
	all_users = []
	
	if request.method == 'POST':
		Fname = request.form['firstName']
		Lname = request.form['lastName']
		username = request.form['username']
		email = request.form['email']
		PW = request.form['setPassword']
		mobile = request.form['phoneNum']

	try:
		repeat = False
		sqlcheck = "SELECT Username FROM Member" #check for repeated username

		cursor.execute(sqlcheck)
		db.commit()

		results = cursor.fetchall()
		for row in results:
			all_users.append(row)

		i = 0
		
		for i in all_users:
			if username in str(all_users):
				repeat = True
				break

		
		if repeat == False:
			sqlinsert = "INSERT INTO Member (FirstName, LastName, Username, Email, Password, ContactNumber) VALUES" + "('"  + Fname + "','" + Lname + "','" + username + "','" + email + "','" + PW + "','" + mobile + "')"
			cursor.execute(sqlinsert)
			db.commit()
		
		else:
			errorMessage = "This username has already been used. Please set another username."
			return(render_template("error_message.html", errorMessage = errorMessage))

	except:
		db.rollback()

	
	return render_template("register_success.html", username = username)

@app.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('staff', None)
	return redirect(url_for('home'))

@app.route('/')
@app.route('/home')
def home():
	return render_template("home.html")

@app.route('/feedback')
def feedback():
	return render_template("feedback.html")


@app.route('/feedback/submit', methods = ['POST', 'GET'])
def feedback_submit():
	if request.method == 'POST':
		inputName = request.form.get('name',None)
		if inputName == "":
			name = "NULL"
		else:
			name = "'"+inputName+"'"
		inputRoom = request.form.get('roomChoice')
		room = "Room "+ inputRoom
		roomRate = request.form.get('roomRating')
		serviceRate = request.form.get('serviceRating')
		comment = request.form.get('comment')

		sql = "INSERT INTO Feedback(Name, Room, RoomRating, ServiceRating, Comment) VALUES( " + name +", '"+ str(room) +"', "+ str(roomRate) +", "+ str(serviceRate) +", '"+ comment + "')"
		cursor.execute(sql)
		db.commit()

		return(render_template('feedback_success.html'))

@app.route('/feedback/staff/view')
def feedback_staff_view():
	if 'staff' in session :
		feedback = {"fbID":[], "name":[], "room":[], "roomRate":[], "serviceRate":[], "comment":[]}
		sql = "SELECT * FROM Feedback"

		cursor.execute(sql)
		db.commit()

		results = cursor.fetchall()
		for row in results:
			feedback["fbID"].append(row[0])			
			feedback["room"].append(row[2])			
			feedback["roomRate"].append(row[3])
			feedback["serviceRate"].append(row[4])
			feedback["comment"].append(row[5])
			if row[1] == None:
				feedback["name"].append('Anonymous')
			else:
				feedback["name"].append(row[1])


		#for storing room rate
		allRate={}
		sumRate={}
		avgRate={}

		sumService = 0
		for i in range(len(feedback["serviceRate"])):
			sumService += feedback["serviceRate"][i]

		avgService = round(sumService/len(feedback["serviceRate"]) , 1) #average service rate

		for x in feedback["room"]:
			if not(x in avgRate):
				sumRate[x]= 0
				avgRate[x]= 0
				allRate[x]=[]	#add db room name to dict

		for y in range(len(feedback["room"])):
			sumRate[feedback["room"][y]]+= feedback["roomRate"][y] #sum rate of each room
			allRate[feedback["room"][y]].append(feedback["roomRate"][y]) #append each rate to corresponding room list

		for z in sumRate:
			avgRate[z] = round(sumRate[z]/len(allRate[z]) , 1) #avg rate of each room


		return(render_template('staff_view_feedback.html', fb=feedback, avgService=avgService, avgRate=avgRate))
	else:
		errorMessage = "Please login as staff to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))

@app.route('/rooms')
def rooms():
	info = {"roomID":[],
			"roomName":[],
			"area":[],
			"capacity":[],
			"theme":[]}

	sql = "SELECT * FROM Room"

	cursor.execute(sql)
	db.commit()

	results = cursor.fetchall()
	for row in results:
		info["roomID"].append(row[0])
		info["roomName"].append(row[1])
		info["area"].append(row[2])
		info["capacity"].append(row[3])
		info["theme"].append(row[4])

	img = sorted(os.listdir(os.path.join(app.static_folder,'IMG/Room')))
	carousel = []
	for i in range(len(info["roomID"])):
		carousel.append("carousel-"+str(i+1)) #create different id for the slides div in rooms.html 
	
	sqlget_rate = "SELECT Room, RoomRating FROM Feedback"

	cursor.execute(sqlget_rate)
	db.commit()

	allRate={}
	sumRate={}
	avgRate={}

	for i in info["roomName"]:
		allRate[i]=[]
		sumRate[i]= 0
		avgRate[i]= 0

	results_rate = cursor.fetchall()
	for row in results_rate:
		allRate[row[0]].append(row[1])
		sumRate[row[0]] += row[1]

	for y in allRate:
		avgRate[y]= round(sumRate[y]/len(allRate[y]), 1)
			

	return render_template("rooms.html", info=info, img=img, carousel=carousel, rate=avgRate)


@app.route('/rooms/staff/edit')
def rooms_staff_edit():

	if 'staff' in session :
		info = {"roomID":[],
				"roomName":[],
				"area":[],
				"capacity":[],
				"theme":[]}

		sql = "SELECT * FROM Room"

		cursor.execute(sql)
		db.commit()

		results = cursor.fetchall()
		for row in results:
			info["roomID"].append(row[0])
			info["roomName"].append(row[1])
			info["area"].append(row[2])
			info["capacity"].append(row[3])
			info["theme"].append(row[4])

		img = sorted(os.listdir(os.path.join(app.static_folder,'IMG/Room')))
		carousel = []
		for i in range(len(info["roomID"])):
			carousel.append("carousel-"+str(i+1)) #create different id for the slides div in rooms.html 
			

		return render_template("rooms_staff_edit.html", info=info, img=img, carousel=carousel)
	else:
		errorMessage = "Please login as staff to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))

@app.route('/rooms/staff/edit/submit', methods = ['POST', 'GET'])
def rooms_staff_edit_submit():
	if 'staff' in session :
		if request.method == 'POST':
			ID = request.form['editID']
			area = request.form['editArea']
			capacity = request.form['editCapacity']
			theme = request.form['editTheme']

			sql = "UPDATE Room SET Area = " + area + ", Capacity = " + capacity + ", Theme = '" + theme + "' WHERE RoomID = " + ID
			cursor.execute(sql)
			db.commit()

			
			return(redirect(url_for('rooms')))
	else:
		errorMessage = "Please login as staff to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))

@app.route('/menu')
def menu():
	facilityName = []
	price = []

	db_menuTable=[]
	# to get total amt of menu set and name of the menu set table 
	sqlget_table = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = '205CDE' AND TABLE_NAME LIKE '%MenuSet%'" 

	cursor.execute(sqlget_table)
	db.commit()

	results_table = cursor.fetchall() 
	for row in results_table:
		db_menuTable.append(row[0])
		
	menu = []
	for x in db_menuTable:
		x = {"id":[], "item": [], "qty":[], "unit":[]}
		menu.append(x)


	sqlget_price = "SELECT FacilityName, Price FROM ExtraFacility WHERE FacilityName LIKE '%Menu%'"
	cursor.execute(sqlget_price)
	db.commit()

	results_price = cursor.fetchall() 
	for row in results_price:
		facilityName.append(row[0])
		price.append(row[1])


	sqlget_menu = ""

	for i in range(len(menu)):

		sqlget_menu = "SELECT * FROM " + db_menuTable[i]
		cursor.execute(sqlget_menu)
		db.commit()

		results_menu = cursor.fetchall() 

		
		for row in results_menu:
			menu[i]["id"].append(row[0])
			menu[i]["item"].append(row[1])
			menu[i]["qty"].append('%g'%(row[2]))
			menu[i]["unit"].append(row[3])

	return render_template("menu.html", facilityName=facilityName, price=price, menu=menu)


@app.route('/menu/staff/edit')
def menu_staff_edit():
	if 'staff' in session :
		
		facilityName = []
		price = []

		db_menuTable=[]
		# to get total amt of menu set and name of the menu set table 
		sqlget_table = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = '205CDE' AND TABLE_NAME LIKE '%MenuSet%'" 

		cursor.execute(sqlget_table)
		db.commit()

		results_table = cursor.fetchall() 
		for row in results_table:
			db_menuTable.append(row[0])
			
		menu = []
		for x in db_menuTable:
			x = {"id":[], "item": [], "qty":[], "unit":[]}
			menu.append(x)


		sqlget_price = "SELECT FacilityName, Price FROM ExtraFacility WHERE FacilityName LIKE '%Menu%'"
		cursor.execute(sqlget_price)
		db.commit()

		results_price = cursor.fetchall() 
		for row in results_price:
			facilityName.append(row[0])
			price.append(row[1])

		sqlget_menu = ""

		for i in range(len(menu)):

			sqlget_menu = "SELECT * FROM " + db_menuTable[i]
			cursor.execute(sqlget_menu)
			db.commit()

			results_menu = cursor.fetchall() 

			
			for row in results_menu:
				menu[i]["id"].append(row[0])
				menu[i]["item"].append(row[1])
				menu[i]["qty"].append('%g'%(row[2]))
				menu[i]["unit"].append(row[3])

		return render_template("menu_staff_edit.html", facilityName=facilityName, price=price, menu=menu, menuName = db_menuTable)

	else:
		errorMessage = "Please login as staff to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))


@app.route('/menu/staff/delete',methods = ['POST', 'GET'])
def menu_staff_delete():
	if 'staff' in session :
		if request.method == 'POST':
			menuName = request.form['delMenuName']
			itemID = request.form['delItemID']

			sql = "DELETE FROM " + menuName +" WHERE ItemID = " + str(itemID)
			cursor.execute(sql)
			db.commit()

		return(redirect(url_for('menu_staff_edit')))

	else:
		errorMessage = "Please login as staff to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))


@app.route('/menu/staff/add',methods = ['POST', 'GET'])
def menu_staff_add():
	if 'staff' in session :
		if request.method == 'POST':
			menuName = request.form['addMenuName']

			itemName = request.form['addItemName']
			itemQty = request.form['addItemQty']
			itemUnit = request.form['addItemUnit']

			sql = "INSERT INTO " + menuName +" (FoodItem, Quantity, Unit) VALUES('" + itemName+ "', " + str(itemQty) + ", '" + itemUnit + "')"
			cursor.execute(sql)
			db.commit()

		return(redirect(url_for('menu_staff_edit')))

	else:
		errorMessage = "Please login as staff to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))

@app.route('/menu/staff/change_price',methods = ['POST', 'GET'])
def menu_staff_change_price():
	if 'staff' in session :
		if request.method == 'POST':
			menuName = request.form['menuName']

			price = request.form['changePrice']


			sql = "UPDATE ExtraFacility SET Price = " + str(price) + " WHERE FacilityName = '" + menuName + "'"
			cursor.execute(sql)
			db.commit()

		return(redirect(url_for('menu')))

	else:
		errorMessage = "Please login as staff to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))

@app.route('/pricing')
def pricing():
	room_info = {"name":[],"threeHR":[], "exHR":[]} # 3 hrs / extra hrs price for room
	sqlget_room = "SELECT RoomName, ThreeHrPrice, ExtraHrPrice FROM Room"
	cursor.execute(sqlget_room)
	db.commit()

	results_room = cursor.fetchall() 
	for row in results_room:
		room_info["name"].append(row[0])
		room_info["threeHR"].append(row[1])
		room_info["exHR"].append(row[2])


	ex_info = {"facilityName":[],"price":[]} # price for extra facilities
	sqlget_ex = "SELECT FacilityName, Price FROM ExtraFacility WHERE facilityName NOT LIKE '%Menu%'"
	cursor.execute(sqlget_ex)
	db.commit()

	results_ex = cursor.fetchall() 
	for row in results_ex:
		ex_info["facilityName"].append(row[0])
		ex_info["price"].append(row[1])
		

	return render_template("pricing.html", room=room_info, ex=ex_info)


@app.route('/pricing/staff/edit')
def pricing_staff_edit():
	if 'staff' in session :
		room_info = {"id":[],"name":[],"threeHR":[], "exHR":[]} # 3 hrs / extra hrs price for room
		sqlget_room = "SELECT RoomID, RoomName, ThreeHrPrice, ExtraHrPrice FROM Room"
		cursor.execute(sqlget_room)
		db.commit()

		results_room = cursor.fetchall() 
		for row in results_room:
			room_info["id"].append(row[0])
			room_info["name"].append(row[1])
			room_info["threeHR"].append(row[2])
			room_info["exHR"].append(row[3])


		ex_info = {"facilityID":[],"facilityName":[],"price":[]} # price for extra facilities
		sqlget_ex = "SELECT FacilityID, FacilityName, Price FROM ExtraFacility WHERE FacilityName NOT LIKE '%Menu%'"
		cursor.execute(sqlget_ex)
		db.commit()

		results_ex = cursor.fetchall() 
		for row in results_ex:
			ex_info["facilityID"].append(row[0])
			ex_info["facilityName"].append(row[1])
			ex_info["price"].append(row[2])

		return render_template("pricing_staff_edit.html", room=room_info, ex=ex_info)

	else:
		errorMessage = "Please login as staff to continue."
		return(render_template("error_message.html", errorMessage = errorMessage))

@app.route('/pricing/staff/edit/submit',methods = ['POST', 'GET'])
def pricing_staff_edit_submit():
	if request.method == 'POST':
		if 'staff' in session :

			rm1_3hr = request.form.get('room1_3hr_edit')
			rm2_3hr = request.form.get('room2_3hr_edit')
			rm3_3hr = request.form.get('room3_3hr_edit')
			threeHR = [rm1_3hr, rm2_3hr, rm3_3hr]

			rm1_exhr = request.form.get('room1_extra_edit')
			rm2_exhr = request.form.get('room2_extra_edit')
			rm3_exhr = request.form.get('room3_extra_edit')
			exHR = [rm1_exhr, rm2_exhr, rm3_exhr]

			facility1 = request.form.get('facility1_edit')
			facility2 = request.form.get('facility2_edit')
			facility = [facility1, facility2]

			sql=""

			for i in range(len(threeHR)):
				sql = "UPDATE Room SET ThreeHrPrice = " + str(threeHR[i]) + ", ExtraHrPrice = " + str(exHR[i])+ " WHERE RoomID = " + str(i+1)

				cursor.execute(sql)
				db.commit()


			for i in range(len(facility)):
				sql = "UPDATE ExtraFacility SET Price = " + str(facility[i]) + " WHERE FacilityID = " + str(i+1)

				cursor.execute(sql)
				db.commit()


			return(redirect(url_for('pricing')))

		else:
			errorMessage = "Please login as staff to continue."
			return(render_template("error_message.html", errorMessage = errorMessage))



@app.route('/bookingform')
def bookingform():
	if 'username' in session:
		info = {}
		sql = "SELECT MemberID, FirstName, LastName, ContactNumber FROM Member WHERE Username = '" + session["username"] + "'"

		cursor.execute(sql)
		db.commit()


		results = cursor.fetchall() 
		for row in results:
			info["memberID"]=row[0]
			info["Fname"]=row[1]
			info["Lname"]=row[2]
			info["contactNum"]=row[3]


		return render_template("bookingform.html", info=info)

	else:
		return render_template("bookingform.html")
	#return (str(info))

@app.route('/booking/confirm',methods = ['POST', 'GET'])
def confirm_booking():
	if request.method == 'POST':
		#==================for filling in the confirmation form============
		info = request.form
		check={}
		check["kitchenCheck"] = request.form.get('cookeryKitchen')
		check["photoCheck"]= request.form.get('photoTaking')
		check["cateringCheck"]= request.form.get('cateringService')
		check["menuACheck"]= request.form.get('menuA')
		check["menuBCheck"]= request.form.get('menuB')
		check["menuCCheck"]= request.form.get('menuC')

		#===================for calculating price=======================
		
		participant = int(request.form['participantNum'])
		date = request.form['bookingDate']
		start = request.form['bookingStartTime']
		end = request.form['bookingEndTime']

		start_time = start.split(":")
		end_time = end.split(":")
		startH = int(start_time[0])
		endH = int(end_time[0])
		if endH == 0:
			endH += 24
		hour = endH - startH #calculate total hours

		roomChoice = request.form['roomChoice']
		if roomChoice == "roomChoiceA":
			room = "Room A" #name same as database RoomName in Room
		elif roomChoice == "roomChoiceB":
			room = "Room B"
		else:
			room = "Room C"

		# fetch room price		
		sqlget_room = "SELECT ThreeHrPrice, ExtraHrPrice FROM Room WHERE RoomName ='" + room + "'"
		cursor.execute(sqlget_room)
		db.commit()

		results_room = cursor.fetchall()
		for row in results_room:
			three_hr_price = row[0]
			ex_hr_price = row[1]

		room_total_price = (three_hr_price + (hour-3)*ex_hr_price) * participant

		#=================================================

		check_ex = [] #add up all the facilities checked (except catering) to calculate payment
		check_menu = {} #add up the menu checked

		kitchenCheck = request.form.get('cookeryKitchen')
		if kitchenCheck:
			kitchen = "YES"
			check_ex.append("Cookery Kitchen")
		else:
			kitchen = "NO"

		photoCheck= request.form.get('photoTaking')
		if photoCheck:
			photo = "YES"
			check_ex.append("Professional Photo Taking")
		else:
			photo = "NO"


		menuA = 0
		menuB = 0
		menuC = 0

		cateringCheck = request.form.get('cateringService') #only calculate the menu amt that are checked in checkbox"
		if cateringCheck:
			menuACheck = request.form.get('menuA')
			menuBCheck = request.form.get('menuB')
			menuCCheck = request.form.get('menuC')

			if menuACheck:
				menuA = request.form.get('menuAamt')
				check_menu["6-7 Person Menu Set"] = int(menuA)

			if menuBCheck:
				menuB = request.form.get('menuBamt')
				check_menu["10-12 Person Menu Set"] = int(menuB)

			if menuCCheck:
				menuC = request.form.get('menuCamt')
				check_menu["18-22 Person Menu Set"] = int(menuC)


		sqlget_ex_name = "SELECT FacilityName FROM ExtraFacility"
		cursor.execute(sqlget_ex_name)
		db.commit()
		ex_name_results = cursor.fetchall()

		ex_name = [] #use check[] to match with the facility names include menu
		for row in ex_name_results:
			ex_name.append(row[0])


		#fetch extra facility prices include menu
		sqlget_ex_price = "SELECT Price FROM ExtraFacility"
		cursor.execute(sqlget_ex_price)
		db.commit()		
		ex_price_results = cursor.fetchall()

		ex_price = []
		for row in ex_price_results:
			ex_price.append(row[0])

		ex_total_price = 0

		for x in range(len(ex_name)):
			for y in range(len(check_ex)):
				if ex_name[x] == check_ex[y]: #if both list has matched name 
					ex_total_price += ex_price[x] #calculate extra facilities excluding catering
					
		for x in range(len(ex_name)):
			if ex_name[x] in check_menu: #if both list and dict has matched name 
				ex_total_price += check_menu[ex_name[x]] * ex_price[x] #calculate the total extra-facilities price including catering
				
		total_price = room_total_price + ex_total_price

		return render_template("bookingform_confirmation.html",info = info, check=check, total_price=total_price)

		
@app.route('/booking/payment',methods = ['POST', 'GET'])
def booking_payment():
	if request.method == 'POST':

		if 'username' in session:
			memberID = request.form['memberID'] #get ID for as foreign key

		name = request.form['bookingName']
		mobile = request.form['contactNum']
		participant = int(request.form['participantNum'])
		date = request.form['bookingDate']
		start = request.form['bookingStartTime']
		end = request.form['bookingEndTime']
		total_price = request.form['totalPrice']

		start_time = start.split(":")
		end_time = end.split(":")
		startH = int(start_time[0])
		endH = int(end_time[0])
		if endH == 0:
			endH += 24
		hour = endH - startH #calculate total hours

		roomChoice = request.form['roomChoice']
		if roomChoice == "roomChoiceA":
			room = "Room A" #name same as database RoomName in Room
		elif roomChoice == "roomChoiceB":
			room = "Room B"
		else:
			room = "Room C"

		repeatTime = True

		sqlget_time = "SELECT StartTime, EndTime FROM Reservation WHERE BookingDate = '" + date + "' AND Room = '" + room + "'"

		cursor.execute(sqlget_time)
		db.commit()

		db_time = {"start":[], "end":[]}

		if cursor.rowcount > 0:

			results_time = cursor.fetchall()

			startZ = datetime.datetime.strptime(start,"%H:%M")
			endZ = datetime.datetime.strptime(end,"%H:%M")


			for row in results_time:
				startX = str(row[0])	#convert db time record to string first, 
				startY = datetime.datetime.strptime(startX, "%H:%M:%S")  #then convert to datetime to match the format with the input time value
				db_time["start"].append(startY)

				endX = str(row[1])
				endY = datetime.datetime.strptime(endX, "%H:%M:%S") 
				db_time["end"].append(endY)


			for i in range(len(db_time["start"])):
				if (endZ <= db_time["start"][i]): #compare time with db records, check for any overlap time
					repeatTime = False
				elif (startZ >= db_time["end"][i]):
					repeatTime = False

		else:
			repeatTime = False


		if repeatTime == False:

			kitchenCheck = request.form.get('cookeryKitchen')
			if kitchenCheck:
				kitchen = "YES"
			else:
				kitchen = "NO"
	
			photoCheck= request.form.get('photoTaking')
			if photoCheck:
				photo = "YES"				
			else:
				photo = "NO"
	
			check_ex = [] #add up all the facilities checked (except catering) to calculate payment
			check_menu = {} #add up the menu checked

			kitchenCheck = request.form.get('cookeryKitchen')
			if kitchenCheck:
				kitchen = "YES"
				check_ex.append("Cookery Kitchen")
			else:
				kitchen = "NO"

			photoCheck= request.form.get('photoTaking')
			if photoCheck:
				photo = "YES"
				check_ex.append("Professional Photo Taking")
			else:
				photo = "NO"

			menuA = 0
			menuB = 0
			menuC = 0

			cateringCheck = request.form.get('cateringService') #only calculate the menu amt that are checked in checkbox"
			if cateringCheck:
				menuACheck = request.form.get('menuA')
				menuBCheck = request.form.get('menuB')
				menuCCheck = request.form.get('menuC')

				if menuACheck:
					menuA = request.form.get('menuAamt')
					check_menu["6-7 Person Menu Set"] = int(menuA)

				if menuBCheck:
					menuB = request.form.get('menuBamt')
					check_menu["10-12 Person Menu Set"] = int(menuB)

				if menuCCheck:
					menuC = request.form.get('menuCamt')
					check_menu["18-22 Person Menu Set"] = int(menuC)


			sqlget_ex_name = "SELECT FacilityName FROM ExtraFacility"
			cursor.execute(sqlget_ex_name)
			db.commit()
			ex_name_results = cursor.fetchall()

			ex_name = [] #use check[] to match with the facility names include menu
			for row in ex_name_results:
				ex_name.append(row[0])	

			#for inserting confirmed form
			if 'username' in session:
				sql = "INSERT INTO Reservation (Name, MemberID, ContactNumber, Participant, BookingDate, StartTime, EndTime, Room, CookeryKitchen, PhotoTaking, MenuAAmt, MenuBAmt, MenuCAmt, TotalPrice) VALUES('"  + name + "','" + memberID + "','" + mobile + "','" + str(participant) + "','" + date + "','" + start + "','" + end + "','" + room + "','" + kitchen + "','" + photo + "','" + str(menuA) + "','" + str(menuB) + "','" + str(menuC) + "','" + str(total_price) + "');"
			else:
				sql = "INSERT INTO Reservation (Name, ContactNumber, Participant, BookingDate, StartTime, EndTime, Room, CookeryKitchen, PhotoTaking, MenuAAmt, MenuBAmt, MenuCAmt, TotalPrice) VALUES('"  + name + "','" + mobile + "','" + str(participant) + "','" + date + "','" + start + "','" + end + "','" + room + "','" + kitchen + "','" + photo + "','" + str(menuA) + "','" + str(menuB) + "','" + str(menuC) + "','" + str(total_price) + "');"
			
			cursor.execute(sql)
			db.commit()
	
			sql_getID = "SELECT LAST_INSERT_ID()" #get auto_incrementID for updating record in payment
			cursor.execute(sql_getID)
			db.commit()
			IDresult = cursor.fetchall()
	
			for row in IDresult:
				ID = row[0]
	
			info = {"name":name, "date":date, "start":start, "end":end, "participant":participant, "hour":hour, "room":room, "total_price":total_price}

			return render_template("booking_payment.html", info = info, check_ex=check_ex, check_menu=check_menu, ID = ID)
		
		else:
			errorMessage = "This period has already been booked. Please choose another time slot or room."
			return(render_template("error_message.html", errorMessage = errorMessage))

@app.route('/booking/success',methods = ['POST', 'GET'])
def booking_success():
	if request.method == 'POST':
		cardType = request.form['cardType']
		cardNum = request.form['cardNum']
		bookingID = request.form['bookingID']

		cardNum_list = cardNum.split("-")

		info= {"cardType":cardType, "cardNum":cardNum, "bookingID":bookingID}

		sqlupdate_card = "UPDATE Reservation SET CardType = '" + cardType + "', CardNumber = '" + cardNum+ "' WHERE BookingID = " + bookingID
		cursor.execute(sqlupdate_card)
		db.commit()


	return(render_template("booking_success.html", info = info, cardNum_list=cardNum_list))


if __name__ == '__main__':
	app.run(debug = True)