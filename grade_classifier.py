def classify(mark):
    if not 0 <= mark <= 100:
        raise ValueError("Mark must be between 0 and 100.")
    if mark >= 90:
        return "A"
    if mark >= 75:
        return "B"
    if mark >= 60:
        return "C"
    if mark >= 40:
        return "D"
    return "F"

mark = float(input("Enter mark: "))
try:
    print("Grade:", classify(mark))
except ValueError as error:
    print("Error:", error)
