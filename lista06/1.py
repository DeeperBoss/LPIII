class Time:

  def __init__(self, h=0, m=0, s=0):
    self.h = h
    self.m = m
    self.s = s

  def addTime(self, *args):
    if len(args) == 1:
      if isinstance(args[0], Time):
        self.s += args[0].s
        self.m += args[0].m
        self.h += args[0].h
      else:
        self.s += args[0]
    elif len(args) == 2:
      self.m += args[0]
      self.s += args[1]
    elif len(args) == 3:
      self.h += args[0]
      self.m += args[1]
      self.s += args[2]

    self.m += self.s // 60
    self.s %= 60
    self.h += self.m // 60
    self.m %= 60

  def __str__(self):
    return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"
