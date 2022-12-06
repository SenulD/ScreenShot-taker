import time
import random

print()
import pyautogui
import tkinter as tk

def screenshot ():

    Name = random.randint(1000000,(1000*100000))
    Name = r'C:\Users\Senul\Desktop\Screen Shot App\SceenShots/{}.png'.format(Name)
    time.sleep(0.5)
    img = pyautogui.screenshot(Name)
    #img.show()

#screenshot()

main = tk.Tk()
main.title('ScreenShot taker')
frame = tk.Frame(main)
main.geometry("400x450")
frame.pack()

Header = tk.Label(text = "Fast ScreenShots", fg = "blue", font = "Castellar",pady = 10
).place(x = 120,y = 0)


button = tk.Button(frame, text ="Take ScreenShot", command = screenshot)

button.pack(padx=15, pady=40)



close = tk.Button(
    frame,
    text= "Quit",
    command = quit,
    fg ='red')
 

close.pack(pady=(270, 0))

main.mainloop()
