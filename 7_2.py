'''Вместо метода show использовать магический метод __str__ у трека для вывода информации по треку.
Пример использования

print(track1)
Bohemian rhapsody-6min
print(track1)
Bohemian rhapsody-6min
У Класса Альбом также реализовать магический метод __str__ для вывода информации по альбому и его треков.
Пример использования

print(my_album)
Name group: Queen
Name album: Bohemian rhapsody
Tracks:
    Bohemian rhapsody-6min
    The show must go on-4min
print(my_album)
Name group: Queen
Name album: Bohemian rhapsody
Tracks:
	Bohemian rhapsody-6min
	The show must go on-4min
Задание 2:
Реализовать возможность сравнивать треки по длительности. Для этого нужно будет определить магические методы.
Пример

track1 = Track('Bohemian rhapsody', 6)
track2 = Track('The show must go on', 4)
track1 > track2
True'''

class Track():
  def __init__(self, name, duration = int):
    self.name = name
    self.duration = duration
  
  def __str__(self):
    return f'{self.name} - {self.duration} min'

  def __lt__(self, another):
    return print(self.duration < another.duration)
  
  def __gt__(self, another):
    return print(self.duration > another.duration)

  def __eq__(self, another):
    return print(self.duration == another.duration)
  
  def __le__(self, another):
    return print(self.duration <= another.duration)

  def __ge__(self, another):
    return print(self.duration >= another.duration)

  #def show(self):
   # print(f'{self.name} - {self.duration}')

class Album():
  def __init__(self, name, group):
    self.name = name
    self.group = group
    self.contain = []

  def __str__(self):
    tracklist = ''
    for tracks in self.contain:
      tracklist += (str(tracks) + '\n')
    return f'{self.name}, {self.group}: \n{tracklist}'

# def get_tracks(self):
#  print(f'{self.group}, {self.name}: ')
#    for track in self.contain:
#      track.show()
  

  def add_track(self, name, duration):
    self.contain.append(Track(name, duration))
    
  
  def get_duration(self):
    duration = 0
    for track in self.contain:
      duration += track.duration
    print(f'продолжительность альбома {self.name} группы {self.group} {duration} мин')
  
track_1 = Track('Main', 5)  

alb_1 = Album('hot', 'BEP')
alb_2 = Album('cold', 'BEP')

alb_1.add_track('hi', 3)
alb_1.add_track('bye', 3)
alb_1.add_track('hello', 4)

alb_2.add_track('love', 8)
alb_2.add_track('hate', 8)
alb_2.add_track('apathy', 6)

#alb_1.get_tracks()

#alb_2.get_tracks()

#alb_1.get_duration()

#alb_2.get_duration()

print(track_1)

print(alb_1)
print(alb_2)

track1 = Track('Bohemian rhapsody', 6)
track2 = Track('The show must go on', 4)
track1 > track2

