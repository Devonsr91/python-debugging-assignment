
# Grade Analyzer
# This program analyzes student scores and letter grades.
# It also lets the user enter additional scores.

MIN_SCORE = 0
MAX_SCORE = 100
PASSING_SCORE = 60

scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]


def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def show_results():
    if not scores:
        print("No scores available to analyze.")
        return

    total = len(scores)
    average = sum(scores) / total
    highest = max(scores)
    lowest = min(scores)

    passing = sum(1 for score in scores if score >= PASSING_SCORE)
    failing = total - passing

    print("\n=== Grade Analyzer ===")
    print(f"Total scores: {total}")
    print(f"Average: {average:.1f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Passing: {passing} ({passing / total * 100:.1f}%)")
    print(f"Failing: {failing} ({failing / total * 100:.1f}%)")

    grade_counts = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for score in scores:
        grade = get_grade(score)
        grade_counts[grade] += 1

    print("\nGrade Distribution:")
    for grade in ["A", "B", "C", "D", "F"]:
        print(f"{grade}: {grade_counts[grade]} students")


show_results()

print("\n--- Add More Scores ---")

while True:
    entry = input("Enter a score (or 'done' to finish): ").strip()

    if entry.lower() == "done":
        break

    try:
        new_score = int(entry)

        if new_score < MIN_SCORE or new_score > MAX_SCORE:
            print("Please enter a score between 0 and 100.")
            continue

        scores.append(new_score)
        average = sum(scores) / len(scores)
        print(f"Updated average: {average:.1f}")

    except ValueError:
        print("Invalid input. Enter a whole-number score or 'done'.")

final_average = sum(scores) / len(scores)
print(f"\nFinal average: {final_average:.1f}")
