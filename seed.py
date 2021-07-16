"""Seed file to make sample data for pets db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
whiskey = Pet(name='Whiskey', 
              species="dog", 
              photo_url="https://2.bp.blogspot.com/-3LLIwjxLQbk/VHtpfCCCtlI/AAAAAAABPNQ/I38y6dc2K8o/s1600/cute-dog-049-46.jpg",
              age="baby",
              notes="Hi",
              available=True)
lance = Pet(name='Lance', 
              species="cat", 
              photo_url="https://2.bp.blogspot.com/-3LLIwjxLQbk/VHtpfCCCtlI/AAAAAAABPNQ/I38y6dc2K8o/s1600/cute-dog-049-46.jpg",
              age="young",
              notes="Hi",
              available=True)
Ray = Pet(name='ray', 
              species="fish", 
              photo_url="https://2.bp.blogspot.com/-3LLIwjxLQbk/VHtpfCCCtlI/AAAAAAABPNQ/I38y6dc2K8o/s1600/cute-dog-049-46.jpg",
              age="adult",
              notes="Hi",
              available=True)

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(lance)
db.session.add(ray)

# Commit--otherwise, this never gets saved!
db.session.commit()
