from typing import Type, List
from datetime import time, date

class Court:

    def __init__(self, identifier: str, is_empty: bool):
        self.identifier = identifier
        self.is_empty = is_empty

    @property
    def identifier(self) -> str:
        return self.identifier

    @property
    def is_empty(self) -> bool:
        return self.is_empty

    @identifier.setter
    def identifier(self, value):
        self._identifier = value

    @is_empty.setter
    def is_empty(self, value):
        self._is_empty = value

    def __repr__(self) -> str:
        return "ID: %s. Is empty: %s" % (self.identifier, self.is_empty)

class Slot:

    def __init__(self, time_from: time):
        self.courts = list()
        self.time_from = time_from

    def add_court(self, court: Type[Court]) -> None:
        self.courts.append(court)

    def get_courts(self) -> List[Court]:
        return self.courts

    def get_time_from(self) -> time:
        return self.time_from


    def __repr__(self) -> str:
        return "Time From: %s. Courts: %s" % (self.get_time_from(), self.get_courts())


class Day:

    def __init__(self, day: date):
        self.day = day
        self.slots = list()

    def add_slot(self, slot: Type[Slot]) -> None:
        self.slots.append(slot)

    def get_slots(self) -> List[Slot]:
        return self.slots

    def get_day(self) -> date:
        return self.day

    def __repr__(self) -> str:
        return "Day: %s. Slots: %s" % (self.get_day(), self.get_slots())

class Schedule:

    def __init__(self):
        self.days = list()

    def add_day(self, day: Type[Day]):
        self.days.append(day)

    def get_days(self) -> List[Day]:
        return self.days

    def __repr__(self) -> str:
        return "Days: %s." % (self.get_days())
