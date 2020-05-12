from PIL import Image
from gtts import gTTS
import pytesseract

#設置tesseract.exe安裝路徑
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

Img_path='1.png'
Detect_Text=pytesseract.image_to_string(Img_path) #偵測文字
print('內容:\n'+Detect_Text)

Convert_Sound=gTTS(Detect_Text,lang='en') #轉為音檔
Convert_Sound.save('Sound.mp3') #儲存音檔