locationX = float(input("Location x-coordinate? "))
locationY = float(input("Location y-coordinate? "))
classroomX = float(input("Classroom x-coordinate? "))
classroomY = float(input("Classroom y-coordinate? "))

distance = ((classroomX - locationX) ** 2 + (classroomY - locationY) ** 2) ** 0.5
print(distance)
