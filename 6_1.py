
class Animals():
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  
  def feed(self):
    print('Спасибо вкусно')


  

class Artiodactyls(Animals):
  def get_milk(self):
    print('Подоено')

class Cow(Artiodactyls):
  def voice(self):
    print('muu')

class Goat(Artiodactyls):
  def voice(self):
      print('mee')
  


class Birds(Animals):
  def collect_eggs(self):
    print('Собрано')

class Duck(Birds):
  def voice(self):
    print('Cra')

class Chicken(Birds):
  def voice(self):
    print('koko')

class Goose(Birds):
  def voice(self):
    print('gaga')

class Sheeps(Animals):
  def voice(self):
    print('bee')
  
  def cut(self):
    print('Подстрижено')


cow = Cow('Манька', 90)
goose_1 = Goose('Белый', 10)
goose_2 = Goose('Серый', 11)
sheep_1 = Sheeps('Кудрявый', 50)
sheep_2 = Sheeps('Барашек', 55)
chicken_1 = Chicken('Коко', 4)
chicken_2 = Chicken('Кукареку', 4)
goat_1 = Goat('Рога', 37)
goat_2 = Goat('Копыта', 29)
duck = Duck('Кряква',6)

zoo = [cow, goose_1, goose_2, sheep_1, sheep_2, chicken_1, chicken_2, goat_1, goat_2, duck]

all_w = 0

fat = 0

for anim in zoo:
  all_w += anim.weight

print(f'Общий вес животных = {all_w} кг' )

for anim in zoo:
  if anim.weight > fat:
    fat = anim.weight

print(f'Самое большое животное весит {fat} кг')
