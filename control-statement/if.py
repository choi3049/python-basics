#if文
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

'''
if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장A
    수행할 문장B
    ...
'''

money = 2000
if money >= 3000:
    print("taxi")
else:
    print("walk")

card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print(1 in [1,2,3])
print(1 not in [1,2,3])

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 간다")
else:
    print("걸어간다")

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("걸어간다")



pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("taxi")
else:
    print("walk")



'''
If <조건문>:
    <수행할 문장1> 
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
...
else:
   <수행할 문장1>
   <수행할 문장2>
   ... 
'''

score = 50
if score >= 60:
    message = "success"
else:
    message = "failure"

message = "success" if score >= 60 else "failure"