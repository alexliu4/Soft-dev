#trackStars_LiuA_ZaiL
#SoftDev1 pd7
#K02 -- NO-body expects the Spanish Inquisition!
#2018-09-09

import random



def randomizer():
    for i in range(5):
        print(random.random())
        return("hi")

print(randomizer())

KREWES = {

        'w': ['William Lu', 'Qian', 'Peter', 'Ahnaf', 'Kenny', 'Sophia', 'Sajed', 'Emily', 'Hasif', 'Brian ', 'Dennis', 'Jiayang', 'Shafali ', 'Isaac ', 'Tania', 'Derek', 'Shin', 'Vincent', 'Ricky', 'Puneet', 'Wei Wen', 'Tim', 'Jeffrey', 'Joyce ', 'Mohtasim', 'Simon', 'Thomas', 'Ray', 'Jack', 'Karen', 'Robin', 'Jabir', 'Johnny ', 'Matthew', 'Johnson Li', 'Angela', 'Crystal', 'Jiajie', 'Theodore (Dont really care)', 'Anton', 'Max', 'Bo', 'Andrew', 'Kendrick', 'Kevin', 'Kyle', 'Jamil', 'Mohammed', 'Ryan', 'Jason'],

        'm': ['Daniel', 'Aleksandra', 'Addison', 'Hui Min', 'Aaron', 'Rubin', 'Raunak', 'Stefan', 'Cheryl', 'Cathy', 'Mai', 'Claire ', 'Alex', 'Bill', 'Daniel', 'Jason'],

        'x': ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad']

}

def name():
    a = (random.choice(list(KREWES.keys())))
    return random.choice(KREWES[a])

print(name())
