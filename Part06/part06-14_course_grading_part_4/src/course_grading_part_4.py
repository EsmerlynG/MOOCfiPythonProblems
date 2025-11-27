# write your solution here
def grade(p: int):
    if 0 <= p <= 14:
        return 0
    elif 15 <= p <= 17:
        return 1
    elif 18 <= p <= 20:
        return 2
    elif 21 <= p <= 23:
        return 3
    elif 24 <= p <= 27:
        return 4
    elif 28 <= p:
        return 5


def info(s_file: str, e_file: str, ep_file: str):
    names = {}
    exercises = {}
    total_points = {}
    exam_points = {}
    table = ''
    with open(s_file) as sf, open(e_file) as ef, open(ep_file) as epf:
        for line in sf:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            names[parts[0]] = f"{parts[1]} {parts[2]}"

        for line in ef:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            exercises[parts[0]] = sum(list(map(int,parts[1:])))
       
        for line in epf:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            total_points[parts[0]] = (exercises[parts[0]]//4) + sum(list(map(int, parts[1:])))
            exam_points[parts[0]] = sum(list(map(int, parts[1:])))
            
    
    table += f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}\n"
    for pic, name in names.items():
        if pic in total_points:
            points = total_points[pic]
            g = grade(points)
            table += (f"{name:30}{exercises[pic]:<10}{exercises[pic]//4:<10}{exam_points[pic]:<10}{total_points[pic]:<10}{g:<10}\n")
        else:
            table += (f"{name} 0\n")

    return table
            
def getCourseData(fileName: str):
    """
        c represents the course name 
        cred represents the course credits
    """
    c = ''
    cred = ''
    with open(fileName) as cf:
        for line in cf:
            parts = line.strip().split()
            if "name:" in parts:
                i = parts.index("name:")
                parts = parts[i+1:]
                for word in parts:
                    c += word + " "
            
            if "credits:" in parts:
                i = parts.index("credits:")
                parts = parts[i+1:]
                for credit in parts:
                    cred = credit
    
    return c[:-1], cred

def get_data_for_csv_file(s_file: str, e_file: str, ep_file: str):
    csv_data = {}
    exercises = {}
    total_points = {}
    exam_points = {}

    with open(s_file) as sf, open(e_file) as ef, open(ep_file) as epf:
        i = 0
        name = ''
        for line in sf:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                i = parts.index("id")
                continue
            id_num = parts[i]
            for words in parts[i+1:]:
                name += words + " "
                
            csv_data[id_num] = [name.strip()]
            name = ''
        
        for line in ef:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            exercises[parts[0]] = sum(list(map(int,parts[1:])))
       
        for line in epf:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            total_points[parts[0]] = (exercises[parts[0]]//4) + sum(list(map(int, parts[1:])))
            exam_points[parts[0]] = sum(list(map(int, parts[1:])))

        for pic, name in csv_data.items():
            if pic in total_points:
                points = total_points[pic]
                g = grade(points)
                csv_data[pic].append(g)
                
    return csv_data


def create_files(fileName: str, s_file: str, e_file: str, ep_file: str):
    csv_data = get_data_for_csv_file(s_file, e_file, ep_file)
    with open("results.txt", "w") as rtxt:
        course, cred = getCourseData(fileName)
        rtxt.write(f"{course}, {cred} credits\n{"="*38}\n")
        rtxt.write(info(s_file, e_file,ep_file))
    
    with open("results.csv", "w") as rcsv:
        for id_num, name_grade in csv_data.items():
            rcsv.write(f"{id_num};{name_grade[0]};{name_grade[1]}\n")


def main():
    s_info_file = input("Student information: ")
    e_info_file = input("Exercises completed: ")
    exam_points_file = input("Exam points: ")
    course_file = input("Course information: ")
    create_files(course_file, s_info_file, e_info_file, exam_points_file)


main()
