#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game  # Make sure models.py is in the same directory or adjust the import

fake = Faker()

if __name__ == '__main__':
    # Create a new database connection
    engine = create_engine('sqlite:///seed_db.db')  # This will create 'seed_db.db' in your directory
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clear existing data
    session.query(Game).delete()
    session.commit()

    print("Seeding games...")

    # Generate fake games
    games = [
        Game(
            title=fake.name(),
            genre=fake.word(),
            platform=fake.word(),
            price=random.randint(0, 60)
        )
        for _ in range(50)
    ]

    # Insert into database
    session.bulk_save_objects(games)
    session.commit()

    print("Done seeding!")