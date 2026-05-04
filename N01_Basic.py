print(not True)
print(not False)

# not = !
# true, false -> True, False

name = 'yena'
age = 19
hobby = 'play computer game'
is_adult = age >= 19

print(name + ' is ' + str(age) + ' years old.\n'+name+ ' likes ' + hobby + '.')
# print(name + ' is ' + age + ' years old.\n'+name+ ' likes ' + hobby + '.')

'''
숫자형, boolean은 str(변수 이름)로 감싸야 출력이 가능하다.
그렇지 않으면 오류(TypeError: can only concatenate str (not "int") to str)가 발생한다.
'''

print(name + ' is', age,'years old.\n'+name+ ' likes ' + hobby + '.')
print('Is ' +name,'Adult? : ' + str(is_adult))
