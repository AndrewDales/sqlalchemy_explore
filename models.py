from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Sets up a Person table, this references "activities" via the person_activities table
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    # Gives a representation of a Person (for printing out)
    def __repr__(self):
        return f"<Person({self.first_name} {self.last_name})>"