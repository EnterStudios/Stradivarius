# artists/mongoadmin.py

# Import the MongoAdmin base class
from mongonaut.sites import MongoAdmin

# Import your custom models
from artists.models import Musician

# Instantiate the MongoAdmin class
# Then attach the mongoadmin to your model
Musician.mongoadmin = MongoAdmin()