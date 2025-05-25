#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    
    Session = sessionmaker(bind=engine)
    session = Session()
    import ipdb; ipdb.set_trace()
    
    dev = session.query(Dev).filter_by(name="Alice").first()
    if dev:
        print("Dev's companies:", dev.companies)

    company = session.query(Company).filter_by(name="Amazon").first()
    if company:
        print("Company's devs:", company.devs)

    freebie = session.query(Freebie).first()
    if freebie:
        print("Freebie details:", freebie.print_details())

