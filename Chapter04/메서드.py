

# Unit 클래스 

class Unit:
    """
    속성:  이름, 체력, 기분, 공격력
    """

    # 생성자( constructor)
    # 객체 생성할 때 호출되는 메서드

    count = 0
    def __init__(self, name, hp, shield, damage):
        self.name = name 
        self.hp = hp
        self.shield = shield
        self.damage = damage
        print(f"[{self.name}]이 생성 되었어요.")

    # 객체 출력 호출 메서드
    def __str__(self):
        return f"[{self.name}] 체력 : {self.hp} 기분 : {self.shield}  공격력: {self.damage}" 


     # 인스턴스 메서드 =  인스턴스 속성에 접근 가능 메서드

    def hit(self, damage):
        if self.shield >= damage:
            self.shield -= damage
            damage = 0
        
        else: 
             damage -= self.shield
             self.shield = 0 

      # 체력변경
        if damage > 0:
            if self.hp >  damage:
                self.hp -= damage   
            else:
                self.hp = 0

    # 클래스 메서드 (class method)
    # 클래스 속성에 접근하는 메서드

    @classmethod
    def print_count(cls):
        print(f"생성된 유닛 개수: [{cls.count}]개")



carrot = Unit("당근", 20, 30, 5)

tori = Unit("토리", 30, 100, 2)

happy = Unit("해피", 29, 83, 10)


carrot.hit(20)
print(carrot)
carrot.hit(20)
print(carrot)
carrot.hit(20)
print(carrot)

Unit.print_count()

print(dir(carrot))