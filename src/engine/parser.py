from typing import Type
from .exceptions import InputException
from .crates import Schedule, Day, TypeSlot, Slot, Court
from bs4 import BeautifulSoup, Tag
from datetime import date, datetime, time
from typing import List, Dict
import re
import json

TypeTimeMatrix = Dict[str, Dict[int, bool]]

class Parser:


    def parse_schedule(self, html_page: str) -> Schedule:

        courts = ['kurt 1', 'kurt 2', 'kurt 3', 'kurt 4']
        first_slot_time = 360
        last_slot_time = 1260
        slot_length = 60
        matrix = self.generate_matrix(first_slot_time=first_slot_time, last_slot_time=last_slot_time, slot_length=slot_length, court_ids=courts)

        schedule = Schedule()
        soup = BeautifulSoup(html_page, 'html.parser')

        schedule_data = self.get_schedule_data(html_page)
        processed_schedule_data = json.loads(schedule_data)
        processed_events = list(map(lambda event: {
            "event_id": event.get("htmlId"),
            "start": event.get('start'),
            "end": event.get('end')
        }, processed_schedule_data.get('events')))

        for processed_event in processed_events:
            for expanded_entry in self.expand_entries(processed_event.get('start'), processed_event.get('end'), processed_event.get('event_id')):
                court_id = courts[expanded_entry.get('court')]
                slot_id = first_slot_time + (slot_length * expanded_entry.get('time'))
                event_id = expanded_entry.get('event_id')
                matrix.get(court_id).update({slot_id: True})

        tables = soup.find_all('table', { "class": "schedule"})

        if len(tables) != 1:
            raise InputException("Zero or more than one tables with class schedule found. Aborting")

        schedule_table = tables[0]

        date_string = self.extract_date_string(schedule_table)
        day = Day(self.parse_day_date(date_string))
        schedule.add_day(day)

        for slot in self.generate_slots_from_matrix(matrix):
            day.add_slot(slot)

        return schedule

    @staticmethod
    def generate_matrix(first_slot_time: int, last_slot_time: int, slot_length: int, court_ids: List[str]) -> TypeTimeMatrix:
        """
        Return matrix representing states of slots in various times.
        First index is ID of court
        Second index is time of slot in number of minutes from the midnight.

        E.g. generating matrix for 60 minutes slots from 06:00 to 21:00, following input params shall be given:
            first_slot_time = 360
            last_slot_time = 1260
            slot_lenght = 60
            ['court 1', 'court 2', 'court 3']

        Response shall contain following data:
          {
            'court 1': {
                360: False, # State of court 1 at 6 o'clock
                420: False, # State of court 1 at 7 o'clock
                460: False, # State of court 1 at 8 o'clock
                ...
            },
            'court 2': {
                360: False, # State of court 2 at 6 o'clock
                420: False, # State of court 2 at 7 o'clock
                460: False, # State of court 2 at 8 o'clock
                ...
            },
          }

        :param first_slot_time: Time in minutes in which the first slot starts.
        :param last_slot_time:  Time in minutes in which the last slot ends.
        :param slot_length: Time in minutes how long does the slot takes.
        :param court_ids:
        :return: TypeTimeMatrix
        """
        duration = last_slot_time - first_slot_time
        number_of_slots = int(duration / slot_length) + 1

        result = dict()

        for court_id in court_ids:
            result[court_id] = dict()
            for i in range(0, number_of_slots):
                index = first_slot_time + (i * slot_length)
                result[court_id][index] = False

        return result



    @staticmethod
    def extract_date_string(table_tag: Type[Tag]) -> str:
        date_string = table_tag.caption.string
        parts = date_string.split(' ')

        return parts[1]

    @staticmethod
    def parse_day_date(date_string: str, reference_date: date = None) -> date:
        if reference_date is None:
            reference_date = datetime.now().date()

        (entry_day, entry_month) = date_string.split('/')
        current_year = reference_date.year

        probable_date = date(current_year, int(entry_month), int(entry_day))

        if probable_date < reference_date:
            probable_date = date(current_year + 1, int(entry_month), int(entry_day))

        return probable_date

    @staticmethod
    def get_schedule_data(html_page: str) -> str:
        pattern = re.compile('^var scheduleData = (.*);$')
        for line in html_page.split("\n"):
            result = pattern.match(line.strip())
            if result is not None:
                return result.group(1)

    def expand_entries(self, start: List[int], end: List[int], event_id: str):
        result = list()

        start_time = start[0]
        start_court = start[1]
        end_time = end[0]
        end_court = end[1]

        for time in range(start_time, end_time + 1):
            for court in range(start_court, end_court + 1):
                result.append({
                    'court': court,
                    'time': time,
                    'event_id': event_id,
                })

        return result

    def generate_slots_from_matrix(self, matrix: TypeTimeMatrix) -> List[TypeSlot]:
        slots_by_time = {} # type: Dict[int, TypeSlot]

        for court_name in matrix:
            for slot_start in matrix.get(court_name):
                is_occupied = matrix.get(court_name).get(slot_start)
                court = Court(court_name, not is_occupied)
                if slots_by_time.get(slot_start) is None:
                    new_slot = Slot(time(int(slot_start / 60), slot_start % 60))
                    slots_by_time.update({slot_start: new_slot})
                slots_by_time.get(slot_start).add_court(court)

        return list(slots_by_time.values())