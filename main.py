import random
import tkinter as tk

def secret_santa(participants, exclusions):
    givers = participants[:]
    receivers = participants[:]

    max_attempts = 10000
    for _ in range(max_attempts):
        random.shuffle(receivers)

        if all(
            g != r and
            (g, r) not in exclusions and
            (r, g) not in exclusions
            for g, r in zip(givers, receivers)
        ):
            return dict(zip(givers, receivers))

    raise ValueError("Nincs érvényes sorsolás ennyi kitétellel.")

def draw_names():
    participants = [p.strip() for p in entry.get().split(",") if p.strip()]

    if len(participants) < 2:
        result_label.config(text="Adj meg legalább két nevet!")
        return

    exclusions = set()
    exclusions_text = exclusions_entry.get().strip()

    if exclusions_text:
        for pair in exclusions_text.split(","):
            a, b = [x.strip() for x in pair.split("-")]
            exclusions.add((a, b))
            exclusions.add((b, a))  # kétirányú tiltás

    try:
        result = secret_santa(participants, exclusions)
        output = "\n".join(f"{giver} -> {receiver}" for giver, receiver in result.items())
        result_label.config(text=output)
    except ValueError as e:
        result_label.config(text=str(e))

root = tk.Tk()
root.title("Secret Santa Sorsoló")

tk.Label(root, text="Írd be a neveket vesszővel elválasztva:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Label(root, text="Tiltott párok (pl.: Elek-Karina):").pack(pady=5)
exclusions_entry = tk.Entry(root, width=50)
exclusions_entry.pack(pady=5)

tk.Button(root, text="Sorsolás!", command=draw_names).pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()
