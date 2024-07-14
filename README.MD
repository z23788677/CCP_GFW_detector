Statement
===

### This project doesn't mean to political propaganda, this is aiming for fun and learning.
### Wish you get offended by it.

CCP_GFW_Detector
===

This is a program with a GUI, allowing users to input a URL link to the program. The program will access any single Chinese characters from the website HTML content. Since some websites use images more than text, once the program accesses the HTML content, it'll also process images for Chinese characters. It doesn't matter if the website uses simplified or traditional Chinese, the program won't miss any of them.

What is GFW
===
### Great Fire Wall

The Chinese government has a GFW policy. Generally speaking, this means that Chinese people can't access websites banned by the government, such as YouTube and Facebook. Since some website content is something that the CCP doesn't want Chinese people to see, this is the aim of the project.

The "word_list" Folder
===

I listed a lot of words that the CCP may not like, and rated them by "Red", "Orange", and "Yellow".

- **Red**: Words that MUST BE BANNED
- **Orange**: Words that are OKAY to use, but as less as possible
- **Yellow**: Words that are between safe and Orange words

These DAT files can be edited.

Some of the Python files have this, please ignore them as they are for testing during the developing process.

` if __name__ == "__main__":
    something... `

Please Notice
===
You may have to Install Firefox Befoce running the program.
Since the GUI using "微軟正黑體", if you don't have this font in your local machine, the program may not running properly.
