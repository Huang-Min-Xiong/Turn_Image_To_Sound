from gtts import gTTS
import pytesseract

#設置tesseract.exe安裝路徑
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

Img_path = r'Img\1.png'
Detect_Text = pytesseract.image_to_string(Img_path) #偵測文字
print('內容:\n'+Detect_Text)

with open(r"Detect_Text\Detect_Text.txt","w") as f:
    f.write(Detect_Text) #寫入文字檔
    print('已寫入文字檔!')

Convert_Sound = gTTS(Detect_Text,lang='en') #轉為音檔
Convert_Sound.save(r'Sound\Sound.mp3') #儲存音檔
print('已存成音檔!')
