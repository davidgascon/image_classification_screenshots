import pyautogui
import time
try:
	import pyperclip
except:
	print("pip install pyperclip.")
	exit()

print("Tracking mouse location\n\n")

size = pyautogui.size()
print(f"Display Screen Size {size}\n\n")

def printlocation():
	location = pyautogui.position()
	print(f"Location is {location}")
	pixelcolor = pyautogui.screenshot().getpixel((x,y))


status = 0
redcordlist = []
notcordlist = []
cordlist = []
barcheck = False
spotlist = False
while 1 == 1 :
	#time.sleep(1)
	print("Enter cord to move mouse to those cordinates")
	print("Enter Barrack to copy barrack information")
	inputvar = input("Press enter to get cordinates or enter 'cord' to mvoe to that location")



	if inputvar == '':
		x, y = pyautogui.position()
		pixelColor = pyautogui.screenshot().getpixel((x, y))
		print("X: " + str(x) + " Y: " + str(y) + " RBG: " + str(pixelColor) + "\n\n")
		copied = str("pixelMatchesColor(" + str(x) + ", " + str(y) + ", " + str(pixelColor) + ", tolerance=10)" )
		pyperclip.copy(str(copied))
		
		if barcheck == True:

			if cordlist == []:
				print("one-----------------------")
				cordlist.append(x)
				cordlist.append(y)
				cordlist.append(pixelColor[0])
				cordlist.append(pixelColor[1])
				cordlist.append(pixelColor[2])

				print(cordlist)

				print("zero " + str(cordlist[0]))
				print("one " + str(cordlist[1]))
				print("two " + str(cordlist[2]))
				print("three " + str(cordlist[3]))
				print("four " + str(cordlist[4]))
			else:
				print("two -----------------------")
				print("x diff " + str((cordlist[0]) - x))
				print("y diff " + str((cordlist[1]) - y))
				print("two " + str(cordlist[2] - pixelColor[0]))
				print("three " + str(cordlist[3] - pixelColor[1]))
				print("found " + str(cordlist[4] - pixelColor[2]))

				print(cordlist)
				cordlist = []


		if spotlist == True:
			if pixelColor[0] > 1.5*pixelColor[1] and pixelColor[0] > 1.5*pixelColor[2]:
				print("Complicated RED")

			if pixelColor[0] > 100 and pixelColor[1] < 100 and pixelColor[2] < 100:
				print("RED")
				redcordlist.append(f"({x}, {y})")
			else:
				print("NOT RED")
				notcordlist.append(f"({x}, {y})")
			print("red cord list")
			print(redcordlist)
			print("Not red cord list")
			print(notcordlist)

			
		continue
	if inputvar == 'barrack':
		x, y = pyautogui.position()
		pixelColor = pyautogui.screenshot().getpixel((x, y))
		print("X: " + str(x) + " Y: " + str(y) + " RBG: " + str(pixelColor) + "\n")
		copied = str("(" + str(x) + ", " + str(y) + ", " + str(pixelColor[0]) + ", " + str(pixelColor[1]) + ", " + str(pixelColor[2]) + ", X )")
		print(copied)
		pyperclip.copy(str(copied))
		continue

	if inputvar == 'cord' :
		xcord = int(input("Input X cord"))
		ycord = int(input("Input Y cord"))
		pyautogui.moveTo(xcord, ycord)
		continue
	if inputvar == 'barcheck':
		barcheck = True
		print("Turning barcheck on")
		continue

	if inputvar == 'spot':
		spotlist = True



	else :
		break

print("Done--------------------")


#pyautogui.moveTo(200,15)
#pyautogui.click()
#location = pyautogui.position()
#print(f"{location}")