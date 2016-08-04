
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
			password=request.form['password'])
		print ("DID I MADE A FRIEND?")
		session.add(friend)
		session.commit()
		print ("I made it past the commit")
		return redirect(url_for('main',friend=friend))

@app.route('/edit_info/', methods=['GET','POST'])
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
		return redirect(url_for('main'))




@app.route('/main/<int:person_id>')
def main(person_id):
	person=session.query(Person).filter_by(id=person_id).first()

	return render_template('main_page.html',person=person)

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
		return redirect(url_for('main'))




@app.route("/my_bucket/<int:person_id>", methods = ['GET', 'POST'])
def my_bucket(person_id):
	person = session.query(Person).filter_by(id=person_id).first()
	styles = person.split(",")
	totla_event = []
	for s in styles:
		current_events = session.query(Event).filter_by(style = s).all()
		totla_event += current_events 
	return render_template("my_bucket.html", person=person, events=totla_event)





if __name__ == '__main__':
	app.run(debug=True)
