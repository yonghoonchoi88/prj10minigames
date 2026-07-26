import random

def playRPS():
    print("==================== ROCK PAPER SCISSORS GAME ====================")

    while True:
        answer = random.randint(1, 3)
        answer = "가위" if answer == 1 else "바위" if answer == 2 else "보"

        hand = input("가위 바위 보:")

        if hand != "가위" and hand != "바위" and hand != "보":
            print("가위, 바위, 보 중에 다시 선택하세요")
        elif hand == answer:
            print(f"컴퓨터: {answer} 유저: {hand}")
            print("비겼습니다! 다시 선택하세요")

        elif answer != hand:
            print(f"컴퓨터: {answer} 유저: {hand}")
            if hand == "가위":
                result = "컴퓨터승" if answer == "바위" else "유저승"
            elif hand == "바위":
                result = "컴퓨터승" if answer == "보" else "유저승"
            elif hand == "보":
                result = "컴퓨터승" if answer == "가위" else "유저승"
            print(result)

        replay = input("Press any key to replay (N 입력시 종료)").upper()
        if replay == "N":
            break
