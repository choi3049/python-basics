#for
'''
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
'''

test_list = ['one', 'two', 'three'] 
for i in test_list:
    print(i)


a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)


'''
"총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 
합격인지 불합격인지 결과를 보여 주시오."
'''

marks = [90, 25, 67, 45, 80]
number = 0 
for mark in marks: 
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)



# marks2.py 
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)


add = 0 
for i in range(1, 11):
    add = add + i
print(add)



#marks3.py
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: 
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))



for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')




a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)

result = [num * 3 for num in a]
print(result)

result = [num * 3 for num in a if num % 2 == 0]
print(result)