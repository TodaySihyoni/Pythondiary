# 리스트 메서드

# 리스트 데이터 삭제

Animals = ['dog', 'cat', 'fox']
del Animals[1]
print(Animals)

# 리스트 정렬

num = [3, 6, 2, 9, 10]
num.sort()
print(num)

# enumerate : 열거 
 
titles = ['출석', '결석', '휴학']


for index, title in enumerate(titles, 1):
    print(f'{index} 번 째 학생입니다. 여부: {title}')