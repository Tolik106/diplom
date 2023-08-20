
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()





class Last_person(Base):
    __tablename__ = "last_person"
    user_id = sq.Column(sq.Integer, primary_key=True)
    person_id = sq.Column(sq.String(length=40), unique=True)



class User(Base):
    __tablename__ = "user"
    id = sq.Column(sq.Integer,sq.ForeignKey("last_person.user_id"), primary_key=True)
    # last_person_id = sq.Column(sq.Integer, sq.ForeignKey("last_person.user_id"))
    page = sq.Column(sq.String(length=6), unique=True)
    last_person = relationship("Last_person", backref="user", uselist=False)



class Favorites(Base):
    __tablename__ = "favorites"

    user_id = sq.Column(sq.Integer(), sq.ForeignKey('user.id'), primary_key=True)
    person_id = sq.Column(sq.Integer, primary_key=True)


class Black_list(Base):
    __tablename__ = "black_list"


    user_id = sq.Column(sq.Integer(), sq.ForeignKey('user.id'), primary_key=True)
    person_id = sq.Column(sq.Integer, primary_key=True)



def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)