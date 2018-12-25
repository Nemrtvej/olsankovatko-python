from typing import Type
from .exceptions import InputException
from .crates import Schedule, Day
from bs4 import BeautifulSoup, Tag
from datetime import date, datetime
from typing import List, Dict

TimeMatrix = Dict[str, Dict[int, bool]]

class Parser:

    def parse_schedule(self, html_page: str) -> Schedule:
        schedule = Schedule()
        soup = BeautifulSoup(html_page, 'html.parser')

        tables = soup.find_all('table', { "class": "schedule"})

        if len(tables) != 1:
            raise InputException("Zero or more than one tables with class schedule found. Aborting")

        schedule_table = tables[0]

        date_string = self.extract_date_string(schedule_table)
        day = Day(self.parse_day_date(date_string))
        schedule.add_day(day)

        for row in schedule_table.find_all('tr'):
            print(row)

        return schedule

    def generate_matrix(self, first_slot_time: int, last_slot_time: int, slot_length: int, court_ids: List[str]) -> TimeMatrix:
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
        :return: TimeMatrix
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
