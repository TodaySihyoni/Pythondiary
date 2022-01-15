# 1/ 위치 매개변수
# 가장 기본적

from optparse import Values


def my_func(a,b):
    print(a,b)

my_func(3,5)

# 2/ 기본 매개변수
# 매개변수의 기본값 지정 가능

def post_info(title, content='내용 없다'):
    print('제목  :', title)
    print('내용 :', content)

post_info('출석!')

# 3/ 키워드 매개변수
# 함수 호출 시 -> 키워드 붙여서 호출
# 매개변수 순서 안지켜도 됨

def print_n_times(*values, n=2):
    # n번 반복합니다.
  for i in range(n):
      for value in values:
          print(value)

print()

print_n_times("헬로","배고파","코딩 맛있당", n=3) 

#  2번째 예제

def my_info(title, content):
    print('제목 :', title)
    print('내용 :', content)

my_info(content='글쎄요', title='여친 만드는 방법')