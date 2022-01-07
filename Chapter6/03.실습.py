#로또 예상번호 추출 프로그램

#로또 번호 6개 생성
# 로또 번호는 1~ 45 랜덤
# 6개 숫자 모두 다름
# random 모듈 sample 함수 사용 안됨
# 1. 반복문, 조건문 2. 리스트 3. 함수 사용 

import random                                         


def getRandomNumber():
    number = random.randint(1, 45)
    return number

lotto_number = []   #로또 번호 저장 리스트       

count =  0 # 현재 뽑은 숫자

while True:                              # while문 사용 이유 : 반복 횟수 정해지지 않음, 
    if count > 5:     # if count == 6:   
        break
    random_number =  getRandomNumber()
    if  random_number not in lotto_number:
     lotto_number.append(random_number)
     count += 1

lotto_number.sort()
for number in lotto_number:
    print(number, end= " ")