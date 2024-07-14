from PIL import Image
import shot
import pytesseract


if __name__ == "__main__":
    shot.screenshooter("https://www.epochtimes.com")
    img = Image.open("screenshot.png")

    text1 = pytesseract.image_to_string(img, "chi_tra")
    text2 = pytesseract.image_to_string(img, "chi_sim")
    text = text1 + text2

    text = text.replace(" ","")
    print(text)
