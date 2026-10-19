class Animal():
    def __init__(self, name_animal, ves_kg, type_pitania, color, dikii_or_domash):
        self.name_animal = name_animal
        self.ves = ves_kg
        self.type_pitania = type_pitania
        self.color = color
        self.dikii_or_domash = dikii_or_domash.lower()

    def kol(self):
        
        if self.ves > 100:
            return (f'Имя животного: {self.name_animal}\nВес больше 100')
        elif self.ves < 100:
            return ('Кроха')
    def whois(self):
        if self.dikii_or_domash == 'домашний':
            return (f'Имя животного: {self.name_animal}\nне ест людей')
        elif self.dikii_or_domash == 'дикий':
            return (f'Имя животного: {self.name_animal}\nест людей')
    def __str__(self):
        return (f'Имя животного: {self.name_animal}\nРост: {self.ves}\n\
Тип питания: {self.type_pitania},\nЦвет: {self.color}\nДомашний или дикий: {self.dikii_or_domash}')


animal = Animal(name_animal='lion', ves_kg=50, type_pitania="getero", color='yellow', dikii_or_domash='Дикий')
print(animal)
print()
print(animal.kol())
print(animal.whois())

class Presmyk(Animal):
    def __init__(self, name_animal, ves_kg, type_pitania, color, dikii_or_domash, otryd):
        super().__init__(name_animal, ves_kg, type_pitania, color, dikii_or_domash)
        self.otryd = otryd.lower()
    def presmyk_or_not(self):
        if self.otryd in ['Чешуйчатые', "Черепахи", "Крокодилы", "Клювоголовые", "Первоящеры " ]:
            return (f"Имя животного: {self.name_animal}\nпресмыкающее")
        else:
            return (f"Имя животного: {self.name_animal}\nне Пресмыкающее")



    def __str__(self):
        return self.presmyk_or_not()

animal_presmyk = Presmyk(name_animal='lion', ves_kg=50, type_pitania="getero", color='yellow', \
                dikii_or_domash='Дикий', otryd = "" )

print(animal)
print()


class Zemnovod(Animal):
    def __init__(self, name_animal, ves_kg, type_pitania, color, dikii_or_domash, pokrov):
        super().__init__(name_animal, ves_kg, type_pitania, color, dikii_or_domash)
        self.pokrov = pokrov.lower()
    def presmyk_or_not(self):
        if self.pokrov in ['Животные с тонкой', "голой кожей с большим количеством желез"]:
            return (f"Имя животного: {self.name_animal}\земноводное")
        else:
            return (f"Имя животного: {self.name_animal}\nне земноводное")



    def __str__(self):
        return self.presmyk_or_not()

animal_zemnovod = Zemnovod(name_animal='lion', ves_kg=50, type_pitania="getero", color='yellow', \
                dikii_or_domash='Дикий', pokrov = "" )
print(animal)
print()

# _____доп_____

class ZooShow(Presmyk, Zemnovod):
    
    print ('Шоу: \nПресмыкающие - 100 с\nЗемноводные - 150 с')
    input_show = str(input())

    if input_show == 'Пресмыкающие':
        print(animal_presmyk)
    else:
        print(animal_zemnovod)


print(ZooShow)