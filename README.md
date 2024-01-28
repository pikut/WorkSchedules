# Contents:
* [Features](#features)
* [Installation](#installation)
* [How it looks?](#how-it-looks)
* [Upcoming features](#upcoming-features)
___
## Features
* For the selected month, display details (in the application window or cmd) such as:
  * Number of working days, weekends and holidays.
  * Which days are working days, weekends and holidays.
  * Number of hours to work.
* Create and save the selected month as a calendar in a *json file.
* Create and save the selected month as a calendar in a *xlsx file.
___
## Installation
Prepare the virtual environment and then install the necessary packages:
```bash
pip install -r requirements.txt
```
Use the command below to build the EXE package:
```bash
pyinstaller main.spec
```
___
## How it looks?
![](https://github.com/pikut/WorkSchedules/blob/main/documentation/how-it-looks.png)
___
## Upcoming features
* Possibility of adding the number of employees working in a selected month in 12-hour work mode.
* Creating a work schedule for the entire month, taking into account vacation request.
