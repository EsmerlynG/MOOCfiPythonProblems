# Write your solution here
from datetime import datetime, timedelta
from csv import reader

def final_points() -> dict:
    start_time = {}
    students_points = {}
    NUM_TASKS = 8

    with open("start_times.csv", "r") as stfile, open("submissions.csv", "r") as sub_file:
        for name, time in reader(stfile, delimiter=";"):
            start_time[name] = datetime.strptime(time, "%H:%M")
            students_points[name] = [0] * NUM_TASKS
        
        for name, task, points, time in reader(sub_file, delimiter=";"):
            if name not in start_time:
                continue

            if datetime.strptime(time, "%H:%M") - start_time[name] > timedelta(hours=3):
                continue

            index = int(task) - 1
            points_list = students_points[name]

            if int(points) > points_list[index]:
                points_list[index] = int(points)
    
    return {name: sum(points) for name, points in students_points.items()}
    



if __name__ == "__main__":
    print(final_points())
    """
    1. Import datetime, timedelta from datetime module
    2. Import reader form csv module
    3. define if __name__ == "__main__":
    4. define final_points() function with retun type hint for dict
    5. Create all necessary data structures, start_time{} dict, 
       student_points{} dict, all kwys will be list[int].
   
    6. Open start_times.csv file in 'r' as stfile, and submission.csv
       file in 'r' as sub_file.

    7. Parse through stfile using reader and deliminating with ';', use strptime() to retrive the
       start_time as a datetime obj.

       8. Add name and datetime obj to start_time dict  
       9. Add name and list[int] with eight zeros to student_points{}

    10. Use for loop to parse through reader(sub_file), use these variable names
       (name, task, points time).
       11. check if end time minus start time is not less than 3 hours if so end this iteration as it is
           invalid and contnue.

       12. get task number and subtract it by one to get index location where all points with that task number will go

       13. add an if statement checking if the number in the specified index is greater than the number just retrived,
           if so, replace the number in the desired index else contiue.

    14. return students_points dict

    """