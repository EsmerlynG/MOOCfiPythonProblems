# Write your solution here
from datetime import datetime, timedelta

def add_screen_time(filename: str, starting_date: datetime, time_entries: int) -> str:
    one_day = timedelta(days=1)

    incrementing_date = starting_date
    startDate = starting_date
    endDate = starting_date + timedelta(days=time_entries - 1)

    log_records = {}
    for _ in range(time_entries):
        time = input(f"Screen time {incrementing_date.strftime('%d.%m.%Y')}: ")
        log_records[incrementing_date.strftime('%d.%m.%Y')] = list(map(int, time.strip().split()))
        incrementing_date += one_day

    total_min = sum(sum(log) for _, log in log_records.items())
    avg_min = total_min / time_entries
    try:
        with open(filename, "w") as time_log:
            time_log.write(f"Time period: {startDate.strftime('%d.%m.%Y')}-{endDate.strftime('%d.%m.%Y')}\n")
            time_log.write(f"Total minutes: {total_min}\n")
            time_log.write(f"Average minutes: {avg_min}\n")
            
            for dates, logs in log_records.items():
                loged_time = '/'.join(map(str, logs))
                time_log.write(f"{dates}: {loged_time}\n")

    except PermissionError:
        return f"You do not have permission to write file - {filename}"
    except Exception as e:
        return f"An unexpected error has occured when interacting with file - {filename}: {e}"
    
    return f"Data stored in file {filename}"
        

def main():
    
    filename = input("Filename: ").strip()
    try:
        starting_date = datetime.strptime(input("Starting date: "), "%d.%m.%Y")
    except ValueError:
        print("Invalid date format, please use dd.mm.yyyy")
        exit(1)

    try:
        time_entries = int(input("How many days: "))
    except ValueError:
        print("Invalid input, please enter an integer")
        exit(1)
    
    print("Please type in screen time in minutes on each day (TV computer mobile):")
    print(add_screen_time(filename, starting_date, time_entries))
    

main()


    
    