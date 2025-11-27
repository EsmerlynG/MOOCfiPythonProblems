# Write your solution here
from datetime import timedelta, datetime
from csv import reader

def cheaters() -> list:
    # Create start time dictionary to store name and start_times
    start_times = {}
    
    # And create the set where all cheaters will be stored
    cheaters = set()

    # Open both csv files and store start_times.csv statistics and submission statistics
    with open('start_times.csv', 'r') as stime_file, open('submissions.csv', 'r') as sub_file:
        
        for student, time in reader(stime_file, delimiter=";"):
            start_times[student] = datetime.strptime(time,  "%H:%M")
        
        for student in reader(sub_file, delimiter=";"):
            name = student[0]
            start_time = start_times[name]
            end_time = datetime.strptime(student[-1], "%H:%M")
            
            if end_time - start_time > timedelta(hours=3):
                cheaters.add(name)
    
    return list(cheaters)


if __name__ == "__main__":
    print(cheaters())