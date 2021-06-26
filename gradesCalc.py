def is_valid_id(student_id):
    return student_id and student_id[0] != '0' and 10000000 < int(student_id) < 99999999


def is_valid_name(name):
    for letter in name:
        if not (('a' <= letter <= 'z') or ('A' <= letter <= 'Z') or (letter == ' ')):
            return False
    return True


def is_valid_semester(semester):
    return int(semester) >= 1


def is_valid_avg(avg):
    return 50 < int(avg) <= 100


def calc_grade(student_id, average):
    return int(((int(student_id) % 100) + int(average)) / 2)


def final_grade(input_path, output_path):
    in_file = open(input_path, 'r')
    out_file = open(output_path, 'w')
    id_to_average = {}

    for line in in_file:
        split = [l.strip() for l in line.split(',')]
        if len(split) != 4:
            continue
        student_id, student_name, semester, student_avg = split
        if not (is_valid_id(student_id)
                and is_valid_name(student_name)
                and is_valid_semester(semester)
                and is_valid_avg(student_avg)):
            continue
        id_to_average[student_id] = student_avg

    for student_id, average in sorted(id_to_average.items()):
        grade = calc_grade(student_id, average)
        l1 = [student_id, average, grade]
        out_file.write(", ".join([str(l) for l in l1]) + "\n")


def check_strings(s1: str, s2: str) -> bool:
    s1_hist = {}
    for letter in s1:
        if 'a' <= letter <= 'z':
            s1_hist[letter] = letter
