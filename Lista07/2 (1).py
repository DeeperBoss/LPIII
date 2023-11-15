    from datetime import datetime, timedelta

    class Time:
        def __init__(self, hour, minute, second):
            self.hour = hour
            self.minute = minute
            self.second = second

        @staticmethod
        def diffTime(t1, t2):
            time1 = timedelta(hours=t1.hour, minutes=t1.minute, seconds=t1.second)
            time2 = timedelta(hours=t2.hour, minutes=t2.minute, seconds=t2.second)
            return abs(time1 - time2)

        @staticmethod
        def diffTimeCurrent(t):
            current_time = datetime.now()
            time = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
            current_time_delta = timedelta(hours=current_time.hour, minutes=current_time.minute, seconds=current_time.second)
            return abs(current_time_delta - time)

        @staticmethod
        def isAm(t):
            return t.hour < 12

        @staticmethod
        def isPm(t):
            return t.hour >= 12