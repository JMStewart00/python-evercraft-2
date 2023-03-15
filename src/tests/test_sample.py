# You can write tests here or create new files in this directory with the name test_[something].py
from character import Character

# Tests
# Create a Character
def test_create_character():
    c = Character()
    assert isinstance(c, Character)

# Character has a name
def test_create_character_with_name():
    c = Character()
    assert hasattr(c, 'name')

def test_characters_have_unique_names():
    c1 = Character()
    c2 = Character()
    c2.name = 'Toby'
    assert c1.name != c2.name
# Character can set name

# Character can have alignment
def test_alignment():
    assert hasattr(Character(), 'alignment')

def test_alignment_unique():
    c1 = Character()
    c2 = Character()
    c2.alignment = 'Evil'
    assert c1.alignment is not c2.alignment
# Character can be Neutral
# Character can be Good
# Character can be Evil
# Class for alignment? 
# Character has armor attribute
# Character has hit points (hp) attribute
# Character armor defaults to 10
# Character hp defaults to 5
# Character needs to be able to attack another Character
# Character rolls a 20, attack succeeds
# Character rolls a 17, beats opp armor, attack succeeds
# Character rolls a 1, opp armor to much, attack fails
# some sort of loop test to test for all rolls
# On successful attack, combatant loses hit points
# On roll = 20, critical hit dealt, attack x2
# Check hitpoints after successful attack, if < 0, dead
# Character has an attribute of alive: true