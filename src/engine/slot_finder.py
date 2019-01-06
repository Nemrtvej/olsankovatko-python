from datetime import datetime
from typing import Optional, List

from .crates import Schedule

class DesiredSlot:
    def __init__(self, court_priorities: List[str], start_time: datetime) -> None:
        self._court_priorities = court_priorities
        self._start_time = start_time

    @property
    def court_names(self) -> List[str]:
        return self._court_priorities

    @property
    def start_time(self) -> datetime:
        return self._start_time

class FoundSlot:

    def __init__(self, court_name: str, start_time: datetime) -> None:
        self._court_name = court_name
        self._start_time = start_time

    @property
    def court_name(self) -> str:
        return self._court_name

    @property
    def start_time(self) -> datetime:
        return self._start_time

    def __repr__(self):
        return "%s @ %s" % (self.start_time, self.court_name)

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

class SlotFinder:

    def find_empty_slot(self, schedule: Schedule, desired_slot: DesiredSlot) -> Optional[FoundSlot]:

        date = desired_slot.start_time.date()
        time = desired_slot.start_time.time()

        for day in schedule.get_days():
            if day.get_date() != date:
                continue

            for slot in day.get_slots():
                day.get_slots()

                if slot.get_time_from() != time:
                    continue

                court_availabilities = dict()

                for court in slot.get_courts():
                    court_availabilities[court.identifier] = court.is_empty

                for desired_court in desired_slot.court_names:
                    if court_availabilities[desired_court]:
                        return FoundSlot(desired_court, desired_slot.start_time)

        return None