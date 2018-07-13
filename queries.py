from charactercreator.models import *
from armory.models import *
# How many total Characters are there - 302
# SQL
SELECT COUNT(*) FROM charactercreator_character
# ORM
Get All Characters
    charactors = Character.objects.all()
    len(charactors) = 302

# How many of each specific subclass?
# Cleric : 75
# SQL
SELECT COUNT(*) FROM charactercreator_cleric

# ORM
Get All Cleric Characters
    clerics = Cleric.objects.all()
    len(cleric) = 75


# Mage: 108
# SQL
SELECT COUNT(*) FROM charactercreator_mage

# ORM
Get All Mage Characters
    mage = Mage.objects.all()
    len(mage) = 108

# Thief: 51
# SQL
SELECT COUNT(*) FROM charactercreator_thief

# ORM
Get All Thief Characters
    thief = Fighter.objects.all()
    len(thief) = 51

# Fighter: 68
# SQL
SELECT COUNT(*) FROM charactercreator_fighter

# ORM
Get All Fighter Characters
    fighter = Fighter.objects.all()
    len(fighter) = 68

# necromancer: 11
# SQL
SELECT COUNT(*) FROM charactercreator_necromancer

# ORM
Get All Necromancer Characters
    necromancer = Necromancer.objects.all()
    len(necromancer) = 11

# How many total Items - 174
# SQL
SELECT COUNT(*) FROM armory_item

# ORM
Get items
    items = Item.objects.all()
    len(Item) = 174

# How many of the Items are weapons? How many are not?

# On average, how many Items does each Character have?
# On average, how many Weapons does each character have?