#Question 2 - Assignment 1
english_marks = int(input("Enter english marks : "));
maths_marks = int(input("Enter maths marks : "));
database_marks = int(input("Enter database marks : "));
os_marks = int(input("Enter os marks : "));

total_marks = english_marks + maths_marks + database_marks + os_marks ;

percentage = (total_marks * 100) / 400 ;

print("Total marks : ",total_marks,"\nPercentage : ",percentage);