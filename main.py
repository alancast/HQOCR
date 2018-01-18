import argparse
from ocr import ProcessImage

def main():
    # Parse arguments from the call
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, 
        help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh",
        help="type of preprocessing to be done")
    args = vars(ap.parse_args())

    # Process the image
    ProcessImage(args)
  
if __name__== "__main__":
    main()