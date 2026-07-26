import random

def playLotto():
    print("==================== Lotto Game ====================")

    while True:
        lotto_list = sorted(random.sample(range(1, 51), 6))
        user_list = []
        print("1부터 50까지중에 번호를 고르세요. (중복불가)")

        for i in range(6):
            while True:
                try:
                    number = int(input(f"{i + 1}번째 번호 : "))
                except ValueError:
                    print("1부터 50까지중에 번호를 고르세요. (중복불가)")
                    continue
                if number in user_list:
                    print("중복된 번호에요 다시 입력하세요.")
                elif number > 50 or number < 1:
                    print("1부터 50까지만 가능합니다.")
                else:
                    user_list.append(number)
                    break
        user_list = sorted(user_list)

        count = 0
        for i in lotto_list:
            for j in user_list:
                if i == j:
                    count += 1

        prize = {0:"꽝", 1:"6등", 2:"5등", 3:"4등", 4:"3등", 5:"2등", 6:"1등"}
        result = prize[count]

        print(f"당첨번호 : {lotto_list}")
        print(f"내 번호 : {user_list}")
        print(f"{count}/6 번호 일치 -> {result}")

        replay = input("Press ENTER to replay (N 입력시 종료)").upper()
        if replay == "N":
            break