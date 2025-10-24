# pyCompile by qromatic
# 10 / 23 / 25
# V1

import os
import subprocess
from pathlib import Path
import time
import sys

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

print('Python to EXE Compiler Utility')
print()
time.sleep(0.8)
print('This tool allows you to convert Python scripts into standalone executable files (.exe), enabling them to run on systems that do not have Python installed.')
time.sleep(2.5)
print('Please note: because this utility relies on PyInstaller, it requires Python to be installed on your system in order to function correctly.')
print()
time.sleep(3)

while True:
    checkPython = input('Do you have Python installed (y/n): ').strip().lower()
    if checkPython == 'y':
        print('Perfect, continuing...')
        time.sleep(0.5)
        clearTerminal()
        break

    elif checkPython == 'n':
        print('Let`s change that...')
        installMethod = input('Do you prefer Microsoft Store or the official Website? Please input a M for Microsoft Store or P for the Python Website: ').strip().lower()
        if installMethod == 'm':
            print('https://apps.microsoft.com/detail/9PNRBTZXMB4Z')
            while True:
                installDone = input('Once you´re done input (y): ').strip().lower()
                if installDone == 'y':
                    break
                else:
                    print('Input not recognized // Only y!')
                    continue
        elif installMethod == 'p':
            print('https://python.org/downloads/')
            while True:
                installDone = input('Once you´re done input (y): ').strip().lower()
                if installDone == 'y':
                    break
                else:
                    print('Input not recognized // Only y!')
                    continue
            break
        else:
            print('Input not recognized // Only m/p!')

print(r'                                        __  _          ')  
print(r'      ____ __________  ____ ___  ____ _/ /_(_)____     ')  
print(r'     / __ `/ ___/ __ \/ __ `__ \/ __ `/ __/ / ___/     ')  
print(r'    / /_/ / /  / /_/ / / / / / / /_/ / /_/ / /__       ')  
print(r'    \__, /_/   \____/_/ /_/ /_/\__,_/\__/_/\___/       ')  
print(r'      / /                                              ') 
print(r'     /_/       python to exe compiler                  ')
print()

scriptPath = input('Please list the full path to the script: ')

exeDestination = Path.home() / 'Downloads'
print(f'Executable will be saved to: {exeDestination}')
time.sleep(0.4)

print('installing pyinstaller...')
time.sleep(0.2)
installPyinstaller = [
    'pip',
    'install',
    'pyinstaller'
]

try:
    subprocess.run(installPyinstaller, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print('PyInstaller was successfully installed!')
except subprocess.CalledProcessError as e:
    print(f'error: {e}')


print('compiling your script now...')
compileScript = [
    'pyinstaller',
    '--onefile',
    scriptPath,
    '--distpath',
    exeDestination
]

time.sleep(0.5)

try:
    subprocess.run(compileScript, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f'Script was successfully compiled to: {exeDestination}!')
except subprocess.CalledProcessError as e:
    print(f'error: {e}')

time.sleep(0.5)

print()
print('- optional cleanup -')
print()

time.sleep(0.5)

while True:

    finishCleanUp = input('uninstall PyInstaller (y/n): ').strip().lower()
    if finishCleanUp == 'y':
        print('removing PyInstaller...')
        uninstallPyInstaller = [
            'pip',
            'uninstall',
            'pyinstaller',
            '-y'
        ]

        try:
            subprocess.run(uninstallPyInstaller, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print('successfully removed PyInstaller')
        except subprocess.CalledProcessError as e:
            print(f'error: {e}')

        print('exiting...')
        time.sleep(0.4)
        sys.exit()

    elif finishCleanUp == 'n':
        print('PyInstaller will remain on your system!')
        print('exiting...')
        time.sleep(0.2)
        sys.exit()

    else:
        print('Input not recognized // Only y/n!')
        continue