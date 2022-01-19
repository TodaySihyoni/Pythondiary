class Unit:
    """
    인스턴스 속성: 이름, 체력, 기분, 공격력
    -> 객체마다 다른값을 가진다.

    클래스 속성: 전체 유닛 갯수 
    -> 모든 객체가 공유하는 속성

    비공개 속성 
    -> 클래스 내에서만 사용가능
    """
    count = 0 
    def __init__(self, name, hp, feel, damage):
        self.name = name 
        self.__hp = hp
        self.feel = feel
        self.damage = damage
        Unit.count += 2
        print(f"[{self.name}]이 생성 되었어요.")
    
    def __str__(self):
        return f"[{self.name}] 체력 : {self.__hp} 기분 : {self.feel}  공격력: {self.damage}" 


carrot = Unit("당근", 20, 30, 5)
tori =   Unit("토리", 30, 100, 2)
happy = Unit("해피", 29, 83, 10)

#인스턴스 속성 수정
carrot.damage += 3
print(carrot)

# 네임 맹글링
carrot._Unit__hp = 9990
print(carrot)
# 비공개 속성 접근
carrot.__hp =  9999
print(carrot)

# 전체 출력
print(Unit.count)