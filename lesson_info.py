#!/usr/bin/env python3
import json
from datetime import datetime
import colorful

lessonsfile_path = "/home/joco/.school/lessons.json"
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def upcoming_lesson(lesson):
    print(colorful.bold("- ") + lesson["name"] + ", " + lesson["room"] + ", " + str(lesson["starttimehour"]) + ":" + str(lesson["starttimeminute"]) + "-" + str(lesson["endtimehour"]) + ":" + str(lesson["endtimeminute"]))


def current_lesson(lesson):
    print("---")
    print(colorful.bold_green("Weekday: ") + days[weekday])
    print(colorful.bold_green("Current time: ") + str(now.strftime("%H:%M")))
    print("---")
    print(colorful.bold_green("Lesson: ") + lesson["name"])
    print(colorful.bold_green("Teacher: ") + lesson["teacher"])
    print(colorful.bold_green("Room: ") + lesson["room"])
    print(colorful.bold_green("Starttime: ") + str(lesson["starttimehour"]) + ":" + str(lesson["starttimeminute"]))
    print(colorful.bold_green("Endtime: ") + str(lesson["endtimehour"]) + ":" + str(lesson["endtimeminute"]))
    print(colorful.bold_green("Time till break: ") + str(endtime - now))
    print("---")


with open(lessonsfile_path) as json_file:
    weekday = datetime.today().weekday()
    data = json.load(json_file)
    now = datetime.now()
    day_running = False
    for lesson in data[weekday]:
        starttime = now.replace(hour=lesson["starttimehour"], minute=lesson["starttimeminute"], second=0, microsecond=0)
        endtime = now.replace(hour=lesson["endtimehour"], minute=lesson["endtimeminute"], second=0, microsecond=0)
        if starttime > now < endtime:
            upcoming_lesson(lesson)
        elif starttime < now < endtime:
            current_lesson(lesson)
            day_running = True
        elif day_running:
            if weekday == 4 or weekday == 5:
                print(colorful.green("WEEKEND!!!"))
            else:
                print(colorful.red("Tomorrows Lessons:"))
                if weekday == 7:
                    weekday = 0
                for tomorrow_lesson in data[weekday + 1]:
                    upcoming_lesson(tomorrow_lesson)
            break
