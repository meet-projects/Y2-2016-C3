from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base

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
@app.route('/edit_info')
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






if __name__ == '__main__':
    app.run(debug=True)
