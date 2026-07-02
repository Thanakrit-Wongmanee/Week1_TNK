import tkinter as tk

# -----------------------------
# ฟังก์ชัน
# -----------------------------
def press(num):
    display.insert(tk.END, num)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# -----------------------------
# หน้าต่างหลัก
# -----------------------------
root = tk.Tk()
root.title("Calculator")
root.geometry("360x520")
root.configure(bg="#1E1E2E")
root.resizable(False, False)

# ช่องแสดงผล
display = tk.Entry(
    root,
    font=("Segoe UI", 24),
    bg="#2D2D44",
    fg="white",
    bd=0,
    justify="right"
)
display.pack(fill="both", padx=15, pady=20, ipady=15)

# ปุ่ม
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

colors = {
    "num": "#3A3A55",
    "op": "#FF9500",
    "eq": "#34C759",
    "clear": "#FF3B30"
}

frame = tk.Frame(root, bg="#1E1E2E")
frame.pack(expand=True, fill="both", padx=10, pady=10)

for r, row in enumerate(buttons):
    for c, text in enumerate(row):

        if text == "=":
            cmd = calculate
            color = colors["eq"]
        elif text == "C":
            cmd = clear
            color = colors["clear"]
        elif text in "+-*/":
            cmd = lambda t=text: press(t)
            color = colors["op"]
        else:
            cmd = lambda t=text: press(t)
            color = colors["num"]

        btn = tk.Button(
            frame,
            text=text,
            command=cmd,
            font=("Segoe UI", 20, "bold"),
            bg=color,
            fg="white",
            activebackground="#666",
            bd=0,
            relief="flat"
        )

        btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

for i in range(4):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

root.mainloop()