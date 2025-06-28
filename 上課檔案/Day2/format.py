# print('Kevin 20')
# print('Alan 9')
# print('Cindy 18')

# #my name is {name}, I'm {age} years old 
# print('my name is', name, 'I am', age, 'years old')
name = 'Kevin'
age = 20

print('my name is %5s, I am %3s years old' % (name, age))

name = 'Alan'
age = 9

print('my name is %5s, I am %3s years old' % (name, age))

name = 'Cindy'
age = 18

print('my name is %5s, I am %3s years old' % (name, age))

'''
格式符號
%s -> str
%d -> int
%f -> float
'''
name = 'Kevin'
age = 20

print('my name is {:5s}, I am {:3d} years old'.format(name, age))

name = 'Alan'
age = 9

print('my name is {:5s}, I am {:3d} years old'.format(name, age))

name = 'Cindy'
age = 18

print('my name is {:5s}, I am {:3d} years old'.format(name, age))

print(f'my name is {name:5s}, I am {age:3d} years old') #f-string function

#取小數後第幾位
pi = 3.1415926
print('%.3f'%(pi))
print('{:.3f}'.format(pi))
print(f'{pi:.3f}')
