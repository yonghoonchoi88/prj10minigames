from game.playUpDown import *
from game.playRPS import *
from game.playLotto import *
from game.playDOE import *
from game.playReaction import *

guide = "1, 2, 3, 4, 5, 0 중 하나를 선택하시오"
menu_list = {1:playUpDown, 2:playRPS, 3:playLotto, 4:playDOE, 5:playReaction}

while True:
    # 메뉴 출력
    print("==================== Mini Games====================")
    print("1. 업다운 게임")
    print("2. 가위바위보")
    print("3. 로또 번호 맞추기")
    print("4. 주사위 홀짝 게임")
    print("5. 반응속도 게임 (GUI)")
    print("0. 종료")

    # 선택 입력 받기
    try:
        menu = int(input("메뉴 선택 : "))
    except ValueError:
        print(guide)
        continue
    if menu == 0:
        print("==================== Mini Games Ended ====================")
        break
    elif menu in menu_list:
        menu_list[menu]()
    else:
        print(guide)