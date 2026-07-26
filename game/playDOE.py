import random

def playDOE():
    print("==================== DICE ODD OR EVEN GAME ====================")

    while True:
        dice_number = random.randint(1, 6)
        if dice_number == 1 or dice_number == 3 or dice_number == 5:
            dice_result = "홀"
        else:
            dice_result = "짝"

        user_choice = input("홀/짝 예측 (홀 또는 짝) : ")
        if user_choice != "홀" and user_choice != "짝":
            print("홀 또는 짝 중에 하나만 고르시오.")
            continue
        else:
            if user_choice == dice_result:
                result = "정답!!"
            else:
                result = "오답 ㅠㅠ"
        print(f"주사위 : {dice_number} ({dice_result})\n{result}")

        replay = input("Press ENTER to replay (N 입력시 종료)").upper()
        if replay == "N":
            break