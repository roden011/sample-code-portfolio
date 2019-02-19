from ezgraphics import *
from imgProcTools import *

'''
This program requires that the image files be formatted as bitmap (or raster) images.  Each pixel has a distinct location in a 2 dimensional matrix (x,y plot or grid) as well as a r(red), g(green),b(blue) color value of 0-255.     

https://en.wikipedia.org/wiki/Raster_graphics
'''
def main():
    print('-'*75)
    print("Welcome to the CSC 131 Image Processing Tools Application!!!")
    print()
    print("You will be asked to enter the name of an image file that you would like to be displayed (must gif or png format).\nNext you will be prompted to select a processing option from the menu below.")
    print()
    imgFile = input("Please enter the name of the image file you wish to display: ")
    print()
    
    # Load the image from the file and display it in a window.
    theImg = GraphicsImage(imgFile)
    win = GraphicsWindow()
    win.setTitle("CSC 131 Image Processing Tool: " + imgFile)
    canvas = win.canvas()
    canvas.drawImage(theImg)
    done = False
    
    # When the graphics window displays "not responding", it is because of a threading issue and will 
    # not affect our program.  Multithreading is an advanced topic that will be addressed in later courses. 
    
    while not done :
        # Prompt the user for the type of processing.
        print("How should the image be processed? ")
        print("1  - create image negative")
        print("2  - adjust brigthness")
        print("3  - flip vertically")
        print("4  - rotate to the left")
        print("5  - apply sepia filter")
        print("6  - black/white")
        print("7  - smooth")
        print("8  - detect edge")
        print("9  - shrink")
        print("10 - greyscale")
        print("11 - Negative to Color")
        print("12 - Histogram Eq")
        print("13 - RGB HistoEQ")
        print("14 - Rotate")
        print("15 - Warp")
        print("16 - quit")
     
        response = int(input("Enter your choice: "))
        print()
              
     # Process the image
        if response == 1 :
            option = "Negative"
            newImg = createNegative(theImg)
        elif response == 2 :
            option = "Adjust Brightness"
            amount = float(input("Adjustment between -1.0 and 1.0: "))
            newImg = adjustBrightness(theImg, amount)
        elif response == 3 :
            option = "Flip Vertically"
            newImg = flipVertically(theImg)
        elif response == 4 :
            option = "Rotate Left"
            newImg = rotateLeft(theImg)
        elif response == 5 :
            option = "Sepia"
            newImg = sepiaFilter(theImg) 
        elif response == 6:
            option = "Black/White"
            newImg = blackWhite(theImg)
        elif response == 7:
            option = "Smooth"
            newImg = smooth(theImg)
        elif response == 8:
            option = "Detect Edge"
            newImg = edgeDetection(theImg)
        elif response == 9:
            option = "Shrink"
            newImg = shrink(theImg)
        elif response == 10:
            option = "Greyscale"
            newImg = greyScale(theImg)
        elif response == 11:
            option = "Neg to Color"
            newImg = createNegative(theImg)
        elif response == 12:
            option = "Histogram EQ"
            newImg = histoEqual(theImg)
        elif response == 13:
            option = "RGB Histogram EQ"
            newImg = colorHistoEqual(theImg)
        elif response == 14:
            theta = int(input('How many degrees to rotate?: '))
            option = "Img Rotation"
            newImg = rotateImage(theImg, theta)
        elif response == 15:
            option = "Img Warping"
            newImg = warpImage(theImg)
     
       # win.quit() deystroys all graphic window objects and ends the application
        if response == 16 :
            win.quit()  
            done = True
            
        # If quit is not selected, display the processed image in a new window.
        else :
            newWin = GraphicsWindow()
            newCanvas = newWin.canvas()         
            newWin.setTitle("Image Processing Tool: " + imgFile + " (" + option + ")")
            newCanvas.drawImage(newImg)
            badInput = True
            saveFile = input("Would you like to save the new image? [Y/n]: ")
            while badInput:
                if saveFile == "Y" or saveFile == "n":
                    badInput = False                    
                else:                    
                    saveFile = input("Invalid input: Please enter [Y/n]: ")
            if saveFile == "Y":
                name = input("What would you like to name you file? ")
                newImg.save(name + ".gif")   
            
        
main()
