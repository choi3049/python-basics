#Dictionary
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'} #{Key1:Value1, Key2:Value2, Key3:Value3, ...}

a = {1: 'hi'}
a = {'a': [1,2,3]}

a = {1:'a'}
a[2] = 'b'
print(a)

a['name'] = 'pay'
print(a)
a[3] = [1,2,3]
print(a)

del a[1]
print(a)

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

a = {'name': 'pey', 'phon': '0119993323', 'birth': '1118'}
print(a.keys())

for k in a.keys():
    print(k)

print(list(a.keys()))

print(a.values())

print(a.items())

a.clear()
print(a)

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))
print('name' in a)
print('email' in a)