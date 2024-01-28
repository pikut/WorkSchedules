import customtkinter
from PIL import Image
import sys

from create_calendar import CreateCalendar


class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.dependence_folder_name = (
            "dependence/" if getattr(sys, "frozen", False) else str()
        )

        self.msg_run_from_exe = "The app run from the *exe file."
        self.msg_run_from_interpreter = "The app run from the python interpreter."

        self.title("Create Calendar v0.0.1")
        self.iconbitmap(f"{self.dependence_folder_name}static/common/calendar.ico")

        self.img_calendar_file = Image.open(
            f"{self.dependence_folder_name}static/common/calendar.png"
        )
        self.img_calendar_set = customtkinter.CTkImage(
            self.img_calendar_file, size=(48, 48)
        )
        customtkinter.CTkLabel(master=self, image=self.img_calendar_set, text="").grid(
            row=0, columnspan=2, pady=(20, 5)
        )

        customtkinter.CTkLabel(master=self, text="Year: ", anchor="s").grid(
            row=1, column=0, sticky="w", padx=20
        )
        self.entry_year = customtkinter.CTkEntry(master=self)
        self.entry_year.grid(row=2, column=0, padx=(20, 5))

        customtkinter.CTkLabel(master=self, text="Month: ", anchor="s").grid(
            row=1, column=1, sticky="w", padx=5
        )
        self.entry_month = customtkinter.CTkEntry(master=self)
        self.entry_month.grid(row=2, column=1, padx=(5, 20))

        self.img_cmd_file = Image.open(
            f"{self.dependence_folder_name}static/light/cmd.png"
        )
        self.img_cmd_set = customtkinter.CTkImage(self.img_cmd_file, size=(20, 20))
        customtkinter.CTkButton(
            master=self,
            text="View in CMD",
            command=self.view_details_of_calendar_in_cmd,
            anchor="center",
            image=self.img_cmd_set,
        ).grid(
            row=5,
            columnspan=2,
            sticky="news",
            padx=20,
            pady=(20, 5),
        )

        self.img_window_file = Image.open(
            f"{self.dependence_folder_name}static/light/window.png"
        )
        self.img_window_set = customtkinter.CTkImage(
            self.img_window_file, size=(20, 20)
        )
        customtkinter.CTkButton(
            master=self,
            text="View in wind",
            command=self.view_details_of_calendar_in_window,
            anchor="center",
            image=self.img_window_set,
        ).grid(
            row=6,
            columnspan=2,
            sticky="news",
            padx=20,
            pady=(5, 5),
        )

        self.img_json_file = Image.open(
            f"{self.dependence_folder_name}static/light/json.png"
        )
        self.img_json_set = customtkinter.CTkImage(self.img_json_file, size=(20, 20))
        customtkinter.CTkButton(
            master=self,
            text="Save as json",
            command=self.save_as_json_file,
            image=self.img_json_set,
            anchor="center",
        ).grid(
            row=7,
            columnspan=2,
            sticky="news",
            padx=20,
            pady=(5, 5),
        )

        self.img_xlsx_file = Image.open(
            f"{self.dependence_folder_name}static/light/xlsx.png"
        )
        self.img_xlsx_set = customtkinter.CTkImage(self.img_xlsx_file, size=(20, 20))
        customtkinter.CTkButton(
            master=self,
            text="Save as xlsx",
            command=self.save_as_xlsx_file,
            anchor="center",
            image=self.img_xlsx_set,
        ).grid(
            row=8,
            columnspan=2,
            sticky="news",
            padx=20,
            pady=(5, 20),
        )

        self.calendar_details_window = None

    def prepare_date(self):
        year_value = self.entry_year.get()
        month_value = self.entry_month.get()
        self.entry_year.delete(0, "end")
        self.entry_month.delete(0, "end")
        return month_value, year_value

    def view_details_of_calendar_in_cmd(self):
        month_value, year_value = self.prepare_date()
        new_view = CreateCalendar(year=year_value, month=month_value)
        new_view(print_msg="cmd")

    def view_details_of_calendar_in_window(self):
        month_value, year_value = self.prepare_date()
        new_view = CreateCalendar(year=year_value, month=month_value)
        msg = new_view(print_msg="window")

        if (
            self.calendar_details_window is None
            or not self.calendar_details_window.winfo_exists()
        ):
            self.calendar_details_window = CalendarDetailsWindow(msg=msg)
        else:
            self.calendar_details_window.focus()

    # TODO add CTkMessagebox if save file successful.
    def save_as_json_file(self):
        month_value, year_value = self.prepare_date()
        new_view = CreateCalendar(year=year_value, month=month_value)
        new_view(print_msg="json")

    # TODO add CTkMessagebox if save file successful.
    def save_as_xlsx_file(self):
        month_value, year_value = self.prepare_date()
        new_view = CreateCalendar(year=year_value, month=month_value)
        new_view(print_msg="xlsx")

    def run(self):
        (
            print(self.msg_run_from_exe)
            if getattr(sys, "frozen", False)
            else print(self.msg_run_from_interpreter)
        )
        self.mainloop()


class CalendarDetailsWindow(customtkinter.CTkToplevel):
    def __init__(self, msg: str):
        super().__init__()
        self.dependence_folder_name = (
            "dependence/" if getattr(sys, "frozen", False) else str()
        )
        self.grab_set()
        self.attributes("-topmost", True)
        self.title("Month details")
        # set the icon like this way because customtkinter has a bug
        self.after(
            250,
            lambda: self.iconbitmap(
                f"{self.dependence_folder_name}static/common/calendar.ico"
            ),
        )
        customtkinter.CTkLabel(self, text=msg).pack(padx=20, pady=20)


if __name__ == "__main__":
    app = MainWindow()
    app.run()
