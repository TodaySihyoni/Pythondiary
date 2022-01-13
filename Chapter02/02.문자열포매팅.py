name= '당근'
duration = 10


# 문자열 포매팅 사용시!!!


message_format = f'{name}님 수강기간이 {duration}일 남았습니다.'
print(message_format)


# format 메서드 사용

a = 'Hello {2} {1} {0}'.format('apple','orange','purple')
print(a)

b = 'Hello {} {} {}'.format('apple','orange','purple')
print(b)

# f-string

name1 = 'apple'
name2 = 'orange'
name3 = 'purple'

c = f'Hi {name1} {name2} {name3}'
print(c)