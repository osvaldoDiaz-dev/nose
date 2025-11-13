
import tkinter as tk
import winsound
import random
import threading


MESSAGE = "DIOS ESTÁ MUERTO"
EXTRA_MESSAGES = [
    MESSAGE,
    "1298374h1203noiu-´.+sa-df+á-dsf¿'-4¿r´12{213}.############"
]


COLORS = ["red", "black", "white", "darkred", "purple", "#8B0000", "#222", "#440044", "#00FF00", "#FF00FF", "#FFFF00"]
BG_COLORS = ["black", "darkred", "#222", "#440044", "#1a1a1a", "#00FF00", "#FF00FF", "#FFFF00"]
FREQUENCIES = [400, 600, 800, 1000, 1200, 150, 300, 900, 666, 1337, 2048, 50, 2500]
DURATION = 80
FONTS = ["Impact", "Arial Black", "Comic Sans MS", "Courier", "System", "Fixedsys", "Terminal", "Consolas", "MS Gothic", "Lucida Console", "Times", "Verdana"]


class ScaryApp:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        # Crear muchas etiquetas superpuestas para saturación extrema
        self.labels = []
        for i in range(14):
            lbl = tk.Label(root, text=MESSAGE, font=(random.choice(FONTS), random.randint(50, 120)), fg=random.choice(COLORS), bg="black")
            lbl.place(relx=0.5 + random.uniform(-0.04, 0.04), rely=0.5 + random.uniform(-0.04, 0.04), anchor='center')
            self.labels.append(lbl)
        self.extra_label = tk.Label(root, text="", font=(random.choice(FONTS), 40), fg="white", bg="black")
        self.extra_label.place(relx=0.5, rely=0.7, anchor='center')
        self.blink()
        self.bg_blink()
        self.move_text()
        self.show_extra_message()
        threading.Thread(target=self.play_sound, daemon=True).start()
        self.root.bind('<Escape>', lambda e: self.root.destroy())


    def blink(self):
        # Saturar el parpadeo y glitch en todas las etiquetas, alternando fuentes
        for lbl in self.labels:
            color = random.choice(COLORS)
            font_size = random.randint(50, 130)
            font_type = random.choice(FONTS)
            text = MESSAGE if random.random() > 0.2 else MESSAGE[::-1]
            lbl.config(fg=color, font=(font_type, font_size), text=text)
            lbl.place(relx=0.5 + random.uniform(-0.07, 0.07), rely=0.5 + random.uniform(-0.07, 0.07), anchor='center')
        self.root.after(random.randint(15, 35), self.blink)


    def bg_blink(self):
        bg = random.choice(BG_COLORS)
        self.root.configure(bg=bg)
        for lbl in self.labels:
            lbl.config(bg=bg)
        self.extra_label.config(bg=bg)
        self.root.after(random.randint(20, 60), self.bg_blink)


    def move_text(self):
        # Mueve el texto extra aleatoriamente y mucho más rápido
        x2 = 0.5 + random.uniform(-0.25, 0.25)
        y2 = 0.7 + random.uniform(-0.15, 0.15)
        font_type = random.choice(FONTS)
        self.extra_label.config(font=(font_type, random.randint(30, 60)))
        self.extra_label.place(relx=x2, rely=y2, anchor='center')
        self.root.after(18, self.move_text)


    def show_extra_message(self):
        msg = random.choice(EXTRA_MESSAGES)
        # Glitch: sobreponer caracteres aleatorios
        if random.random() < 0.7:
            msg += "\n" + ''.join(random.choices('#$%&/()=?¡¿@', k=random.randint(20, 50)))
        self.extra_label.config(text=msg)
        self.root.after(random.randint(10, 40), self.show_extra_message)

    def play_sound(self):
        while True:
            freq = random.choice(FREQUENCIES)
            winsound.Beep(freq, random.randint(100, 350))

if __name__ == "__main__":
    root = tk.Tk()
    app = ScaryApp(root)
    root.mainloop()
