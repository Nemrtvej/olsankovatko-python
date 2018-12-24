from .crates import Schedule
from bs4 import BeautifulSoup

class Parser():

    def parse_schedule(self, html_page: str) -> Schedule:
        schedule = Schedule()
        soup = BeautifulSoup(html_page, 'html.parser')


        print(soup.prettify())
        return schedule