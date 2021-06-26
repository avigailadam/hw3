#### PART 1 ####
# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output
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
    if len(id_to_average) == 0:
        return 0
    return int(tot_sum / len(id_to_average))


#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def make_lower_case(let):
    if ord('a') <= ord(let) <= ord('z'):
        return ord(let)
    return ord(let) - ord('A') + ord('a')


def check_strings(s1, s2):
    s2_hist = {}
    for k in range(ord('a'), ord('z') + 1):
        s2_hist[k] = 0
    for let in s2:
        letter = make_lower_case(let)
        s2_hist[letter] += 1
    for let in s1:
        letter = make_lower_case(let)
        if s2_hist[letter] == 0:
            return False
        s2_hist[letter] -= 1
    return True
