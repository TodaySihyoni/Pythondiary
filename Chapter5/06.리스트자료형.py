#데이터 있는 리스트
animals = ["강아지", "고양이", "곰"]

#데이터 없는 리스트
empty = []

#데이터 접근하기
print(animals[2])
#데이터 추가
animals.append("사슴")
print(animals)
#데이터 삭제하기 
del animals[0]
print(animals)

#리스트 길이
print(len(animals))
#리스트 정렬
animals.sort(reverse=True)
print(animals)