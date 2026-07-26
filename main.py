from game.playUpDown import *
from game.playRPS import *
from game.playLotto import *

while True:
    # 메뉴 출력
    print("==================== Mini Games====================")
    print("1. 업다운 게임")
    print("2. 가위바위보")
    print("3. 로또 번호 맞추기")
    print("0. 종료")

    # 선택 입력 받기
    menu = int(input("메뉴 선택 : "))

    if menu == 1:
        playUpDown()
    elif menu == 2:
        playRPS()
    elif menu == 3:
        playLotto()

    elif menu == 0:
        print("==================== Mini Games Ended ====================")
        break
    else:
        print("1, 2, 3, 0 중 하나를 선택하시오")
