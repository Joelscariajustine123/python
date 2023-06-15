import tkinter as tk

def compute_distance():
    try:
        initial_height = float(entry_height.get())
        bounciness_index = float(entry_bounciness.get())
        num_bounces = int(entry_bounces.get())

        total_distance = initial_height
        for _ in range(num_bounces):
            total_distance += 2 * initial_height * bounciness_index
            initial_height *= bounciness_index

        label_result.config(text=f"Total Distance: {total_distance:.2f} units")
    except ValueError:
        label_result.config(text="Invalid input!")

window = tk.Tk()
window.title("Bouncy Program")

inputs = [
    ("Initial Height:", "entry_height"),
    ("Bounciness Index:", "entry_bounciness"),
    ("Number of Bounces:", "entry_bounces")
]

for label_text, entry_name in inputs:
    label = tk.Label(window, text=label_text)
    label.pack()
    globals()[entry_name] = tk.Entry(window)
    globals()[entry_name].pack()

button_compute = tk.Button(window, text="Compute Distance", command=compute_distance)
button_compute.pack()

label_result = tk.Label(window, text="")
label_result.pack()

window.mainloop()
