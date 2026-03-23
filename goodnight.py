import tkinter as tk
import math
import random

root = tk.Tk()
root.title("Good Night")
root.geometry("480x320")
root.configure(bg="#0a0a1a")
root.resizable(False, False)

canvas = tk.Canvas(root, width=480, height=320, bg="#0a0a1a", highlightthickness=0)
canvas.pack()

# Stars
random.seed(42)
stars = [(random.randint(0, 480), random.randint(0, 200), random.random()) for _ in range(60)]
star_ids = []
for x, y, brightness in stars:
    r = random.choice([1, 1, 1, 2])
    sid = canvas.create_oval(x-r, y-r, x+r, y+r, fill="#ffffff", outline="")
    star_ids.append((sid, brightness))

# Moon
canvas.create_oval(360, 30, 440, 110, fill="#fff5c0", outline="#ffeaa0", width=2)
canvas.create_oval(375, 25, 445, 95, fill="#0a0a1a", outline="")

# Text
canvas.create_text(240, 175, text="Good Night", font=("Georgia", 36, "italic"),
                   fill="#c8b8f0", anchor="center")
canvas.create_text(240, 220, text="Rest well ✦", font=("Georgia", 14),
                   fill="#8878a8", anchor="center")

# Close button
btn = tk.Button(root, text="Sleep  💤", font=("Georgia", 11, "italic"),
                bg="#1a1a3a", fg="#c8b8f0", activebackground="#2a2a4a",
                activeforeground="#e8d8ff", bd=0, padx=20, pady=8,
                cursor="hand2", command=root.destroy)
canvas.create_window(240, 275, window=btn)

# Twinkle animation
tick = [0]
def twinkle():
    tick[0] += 1
    for i, (sid, brightness) in enumerate(star_ids):
        phase = (tick[0] * 0.05 + i * 0.7) % (2 * math.pi)
        alpha = int(128 + 127 * math.sin(phase) * brightness)
        hex_val = f"#{alpha:02x}{alpha:02x}{alpha:02x}"
        canvas.itemconfig(sid, fill=hex_val)
    root.after(60, twinkle)

twinkle()
root.mainloop()