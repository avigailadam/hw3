def check_id(student_id):
    if student_id < 10000000 or student_id > 99999999:
        return 0
    return 1


def check_legal_name(name):
    for letter in name:
        if not ('a' <= letter <= 'z') or (letter >= 'A' or letter <= 'Z'):
            return 0
    return 1


def check_semester(semester):
    if semester >= 1:
        return 1
    return 0


def check_hw_avg(avg):
    if 50 < avg <= 100:
        return 1
    return 0


def calc_grade(student_id, average):
    return ((student_id % 100) + average) / 2


def final_grade(input_path, output_path):
    in_file = open(input_path, 'r')
    out_file = open(output_path, 'w')
    id_to_average = {}
    for line in in_file:
        student = line.split(',')  # [id,name,semester,hw avg]
        if not check_id(student[0]) and check_legal_name(student[1]) and check_semester(student[2]) and check_hw_avg(
                student[3]):
            continue
        id_to_average[student[0]] = student[3]
    for student_id, average in id_to_average.items():
        grade = calc_grade(student_id, average)
        l1 = [student_id, average, grade]
        out_file.write(",".join(l1))
