import os
import subprocess
from rofi import Rofi

if __name__ == '__main__':
    r = Rofi(rofi_args=['-i', '-dpi', '1.25'])

    options = [' Shutdown', ' Reboot', ' Logout', 'quit']

    option = 0

    option, key = r.select('What do you want to do', options)

    if(key == -1):
        exit(1)

    if(option == -1):
        exit(1)

    if(option == 0):
        os.system('shutdown now')
    elif(option == 1):
        os.system('reboot')
    else:
        os.system('systemctl restart sddm')





