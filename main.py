import argparse
import pyscreenshot as ImageGrab
import webbrowser

from ocr import ProcessTextFromImage

def main():
    # ---------- All for Question ----------
    questionBox=(60,270,500,430) # X1,Y1,X2,Y2
    CapturePicture(questionBox, 'images/question.png')
    
    # Process the question image
    questionArgs = CreateCVArgs('images/question.png')
    questionWords = ProcessTextFromImage(questionArgs).split()
    question = ' '.join(word for word in questionWords)
    print(question)

    # DoQuestionAnalysis(text)

    # ---------- All for answers ----------
    answersBox=(30,470,510,790) # X1,Y1,X2,Y2
    CapturePicture(answersBox, 'images/answers.png')

    # Process the answers image
    answerArgs = CreateCVArgs('images/answers.png')
    answers = ProcessTextFromImage(answerArgs).split('\n')
    answers = [x for x in answers if x != '']
    print(answers)


def DoQuestionAnalysis(question):
    webbrowser.open("https://www.google.com/search?q=" + question)

# PURPOSE: Capture and save a picture for the given box and filename
# INPUTS: box: the coordinates of the screenshot we want to take
#         filename: the name we want to save the screenshot as
# RETURNS: nothing
def CapturePicture(box, filename):
    im=ImageGrab.grab(box) # X1,Y1,X2,Y2
    im.save(filename)

# PURPOSE: Create the list of args to be used for image analysis
# INPUTS: filename: the name of the image we want to parse
# RETURNS: the list of args to be used for image analysis
def CreateCVArgs(filename):
    # Parse arguments from the call 
    # (but realistically just add them all here and none in call)
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", default=filename, 
        help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh",
        help="type of preprocessing to be done")
    return vars(ap.parse_args())
  
if __name__== "__main__":
    main()