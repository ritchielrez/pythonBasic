import os

def undimbrightness():
    with open('currentbrightness.txt', 'r') as prevbrightness:
        prevbrightness = prevbrightness.read()

        os.system(f'xbacklight -set {prevbrightness}')

