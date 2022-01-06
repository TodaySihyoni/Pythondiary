korean = int(input("국어 >>>"))
math = int(input("수학 >>>"))
english = int(input("영어 >>>"))

total = korean + math + english
avg = total / 3 


if korean < 0 or korean > 100 or math < 0 or math > 100 or english < 0 or english > 100:
    print("오류입니다.")
elif avg >= 80:
    print("불합격")
else: 
    print("합격")