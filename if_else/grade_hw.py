score = int(input("Enter your score: "))

if score >= 80:
    print("grade : A")
elif score < 80 and score >= 75:
    print("grade : B+")
elif score < 75 and score >= 70:
    print("grade : B")
elif score < 70 and score >= 65:
    print("grade : C+")
elif score < 65 and score >= 60:
    print("grade : C")
elif score < 60 and score >= 55:
    print("grade : D+")
elif score < 55 and score >= 50:
    print("grade : D")
elif score <= 49:
    print("grade : F")
