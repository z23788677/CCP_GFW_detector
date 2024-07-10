from tkinter import *
from PIL import ImageTk
import return_words_list as rwl
import html_donwloader as hd
import shot
import requests

#Variable
main_win = Tk()

WINDOWS_WIDTH = 1200
WINDOWS_HEIGHT = 450
WINDOWS_TITLE = "Please Enter URL: "
LANGUAGE_TEXT = "Language:"
SUBMIT_BUTTON = "SUBMIT"
CANT_ACCESS = "UNACCESSIBLE"
COMMIE_FLAG_PATH = ImageTk.PhotoImage(file = "Picture/commie_flag.png")
SUN_CAN_SETS_EMPIRE_FLAG_PATH = ImageTk.PhotoImage(file = "Picture/sun_can_sets_empire_flag.png")
NEW_LGBT_CHINA_FLAG_PATH = ImageTk.PhotoImage(file = "Picture/new_lgbt_china_flag.png")

SCORE = 0
RED_SCORE = 100
ORANGE_SCORE = 20
YELLOW_SCORE = 10

#command action
    #Language
def chinese_sim():
    WINDOWS_TITLE = "请输入连结: "
    LANGUAGE_TEXT = "语言:"
    SUBMIT_BUTTON = "提交"
    CANT_ACCESS = "无法访问"
    windows_title.config(text = WINDOWS_TITLE)
    language_label.config(text = LANGUAGE_TEXT)
    state.config(text = CANT_ACCESS)
    submit_button.config(text = SUBMIT_BUTTON)
    language_label.place(x = 750, y = 390)
def english():
    WINDOWS_TITLE = "Please Enter URL: "
    LANGUAGE_TEXT = "Language:"
    SUBMIT_BUTTON = "SUBMIT"
    CANT_ACCESS = "UNACCESSIBLE"
    windows_title.config(text = WINDOWS_TITLE)
    language_label.config(text = LANGUAGE_TEXT)
    state.config(text = CANT_ACCESS)
    submit_button.config(text = SUBMIT_BUTTON)
    language_label.place(x = 680, y = 390)
def chinese_tra():
    WINDOWS_TITLE = "請輸入連結: "
    LANGUAGE_TEXT = "語言:"
    SUBMIT_BUTTON = "提交"
    CANT_ACCESS = "無法訪問"
    windows_title.config(text = WINDOWS_TITLE)
    language_label.config(text = LANGUAGE_TEXT)
    submit_button.config(text = SUBMIT_BUTTON)
    state.config(text = CANT_ACCESS)
    language_label.place(x = 750, y = 390)
def take_url():
    global SCORE
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
        HTML_TEXT_CHINESE_WORD = hd.take_html(RECEIVED_URL)
        for word in rwl.red_list:
            if word in HTML_TEXT_CHINESE_WORD:
                SCORE += RED_SCORE
        for word in rwl.orange_list:
            if word in HTML_TEXT_CHINESE_WORD:
                SCORE += ORANGE_SCORE
        for word in rwl.yellow_list:
            if word in HTML_TEXT_CHINESE_WORD:
                SCORE += YELLOW_SCORE
        
        shot.screenshooter(RECEIVED_URL)
        website_image = "screenshot.png"



        print("該網站分數為:",SCORE)

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
                      fg = "white",font=("微軟正黑體",30))
windows_title.pack()

commie_flag_button = Button(image=COMMIE_FLAG_PATH, command=chinese_sim)
commie_flag_button.place(x = 1070, y = 390)

sun_can_sets_empire_flag_button = Button(image = SUN_CAN_SETS_EMPIRE_FLAG_PATH, command = english)
sun_can_sets_empire_flag_button.place(x = 950, y = 390)

new_lgbt_china_flag_button = Button(image = NEW_LGBT_CHINA_FLAG_PATH, command=chinese_tra)
new_lgbt_china_flag_button.place(x =830, y = 390)

language_label = Label(text=LANGUAGE_TEXT,bg="#646464",
                      fg = "white",font=("微軟正黑體",20))
language_label.place(x = 680, y = 390)

URL_enter = Entry(main_win, width=45,font=("微軟正黑體",25))
URL_enter.pack()

submit_button = Button(text = SUBMIT_BUTTON,bg="#6e6e6e",
                      fg = "white",font=("微軟正黑體",25),command = take_url)
submit_button.pack()

state = Label(text = "",bg="#646464",
                      fg = "red",font=("微軟正黑體",25))

main_win.mainloop()
