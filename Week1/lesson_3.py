class Person:
    
    def __init__(self, name: str, surname: str, qualification: int = 1):
        self.name = name
        self.surname = surname
        self.qualification = qualification
        
    def information(self):
        print(f'Имя Фамилия: {self.name} {self.surname}. Квалификация: {self.qualification}')
        
    def __del__(self):
        print(f'До свидания, мистер {self.name} {self.surname}.')
    
Jon = Person('Jon', 'Jones', 3)
Daniel = Person('Daniel', 'Cormier', 2)
Stipe = Person('Stipe', 'Miocic')
Jon.information()
Daniel.information()
Stipe.information()
del Stipe
close = input()