from typing import Type
from .exceptions import InputException
from .crates import Schedule, Day
from bs4 import BeautifulSoup, Tag
from datetime import date, datetime

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
