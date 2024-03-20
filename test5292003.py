import json
from _model import Auther, Book
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import traceback

def load_data_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        return data

def main():
    # Load data from JSON file
    data = load_data_from_json('test2.json')

    # Establish database connection
    engine = create_engine("sqlite:///./m2m.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        for item in data:
            # Create Book object
            book = Book(title=item['title'])

            # Create or get Author objects and associate with the book
            for author_name in item['authors']:
                author = session.query(Auther).filter_by(name=author_name).first()
                if not author:
                    author = Auther(name=author_name)
                book.authers.append(author)

            # Add book to session
            session.add(book)

        # Commit changes
        session.commit()
        print("Data loaded into the database successfully.")

    except Exception as e:
        print("An exception occurred while loading data into the database:")
        print(traceback.format_exc())
        session.rollback()

    finally:
        session.close()

if __name__ == "__main__":
    main()
