time = input("시간 커몬>>> ")

if time.find('시간') == -1:    
    #분 만
  result =  int(time.split('분')[0])
else:
    if time.find('분') == -1:
        #시간만
        result = int(time.split('시간')[0])* 60
    else:
        #시간과 분이 있는 경우
        sub = time.split('시간')
        result = int(sub[0]) * 60 + int(sub[1].split('분')[0])
        
print(result)

        
   

