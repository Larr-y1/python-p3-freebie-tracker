from models import Dev, Company, Freebie
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()

# Create
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

company1 = Company(name="Google", founding_year=1998)
company2 = Company(name="Amazon", founding_year=1994)

session.add_all([dev1, dev2, company1, company2])
session.commit()

# Add Freebies
fb1 = Freebie(item_name="T-shirt", value=10, dev=dev1, company=company1)
fb2 = Freebie(item_name="Sticker", value=2, dev=dev1, company=company2)
fb3 = Freebie(item_name="Mug", value=15, dev=dev2, company=company1)

session.add_all([fb1, fb2, fb3])
session.commit()
