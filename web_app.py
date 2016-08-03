
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base, Event

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


#YOUR WEB APP CODE GOES HERE
@app.route('/')
def main():
    return render_template('main_page.html')
<<<<<<< HEAD
@app.route('/edit_info', methods=['GET','POST'])
=======


@app.route('/edit_info' methods=['get','post'])
>>>>>>> 7d9197515c7d7f79949bacd2f941076f28e38489
def edit_info(person_id):
	friend = session.query(Person).filter_by(id=person_id).first()
	if request.method == 'GET':
		return render_template("edit_info.html", friend=friend)
	else:
		list_of_info=["name","sir_name","gender","birth_date","country","city","user_name","password"]
		for i in list_of_info:
			setattr(friend, i, request.form[i])


		session.commit()
		return redirect(url_for('main_page'))

	return render_template('edit_info')

<<<<<<< HEAD
@app.route('/sign_up' ,methods=['GET','POST'])
=======

@app.route('/add_event', methods=['GET', 'POST'])
def add_friend():
	if(request.method == 'GET'):
		return render_template("add_event.html")
	# read form data
	else:
		new_name = request.form['name']
		new_date = request.form['date']
		new_type = request.form['type']
		new_location = request.form['location']
		

		
		newevent = Event(name = new_name, date = new_date, type = new_type, location = new_location)

		
		session.add(newevent)
		session.commit()
		

		# redirect user to the page that views all friends
		return redirect(url_for('main_page'))



@app.route('/sign_up' methods=['get','post'])
>>>>>>> 7d9197515c7d7f79949bacd2f941076f28e38489
def sign_up():
	if request.method == 'GET':
		return render_template("sign_up.html", friend=friend)
	else:
		list_of_info=[name,sir_name,gender,birth_date,country,city,user_name,password]
		for i in list_of_info:
			i=request.form(str(i))
			
		friend=Person(name=name,sir_name=sir_name,gender=gender,birth_date=birth_date,country=country,city=city,user_name=user_name,password=password)
		session.add(friend)
	session.commit()



if __name__ == '__main__':
    app.run(debug=True)
