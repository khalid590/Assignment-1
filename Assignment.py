
bangla_mark = int(input("Bangla Marks: "))
english_mark = int(input("English Marks: "))
math_mark = int(input("Math Marks: "))
science_mark = int(input("Science Marks: "))

total_marks = bangla_mark + english_mark + math_mark + science_mark

average_mark = total_marks / 4

print("Average mark: ",average_mark)

marks = int(input("\nEnter your marks 1 to 100 : "))

if marks >= 91 and marks <= 100:
    print('A+')

elif marks >= 81 and marks <= 90:
    print('A')

elif marks >= 71 and marks <= 80:
    print('B')

elif marks >= 61 and marks <= 70:
    print('C')

elif marks >= 41 and marks <= 60:
    print('D')

else:
    print('F')