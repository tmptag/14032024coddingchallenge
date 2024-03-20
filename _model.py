from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship
import traceback

try:

    engine = create_engine("sqlite:///./m2m.db")
    Base = declarative_base()

    book_authers = Table(
        "book_authers",
        Base.metadata,
        Column("book_id", ForeignKey("books.id"), primary_key=True),
        Column("auther_id", ForeignKey("authers.id"), primary_key=True),
    )

    class Auther(Base):
        __tablename__ = "authers"

        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)

        books = relationship("Book", secondary="book_authers", back_populates="authers")

    class Book(Base):
        __tablename__ = "books"

        id = Column(Integer, primary_key=True)
        title = Column(String, nullable=False)

        authers = relationship(
            "Auther", secondary="book_authers", back_populates="books"
        )

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("Done the changes..")
except:
    print("in exception.")
    print(traceback.format_exc())
