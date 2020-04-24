class MyTime:
    def __init__(self, hrs=0, mins=0, secs=0):
        totalsecs = hrs * 3600 + mins * 60 + secs
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return "({0}:{1}:{2})".format(self.hours,self.minutes,self.seconds)

    def add_time1(self, t2):
        secs = self.to_seconds() + t2.to_seconds()
        return MyTime(0, 0, secs)

    def increment(self, seconds):           #add seconds to time
        self.seconds += seconds
        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        while self.minutes >= 60:
            self.minutes -= 60
        return "({0}:{1}:{2})".format(self.hours,self.minutes,self.seconds)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        return self.to_seconds() > time2.to_seconds()

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def within(self,t1,t2):
        if self.to_seconds() > t2.to_seconds() and self.to_seconds() < t1.to_seconds():
            return True
        else:
            return False
