Student_marks=[5]

for i in range(5):
    mark=int(input("Enter the Student's marks:"))
    if mark<0 or mark>100:
        print("Invalid marks entered, considered as 0")
        mark=0
    elif mark<40:
        print("Student has failed.")    
        break
    Student_marks.append(mark)

agg=sum(Student_marks)/len(Student_marks)

if agg>75:
    print("Distinction")
elif agg>=60 and agg<=75:
    print("First divison")
elif agg<60 and agg>=50:
    print("Second division")
elif agg<50 and agg>=40:
    print("Third division")

    
