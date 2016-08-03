
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


@app.route('/edit_info', methods=['GET','POST'])
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





@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
	if(request.method == 'GET'):
		return render_template("add_event.html")
	# read form data
	else:
		new_name = request.form['name']
		new_date = request.form['date']
		new_style = request.form['style']
		new_location = request.form['location']
		

		
		newevent = Event(name = new_name, date = new_date, style = new_style, location = new_location)

		
		session.add(newevent)
		session.commit()
		

		# redirect user to the page that views all friends
		return redirect(url_for('main'))





@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
	if request.method == 'GET':
		return render_template("sign_up.html")
	else:
		
			
		friend=Person(name=request.form['name'],sir_name=request.form['sir_name'],gender=request.form['gender'],birth_date=request.form['birth_date'],country=request.form['country'],city=request.form['city'],user_name=request.form['user_name'],password=request.form['password'])
		session.add(friend)
		session.commit()
	return redirect(url_for('main_page'))

if __name__ == '__main__':
    app.run(debug=True)
