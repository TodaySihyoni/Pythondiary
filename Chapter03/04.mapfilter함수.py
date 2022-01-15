# 사용 이유: 기존 리스트에서 수정 후 새로운 리스트 만듦

# 대표함수
# map(함수, 리스트)
import re


print(list(map(int, ['1', '3', '5', '3'])))

# 리스트 모든 공백 제거
words = ['    귀엽다   ', '   예쁘다      ',  '   고마워   ']

# 1 )  for 사용
#for i in range(len(words)):
 #   words[i]  = words[i].strip()
#print(words)

# 2) map 사용

#def strip_all(x):
 #   return x.strip()
#words = list(map(strip_all, words))
#print(words)

# 3) 람다 사용

words = list(map(lambda x : x.strip(), words))
print(words)

# 2. filter(함수, 리스트)  -> 기존 리스트에서 조건을 만족하는 요소만 뽑을때

# 사용
def func(o):
    return o < 0
print(list(filter(func, [-5, -3, - 2, 9, 3])))

# 예제 : 리스트에서 길이가 5 이하인 문자들만 필터링

fruits = ['banana', 'carrot', 'apple', 'kiwi', 'melon' ]

#result = []
#for i in fruits:
 #  if len(i) <= 5:
  #  result.append(i)
#print(result)
 
#2) filter 사용
#def word_check(x):
 #   return  len(x) <= 5

#result =  list(filter(word_check, fruits))
 #print(result)

# 3) 람다 사용 - 한줄로 사용

result = list(filter(lambda x :len(x) <= 5, fruits))
print(result)
