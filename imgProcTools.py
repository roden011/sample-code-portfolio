
# CIS 131 Spring 2017
# Image processing toolkit to be developed
from ezgraphics import GraphicsImage
from statistics import median
import math

## Creates and returns a new image that is the negative of the original. 
#  @param image the source image
#  @return the new negative image 
#
def createNegative(image) :
   width = image.width()
   height = image.height()
  
   # Create a new image that is the same size as the original.
   newImage = GraphicsImage(width, height)
   for row in range(height) :
      for col in range(width) :

         # Get the color of the pixel in the original image.
         red = image.getRed(row, col)
         green = image.getGreen(row, col)
         blue = image.getBlue(row, col)
      
         # Filter the pixel.
         newRed = 255 - red
         newGreen = 255 - green
         newBlue = 255 - blue
  
         # Set the pixel in the new image to the new color.
         newImage.setPixel(row, col, newRed, newGreen, newBlue)

   return newImage
   
   
def greyScale(image):
    width = image.width()
    height = image.height()
    
    newImage = GraphicsImage(width, height)
    for row in range(height):
        for col in range(width):
            red = image.getRed(row, col)
            green = image.getGreen(row, col)
            blue = image.getBlue(row, col)
        
            # Filter the pixel.
            
            
            newRed = int(0.21 * red)
            newGreen = int(0.72 * green)
            newBlue = int(0.07 * blue)
            
            
            grey = newRed + newGreen + newBlue
            
            # Set the pixel in the new image to the new color.
            newImage.setPixel(row, col, grey, grey, grey)

    return newImage
   

## Creates and returns a new image in which the brightness levels of
#  all three color components are adjusted by a given percentage.
#  @param image the source image
#  @param amount the percentage by which to adjust the brightness
#  @return the new image
#
def adjustBrightness(image, amount) :
   width = image.width()
   height = image.height()
  
   # Create a new image that is the same size as the original.
   newImage = GraphicsImage(width, height)
   for row in range(height) :
      for col in range(width) :

         # Get the color of the pixel in the original image.
         red = image.getRed(row, col)
         green = image.getGreen(row, col)
         blue = image.getBlue(row, col)
      
         # Adjust the brightness and cap the colors.
         newRed = int(red + red * amount)
         if newRed > 255 :
            newRed = 255
         elif newRed < 0 :
            newRed = 0
         newGreen = int(green + green * amount)
         if newGreen > 255 :
            newGreen = 255
         elif newGreen < 0 :
            newGreen = 0
         newBlue = int(blue + blue * amount)
         if newBlue > 255 :
            newBlue = 255
         elif newBlue < 0 :
            newBlue = 0
      
         # Set the pixel in the new image to the new color.
         newImage.setPixel(row, col, newRed, newGreen, newBlue)

   return newImage


## Creates and returns a new image that results from flipping an original 
#  image vertically.
#  @param image the source image
#  @return the new vertically flipped image
#
def flipVertically(image) :  
   # Create a new image that is the same size as the original.
   width = image.width()
   height = image.height()
   newImage = GraphicsImage(width, height)
  
   # Flip the image vertically.
   newRow = height - 1
   for row in range(height) :
      for col in range(width) :
         newCol = col
         pixel = image.getPixel(row, col)
         newImage.setPixel(newRow, newCol, pixel)
        
      newRow = newRow - 1      

   return newImage

## Rotates the image 90 degrees to the left.
#  @param image the image to be rotated
#  @return the new rotated image
# 
def rotateLeft(image) :
   # Create a new image whose dimensions are the opposite of the original.
   width = image.width()
   height = image.height()
   newImage = GraphicsImage(height, width)
  
   # Rotate the image.
   for row in range(height) :
      newCol = row
      for col in range(width) :
         newRow = col
         pixel = image.getPixel(row, col)
         newImage.setPixel(newRow, newCol, pixel)
        
   return newImage


