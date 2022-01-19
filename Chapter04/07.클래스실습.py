# 유닛 정보

unit_info = {
    "probe" : {
  "name": "프로브",
  "mineral": 50,
  "gas" : 0,
  "hp" : 20,
  "shield" : 20,
  "damage" : 5
},

    "zealot" : {
  "name": "질럿",
  "mineral": 100,
  "gas" : 0,
  "hp" : 100,
  "shield" : 60,
  "damage" : 16
},
    "dragon" : {
  "name": "드라군",
  "mineral": 125,
  "gas" : 50,
  "hp" : 100,
  "shield" : 80,
  "damage" : 20
}
}

# 클래스 유닛

class Unit:
   
   def __init__(self, name, hp, shield, damage):
      self.name = name
      self.hp = hp
      self.shield = shield 
      self.damage =damage


class Player:

    """
   속성: 닉네임, 미네랄, 가스 , 유닛리스트 
   """
    def __init__(self, myname, mineral, gas, unit_list = []):
      self.myname = myname
      self.mineral = mineral
      self.gas = gas
      self.unit_list = unit_list

    
    # 생산하기

    def produce(self, name, mineral, gas, hp, shield, damage):
        if self.mineral - mineral < 0:
            print("미네랄 부족")
        elif self.gas - gas < 0:
            print("가스 부족")
        else:
            self.mineral -= mineral
            self.gas -= gas
            unit = Unit(name, hp, shield, damage)
            self.unit_list.append(unit)
            print(f"[{name}]을 생산")

#플레이어

player1 = Player("Bisu", 400, 50)

# 유닛

player1.produce(unit_info['probe']['name'], unit_info['probe']['mineral'], 
                unit_info['probe']['gas'],  unit_info['probe']['hp'], 
                unit_info['probe']['shield'], unit_info['probe']['damage'])
player1.produce(unit_info['zealot']['name'], unit_info['zealot']['mineral'], 
                unit_info['zealot']['gas'],  unit_info['zealot']['hp'], 
                unit_info['zealot']['shield'], unit_info['zealot']['damage'])
player1.produce(unit_info['dragon']['name'], unit_info['dragon']['mineral'], 
                unit_info['dragon']['gas'],  unit_info['dragon']['hp'], 
                unit_info['dragon']['shield'], unit_info['dragon']['damage'])

# 생성된 유닛 확인 
for unit in player1.unit_list:
    print(f"[{unit.name}] 체력: {unit.hp}   방어: {unit.shield}  공격: {unit.damage} ")