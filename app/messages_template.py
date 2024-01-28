from string import Template


def message_in_cmd_template(
    number_of_days_in_month: int,
    list_of_work_days: list,
    list_of_holidays: list,
    list_of_weekends: list,
) -> str:

    template = Template(
        f"""{"_"* 100}
Według podanego harmonogramu pracy, w tym miesiącu wychodzi: {len(list_of_work_days) * 8} roboczogodzin.
        
W tym miesiącu dni pracujące to: {list_of_work_days}
W tym miesiącu weekendy to: {list_of_weekends}
W tym miesiącu dni świąteczne to: {list_of_holidays}

W tym miesiącu jest {number_of_days_in_month} dni, w tym: {len(list_of_work_days)} dni pracujących, czyli {len(list_of_work_days) * 8} roboczogodzin.
W tym miesiącu jest {number_of_days_in_month} dni, w tym: {len(list_of_holidays)} dni świątecznych.
W tym miesiącu jest {number_of_days_in_month} dni, w tym: {len(list_of_weekends)} dni weekendowych.
{"_"* 100}"""
    )

    return template.substitute(
        number_of_days_in_mont=number_of_days_in_month,
        list_of_work_days=list_of_work_days,
        list_of_holidays=list_of_holidays,
        list_of_weekends=list_of_weekends,
    )


def message_in_window_template(
    number_of_days_in_month: int,
    list_of_work_days: list,
    list_of_holidays: list,
    list_of_weekends: list,
) -> str:
    template = Template(
        f"""Według podanego harmonogramu pracy, w tym miesiącu wychodzi: {len(list_of_work_days) * 8} roboczogodzin.

W tym miesiącu dni pracujące to: {list_of_work_days}
W tym miesiącu weekendy to: {list_of_weekends}
W tym miesiącu dni świąteczne to: {list_of_holidays}

W tym miesiącu jest {number_of_days_in_month} dni, w tym: {len(list_of_work_days)} dni pracujących, czyli {len(list_of_work_days) * 8} roboczogodzin.
W tym miesiącu jest {number_of_days_in_month} dni, w tym: {len(list_of_holidays)} dni świątecznych.
W tym miesiącu jest {number_of_days_in_month} dni, w tym: {len(list_of_weekends)} dni weekendowych."""
    )

    return template.substitute(
        number_of_days_in_mont=number_of_days_in_month,
        list_of_work_days=list_of_work_days,
        list_of_holidays=list_of_holidays,
        list_of_weekends=list_of_weekends,
    )