## Creates and returns a new image filter by the sepia values
#  all three color components are adjusted by a given value.
def sepiaFilter(image):
   width = image.width()
   height = image.height()
  
   # Create a new image that is the same size as the original.
   newImage = GraphicsImage(width, height)
   for row in range(height) :
      for col in range(width) :

         # Get the color of the pixel in the original image.
         red = image.getRed(row, col)
         green = image.getGreen(row, col)
         blue = image.getBlue(row, col)
      
         # Filter the pixel.
         newRed = int((0.393*red) + (0.796*green) + (0.198*blue))
         if newRed > 255:
            newRed = 255
         newGreen = int((0.349*red) + (0.686*green) + (0.168*blue))
         if newGreen > 255:
            newGreen = 255         
         newBlue = int((0.272*red) + (0.534*green) + (0.131*blue))
         if newBlue > 255:
            newBlue = 255         
  
         # Set the pixel in the new image to the new color.
         newImage.setPixel(row, col, newRed, newGreen, newBlue)

   return newImage
"""
Creates and returns a new image that is the original image, but in black and white
@param image - the image to be turned black and white
@return the new image in black and white
"""
def blackWhite(image):
   width = image.width()
   height = image.height()
  
   # Create a new image that is the same size as the original.
   newImage = GraphicsImage(width, height)
   for row in range(height) :
      for col in range(width) :  
         
         # Get the color of the pixel in the original image.
         red = image.getRed(row, col)
         green = image.getGreen(row, col)
         blue = image.getBlue(row, col)  
         
         if red + blue + green >= 382:#if the intensity is >= half full intensity, the new pixel is set to full intensity(white)
            newRed = 255 
            newGreen = 255
            newBlue = 255
         else:                      #otherwise it is set to 0 intensity(black)
            newRed = 0 
            newGreen = 0
            newBlue = 0            
     
         # Set the pixel in the new image to the new color.
         newImage.setPixel(row, col, newRed, newGreen, newBlue)  
   return newImage
"""
enhances grainy images by setting each pixel to the median value of all the pixels around it
@param image - the image to be enhanced
@return the new enhanced image
"""
def smooth(image):
   width = image.width()
   height = image.height()
  
   # Create a new image that is the same size as the original.
   newImage = GraphicsImage(width, height)
   for row in range(1, height - 1) :
      for col in range(1, width - 1) :  
         #list of red values around the pixel
         reds = [image.getRed(row, col -1),
                 image.getRed(row, col+1),
                 image.getRed(row+1, col),
                 image.getRed(row-1, col),
                 image.getRed(row+1, col +1),
                 image.getRed(row+1, col-1),
                 image.getRed(row-1, col-1),
                 image.getRed(row-1, col+1)]
         #list of green values around the pixel
         greens = [image.getGreen(row, col -1),
                   image.getGreen(row, col+1),
                   image.getGreen(row+1, col),
                   image.getGreen(row-1, col),
                   image.getGreen(row+1, col +1),
                   image.getGreen(row+1, col-1),
                   image.getGreen(row-1, col-1),
                   image.getGreen(row-1, col+1)]
         #list of blue values around the pixel
         blues = [image.getBlue(row, col -1),
                  image.getBlue(row, col+1),
                  image.getBlue(row+1, col),
                  image.getBlue(row-1, col),
                  image.getBlue(row+1, col +1),
                  image.getBlue(row+1, col-1),
                  image.getBlue(row-1, col-1),
                  image.getBlue(row-1, col+1)]
         
         newRed = int(median(reds))#median value of the reds list
         newGreen = int(median(greens))#median value of the greens list
         newBlue = int(median(blues))#median value of the blues list
         
         # Set the pixel in the new image to the new color.
         newImage.setPixel(row, col, newRed, newGreen, newBlue) 
           
   return newImage
