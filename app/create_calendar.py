import calendar
from typing import Literal
import holidays
from datetime import date
import xlsxwriter
import json
import sys

from messages_template import message_in_cmd_template, message_in_window_template


class CreateCalendar:
    def __init__(self, year: str, month: str):
        self.dependence_folder_name = (
            "dependence/" if getattr(sys, "frozen", False) else str()
        )
        self.pl_holidays = holidays.PL()
        self.list_of_weekday = ["pn", "wt", "śr", "cz", "pt", "so", "nd"]
        self.file_name = f"{year}_{month}"
        self.get_year = int(year)
        self.get_month = int(month)
        self.get_date = None
        self.is_holiday = None
        self.weekday = None
        self.day_of_weekday = None
        self.month_range = None
        self.number_of_days_in_month = None
        self.list_of_work_days = None
        self.list_of_weekends = None
        self.list_of_holidays = None
        self.my_calendar = None

    def __call__(
        self, print_msg: Literal["cmd", "window", "json", "xlsx"]
    ) -> None | str:
        self.current_month_details()
        self.create_list_of_work_days()
        self.create_list_of_holidays()
        self.create_list_of_weekends()
        self.create_dict_of_my_calendar()
        if print_msg == "cmd":
            self.print_message_in_cmd()
        elif print_msg == "window":
            return self.print_message_in_window()
        elif print_msg == "json":
            self.convert_dict_to_json()
        elif print_msg == "xlsx":
            self.convert_dict_to_xlsx()
        return

    def current_day_details(self, get_day: int) -> tuple[bool, int, date, str]:
        self.get_date = date(self.get_year, self.get_month, get_day)
        self.is_holiday = self.get_date in self.pl_holidays
        self.weekday = calendar.weekday(self.get_year, self.get_month, get_day)
        self.day_of_weekday = self.list_of_weekday[self.weekday]

        return self.is_holiday, self.weekday, self.get_date, self.day_of_weekday

    def current_month_details(self) -> None:
        self.month_range = calendar.monthrange(self.get_year, self.get_month)
        self.number_of_days_in_month = self.month_range[1]

    def create_list_of_work_days(self) -> None:
        self.list_of_work_days = [
            current_day
            for current_day in range(1, self.number_of_days_in_month + 1)
            if self.current_day_details(current_day)[1] < 5
            and not self.current_day_details(current_day)[0]
        ]

    def create_list_of_holidays(self) -> None:
        self.list_of_holidays = [
            current_day
            for current_day in range(1, self.number_of_days_in_month + 1)
            if self.current_day_details(current_day)[0]
        ]

    def create_list_of_weekends(self) -> None:
        self.list_of_weekends = [
            current_day
            for current_day in range(1, self.number_of_days_in_month + 1)
            if self.current_day_details(current_day)[1] >= 5
        ]

    def create_dict_of_my_calendar(self) -> None:
        self.my_calendar = {
            current_day: {
                "data": str(self.current_day_details(current_day)[2]),
                "dzień tygodnia": self.current_day_details(current_day)[3],
                "święto": self.pl_holidays.get(
                    self.current_day_details(current_day)[2]
                ),
            }
            for current_day in range(1, self.number_of_days_in_month + 1)
        }

    def convert_dict_to_json(self) -> None:
        my_calendar_to_json = json.dumps(self.my_calendar, indent=4, ensure_ascii=False)
        with open(
            f"{self.dependence_folder_name}data/{self.file_name}.json",
            "w",
            encoding="utf8",
        ) as file:
            file.write(my_calendar_to_json)
        print("The calendar saved to json file.")

    def convert_dict_to_xlsx(self) -> None:
        workbook = xlsxwriter.Workbook(
            f"{self.dependence_folder_name}data/{self.file_name}.xlsx"
        )
        worksheet = workbook.add_worksheet(f"{self.get_year}")
        len_days_month = self.my_calendar.keys().__len__() + 1
        worksheet.set_column(len_days_month, len_days_month, 5)
        row = 0
        col = 0
        worksheet.set_column(0, 0, 12)
        worksheet.set_column(1, 31, 3)

        cell_format_for_nd = workbook.add_format(
            {
                "border": 1,
                "bg_color": "red",
                "font_color": "white",
                "align": "center",
                "bold": "bold",
            }
        )

        cell_format_for_so = workbook.add_format(
            {"border": 1, "bg_color": "999999", "align": "center", "bold": "bold"}
        )

        cell_format_for_weekday = workbook.add_format(
            {"border": 1, "align": "center", "bold": "bold"}
        )

        cell_format_for_other = workbook.add_format({"border": 1, "align": "center"})

        worksheet.write(
            row, col, f"{self.get_year}/{self.get_month}", cell_format_for_weekday
        )
        worksheet.write(row + 1, col, "Imię i nazwisko", cell_format_for_other)
        worksheet.write(row, col + len_days_month, "Suma", cell_format_for_other)
        for day, day_details in self.my_calendar.items():
            worksheet.write(row, col + 1, day, cell_format_for_weekday)
            workday = day_details["dzień tygodnia"]
            if workday == "nd" or day in self.list_of_holidays:
                worksheet.write(row, col + 1, day, cell_format_for_nd)
                worksheet.write(row + 1, col + 1, workday, cell_format_for_nd)
            elif workday == "so":
                worksheet.write(row, col + 1, day, cell_format_for_so)
                worksheet.write(row + 1, col + 1, workday, cell_format_for_so)
            else:
                worksheet.write(row + 1, col + 1, workday, cell_format_for_weekday)
            col += 1

        workbook.close()
        print("The calendar saved to xlsx file.")

    def print_message_in_cmd(self) -> None:
        msg = message_in_cmd_template(
            number_of_days_in_month=self.number_of_days_in_month,
            list_of_weekends=self.list_of_weekends,
            list_of_holidays=self.list_of_holidays,
            list_of_work_days=self.list_of_work_days,
        )
        print(msg)

    def print_message_in_window(self) -> str:
        msg = message_in_window_template(
            number_of_days_in_month=self.number_of_days_in_month,
            list_of_weekends=self.list_of_weekends,
            list_of_holidays=self.list_of_holidays,
            list_of_work_days=self.list_of_work_days,
        )
        return msg
