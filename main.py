import argparse
import pyscreenshot as ImageGrab
import webbrowser

from ocr import ProcessTextFromImage

def main():
    CaptureQuestionPicture()

    # Parse arguments from the call
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", default="images/screenshot.png", 
        help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh",
        help="type of preprocessing to be done")
    args = vars(ap.parse_args())

    # Process the image
    text = ProcessTextFromImage(args)
    print(text)

    DoQuestionAnalysis(text)

def DoQuestionAnalysis(question):
    webbrowser.open("https://www.google.com/search?q=" + question)

def CaptureQuestionPicture():
    im=ImageGrab.grab(bbox=(60,270,500,430)) # X1,Y1,X2,Y2
    im.save('images/screenshot.png')
  
if __name__== "__main__":
    main()