"""
creates a new image that highlights drastics changes in intensity from one pixel to the next
@params image-image to have the edges shown
@returns new image highlighting the edges
"""
def edgeDetection(image):
   width = image.width()
   height = image.height()
  
   # Create a new image that is the same size as the original.
   newImage = GraphicsImage(width, height)
   for row in range(1, height - 1) :
      for col in range(1, width - 1) :  
         
         reds = [image.getRed(row - 1, col - 1),
                 image.getRed(row, col - 1),
                 image.getRed(row + 1, col - 1),
                 image.getRed(row-1, col),
                 image.getRed(row+1, col),
                 image.getRed(row - 1, col + 1),
                 image.getRed(row, col + 1),
                 image.getRed(row + 1, col + 1)]
         #list of green values around the pixel
         greens = [image.getRed(row - 1, col - 1),
                 image.getGreen(row, col - 1),
                 image.getGreen(row + 1, col - 1),
                 image.getGreen(row-1, col),
                 image.getGreen(row+1, col),
                 image.getGreen(row - 1, col + 1),
                 image.getGreen(row, col + 1),
                 image.getGreen(row + 1, col + 1)]
         #list of blue values around the pixel
         blues = [image.getRed(row - 1, col - 1),
                 image.getBlue(row, col - 1),
                 image.getBlue(row + 1, col - 1),
                 image.getBlue(row-1, col),
                 image.getBlue(row+1, col),
                 image.getBlue(row - 1, col + 1),
                 image.getBlue(row, col + 1),
                 image.getBlue(row + 1, col + 1)]
                 
         aveIntensity = []        
         for x in range(8):
            aveIntensity.append((reds[x] + greens[x] + blues[x]) // 3)
            
         gX = -1 * (aveIntensity[0] + aveIntensity[2]) + (aveIntensity[5] + aveIntensity[7]) + (2 * aveIntensity[6]) - (2 * aveIntensity[1])
         gY = -1 * (aveIntensity[0] + aveIntensity[5]) + (aveIntensity[2] + aveIntensity[7]) + (2 * aveIntensity[4]) - (2 * aveIntensity[3])
         tG = int((gX**2 + gY**2)**.5)
         if tG >= 128:
            tG = 255
         else:
            tG = 0
         newImage.setPixel(row, col, tG, tG, tG)      
   return newImage
   
   
def shrink(image):
   width = image.width()
   height = image.height()  
   # Create a new image that is 1/4 the size as the original.
   newImage = GraphicsImage(width//2, height//2)   
   newRow = 0
   for row in range(0,height-1, 2) :
      newCol = 0
      for col in range(0,width-1, 2) : 
         # _ _    
         #|1|2|
         #|4|3|
         #-----This is the manner in which each pixel is evaluated each iteration, then increments by 2 in the col's and row's to evaluate the next grid square

         #list of red values in each grid
         reds = [image.getRed(row, col),
                 image.getRed(row, col+1),
                 image.getRed(row+1, col+1),
                 image.getRed(row+1, col)]
         #list of green values in each grid
         greens = [image.getGreen(row, col),
                   image.getGreen(row, col+1),
                   image.getGreen(row+1, col+1),
                   image.getGreen(row+1, col)]
         #list of blue values in each grid
         blues = [image.getBlue(row, col),
                  image.getBlue(row, col+1),
                  image.getBlue(row+1, col+1),
                  image.getBlue(row+1, col)]
         
         newRed = int(median(reds))#median value of the reds in each grid
         newGreen = int(median(greens))#median value of the green in each grid
         newBlue = int(median(blues))#median value of the blue in each grid
         
         # Set the pixel in the new image to the new color.
         newImage.setPixel(newRow, newCol, newRed, newGreen, newBlue)        
         newCol = newCol + 1
      newRow = newRow + 1   
   return newImage  
   
   
def histoEqual(image) :
    image = greyScale(image)
    width = image.width()
    height = image.height()
    newImage = GraphicsImage(width, height)
    histogram = []
    for i in range(256):
       histogram.append(0)
  
    for row in range(height) :
       for col in range(width) :
         r, g, b = image.getPixel(row, col)
         avgIntensity = (r + g + b)//3
         histogram[avgIntensity] += 1
        
    cdf = [] #cumulative distribution frequency
    eqHist = []
    for j in range(256):
        if j > 0:
            cdf.append(cdf[j-1] + histogram[j])
        else:
            cdf.append(histogram[j])
        eqHist.append(255 * cdf[j] // (width*height) )
        
    for row in range(height) :
       for col in range(width) :
         r, g, b = image.getPixel(row, col)
         avgIntensity = (r + g + b)//3
         newIntensity = eqHist[avgIntensity]
         newImage.setPixel(row, col, newIntensity, newIntensity, newIntensity)
                            
    return newImage
    
def colorHistoEqual(image):
    width = image.width()
    height = image.height()
    newImage = GraphicsImage(width, height)
    redHisto = []
    greenHisto = []
    blueHisto = []
    for i in range(256):
        redHisto.append(0)
        greenHisto.append(0)
        blueHisto.append(0)
        
    for row in range(height):
        for col in range(width):
            r, g, b = image.getPixel(row, col)
            redHisto[r] += 1
            greenHisto[g] += 1
            blueHisto[b] += 1
              
    redCDF = []
    greenCDF = []
    blueCDF = []
    redEQ = []
    greenEQ = []
    blueEQ = []
    for j in range(256):
        if j > 0:
            redCDF.append(redCDF[j-1] + redHisto[j])
            greenCDF.append(greenCDF[j-1] + greenHisto[j])
            blueCDF.append(blueCDF[j-1] + blueHisto[j])
        else:
            redCDF.append(redHisto[j])
            greenCDF.append(greenHisto[j])
            blueCDF.append(blueHisto[j])
        redEQ.append(255*redCDF[j] // (width * height))
        greenEQ.append(255*greenCDF[j] // (width * height))
        blueEQ.append(255*blueCDF[j] // (width * height))
        
    for row in range(height) :
       for col in range(width) :
         r, g, b = image.getPixel(row, col)
         newRed = redEQ[r]
         newGreen = greenEQ[g]
         newBlue = blueEQ[b]      
         newImage.setPixel(row, col, newRed, newGreen, newBlue)
    return newImage
            

def rotateImage(image, theta):
    width = image.width()
    height = image.height()
    newWidth = int((image.width()**2 + image.height()**2)**.5)
    newHeight =int((image.width()**2 + image.height()**2)**.5)
    newImage1 = GraphicsImage(newWidth, newHeight)
    newImage2 = GraphicsImage(newWidth, newHeight)
    angle = math.radians(theta)    
    hEdgeDiff = newHeight - height
    wEdgeDiff = newWidth - width
    h = (newWidth // 2)
    k = (newHeight // 2)
    print(height, width, newHeight, newWidth)
    
    for row in range(height):
        for col in range(width):            
            
            r,g,b = image.getPixel(row, col)
            newImage1.setPixel(row + hEdgeDiff//2, col + wEdgeDiff//2, r, g, b)
     
            
    for row in range(newHeight):
        for col in range(newWidth):     
            x = col - h
            y = row - k
            
            x1 = int(x*math.cos(angle) + y*math.sin(angle))
            y1 = int(y*math.cos(angle) - x*math.sin(angle))
            
            x = x1 + h
            y = y1 + k
                    
            if (x >= 0 and y >= 0) and (x < newWidth and y < newHeight):
                r,g,b = newImage1.getPixel(y,x)
                
            else:
                r,g,b = 0,0, 0
            newImage2.setPixel(row, col, r, g, b)
            
    return newImage2
    
def warpImage(image):
    width = image.width()
    height = image.height()
    newImage = GraphicsImage(width, height)
    for row in range(height):
        for col in range(width//6):            
            r,g,b = image.getPixel(row, col)           
            newImage.setPixel(row, col, r, g, b)
            
    for row in range(height):
        offset = 0
        for col in range(width//6, width//3):            
            if col % 2 == 1:
                r,g,b = image.getPixel(row, col)           
                newImage.setPixel(row, col - offset, r, g, b)                
                offset+=1
    
    for row in range(height):
        offset = 0
        for col in range(width//3, width//2):
            
            if col % 2 == 1:            
                r,g,b = image.getPixel(row, col)
                offset+=2           
                newImage.setPixel(row, col - offset, r, g, b)
            
    
    for row in range(height):
        offset = (2*width//3 - width//2)//2
        for col in range(width//2, 2*width//3):
            if col % 2 == 1:            
                r,g,b = image.getPixel(row, col)
                offset -= 2           
                newImage.setPixel(row, col + offset, r, g, b)   
            
    for row in range(height):
        offset = (5*width//6 - 2*width//3)//2
        for col in range(2*width//3, 5*width//6):
            if col % 2 == 1:
                r,g,b = image.getPixel(row, col)               
                offset-=1
            newImage.setPixel(row, col + offset, r, g, b)
            
    for row in range(height):
        for col in range(5*width//6, width):            
            r,g,b = image.getPixel(row, col)           
            newImage.setPixel(row, col, r, g, b)        
    return newImage
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
