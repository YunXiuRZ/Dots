import json
import random
import math

def linear_result(x, y):
    return (x * 5 / 4 + y) >= 1000

def rectangle_result(x, y):
    return 1200 >= x and x >= 400 and 800 >= y and y >= 200

def quadratic_result(x, y):
    return  ((x-1200)**2) / 1800 + 200 - y >= 0

def oval_result(x, y):
    return ((x - 400)**2 + (y - 500)**2)**0.5 + ((x - 1200)**2 + (y - 500)**2)**0.5 <= 1000

def sine_result(x, y):
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


data = generate_dataset(sine_result, 1000)
with open("dots.json", 'w') as file:
    json.dump(data, file)