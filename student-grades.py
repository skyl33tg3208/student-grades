score = float(input("Enter your score: "))

if score >= 90:
    print("Grade: A - Excellent work!")
elif score >= 80:
    print("Grade: B - Great job!")
elif score >= 70:
    print("Grade: C - Good job but can improve")
elif score >= 60:
    print("Grade: D - Mediocre and needs to improve")
else:
    print("Grade: F - You failed")