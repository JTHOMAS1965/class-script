import webbrowser
import subprocess
import time
import easygui

chrome_path = r"define the path of chrome.exe on your computer"
r_studio_path =r"define your file path of an application you use for another class"

courses = {
    "ACCTCY_4356" : ["link to class website","link to class textbook"],
    "FINANC_4010" : ["link to class website","link to class textbook"],
    "FINANC_4020" : ["link to class website","link to class textbook"],
    "MANGMT_4010" : ["link to class website","link to class textbook"],
    "STAT_3500" : ["link to class website"]
}

course_choice = easygui.choicebox("Choose a course:", choices=list(courses.keys()))

if course_choice:
    course_urls = courses.get(course_choice)
    if course_urls:
        for url in course_urls:
            webbrowser.open(url)

        # If you want to open up an application alongside a class (like STAT_3500 here)
        if course_choice == "STAT_3500":
            subprocess.Popen([r_studio_path])
