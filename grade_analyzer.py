# Task 1 — Process the Scores
def process_scores(students):
    """
    Calculate the average score for each student.

    Args:
        students (dict): {name: [scores]}

    Returns:
        dict: {name: average_score}
    """
    averages = {}
    for name, scores in students.items():
        if scores:  # avoid division by zero
            avg = round(sum(scores) / len(scores), 2)
        else:
            avg = 0.0
        averages[name] = avg
    return averages


# Task 2 — Classify the Grades
def classify_grades(averages):
    """
    Assign letter grades based on average scores.

    Args:
        averages (dict): {name: average_score}

    Returns:
        dict: {name: (average, grade)}
    """
    # Grading thresholds
    grade_A = 90
    grade_B = 75
    grade_C = 60

    classified = {}
    for name, avg in averages.items():
        if avg >= grade_A:
            grade = "A"
        elif avg >= grade_B:
            grade = "B"
        elif avg >= grade_C:
            grade = "C"
        else:
            grade = "F"
        classified[name] = (avg, grade)
    return classified


# Task 3 — Generate the Report
def generate_report(classified, passing_avg=70):
    """
    Print a formatted student grade report and return the number of passing students.

    Args:
        classified (dict): {name: (average, grade)}
        passing_avg (float): threshold for passing

    Returns:
        int: number of students who passed
    """
    print("===== Student Grade Report =====")
    passed_count = 0
    total_students = len(classified)

    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed_count += 1
        print(f"{name:<10} | Avg: {avg:.2f} | Grade: {grade} | Status: {status}")

    failed_count = total_students - passed_count
    print("================================")
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed_count}")
    print(f"Failed         : {failed_count}")
    return passed_count


# Main block
if __name__ == "__main__":
    students = {
        "Alice": [88, 92, 85, 80],
        "Bob": [60, 65, 70, 65],
        "Clara": [95, 97, 96, 93]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)