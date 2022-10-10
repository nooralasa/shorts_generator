import wave
import numpy as np
import sys
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

wav = wave.open("songM00-22.wav","r")
raw = wav.readframes(-1)
raw = np.frombuffer(raw, "int32")
#print raw.size
print len(raw)
#print min(raw)
#print max(raw)
#print raw

# # The aspect ratio of the image
# BUFFER_LENGTH = len(buffer)
# HEIGHT = 960 #columns
# WIDTH = 540 #rows

# print 'The size of the buffer for 22 seconds is: {}'.format(BUFFER_LENGTH)
# print 'Aspect ratio is {} x {} = {}'.format(HEIGHT, WIDTH, HEIGHT*WIDTH)

#Creating the data
#L0-L3 in previous code. Four 0-255 values for each dot.
# rbg_values = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
# bytes = np.zeros((BUFFER_LENGTH, 1, 4), dtype=np.uint8)

# NUM_DOTS = 180
# CHUNKS = 4

# for i in range(len(rbg_values)):
# 	for j in range(len(rbg_values[i])):
# 		if rbg_values[i][j] < 0.5:
# 			rbg_values[i][j] *= 32
# 		else:
# 			rbg_values[i][j] *= 255
			
# print rbg_values

# i = 0
# pixels_per_dot = (HEIGHT*WIDTH)/NUM_DOTS
# sums = [0.0, 0.0, 0.0, 0.0]
# while i < BUFFER_LENGTH and (i/pixels_per_dot) < 180:
# 	i+=1
# 	if i%pixels_per_dot == 0: # point
# 		rbg_values[0][(i/pixels_per_dot)-1] = sums[0]//pixels_per_dot
# 		rbg_values[1][(i/pixels_per_dot)-1] = sums[1]//pixels_per_dot
# 		rbg_values[2][(i/pixels_per_dot)-1] = sums[2]//pixels_per_dot
# 		rbg_values[3][(i/pixels_per_dot)-1] = sums[3]//pixels_per_dot
# 		sums = [0.0, 0.0, 0.0, 0.0]
# 	else:
# 		sums[0] += abs((buffer[i]>>24) & 0xff)
# 		sums[1] += abs((buffer[i]>>16) & 0xff)
# 		sums[2] += abs((buffer[i]>>8) & 0xff)
# 		sums[3] += abs((buffer[i]) & 0xff)

# print rbg_values

# #Normalize rbg_values 0-1
# for i in range(4):
# 	minVal = min(rbg_values[i])
# 	maxVal = max(rbg_values[i])
# 	rbg_values[i] = [((x-minVal)/(maxVal-minVal)) for x in rbg_values[i]]

# for i in range(len(rbg_values)):
# 	for j in range(len(rbg_values[i])):
# 		if rbg_values[i][j] < 0.5:
# 			rbg_values[i][j] *= 32
# 		else:
# 			rbg_values[i][j] *= 255
			
# print rbg_values


# Creates a list containing 5 lists, each of 8 items, all set to 0
h, w = 960, 540
L3 = [[0 for x in range(h)] for y in range(w)] 
L2 = [[0 for x in range(h)] for y in range(w)] 
L1 = [[0 for x in range(h)] for y in range(w)] 
L0 = [[0 for x in range(h)] for y in range(w)] 


rows = len(L3)
columns = len(L3[0])
print(rows)
print(columns)


#Creating the data
data = np.zeros((h, w, 3), dtype=np.uint8)
rawData = np.zeros((len(raw), 1, 4), dtype=np.uint8)
x = 0
for i in range(w):
	for j in range(h):
		L3 [i][j]= abs((raw[x]>>24) & 0xff)
		L2 [i][j]= abs((raw[x]>>16) & 0xff)
		L1 [i][j]= abs((raw[x]>>8) & 0xff)
		L0 [i][j]= abs((raw[x]) & 0xff)
		data[j, i] = [L2[i][j], L1[i][j], L0[i][j]]
		rawData [x][0]=[L3[i][j],L2[i][j], L1[i][j], L0[i][j]]
		#print ("L3[%d][%d] = %d" %(i,j, L3 [i][j]))
		#print ("rawData[%d][0] =" %(x))
		#print (rawData[x][0])
		#print x
		x=x+1
		
#print len(rawData)
##print("The variable, rawData[512, 0] is of type:", type(rawData[512, 0,3]))
#find data type in L3		
#print("The variable, L3[0][0] is of type:", type(L3[0][0]))


#Image manipulation
#data = np.zeros((h, w, 3), dtype=np.uint8)
#data[512, 511] = [L3[0][0], L2[0][0], L1[0][0]]
#data[512, 512] = [0, 255, 0]
#data[512, 513] = [0, 0, 255]

##print("The variable, data[512, 511] is of type:", type(data[512, 511,0]))


#image = Image.fromarray(data)
#image.show()




y = 0
v = 2880
t = 180
dataArtL3 = np.zeros((t, 1), dtype=np.uint8) 
dataArtL2 = np.zeros((t, 1), dtype=np.uint8) 
dataArtL1 = np.zeros((t, 1), dtype=np.uint8) 
dataArtL0 = np.zeros((t, 1), dtype=np.uint8)  
AvgL3 = 0
AvgL2 = 0
AvgL1 = 0
AvgL0 = 0
i = 0

