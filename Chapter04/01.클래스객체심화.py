# Unit 클래스 

class Unit:
    """
    속성:  이름, 체력, 기분, 공격력
    """

    # 생성자( constructor)
    # 객체 생성할 때 호출되는 메서드
    def __init__(self, name, hp, feel, damage):
        self.name = name 
        self.hp = hp
        self.feel = feel
        self.damage = damage
        print(f"[{self.name}]이 생성 되었어요.")
    # 객체 출력 호출 메서드
    def __str__(self):
        return f"[{self.name}] 체력 : {self.hp} 기분 : {self.feel}  공격력: {self.damage}" 

carrot = Unit("당근", 20, 30, 5)

tori = Unit("토리", 30, 100, 2)

happy = Unit("해피", 29, 83, 10)

print(carrot)
print(tori)
print(happy)