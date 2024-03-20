from _model import Auther, Book
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import traceback


session = None

engine = create_engine("sqlite:///./m2m.db")
Session = sessionmaker(bind=engine)
session = Session()

try:
    # book1 = Book(title="Dead people")
    # book2 = Book(title="How to make friends")

    # auther1 = Auther(name="Blue Renolds")
    # auther2 = Auther(name="Chip Egan")
    # auther3 = Auther(name="Alysaa Wytee")

    # book1.authers = [auther1, auther2]
    # book2.authers = [auther1, auther3]
    # session.add_all([book1, book2, auther1, auther2, auther3])
    # session.commit()

    

    print("data got filed in the db")


except:
    print("exception occurs...")
    print(traceback.format_exc())
    if session:
        session.close()
