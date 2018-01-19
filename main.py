import argparse
import pyscreenshot as ImageGrab
import requests
import webbrowser

from bs4 import BeautifulSoup
from ocr import ProcessTextFromImage

def main():
    # ---------- All for Question ----------
    questionBox=(110,170,450,330) # X1,Y1,X2,Y2
    CapturePicture(questionBox, 'images/question.png')
    
    # Process the question image
    questionArgs = CreateCVArgs('images/question.png')
    questionWords = ProcessTextFromImage(questionArgs).split()
    question = ' '.join(word for word in questionWords)
    # print(question)

    DoQuestionAnalysis(question)

    # ---------- All for answers ----------
    answersBox=(110,350,450,550) # X1,Y1,X2,Y2
    CapturePicture(answersBox, 'images/answers.png')

    # Process the answers image
    answerArgs = CreateCVArgs('images/answers.png')
    answers = ProcessTextFromImage(answerArgs).split('\n')
    answers = [x for x in answers if x != '']
    # print(answers)

    # Get hit count for each of the three answers
    query1 = FormulateAnswersSearch(question, answers[0])
    results1 = FindResultsCount(query1)
    # print(query1)
    # DoQuestionAnalysis(query1)

    query2 = FormulateAnswersSearch(question, answers[1])
    results2 = FindResultsCount(query2)
    # DoQuestionAnalysis(query2)

    query3 = FormulateAnswersSearch(question, answers[2])
    results3 = FindResultsCount(query3)
    # DoQuestionAnalysis(query3)

    print("\"%s\" : %s" % (answers[0], results1))
    print("\"%s\" : %s" % (answers[1], results2))
    print("\"%s\" : %s" % (answers[2], results3))


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

# PURPOSE: Create the query string for question + answer
# INPUTS: question: the HQ question
#         answer: the HQ answer choice
# RETURNS: the string of: question + " + answer + "
def FormulateAnswersSearch(question, answer):
    return question + " “" + answer + "”"

# PURPOSE: finds the result count of a google query
# INPUTS: query: the query we want the result count for
# RETURNS: text of the number of hits
def FindResultsCount(query):
    r = requests.get('http://www.google.com/search', 
                        params={'q':query})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.find('div',{'id':'resultStats'}).text
  
if __name__== "__main__":
    main()