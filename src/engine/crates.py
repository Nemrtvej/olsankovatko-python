from typing import Type, List, Union
from datetime import time, date

TypeCourt = Union[Type['Court'], 'Court']
TypeSchedule = Union[Type['Schedule'], 'Schedule']
TypeSlot = Union[Type['Slot'], 'Slot']
TypeDay = Union[Type['Day'], 'Day']

class Court(object):

    def __init__(self, identifier: str, is_empty: bool):
        self._identifier = identifier
        self._is_empty = is_empty

    @property
    def identifier(self) -> str:
        return self._identifier

    @property
    def is_empty(self) -> bool:
        return self._is_empty

    def __repr__(self) -> str:
        return "ID: %s. Is empty: %s" % (self.identifier, self.is_empty)

class Slot:

    def __init__(self, time_from: time):
        self.courts = list() # type: List[TypeCourt]
        self.time_from = time_from

    def add_court(self, court: TypeCourt) -> None:
        self.courts.append(court)

    def get_courts(self) -> List[TypeCourt]:
        return self.courts

    def get_time_from(self) -> time:
        return self.time_from


    def __repr__(self) -> str:
        return "Time From: %s. Courts: %s" % (self.get_time_from(), self.get_courts())


class Day:

    def __init__(self, date: date):
        self._date = date
        self._slots = list() # type: List[TypeSlot]

    def add_slot(self, slot: TypeSlot) -> None:
        self._slots.append(slot)

    def get_slots(self) -> List[TypeSlot]:
        return self._slots

    def get_date(self) -> date:
        return self._date

    def __repr__(self) -> str:
        return "Date: %s. Slots: %s" % (self.get_date(), self.get_slots())

class Schedule:

    def __init__(self):
        self._days = list()

    def add_day(self, day: TypeDay):
        self._days.append(day)

    def get_days(self) -> List[TypeDay]:
        return self._days

    def __repr__(self) -> str:
        return "Days: %s." % (self.get_days())

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

if __name__ == '__main__':
    s = Schedule()
    d1 = Day(date(2018, 1, 1))
    s.add_day(d1)
    s1 = Slot(time(12, 0))
    d1.add_slot(s1)
    c1 = Court('kurt 1', True)
    s1.add_court(c1)