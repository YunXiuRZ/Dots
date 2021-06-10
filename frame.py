import json
import random
import math
import tkinter as tk

window = tk.Tk()
window.title('Generate Dots')
window.geometry('500x300')

func = tk.StringVar()
quantity = tk.StringVar()

class Result:
    def linear_result(self, x, y):
        return (x * 5 / 4 + y) >= 1000

    def rectangle_result(self, x, y):
        return 1200 >= x and x >= 400 and 800 >= y and y >= 200

    def quadratic_result(self, x, y):
        return  ((x-1200)**2) / 1800 + 200 - y >= 0

    def oval_result(self, x, y):
        return ((x - 400)**2 + (y - 500)**2)**0.5 + ((x - 1200)**2 + (y - 500)**2)**0.5 <= 1000

    def sine_result(self, x, y):
        sin_phi = 5 / 89**0.5 
        cos_phi = 8 / 89**0.5
        x_prime = x*cos_phi - y*sin_phi
        y_prime = y*cos_phi + x*sin_phi
        return math.sin(x_prime / 160) >= (y_prime - 900)/300

def generate_dataset(func, quantity):
    data = []
    for i in range(quantity):
        random_x = random.randint(0, 1600)
        random_y = random.randint(0, 1000)
        if(func(random_x, random_y)):
            color = 1
        else:
            color = 0
        data.append([random_x, random_y, color])
    return data

def generate_json():
    function = getattr(Result(), func.get())
    data = generate_dataset(function, int(quantity.get()))
    with open("dots.json", 'w') as file:
        json.dump(data, file)


func.set("linear_result")
linear_button = tk.Radiobutton(window, text='Linear Result', variable=func, value="linear_result")
linear_button.pack()
linear_button.select()
rectangle_button = tk.Radiobutton(window, text='Rectangle Result', variable=func, value="rectangle_result")
rectangle_button.pack()
quadratic_button = tk.Radiobutton(window, text='Quadratic Result', variable=func, value="quadratic_result")
quadratic_button.pack()
oval_button = tk.Radiobutton(window, text='Oval Result', variable=func, value="oval_result")
oval_button.pack()
sine_button = tk.Radiobutton(window, text='Sine Result', variable=func, value="sine_result")
sine_button.pack()

quantity_entry = tk.Entry(window, textvariable=quantity, font=('Arial', 14))
quantity_entry.pack()
quantity.set("1000")

label = tk.Label(window, textvariable=func)
label.pack()

generate_button = tk.Button(window, text='Generate!', font=('Arial', 12), width=10, height=1, command=generate_json)
generate_button.pack()

window.mainloop()

