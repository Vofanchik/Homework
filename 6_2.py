class Track():
  def __init__(self, name, duration = int):
    self.name = name
    self.duration = duration
  
  def show(self):
    print(f'{self.name} - {self.duration}')

class Album():
  def __init__(self, name, group):
    self.name = name
    self.group = group
    self.contain = []

  def get_tracks(self):
    print(f'{self.group}, {self.name}: ')
    for track in self.contain:
      track.show()
  

  def add_track(self, name, duration):
    self.contain.append(Track(name, duration))
    
  
  def get_duration(self):
    duration = 0
    for track in self.contain:
      duration += track.duration
    print(f'продолжительность альбома {self.name} группы {self.group} {duration} мин')
  

alb_1 = Album('hot', 'BEP')
alb_2 = Album('cold', 'BEP')

alb_1.add_track('hi', 3)
alb_1.add_track('bye', 3)
alb_1.add_track('hello', 4)

alb_2.add_track('love', 8)
alb_2.add_track('hate', 8)
alb_2.add_track('apathy', 6)

alb_1.get_tracks()

alb_2.get_tracks()

alb_1.get_duration()

alb_2.get_duration()

