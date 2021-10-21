import webbrowser
import pyautogui
import time

pyautogui.alert("A sua área de estudo esta inicializando, aguarde...")

time.sleep(3)

# Email
webbrowser.open("https://outlook.live.com/mail/inbox")
time.sleep(3)
# Abre plataforma da Digital Innovation One
webbrowser.open("https://web.digitalinnovation.one/home")
time.sleep(5)

# Abre a plataforma da mesttra
webbrowser.open("https://github.com/")
time.sleep(4)

# Abrir VS Code
pyautogui.hotkey("winleft")
pyautogui.write("Visual")
time.sleep(1)
pyautogui.press("enter")
time.sleep(3)

pyautogui.alert("A sua área de estudo esta Pronta!!!")
