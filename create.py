from database import engine, Base
from database_models import Order  # MUST import models first

Base.metadata.create_all(bind=engine)

print("Tables created!")