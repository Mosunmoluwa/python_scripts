print('input the grade')
grade = int(input())  

if  grade >= 70 and  grade <= 100:
    print('congrats you got an A')
elif grade >= 55 and grade <= 69:
    print('hurray you got a B')
elif grade <= 54 and grade >= 50:
    print('hurray you got a C')
elif grade >= 40 and grade <= 49:
    print('no way you got a D')
else:
    print('you got an F')   
