from typing import Type, List, Union
from datetime import time, date

TypeCourt = Union[Type['Court'], 'Court']
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

    def __init__(self, day: date):
        self.day = day
        self.slots = list() # type: List[TypeSlot]

    def add_slot(self, slot: TypeSlot) -> None:
        self.slots.append(slot)

    def get_slots(self) -> List[TypeSlot]:
        return self.slots

    def get_day(self) -> date:
        return self.day

    def __repr__(self) -> str:
        return "Day: %s. Slots: %s" % (self.get_day(), self.get_slots())

class Schedule:

    def __init__(self):
        self.days = list()

    def add_day(self, day: TypeDay):
        self.days.append(day)

    def get_days(self) -> List[TypeDay]:
        return self.days

    def __repr__(self) -> str:
        return "Days: %s." % (self.get_days())


if __name__ == '__main__':
    s = Schedule()
    d1 = Day(date(2018, 1, 1))
    s.add_day(d1)
    s1 = Slot(time(12, 0))
    d1.add_slot(s1)
    c1 = Court('kurt 1', True)
    s1.add_court(c1)