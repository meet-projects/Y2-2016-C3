
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base, Event, Person

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


logged_in = 1


@app.route('/', methods=['GET','POST'])
def first_page():
	return render_template("first_page.html")

<<<<<<< HEAD


	
=======
>>>>>>> 3a4bede639593fa8713df367047ce360c0d8e376
@app.route('/sign_up',methods=['GET','POST'])
def sign_up():
	if request.method == 'GET':
		return render_template("sign_up.html")
	else:
		print (request.form)
			
		friend=Person(
			name=request.form['name'],
			sir_name=request.form['sir_name'],
			gender=request.form['gender'],
			birth_date=request.form['birth_date'],
			country=request.form['country'],
			city=request.form['city'],
			user_name=request.form['user_name'],
			password=request.form['password'])
		print ("DID I MADE A FRIEND?")
		session.add(friend)
		session.commit()
		print ("I made it past the commit")
		return redirect(url_for('main_page',person_id=logged_in))

@app.route('/edit/<int:person_id>', methods=['GET','POST'])
def edit_info(person_id):
	friend = session.query(Person).filter_by(id=logged_in).first()
	if request.method == 'GET':
		return render_template("edit_info.html",)
	else:
		list_of_info=["name","sir_name","gender","birth_date","country","city","user_name","password", "event_fav"]
		for i in list_of_info:
			setattr(friend, i, request.form[i])


		session.commit()
		return redirect(url_for('main_page'))

	return render_template('edit_info')





@app.route('/add_event/', methods=['GET', 'POST'])
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
		return redirect(url_for('main_page'))




@app.route('/main_page')
def main_page():
	return render_template('main_page.html')

@app.route('/all_events')
def all_events():
	events= session.query(Event).all()
	return render_template('all_events.html', events = events)



@app.route("/edit_event/<int:event_id>", methods=['GET', 'POST'])
def edit_event(event_id):
	print(list(request.form.keys()))
	event = session.query(Event).filter_by(id=event_id).first()
	if request.method == 'GET':
		return render_template("edit_event.html", event=event)
	else:
		# read form data
		new_name = request.form['name']
		new_date = request.form['date']
		new_style = request.form['style']
		new_location = request.form['location']

		
		
		event.name = new_name
		event.date = new_date
		event.style = new_style
		event.location = new_location
	   
		session.commit()
		

		# redirect user to the page that views all friends
		return redirect(url_for('main_page'))




@app.route("/my_bucket/<int:person_id>", methods = ['GET', 'POST'])
def my_bucket(person_id):
	person = session.query(Person).filter_by(id=logged_in).first()
	styles = person.split(",")
	totla_event = []
	for s in styles:
		current_events = session.query(Event).filter_by(style = s).all()
		totla_event += current_events 
	return render_template("my_bucket.html", person=person, events=totla_event)


@app.route("/log_in")
def log_in():
	request.form['username']
	request.form['password']
	person = session.query(Person).filter_by(username=person_username).all()
	if(request.form['password'] == person.password):
		logged_in = person.id





if __name__ == '__main__':
	app.run(debug=True)
