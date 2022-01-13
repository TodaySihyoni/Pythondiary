#  replace   : 문자열 교체

a = '오늘 녹차라떼를 시켰다'.replace("녹차라떼","아아")
print(a)

# find :  문자열 차기

b = 'Hello Dangun'.find('Dangun2')
print(b)

# spilt : 문자열 분리
c = '밥 종류 일식 양식 중식 한식'.split()
print(c)

d = '밥종류:일식:양식:중식:한식'.split(':')
print(d)

# strip :  문자열 공백 제거

e = '    졸리다    '.lstrip()
print(e)
f =  '    졸리다    '.rstrip()
print(f)
g =  '    졸리다    '.strip()
print(g)