while i < len(rawData):
	for j in range(v):
		AvgL3=AvgL3+rawData[i,0,0]
		AvgL2=AvgL2+rawData[i,0,1]
		AvgL1=AvgL1+rawData[i,0,2]
		AvgL0=AvgL0+rawData[i,0,3]
		i += 1
	#print (AvgL3)
	dataArtL3 [y]=AvgL3//v
	dataArtL2 [y]=AvgL2//v
	dataArtL1 [y]=AvgL1//v
	dataArtL0 [y]=AvgL0//v
	#print (dataArtL3 [y])
	AvgL3 = 0
	AvgL2 = 0
	AvgL1 = 0
	AvgL0 = 0
	y += 1
	if y >= t:
		i = len(rawData)

	
#print (dataArtL3)
#print (dataArtL2)
#print (dataArtL1)
#print (dataArtL0)
#print (min(dataArtL3))
#print (max(dataArtL3))
#print (min(dataArtL2))
#print (max(dataArtL2))
#print (min(dataArtL1))
#print (max(dataArtL1))
#print (min(dataArtL0))
#print (max(dataArtL0))

tempValue = 0.0
minMult = 32
maxMult = 255
#float(tempValue)
for i in range (len(dataArtL3)):
	tempValue=float((dataArtL3 [i]-min(dataArtL3))/float(max(dataArtL3)-min(dataArtL3)))
	if tempValue < 0.5:
		tempValue=tempValue*minMult
	else:
		tempValue=tempValue*maxMult
	#print (tempValue)

	dataArtL3 [i]=tempValue
	tempValue =0
	
for i in range (len(dataArtL2)):
	tempValue=float((dataArtL2 [i]-min(dataArtL2))/float(max(dataArtL2)-min(dataArtL2)))
	if tempValue < 0.5:
		tempValue=tempValue*minMult
	else:
		tempValue=tempValue*maxMult	
	#print (tempValue)
	dataArtL2 [i]=tempValue
	tempValue =0
	
for i in range (len(dataArtL1)):
	tempValue=float((dataArtL1 [i]-min(dataArtL1))/float(max(dataArtL1)-min(dataArtL1)))
	if tempValue < 0.5:
		tempValue=tempValue*minMult
	else:
		tempValue=tempValue*maxMult	
	#print (tempValue)
	dataArtL1 [i]=tempValue
	tempValue =0
	
for i in range (len(dataArtL0)):
	tempValue=float((dataArtL0 [i]-min(dataArtL0))/float(max(dataArtL0)-min(dataArtL0)))
	if tempValue < 0.5:
		tempValue=tempValue*minMult
	else:
		tempValue=tempValue*maxMult	
	#print (tempValue)
	dataArtL0 [i]=tempValue
	tempValue =0
	
print (min(dataArtL3))
print (max(dataArtL3))
print (min(dataArtL2))
print (max(dataArtL2))
print (min(dataArtL1))
print (max(dataArtL1))
print (min(dataArtL0))
print (max(dataArtL0))

image = Image.new('RGB', (1080, 1920), (255, 255, 255))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, 1080, 396), fill=(0, 0, 0))
draw.rectangle((0, 1524, 1080, 1920), fill=(0, 0, 0))

X, Y = 210,601.6
r = 20
draw.ellipse([(X-r, Y-r), (X+r, Y+r)], fill=(255, 0, 0))

X, Y = 270,601.6
r = 20
draw.ellipse([(X-r, Y-r), (X+r, Y+r)], fill=(255, 0, 0))

w = 12
h = 15
r = 20
y = 0
X, Y = 210,601.6
for i in range(h):	
	for j in range(w):
		draw.ellipse([(X-r, Y-r), (X+r, Y+r)], fill=(dataArtL2 [y], dataArtL1 [y], dataArtL0 [y]))
		#draw.ellipse([(X-r, Y-r), (X+r, Y+r)], fill=(dataArtL3 [y], 0, 0))
		X = X+60
		y=y+1
	X = 210
	Y = Y+51.2
	

image.show()

	

# write file data for manipulation
#L3_file = open("L3.txt", "w")
#L2_file = open("L2.txt", "w")
#L1_file = open("L1.txt", "w")
#L0_file = open("L0.txt", "w")
#L_file = open("L.txt", "w")
#for x in raw:

	#print((x>>24) & 0xff)
	#print((x>>16) & 0xff)
	#print((x>>8) & 0xff)
	#print(x & 0xff)
	#print (x)
#	L3_file.write(str(abs((x>>24) & 0xff)))
#	L2_file.write(str(abs((x>>16) & 0xff)))
#	L1_file.write(str(abs((x>>8) & 0xff)))
#	L0_file.write(str(abs(x & 0xff)))
#	L_file.write(str(abs(x)))
#	L3_file.write("\n")
#	L1_file.write("\n")
#	L2_file.write("\n")
#	L0_file.write("\n")
#	L_file.write("\n")
	
#L3_file. close()
#L2_file. close()
#L1_file. close()
#L0_file. close()
#L_file. close()

#if wav.getnchannels()=2:
#	print("Stero Files are not supported, Use Mono files")
#	sys.exit(0)

#plt.title("Waveform of WaveFile")
#plt.plot(raw, color="blue")
#plt.ylabel("Amplitude")
#plt.show()

