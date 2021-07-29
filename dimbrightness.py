import os

def dimbrightness():
    os.system('xbacklight -get > prevbrightness.txt')

    os.system('xbacklight -set 0')        

