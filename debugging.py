score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score < 50:
    print("Bad")
elif 49 < score < 91:
    print("Passable")
else:
    print("Excellent")