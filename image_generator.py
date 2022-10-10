import wave
import numpy as np
import sys
from PIL import Image, ImageDraw

from colors import colors

# Parse audio file
wav = wave.open("songM00-22.wav","r")
buffer = wav.readframes(-1)
buffer = np.frombuffer(buffer, "int32")

# The aspect ratio of the image
BUFFER_LENGTH = len(buffer)
HEIGHT = 960 #columns
WIDTH = 540 #rows
NUM_DOTS = 180
CHUNKS_IN_BYTE = 4

print 'The size of the buffer for 22 seconds is: {}'.format(BUFFER_LENGTH)
print 'Aspect ratio is {} x {} = {}'.format(HEIGHT, WIDTH, HEIGHT*WIDTH)

#Creating the data
bytes = np.zeros((BUFFER_LENGTH, 1, 4), dtype=np.uint8)



buffer_values = [0.0]*NUM_DOTS
i = 0
pixels_per_dot = (HEIGHT*WIDTH)/NUM_DOTS
while i < BUFFER_LENGTH and (i/pixels_per_dot) < NUM_DOTS:
    # i/pixels_per_dot corresponds each block of pixels into one dot.
	buffer_values[i/pixels_per_dot] = sum(buffer[i:i+pixels_per_dot+1])//float(pixels_per_dot)
	i+=pixels_per_dot

print buffer_values

#Normalize buffer_values to values between 0-1
minVal = min(buffer_values)
maxVal = max(buffer_values)
buffer_values = [((x-minVal)/(maxVal-minVal)) for x in buffer_values]

print buffer_values

#Determine the actual colors for each buffer_value
rbg_values = []
for val in buffer_values: 
	rbg_values.append(colors[int(val*(len(colors)-1))])

print rbg_values


image = Image.new('RGB', (1080, 1920), (255, 255, 255))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, 1080, 396), fill=(0, 0, 0))
draw.rectangle((0, 1524, 1080, 1920), fill=(0, 0, 0))

w = 12
h = 15
r = 20
y = 0
X, Y = 210,601.6
for i in range(h):	
	for j in range(w):
		draw.ellipse([(X-r, Y-r), (X+r, Y+r)], fill=(rbg_values[y][0], rbg_values[y][1], rbg_values[y][2]))
		#draw.ellipse([(X-r, Y-r), (X+r, Y+r)], fill=(dataArtL3 [y], 0, 0))
		X = X+60
		y=y+1
	X = 210
	Y = Y+51.2
	
image.show()