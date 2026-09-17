attendance = [18, 20, 19, 15, 21]
full_days=0
total_attendance=0
for students in attendance:
    if students >=20:
        print(students, "full")
        full_days +=1
    else:
        print(students, "not null")
        total_attendance +=students
        print("Number of full days:", full_days)
        print("Total attendance:", total_attendance)
    