#Question 3 - Assignment 1
english_marks = int(input("Enter english marks : "));
maths_marks = int(input("Enter maths marks : "));
database_marks = int(input("Enter database marks : "));
os_marks = int(input("Enter os marks : "));

total_marks = english_marks + maths_marks + database_marks + os_marks ;

percentage = (total_marks * 100) / 400 ;

grade = "";

if percentage >= 80 :
    grade = "A+";
elif percentage >= 70 :
    grade = "A";
elif percentage >= 60 :
    grade = "B";
elif percentage >= 50 :
    grade = "C";
elif percentage < 50 :
    grade = "F";


print("Total marks : ",total_marks,"\nPercentage : ",percentage,"\nGrade : ",grade);