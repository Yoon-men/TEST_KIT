import pyautogui as m
import mouse
import keyboard
import sys

print('=' * 30)
print('\n   <마우스 포인터 테스터>\n')
print('=' * 30)

replay = 0

while True :
    if replay == 0 : 
        print('\n[system] 테스트를 진행하시려면 Enter키를 눌러주세요.')
    else : 
        print('\n[system] 테스트를 계속 진행하시려면 Enter키를 눌러주세요. 테스트 종료는 ESC키를 눌러주세요.')

    while True : 
        if keyboard.is_pressed('Enter') : 
            print('\n[system] 테스트를 시작합니다. 마우스 좌클릭을 시도해주세요.')
            while True : 
                if mouse.is_pressed('left') : 
                    x, y = m.position()                                     # 프로그램 종료할 때 까지 계속 마우스 포인터 좌표 확인

                    RGB = m.screenshot().getpixel((x, y))                   # 마우스 포인터가 위치한 곳의 색깔 정보 획득
                    print('\nx : {}, y : {}, RGB = {}'. format(x, y, RGB))    # 마우스 포인터가 위치한 곳의 좌표 및 색깔 정보 표시
                    replay = 1
                    break
            break
    
        elif keyboard.is_pressed('ESC') : 
            sys.exit()

    

