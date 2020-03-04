class Time:

    time_after_one_second = ""

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    
    def get_time(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"


    def next_second(self):
        if self.seconds >= 59:
            self.seconds = 0
            self.minutes += 1
        if self.minutes >= 59:
            self.minutes = 0
            self.hours += 1
        if self.hours >= 25:
            self.hours = 1
        
        return self.get_time()


time = Time(9, 30, 60)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(24, 59, 59)
print(time.next_second())
