import tkinter as tk
import random
import time

def playReaction():
    print("==================== REACTION SPEED GAME ====================")

    win = tk.Tk()
    win.title("반응속도 게임")
    win.geometry("700x700")

    label = tk.Label(
        win,
        text="빨간색이 초록색으로 바뀌면\n 최대한 빨리 클릭하세요 !!",
        font=("맑은 고딕", 33),
        fg="white",
        bg="red",
    )
    label.pack(expand=True, fill="both")

    state = {"ready": False, "start_time": 0}

    def turn_green():
        state["ready"] = True
        state["start_time"] = time.time()
        label.config(text="지금클릭!!!", bg="green")

    def on_click(event):
        if state["ready"]:
            reaction = (time.time() - state["start_time"]) * 1000
            label.config(
                text=f"반응속도 : {int(reaction)}ms\n\n창을 닫으면 종료됩니다",
                bg="blue",
            )
            state["ready"] = False
        else:
            label.config(text="초록색이 될 때까지 기다리세요", bg="red")

    label.bind("<Button-1>", on_click)

    delay = random.randint(2000, 5000)
    win.after(delay, turn_green)

    win.mainloop()