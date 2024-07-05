import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("admin@gmail.com","password")
session.add(user)
 
user = User("nsrikanth2004@gmail.com", "1234")
session.add(user)
 
user = User("nsrikanth2004@gmail.com","python")
session.add(user)
 
# commit the record the database
session.commit()
 
session.commit()
