import time
import webbrowser

print('This program starts at', time.ctime())

for i in range(3):
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=qcnUDxocQko&index=1&list=PLUDB6Ztpgw8ggPKzWUvRFy2ed2yf3E3Ik')
    