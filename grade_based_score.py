score = int(input("Enter your score: "))

if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 50 <= score < 60:
    grade = 'E'
else:
    grade = 'F'

print("Your grade is:", grade)
