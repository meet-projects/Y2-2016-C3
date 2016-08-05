
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

from flask import session as flasksession

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



@app.route('/', methods=['GET','POST'])
def first_page():
	return render_template("first_page.html")

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
			password=request.form['password'],
			event_fav=request.form['event_fav'])
		print ("DID I MADE A FRIEND?")
		session.add(friend)
		session.commit()
		print ("I made it past the commit")
		return redirect(url_for('log_in'))




@app.route('/edit_info', methods=['GET','POST'])
def edit_info():
	person = session.query(Person).filter_by(id=flasksession['user_id']).first()
	if request.method == 'GET':
		return render_template("edit_info.html", person=person)
	else:
		print('1')
		new_name = request.form['name']
		print('1')
		new_sir_name = request.form['sir_name']
		print('1')
		new_gender = request.form['gender']
		print('1')
		new_birth_date = request.form['birth_date']
		print('1')
		new_country = request.form['country']
		print('1')
		new_city = request.form['city']
		print('1')
		new_password = request.form['password']
		print('1')
		new_event_fav = request.form['event_fav']
		print('1')


		person.name = new_name
		person.sir_name = new_sir_name
		person.gender = new_gender
		person.birth_date = new_birth_date
		person.country = new_country
		person.city = new_city
		person.password = new_password
		person.event_fav = new_event_fav

		session.commit()
		return redirect(url_for('main_page'))





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




@app.route("/my_bucket/", methods = ['GET', 'POST'])
def my_bucket():
	person = session.query(Person).filter_by(id=flasksession['user_id']).first()
	styles = person.event_fav.split(",")
	print(styles)
	totla_event = []
	for s in styles:
		current_events = session.query(Event).filter_by(style = s).all()
		totla_event += current_events 
	return render_template("my_bucket.html", person=person, events=totla_event)


@app.route("/log_in", methods= ['GET','POST'])
def log_in():
	if request.method == 'POST':
		person = session.query(Person).filter_by(user_name=request.form['username']).first()
		if(request.form['password'] == person.password):
			flasksession['user_id'] = person.id
			return redirect(url_for('main_page'))
		else:
			return render_template('log_in.html')
	else:
		return render_template('log_in.html')





if __name__ == '__main__':
	app.run(debug=True)
