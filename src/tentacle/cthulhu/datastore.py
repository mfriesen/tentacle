import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Text, DateTime

Base = declarative_base()

# configure Session class with desired options
Session = sessionmaker()

#engine = create_engine('sqlite:///:memory:')
engine = create_engine('sqlite:///tentacle.db')

# associate it with our custom Session class
Session.configure(bind=engine)

def save_screed(base): 
    return save(base)
    
def get_screed(base_id):
    session = Session()
    base = session.query(ScreedBase).get(base_id)
    if base is not None:
        session.expunge(base)
    return base
    
def get_screeds():
    session = Session()
    return session.query(ScreedBase).order_by(ScreedBase.name).all()

def delete_screed(base_id):
    session = Session()
    
    base = session.query(ScreedBase).get(base_id)
    if base is not None:
        session.delete(base)
    session.commit()
    
def delete_screeds():
    session = Session()
    session.query(ScreedBase).delete()
    session.commit()
    
def save(base):
    session = Session()
    session.add(base)
    session.commit()
    return base
                        
class ScreedBase(Base):
    
    __tablename__ = 'screeds'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    type = Column(String)
    Column('last_updated', DateTime, onupdate=datetime.datetime.now),
    text = Column(Text)

    def __repr__(self):
        return "<Name(name='%s', description='%s', type='%s', text='%s')>" % (self.name, self.description, self.type, self.text)

Base.metadata.create_all(engine)