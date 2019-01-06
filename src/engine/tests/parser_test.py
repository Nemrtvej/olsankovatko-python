import os
from django.test import TestCase

from ..crates import Schedule, Day, Court, Slot, TypeSchedule
from ..parser import Parser
from ..slot_finder import SlotFinder, DesiredSlot, FoundSlot

from datetime import date, time, datetime


class ParserTestCase(TestCase):

    def test_parse_response(self) -> None:
        response_data = "%s/data/response_filled.html" % os.path.dirname(os.path.realpath(__file__))
        with open(response_data, 'r') as data_file:
            data = "\n".join(data_file.readlines())

        parser = Parser()
        actual_schedule = parser.parse_schedule(data)

        expected_schedule = self.provide_schedule()

        self.assertEqual(expected_schedule, actual_schedule)

    def test_date_parsing(self) -> None:

        values = [
            ['2018-12-12', '12/12'],
            ['2018-12-31', '31/12'],
            ['2019-01-12', '12/01'],
            ['2019-09-11', '11/09'],
            ['2019-02-28', '28/02'],
        ]

        reference_date = date(2018, 12, 11)
        parser = Parser()

        for (expected_value, entered_value) in values:
            parsed_date = parser.parse_day_date(entered_value, reference_date=reference_date)
            self.assertEqual(expected_value, f"{parsed_date:%Y-%m-%d}")

    def test_slot_finder(self):
        schedule = self.provide_schedule()
        slot_finder = SlotFinder()

        for (desired_slot, expected_slot) in self.provide_slot_finder():
            actual_slot = slot_finder.find_empty_slot(schedule, desired_slot)
            self.assertEqual(actual_slot, expected_slot)

    def test_generate_matrix(self):
        parser = Parser()
        actual_response = parser.generate_matrix(60, 180, 60, ['a', 'b', 'c'])
        expected_response = {
            'a': {
                60: False,
                120: False,
                180: False,
            },
            'b': {
                60: False,
                120: False,
                180: False,
            },
            'c': {
                60: False,
                120: False,
                180: False,
            },
        }

        self.assertEqual(expected_response, actual_response)

    def provide_slot_finder(self):
        day = date(2019, 1, 15)
        court_priorities = ['kurt 1', 'kurt 4', 'kurt 2', 'kurt 3']

        first_start_time = datetime(day.year, day.month, day.day, 17)
        first_desired_slot = DesiredSlot(court_priorities=court_priorities, start_time=first_start_time)
        first_expected_slot = FoundSlot('kurt 1', first_start_time)

        second_start_time = datetime(day.year, day.month, day.day, 22)
        second_desired_slot = DesiredSlot(court_priorities=court_priorities, start_time=second_start_time)
        second_expected_slot = None

        third_start_time = datetime(day.year, day.month, day.day, 19)
        third_desired_slot = DesiredSlot(court_priorities=court_priorities, start_time=third_start_time)
        third_expected_slot = FoundSlot('kurt 4', third_start_time)

        return [
            [first_desired_slot, first_expected_slot],
            [second_desired_slot, second_expected_slot],
            [third_desired_slot, third_expected_slot],
        ]

    @staticmethod
    def provide_schedule() -> TypeSchedule:
        schedule = Schedule()
        day = Day(date(2019, 1, 15))
        schedule.add_day(day)

        slot_06 = Slot(time_from=time(6))
        slot_07 = Slot(time_from=time(7))
        slot_08 = Slot(time_from=time(8))
        slot_09 = Slot(time_from=time(9))
        slot_10 = Slot(time_from=time(10))
        slot_11 = Slot(time_from=time(11))
        slot_12 = Slot(time_from=time(12))
        slot_13 = Slot(time_from=time(13))
        slot_14 = Slot(time_from=time(14))
        slot_15 = Slot(time_from=time(15))
        slot_16 = Slot(time_from=time(16))
        slot_17 = Slot(time_from=time(17))
        slot_18 = Slot(time_from=time(18))
        slot_19 = Slot(time_from=time(19))
        slot_20 = Slot(time_from=time(20))
        slot_21 = Slot(time_from=time(21))

        court1_id = 'kurt 1'
        court2_id = 'kurt 2'
        court3_id = 'kurt 3'
        court4_id = 'kurt 4'

        slot_06.add_court(Court(court1_id, True))
        slot_06.add_court(Court(court2_id, True))
        slot_06.add_court(Court(court3_id, True))
        slot_06.add_court(Court(court4_id, True))

        slot_07.add_court(Court(court1_id, True))
        slot_07.add_court(Court(court2_id, True))
        slot_07.add_court(Court(court3_id, True))
        slot_07.add_court(Court(court4_id, True))

        slot_08.add_court(Court(court1_id, True))
        slot_08.add_court(Court(court2_id, True))
        slot_08.add_court(Court(court3_id, True))
        slot_08.add_court(Court(court4_id, True))

        slot_09.add_court(Court(court1_id, True))
        slot_09.add_court(Court(court2_id, True))
        slot_09.add_court(Court(court3_id, True))
        slot_09.add_court(Court(court4_id, True))

        slot_10.add_court(Court(court1_id, True))
        slot_10.add_court(Court(court2_id, True))
        slot_10.add_court(Court(court3_id, True))
        slot_10.add_court(Court(court4_id, True))

        slot_11.add_court(Court(court1_id, True))
        slot_11.add_court(Court(court2_id, True))
        slot_11.add_court(Court(court3_id, True))
        slot_11.add_court(Court(court4_id, True))

        slot_12.add_court(Court(court1_id, True))
        slot_12.add_court(Court(court2_id, True))
        slot_12.add_court(Court(court3_id, True))
        slot_12.add_court(Court(court4_id, True))

        slot_13.add_court(Court(court1_id, True))
        slot_13.add_court(Court(court2_id, True))
        slot_13.add_court(Court(court3_id, True))
        slot_13.add_court(Court(court4_id, True))

        slot_14.add_court(Court(court1_id, True))
        slot_14.add_court(Court(court2_id, True))
        slot_14.add_court(Court(court3_id, True))
        slot_14.add_court(Court(court4_id, True))

        slot_15.add_court(Court(court1_id, True))
        slot_15.add_court(Court(court2_id, True))
        slot_15.add_court(Court(court3_id, True))
        slot_15.add_court(Court(court4_id, True))

        slot_16.add_court(Court(court1_id, True))
        slot_16.add_court(Court(court2_id, False))
        slot_16.add_court(Court(court3_id, False))
        slot_16.add_court(Court(court4_id, False))

        slot_17.add_court(Court(court1_id, True))
        slot_17.add_court(Court(court2_id, False))
        slot_17.add_court(Court(court3_id, True))
        slot_17.add_court(Court(court4_id, False))

        slot_18.add_court(Court(court1_id, False))
        slot_18.add_court(Court(court2_id, True))
        slot_18.add_court(Court(court3_id, True))
        slot_18.add_court(Court(court4_id, False))

        slot_19.add_court(Court(court1_id, False))
        slot_19.add_court(Court(court2_id, False))
        slot_19.add_court(Court(court3_id, False))
        slot_19.add_court(Court(court4_id, True))

        slot_20.add_court(Court(court1_id, True))
        slot_20.add_court(Court(court2_id, True))
        slot_20.add_court(Court(court3_id, False))
        slot_20.add_court(Court(court4_id, True))

        slot_21.add_court(Court(court1_id, True))
        slot_21.add_court(Court(court2_id, True))
        slot_21.add_court(Court(court3_id, True))
        slot_21.add_court(Court(court4_id, True))

        day.add_slot(slot_06)
        day.add_slot(slot_07)
        day.add_slot(slot_08)
        day.add_slot(slot_09)
        day.add_slot(slot_10)
        day.add_slot(slot_11)
        day.add_slot(slot_12)
        day.add_slot(slot_13)
        day.add_slot(slot_14)
        day.add_slot(slot_15)
        day.add_slot(slot_16)
        day.add_slot(slot_17)
        day.add_slot(slot_18)
        day.add_slot(slot_19)
        day.add_slot(slot_20)
        day.add_slot(slot_21)

        return schedule
