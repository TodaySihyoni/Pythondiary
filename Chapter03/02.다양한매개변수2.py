# 위치 가변 매개변수
def print_fruits(*args):
    for arg in args:
        print(arg)

print_fruits('apple', 'orange', 'mango', 'grape')

# 키워드 가변 매개변수
 # keyword argument= kwargs
def comment_info(**kwargs):
    for key, value in kwargs.items():
     print(f'{key} : {value}')

comment_info(name='코린이', content='감사해용')

# 매개변수 작성 순서

# 위치 -> 기본 > 위치 가변 - > 키워드(기본) -> 키워드 가변

def post_info( *tags, title, content):
    print(f'제목 : {title}')
    print(f'내용 : {content}')
    print(f'태그 : {tags}')

post_info( '#파이썬', '#재밌다', title= '파이썬 정리!', content= '매개변수')