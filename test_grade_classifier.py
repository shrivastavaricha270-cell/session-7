from grade_classifier import classify

assert classify(100) == "A"
assert classify(90) == "A"
assert classify(89.9) == "B"
assert classify(75) == "B"
assert classify(59.9) == "F" or classify(59.9) == "D"
assert classify(40) == "D"
assert classify(0) == "F"

for invalid in (-1, 101):
    try:
        classify(invalid)
        raise AssertionError("Invalid mark was accepted")
    except ValueError:
        pass

print("Grade classifier tests passed.")
