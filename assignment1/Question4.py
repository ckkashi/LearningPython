#Question 4 - Assignment 1
# How many ways are there to remove , add an element from list
#adding element - way-1
print('using append : ')
myList = [];
myList.append("Hello");
print(myList);
myList.append("World");
print(myList);
#way-2
print('using insert : ')
myList = [];
myList.insert(0,"Hello")
print(myList);
myList.insert(1,"World")
print(myList);
#way-3
print('using extend : ')
myList = [];
myList.extend(["Hello","World","from"]);
myList.extend(["szabist"]);
print(myList);

# removing element - way-1
myList = ['Hello', 'World', 'from', 'szabist'];
print("After removing element : ")
myList.pop();
print(myList);
#way-2
myList = ['Hello', 'World', 'from', 'szabist'];
myList.pop(0);
print(myList);
#way-3
myList = ['Hello', 'World', 'from', 'szabist'];
del myList[2];
print(myList);
#way-4
myList = ['Hello', 'World', 'from', 'szabist'];
myList.remove("szabist");
myList.remove("World");
print(myList);
