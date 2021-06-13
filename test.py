"""
A factory needs an iterable object to keep track of employee working hours for each day.
Each employee has a string name and a tuple containing start work and end work time (use format you like).
Iterating the object will return tuple with name and hours worked that day for each employee
1) 40p: Definition
    a) 10p: Class with constructor that receives the date in the format you desire (representing the day)
    b) 10p: Create method to add worker start time
         - if start time has already been added a custom exception inheriting ValueError (exception: WorkStartError)
         exception will be raised with message indicating employee name and existing start time
    c) 10p: Create method to add worker end time
         - if end time has already been added a custom exception inheriting ValueError (exception: WorkEndError)
         exception will be raised with message indicating employee name and existing end time
    c) 10p: Iterating the object will return tuple with name and time worked that day for each employee
2) 40p: Execution:
    a) 10p: Create instance of class with date format you selected.
    b) 10p: Add start of work for the following employees:
        - Joe: 09:01:20 - start time
        - Ana: 09:03:15 - start time
        - Tim: 09:04:25 - start time
        - Tim: 09:04:30 - start time - treat this exception
    c) 10p: Add end of work for the following employees:
        - Joe: 16:01:20 - end time
        - Ana: 18:04:15 - end time
        - Tim: 18:05:25 - end time
        - Tim: 18:05:30 - end time - treat this exception
    d) 10p: Iterate the created object and save each value on a new line in a file
3) 20p: Documenting:
   a) 5p: type hints for all arguments (optional for returned values)
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""

from datetime import datetime


class WorkStartError(ValueError):
    pass


class WorkEndError(ValueError):
    pass


class TimeIter:
    """Iterator for working hours by name"""

    def __init__(self, working_time: list):
        self.working_time = working_time

    def __iter__(self):
        return self

    def __next__(self):
        if not self.working_time:
            raise StopIteration
        else:
            return self.working_time.pop(0)


class TimeKeeper:
    """keeps track or working hours"""
    ledger = {}

    def __init__(self, date: list):
        self.date = date

    def __iter__(self):
        result = []
        for name, start_end in self.ledger.items():
            result.append((name, start_end[1] - start_end[0]))
        return TimeIter(result)

    def start_work(self, name: str, start_time: list):
        """add start time"""
        if self.ledger.get(name, None):
            raise WorkStartError(f'{name} already started work')
        self.ledger[name] = [datetime(*self.date, *start_time)]

    def end_work(self, name: str, end_time: list):
        """add end time"""
        try:
            self.ledger[name][1]
        except IndexError:
            self.ledger[name].append(datetime(*self.date, *end_time))
        else:
            raise WorkEndError(f'{name} already started work')


timer = TimeKeeper([2021, 3, 4])

# start time
timer.start_work('Joe', [9, 1, 20])
timer.start_work('Ana', [9, 3, 15])
timer.start_work('Tim', [9, 4, 25])
try:
    timer.start_work('Tim', [9, 4, 30])
except WorkStartError:
    print('got passed WorkStartError')

# end time
timer.end_work('Joe', [16, 1, 20])
timer.end_work('Ana', [18, 4, 15])
timer.end_work('Tim', [18, 5, 25])
try:
    timer.end_work('Tim', [18, 5, 30])
except WorkEndError:
    print('got passed WorkEndError')

with open('timer.log', 'w') as file:
    for data in timer:
        file.write(f'{data[0]}: {data[1]}\n')
