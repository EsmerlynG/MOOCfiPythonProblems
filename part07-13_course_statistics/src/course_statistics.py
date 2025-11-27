# Write your solution here
import urllib.request
import json

def retrieve_all():
    courses = []
    my_req = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = json.load(my_req)
    
    for course_info in data:
        if course_info["enabled"]:
            courses.append((course_info['fullName'], course_info['name'], course_info['year'], sum(course_info['exercises'])))
    
    return courses

def retrieve_course(course: str) -> dict:
    logs = {"students_logged": [], "hours_logged": [], "exercises_logged": []}

    my_req = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course}/stats")
    data = json.load(my_req)
    
    for _, stats in data.items():
        logs["students_logged"].append(stats["students"])
        logs["hours_logged"].append(stats["hour_total"])
        logs["exercises_logged"].append(stats["exercise_total"])

    weeks_num = len(data)
    max_students = max(logs["students_logged"])
    hours_sum = sum(logs["hours_logged"])
    hours_avg = hours_sum//max_students
    sum_exercises = sum(logs["exercises_logged"])
    exercises_avg = sum_exercises // max_students

    pretty_print = {
        "weeks": weeks_num,
        "students": max_students,
        "hours": hours_sum,
        "hours_average": hours_avg,
        "exercises": sum_exercises,
        "exercises_average": exercises_avg
    }
        
    return pretty_print
    

if __name__ == "__main__":
    print(retrieve_all())
    print(retrieve_course("docker2019"))




