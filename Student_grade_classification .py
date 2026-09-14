marks=float(input('Enter your marks=' ))
if marks < 0 or marks > 100:
    print('Invalid marks, please enter marks between 0 and 100')
    marks=int(input('Enter your marks=' ))
if marks >= 80 and marks <= 100:
    print('Grade= A')
elif marks >= 70 and marks < 80:
    print('Grade= B')
elif marks >= 60 and marks < 70:
    print('Grade= C')
elif marks >= 50 and marks < 60:
    print('Grade= D')
else:
    print('Grade= F')