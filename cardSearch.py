#This part of the code is used for controlling the wrapper to seek out cards from the database
#Using the MTG-sdk wrapper found here: https://github.com/MagicTheGathering/mtg-sdk-python

from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
import json
import requests

cardname = input('Please enter a card name to look up: ')

#Pull list of matching cards

cardlistnames = Card.where(name=cardname).all()

for i in cardlistnames:
    print(i.name, i.set_name, i.multiverse_id, i.image_url) 


