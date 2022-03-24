from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Person

# Create a session
engine = create_engine('sqlite:///activities.db', echo=True)
Session = sessionmaker(bind=engine)

andrew = Person(first_name="Andrew", last_name="Dales")
people = [Person(first_name="Chris", last_name="Brolin"), Person(first_name='Vera', last_name="Malcova")]

sess = Session()
sess.add(andrew)
sess.add_all(people)
sess.commit()
sess.close()
