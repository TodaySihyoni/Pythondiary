study_time = int(input("공부시간을 입력하세요(시간) >>>"))
print(study_time)

if study_time >= 10:
    print("폰 잠금이 해제됩니다.")

elif study_time >= 5:
    print("폰 30분동안 사용가능")

else :
    print("폰 사용 금지!")