from abc import *


class Item(metaclass=ABCMeta):
    """
  속성: 이름
  메서드: 줍기, 버리기
   """
    def __init__(self, name):
      self.name = name

    def grab(self):
      print(f"[{self.name}]을 주웠어요")

    def throw(self):
      print(f"[{self.name}]을 버렸습니다.")

    @abstractmethod
    def use(self):
      pass

class weapon(Item):
    """
    속성: 공격력
    메소드: 공격하기
    """

    def __init__(self, name, hurt):
        super().__init__(name)
        self.hurt = hurt

    def use(self):
        print(f"[{self.name}]를 이용해 {self.hurt}로 공격한다.")

class HealingItem(Item):
    """
    속성 : 회복량
    메서드: 사용하기
    """
    def __init__(self, name, recover):
        super().__init__(name)
        self.recover = recover

    def use(self):
        print(f"[{self.name}]를 이용해 {self.recover}로 회복")


m20 = weapon("m20", 399)
juice = HealingItem("연고", 30)

m20.use()
juice.use()