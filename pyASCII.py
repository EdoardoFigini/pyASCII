from PIL import Image
import sys
from math import floor, ceil

#charArray = 'Ñ@#W$9876543210?!abc;:+=-,._ '
#charArray = ' _.,-=+:;cba!?0123456789$W#@Ñ'
charArray = [' ', '.', ',', '_', ':',';', '+', '*', '?', '%', 'S', '#', '@']

DIMH=int(sys.argv[2])

def load(img):
  im = Image.open(img).convert('RGBA')
  im = im.resize((DIMH, int(im.size[1]*(DIMH/im.size[0]))), Image.NEAREST)
  pix = im.load() 
  return im, pix


def brightness(pix):
  return floor((0.2126*pix[0]+0.7152*pix[1]+0.0722*pix[2]))*ceil(pix[3]/255)


def map(pix, maxbr=255):  
  return floor((brightness(pix)/maxbr)*(len(charArray)-1))


def getmaxbr(img):
  maxbr=0
  for y in range(0, img[0].size[1]):
    for x in range(0, img[0].size[0]):
      if(brightness(img[1][x,y])>maxbr):
        maxbr=brightness(img[1][x, y])
  return maxbr


def printchars(img):
  maxbr=getmaxbr(img)
  for y in range(0, img[0].size[1]):
    for x in range(0, img[0].size[0]):
      print(charArray[map(img[1][x, y], maxbr)], end=' ')
    print()
      

def main():  
  printchars(load(sys.argv[1]))
  #print(charArray)


if __name__ == '__main__':
  main()
