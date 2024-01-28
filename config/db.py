from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymsql://mxme:2024#Hola!@localhost:3306/studentlogin")

conn = engine.connect()

meta_data = MetaData()


