from tkinter import *
from PIL import ImageTk
import return_words_list as rwl
import html_donwloader as hd
import shot



#Variable
main_win = Tk()

WINDOWS_WIDTH = 1200
WINDOWS_HEIGHT = 350
WINDOWS_TITLE = "Please Enter URL: "
LANGUAGE_TEXT = "Language:"
SUBMIT_BUTTON = "SUBMIT"
RESULT = ["BANNED NOW", "CONSIDER TO BAN", "SAFE"]
COMMIE_FLAG_PATH = ImageTk.PhotoImage(file = "Picture/commie_flag.png")
SUN_CAN_SETS_EMPIRE_FLAG_PATH = ImageTk.PhotoImage(file = "Picture/sun_can_sets_empire_flag.png")
NEW_LGBT_CHINA_FLAG_PATH = ImageTk.PhotoImage(file = "Picture/new_lgbt_china_flag.png")

SCORE = 0
RED_SCORE = 100
ORANGE_SCORE = 20
YELLOW_SCORE = 10

BAN_STATE = {1:"BANNED", 2:"CONSIDER TO", 3:"NO ANY WORD DETECTED"}

#command action
    #Language
def chinese_sim():
    WINDOWS_TITLE = "请输入连结: "
    LANGUAGE_TEXT = "语言:"
    SUBMIT_BUTTON = "提交"
    windows_title.config(text = WINDOWS_TITLE)
    language_label.config(text = LANGUAGE_TEXT)
    submit_button.config(text = SUBMIT_BUTTON)
    language_label.place(x = 750, y = 290)
def english():
    WINDOWS_TITLE = "Please Enter URL: "
    LANGUAGE_TEXT = "Language:"
    SUBMIT_BUTTON = "SUBMIT"
    windows_title.config(text = WINDOWS_TITLE)
    language_label.config(text = LANGUAGE_TEXT)
    submit_button.config(text = SUBMIT_BUTTON)
    language_label.place(x = 680, y = 290)
def chinese_tra():
    WINDOWS_TITLE = "請輸入連結: "
    LANGUAGE_TEXT = "語言:"
    SUBMIT_BUTTON = "提交"
    windows_title.config(text = WINDOWS_TITLE)
    language_label.config(text = LANGUAGE_TEXT)
    submit_button.config(text = SUBMIT_BUTTON)
    language_label.place(x = 750, y = 290)
def take_url():
    global SCORE
    SCORE = 0
    RECEIVED_URL = URL_enter.get()
    URL_enter.delete(0, "end")
    if RECEIVED_URL[:7] != "http://":
        if RECEIVED_URL[:8] != "https://":
            RECEIVED_URL = "http://" + RECEIVED_URL
    print(RECEIVED_URL)
    HTML_TEXT_CHINESE_WORD = hd.take_html(RECEIVED_URL)
    for word in rwl.red_list:
        if word in HTML_TEXT_CHINESE_WORD:
            SCORE += RED_SCORE
            print("該網站檢測到政治敏感詞",word)
    for word in rwl.orange_list:
        if word in HTML_TEXT_CHINESE_WORD:
            SCORE += ORANGE_SCORE
            print("該網站檢測到政治敏感詞",word)
    for word in rwl.yellow_list:
        if word in HTML_TEXT_CHINESE_WORD:
            SCORE += YELLOW_SCORE
            print("該網站檢測到政治敏感詞",word)

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
commie_flag_button.place(x = 1070, y = 290)

sun_can_sets_empire_flag_button = Button(image = SUN_CAN_SETS_EMPIRE_FLAG_PATH, command = english)
sun_can_sets_empire_flag_button.place(x = 950, y = 290)

new_lgbt_china_flag_button = Button(image = NEW_LGBT_CHINA_FLAG_PATH, command=chinese_tra)
new_lgbt_china_flag_button.place(x =830, y = 290)

language_label = Label(text=LANGUAGE_TEXT,bg="#646464",
                      fg = "white",font=("微軟正黑體",20))
language_label.place(x = 680, y = 290)

URL_enter = Entry(main_win, width=45,font=("微軟正黑體",25))
URL_enter.pack()

submit_button = Button(text = SUBMIT_BUTTON,bg="#6e6e6e",
                      fg = "white",font=("微軟正黑體",25),command = take_url)
submit_button.pack()

main_win.mainloop()
