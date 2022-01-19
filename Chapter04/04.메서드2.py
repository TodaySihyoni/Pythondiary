class math:
    
    #정적 메서드(static method)
    #인스턴스를 만들 필요 없다.
    @staticmethod
    def add(x,y):
        return x + y

    @staticmethod
    def sub(x, y):
        return  x - y

print(math.add(4, 5))
print(math.sub(5, 6))