from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Text, DateTime

from tentacle.shared.screed import Screed

Base = declarative_base()

class ScreedBase(Base):
    
    __tablename__ = 'screeds'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    type = Column(String)
    inserted = Column(DateTime)
    modified = Column(DateTime)
    text = Column(Text)

    def __repr__(self):
        return "<Name(name='%s', description='%s', type='%s', text='%s')>" % (self.name, self.description, self.type, self.text)
    
def singleton(cls):
    return cls()

@singleton
class Datastore(object):
    
    _engine = None
    
    def __init__(self):
        self.engine(create_engine('sqlite:///:memory:', echo=True))
        Base.metadata.create_all(self.engine()) 

    def save_screed(self, screed):
        base = ScreedBase(name=screed.name(), description=screed.description(), type=screed.typeValue(), text=screed.to_json())
        return self.save(base)
    
    def get_screed(self, base_id):
        base = self.session().query(ScreedBase).get(base_id)
        if base is not None:
            screed = Screed()
            screed.load(base.text)
            return screed
            
        return None
    
    def save(self, base):
        session = self.session()
        session.add(base)
        session.commit()
        return base
    
    def engine(self, engine=None):
        #home = expanduser("~")
        if engine is not None:
            self._engine = engine
        return self._engine
                
    def session(self):
        engine = self.engine()
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    
    
