import tkinter as tk
from tkinter import messagebox

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("XO Game")
root.geometry("400x450")
root.configure(bg="#1e1e2f")

current_player = "X"
board = [""] * 9

def check_winner():
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def on_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(
            text=current_player,
            fg="#00ffcc" if current_player == "X" else "#ffcc00"
        )

        result = check_winner()

        if result:
            if result == "Draw":
                messagebox.showinfo("Game Over", "เสมอจ้า 🤝")
            else:
                messagebox.showinfo("Game Over", f"ผู้ชนะคือ {result} 🎉")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
            label.config(text=f"Turn: {current_player}")

def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    label.config(text="Turn: X")
    for btn in buttons:
        btn.config(text="", bg="#2b2b3d")

# UI Header
label = tk.Label(
    root,
    text="Turn: X",
    font=("Arial", 20, "bold"),
    bg="#1e1e2f",
    fg="white"
)
label.pack(pady=10)

# ปุ่มเกม
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

buttons = []

for i in range(9):
    btn = tk.Button(
        frame,
        text="",
        font=("Arial", 24, "bold"),
        width=5,
        height=2,
        bg="#2b2b3d",
        fg="white",
        activebackground="#444466",
        command=lambda i=i: on_click(i)
    )
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# ปุ่มรีเซ็ต
reset_btn = tk.Button(
    root,
    text="Restart 🔄",
    font=("Arial", 14),
    bg="#ff5555",
    fg="white",
    command=reset_game
)
reset_btn.pack(pady=15)

root.mainloop()