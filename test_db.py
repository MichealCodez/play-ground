from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



Base = declarative_base()
metadata = MetaData()
engine = create_engine('sqlite:///birds.sqlite', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class Birds(Base):
    __tablename__ = 'birds'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    owner = Column(String(20))


Base.metadata.create_all(engine)

bird_1 = Birds(name='Jon', owner='Mike')

session.add(bird_1)
session.commit()
