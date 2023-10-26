class Time:

  def __init__(self, hour, minute, second):
    self.hour = hour
    self.minute = minute
    self.second = second

  def isAm(self):
    return self.hour < 12

  def cron(self, outraHora):
    if outraHora.hour < self.hour or (outraHora.hour == self.hour
                                      and outraHora.minute < self.minute) or (
                                        outraHora.hour == self.hour
                                        and outraHora.minute == self.minute
                                        and outraHora.second < self.second):
      return (outraHora.hour + 24 - self.hour) * 3600 + (
        outraHora.minute - self.minute) * 60 + (outraHora.second - self.second)
    else:
      return (outraHora.hour - self.hour) * 3600 + (
        outraHora.minute - self.minute) * 60 + (outraHora.second - self.second)

  def addSeconds(self, secs):
    self.second += secs
    if self.second >= 60:
      self.minute += self.second // 60
      self.second %= 60
    if self.minute >= 60:
      self.hour += self.minute // 60
      self.minute %= 60
    if self.hour >= 24:
      self.hour %= 24
