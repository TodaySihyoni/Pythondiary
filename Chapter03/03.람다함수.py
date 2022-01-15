# 기존 함수
from lzma import is_check_supported


def minus_word(a):
    return a -1

# 람다 함수 = 이름 필요 없는 간편한 함수 / 메모리사용 효율!!  
lambda a : a-1

# 람다 함수 호출방법 1. 함수 자체 호출
print((lambda a : a-1)(10))

#람다 함수 호출방법 2.  변수에 담아서 호출
minus_one = lambda a :a -1
print(minus_one(100))

# 람다 함수 if 문  -> else 꼭 사용!
# 기존함수
def is_my_word(a):
    if a > 3:
        return True
    else:
        return False

# 람다 함수
lambda a : True if a > 0 else False
#람다 함수 호출 1)

print((lambda a : True if a > 0 else False)(-3))

# 람다함수 호출 2)

is_my_word = lambda a : True if a > 0 else False
print(is_my_word(3))

