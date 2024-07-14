from tkinter import *
from PIL import ImageTk
import return_words_list as rwl
import html_donwloader as hd
import shot
import requests
import pytesseract
from PIL import Image,ImageTk
import time

#Variable
main_win = Tk()
up_social_credit = ImageTk.PhotoImage(file="Picture/up_social_credit.jpg")
down_social_credit = ImageTk.PhotoImage(file="Picture/down_social_credit.jpg")

WINDOWS_WIDTH = 1200
WINDOWS_HEIGHT = 450
WINDOWS_TITLE = "Please Enter URL: (Process may take a min please wait)"
LANGUAGE_TEXT = "Language:"
SUBMIT_BUTTON = "SUBMIT"
CANT_ACCESS = "UNACCESSIBLE"
list_words = "Words In the website"
count = 0

SCORE = 0
RED_SCORE = 100
ORANGE_SCORE = 20
YELLOW_SCORE = 10


def take_url():
    global list_words
    global SCORE
    global count
    state.config(text = "")
    list_all_words.config(text = "")
    social_credit_socre.config(text = "")
    Place_image.config(image =None)
    SCORE = 0
    RECEIVED_URL = URL_enter.get()
    URL_enter.delete(0, "end")
    if RECEIVED_URL[:7] != "http://":
        if RECEIVED_URL[:8] != "https://":
            RECEIVED_URL = "http://" + RECEIVED_URL
    print(RECEIVED_URL)
    try:
        requests.get(RECEIVED_URL)
    except:
        state.config(text = CANT_ACCESS)
        state.pack()
        return
    else:
        word_list = []
        list_words = ""
        HTML_TEXT_CHINESE_WORD = hd.take_html(RECEIVED_URL)
        shot.screenshooter(RECEIVED_URL)
        img = Image.open("screenshot.png")

        text1 = pytesseract.image_to_string(img, "chi_tra")
        text2 = pytesseract.image_to_string(img, "chi_sim")
        
        if HTML_TEXT_CHINESE_WORD == None:
            text = text1 + text2
        else:
            text = text1 + text2 + HTML_TEXT_CHINESE_WORD

        text = text.replace(" ","")

        for order in range(0, 255):
            text = text.replace(chr(order), "")

        for word in rwl.red_list:
            if word in text:
                word_list.append(word)
                SCORE += RED_SCORE
        for word in rwl.orange_list:
            if word in text:
                word_list.append(word)
                SCORE += ORANGE_SCORE
        for word in rwl.yellow_list:
            if word in text:
                word_list.append(word)
                SCORE += YELLOW_SCORE
        for word in word_list:
            count += 1
            list_words += word + ","
            if count % 10 == 0:
                list_words += "\n"
        if SCORE <= 0:
            Place_image.config(image = up_social_credit)
        else:
            Place_image.config(image = down_social_credit)

        state.config(text = "IS DONE")
        list_all_words.config(text = list_words)
        social_credit_socre.config(text = ("Totle Score: ", str(SCORE)))

#access half of user screen info
left = (main_win.winfo_screenwidth()//2)
top = (main_win.winfo_screenheight()//2)

#Windowns setting
main_win.geometry(f"{WINDOWS_WIDTH}x{WINDOWS_HEIGHT}+{left - (WINDOWS_WIDTH // 2)}+{top - (WINDOWS_HEIGHT// 2)}")
main_win.resizable(0,0)
main_win.title("CCP URL CENSORSHIP")
main_win.iconbitmap("Picture/ccp_icon.ico")
main_win.config(background = "#646464")

windows_title = Label(main_win, text=WINDOWS_TITLE,bg="#646464",
                      fg = "white",font=("微軟正黑體",25))
windows_title.pack()


URL_enter = Entry(main_win, width=45,font=("微軟正黑體",25))
URL_enter.pack()

submit_button = Button(text = SUBMIT_BUTTON,bg="#6e6e6e",
                      fg = "white",font=("微軟正黑體",25),command = take_url)
submit_button.pack()

state = Label(text = "",bg="#646464",
                      fg = "red",font=("微軟正黑體",25))
state.pack()

list_all_words = Label(bg="#646464",
                      fg = "white",font=("微軟正黑體",12))
list_all_words.pack()


social_credit_socre = Label(text =(""),bg = "#646464",
                      fg = "red",font=("微軟正黑體",30))
social_credit_socre.pack()

Place_image = Label(bg = "#646464")
Place_image.place(x= 970, y = 320)


main_win.mainloop()