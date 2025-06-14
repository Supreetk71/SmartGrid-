from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Create database base class
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base) 