#문자열,文字列

a = "Hello World"
b = 'Python is fun'
c = """Life is too short, You need python"""
d = '''Life is too short, You need python'''

food = "Python's favorite food is perl"
print(food)
say = '"Python is very easy." he says.'
print(say)

food2 = 'Python\'s favorite food is perl'
print(food2)
say2 = "\"Python is very easy.\" he says."
print(say2)

#行替え
multiline = "Life is too short\nYou need python"
print(multiline)

multiline2 = '''
    Life is too short
    You need python
    '''

print(multiline2)

#文字列演算
head = "Python"
tail = " is fun!"
print(head + tail)

a = "python"
print(a * 2)

a = "Life is too short"
print(len(a))

#文字列インデックスとスライシング
a = "Life is too short, You need Python"
print(a[3])
print(a[-1])
print(a[0])
print(a[-0])

print(a[0:4]) # 0 <= a < 4
print(a[5:7]) 
print(a[12:17]) 
print(a[19:])
print(a[:17])
print(a[:])
print(a[19:-7])


a = "20010331Rainy"
date = a[:8]
weather = a[8:]
day = a[4:8]
print(date)
print(weather)
print(day)


a = "Pithon"
print(a[:1] + 'y' + a[2:])

#文字列フォーマット
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")

number = 3
print("I eat %d apples." % number)

day = "three"
print("I ate %d apples. so I was sick for %s days." % (number,day))

print("Error is %d%%." % 98)

print("%10s" % "hi")
print("%-10sjane." % 'hi')
print("%0.4f" % 3.42134234) #小数点表現
print("%10.4f" % 3.42134234)

#format関数を使ったフォーマット
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))

number = 3
print("I eat {0} apples".format(number))
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))

print("{0:<10}".format("hi")) #左揃え
print("{0:>10}".format("hi")) #右揃え
print("{0:^10}".format("hi")) #中央揃え

print("{0:=^10}".format("hi")) #空白を埋める
print("{0:!<10}".format("hi"))

y = 3.42134234
print("{0:0.4f}".format(y)) #小数点表現
print("{0:10.4f}".format(y)) #小数点表現

print("{{ and }}".format()) #{}表現

#f文字列フォーマット
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.') 
print(f'나는 내년이면 {age+1}살이 된다.')


d = {'name':'choe','age':30}
print(f'私の名前は{d["name"]}です。{d["age"]}歳です。')

print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')

print(f'{"hi":=^10}')
print(f'{"hi":!<10}')

y = 3.42134234
print(f'{y:0.4f}')
print(f'{y:10.4f}')

print(f'{{ and }}')


#文字列関連関数
a = "hobby"
print(a.count('b'))

a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))

a = "Life is too short"
print(a.index('t'))
# print(a.index('k'))

print(",".join('abcd'))
print(",".join(['a', 'b', 'c', 'd']))

a = "hi"
print(a.upper())

a = "HI"
print(a.lower())

a = " hi "
print(a.lstrip())

a= " hi "
print(a.rstrip())

a = " hi "
print(a.strip())

a = "Life is too short"
print(a.replace("Life", "Your leg"))

a = "Life is too short"
print(a.split())

b = "a:b:c:d"
print(b.split(':'))