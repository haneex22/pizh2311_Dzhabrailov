from random import randint


class Person:
    
    id = 0
    
    def __init__(self, number_of_team: int):
        self.id = Person.id
        Person.id += 1
        self.number_of_team = number_of_team
        
        
class Hero(Person):
    
    def __init__(self, number_of_team: int):
        Person.__init__(self, number_of_team)
        self.level = 0

    def level_up(self):
        self.level += 1
        

class Solider(Person):
    
    def __init__(self, number_of_team: int):
        Person.__init__(self, number_of_team)
        self.hero_followed = -1
        
    def follow_hero(self, hero: Hero):
        self.hero_followed = hero.level
        
        
hero_1 = Hero(1)
hero_2 = Hero(2)
soldiers_1 = []
soldiers_2 = []
for i in range(10):
    n = randint(1, 2)
    if n == 1:
        soldiers_1.append(Solider(1))
    else:
        soldiers_2.append(Solider(2))
print(f'Количество солдат в войске первого героя: {len(soldiers_1)}. Второго: {len(soldiers_2)}.')
if len(soldiers_1) > len(soldiers_2):
    hero_1.level_up()
else:
    hero_2.level_up()
soldiers_1[0].follow_hero(hero_1)
print(soldiers_1[0].id, hero_1.id)