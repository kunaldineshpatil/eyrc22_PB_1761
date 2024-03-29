'''
*****************************************************************************************
*
*        		===============================================
*           		Pharma Bot (PB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script is to implement Task 1A of Pharma Bot (PB) Theme (eYRC 2022-23).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			eYRC#PB#1761
# Author List:		Kunal Patil
# Filename:			task_1a.py
# Functions:		detect_traffic_signals, detect_horizontal_roads_under_construction, detect_vertical_roads_under_construction,
#					detect_medicine_packages, detect_arena_parameters
# 					label_nodes, get_shop, break_down, label_missing_vertical_lines, label_missing_horizontal_lines, 
# 					get_road_points_horizontal, get_road_points_vertical


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv)                    ##
##############################################################
from re import S
import cv2
import numpy as np
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################
def label_nodes(centre_point):

	"""
	Purpose:
	---
	This function takes the coordinates of a node as an argument and returns a string
	which is the label of the node present in the image

	Input Arguments:
	---
	`centre_point` :	[ tuple ]
			tuple containing x and y coordinate of the node
	Returns:
	---
	`label` : [ string ]
			string containing label of the node
	
	Example call:
	---
	traffic_signals.append(label_nodes(t))
	"""
	label=''
	if( (centre_point[0]==100)  |  ((centre_point[0]>90)&(centre_point[0]<110)) ):
			label=label+'A'
	elif( (centre_point[0]==200)  |  ((centre_point[0]>190)&(centre_point[0]<210)) ):
			label=label+'B'
	elif( (centre_point[0]==300)  |  ((centre_point[0]>290)&(centre_point[0]<310)) ):
			label=label+'C'
	elif( (centre_point[0]==400)  |  ((centre_point[0]>390)&(centre_point[0]<410)) ):
			label=label+'D'
	elif( (centre_point[0]==500)  |  ((centre_point[0]>490)&(centre_point[0]<510)) ):
			label=label+'E'
	elif( (centre_point[0]==600)  |  ((centre_point[0]>590)&(centre_point[0]<610)) ):
			label=label+'F'
	elif( (centre_point[0]==700)  |  ((centre_point[0]>690)&(centre_point[0]<710)) ):
			label=label+'G'
	label=label+str(int(centre_point[1]/100))
	return label

def get_shop(centre_point):
    
    """
	Purpose:
	---
	This function takes the coordinates of a point as an argument and returns a string
	which is shop in which it is present in the image

	Input Arguments:
	---
	`centre_point` :	[ tuple ]
			tuple containing x and y coordinate of the point
	Returns:
	---
	`shop` : [ string ]
			string containing shop in which the point is present
	
	Example call:
	---
	shop=get_shop(t)
	"""
    shop='Shop_'
    if((centre_point[0]>100) & (centre_point[0]<200)):
        shop=shop+'1'
    elif((centre_point[0]>200) & (centre_point[0]<300)):
        shop=shop+'2'
    elif((centre_point[0]>300) & (centre_point[0]<400)):
        shop=shop+'3'
    elif((centre_point[0]>400) & (centre_point[0]<500)):
        shop=shop+'4'
    elif((centre_point[0]>500) & (centre_point[0]<600)):
        shop=shop+'5'
    elif((centre_point[0]>600) & (centre_point[0]<700)):
        shop=shop+'6'
    return shop

def break_down(Gaps):
    
    """
	Purpose:
	---
	This function takes the coordinates of both the endpoints of the gap between two lines as an argument 
 	and returns a list with the gaps divided into gaps of length 100

	Input Arguments:
	---
	`Gaps` :	[ list of tuples ]
			list of tuple containing coordinates of start and end of a gap
	Returns:
	---
	`Gaps` : [ list of tuple ]
			list of tuple containing gaps divided into length of 100
	
	Example call:
	---
	Lines[line]=break_down(l)
	"""
    for l in Gaps:
        if(l[1]-l[0]>120):
            a=l[0]+100
            Gaps.append((l[0],a))
            while(a+84<l[1]):
                Gaps.append((a,a+100))
                a=a+100
            Gaps.remove(l)
    return Gaps
    
def label_missing_vertical_lines(Lines):
    
    """
	Purpose:
	---
	This function takes the set of missing lines in all the columns as an argument 
 	and returns a list with the labelled missing lines

	Input Arguments:
	---
	`Lines` :	[ dictionary ]
			dictionary containing x coordinates as keys and list of tuples(coordinates) of gaps as values
	Returns:
	---
	`ans` : [ list of strings ]
			list of all the missing lines labelled
	
	Example call:
	---
	ans=label_missing_vertical_lines(Lines)
	"""
    ans=[]
    for column,missing_lines in Lines.items():
        for g in missing_lines:
            s1=label_nodes((column,g[0]+10))
            s2=label_nodes((column,g[1]+10))
            s=s1+'-'+s2
            ans.append(s)
    return ans
    
def  label_missing_horizontal_lines(Lines):
    
    """
	Purpose:
	---
	This function takes the set of missing lines in all the columns as an argument 
 	and returns a list with the labelled missing lines

	Input Arguments:
	---
	`Lines` :	[ dictionary ]
			dictionary containing y coordinates as keys and list of tuples(coordinates) of gaps as values
	Returns:
	---
	`ans` : [ list of tuple ]
			list of all the missing lines labelled
	
	Example call:
	---
	ans=label_missing_horizontal_lines(Lines)
	"""
    ans=[]
    for row,missing_lines in Lines.items():
        for g in missing_lines:
            s1=label_nodes((g[0],row+10))
            s2=label_nodes((g[1],row+10))
            s=s1+'-'+s2
            ans.append(s)
    return ans
            
    
def get_road_points_horizontal(Lines):
    
    """
	Purpose:
	---
	This function takes the set of gaps in all the rows as an argument 
 	and returns a sorted list with all the missing lines

	Input Arguments:
	---
	`Lines` :	[ dictionary ]
			dictionary containing x coordinates as keys and list of tuples(coordinates) of gaps as values
	Returns:
	---
	`ans` : [ list of strings ]
			list of names of all the missing lines
	
	Example call:
	---
	horizontal_roads_under_construction=get_road_points_horizontal(sets_of_lines)
	"""
    ans=[]
    for line,gap in Lines.items():
        gap.sort()
        l=[]
        i=gap[0][0]
        prev=gap[0][1]
        gapc=gap[1:]
        for p in gapc:
            l.append((prev,p[0]))
            prev=p[1]
        if(i>150):
            l.append((96,i))
        if(prev<650):
            l.append((prev,708))
        Lines[line]=break_down(l)
    ans=label_missing_horizontal_lines(Lines)
    ans.sort()
    return ans
    
    
def get_road_points_vertical(Lines):
    
    """
	Purpose:
	---
	This function takes the set of gaps in all the columns as an argument 
 	and returns a sorted list with all the missing lines

	Input Arguments:
	---
	`Lines` :	[ dictionary ]
			dictionary containing y coordinates as keys and list of tuples(coordinates) of gaps as values
	Returns:
	---
	`ans` : [ list of strings ]
			list of names of all the missing lines
	
	Example call:
	---
	vertical_roads_under_construction=get_road_points_vertical(sets_of_lines)
	"""
    ans=[]
    for line,gap in Lines.items():
        gap.sort()
        l=[]
        i=gap[0][0]
        prev=gap[0][1]
        gapc=gap[1:]
        for p in gapc:
            l.append((prev,p[0]))
            prev=p[1]
        if(i>150):
            l.append((96,i))
        if(prev<650):
            l.append((prev,708))
        Lines[line]=break_down(l)
    ans=label_missing_vertical_lines(Lines)
    ans.sort()
    return ans


##############################################################

def detect_traffic_signals(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list of
	nodes in which traffic signals are present in the image

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`traffic_signals` : [ list ]
			list containing nodes in which traffic signals are present
	
	Example call:
	---
	traffic_signals = detect_traffic_signals(maze_image)
	"""    
	traffic_signals = []

	##############	ADD YOUR CODE HERE	##############
	#Converting the image into HSV
	hsv = cv2.cvtColor(maze_image,cv2.COLOR_BGR2HSV)
 
	#Defining the range of Red color
	red_lower=np.array([0,70,50])
	red_upper=np.array([10,255,255])
 
 	#Creating the mask
	mask = cv2.inRange(hsv, red_lower, red_upper)

 	#Detecting the red color
	res = cv2.bitwise_and(maze_image, maze_image, mask=mask)
 
	# using a findContours() function
	contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 
	# Putting Values into list
	for contour in contours:
  
        # finding center point of shape
		M = cv2.moments(contour)
		t=()
		if M['m00'] != 0.0:
			x = int(M['m10']/M['m00'])
			y = int(M['m01']/M['m00'])
			t=(x,y)
		traffic_signals.append(label_nodes(t))
	traffic_signals.sort()
	##################################################
	
	return traffic_signals
	

def detect_horizontal_roads_under_construction(maze_image):
	
	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list
	containing the missing horizontal links

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`horizontal_roads_under_construction` : [ list ]
			list containing missing horizontal links
	
	Example call:
	---
	horizontal_roads_under_construction = detect_horizontal_roads_under_construction(maze_image)
	"""    
	horizontal_roads_under_construction = []

	##############	ADD YOUR CODE HERE	##############
	#  Convert image to grayscale
	gray = cv2.cvtColor(maze_image,cv2.COLOR_BGR2GRAY)
	thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
 
	# Detect horizontal lines
	horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40,1))
	detect_horizontal = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
	cnts = cv2.findContours(detect_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if len(cnts) == 2 else cnts[1]

	# Form a dictionary of lines that have missing parts
	sets_of_lines={}
	for c in cnts:
    
		# If any part of a line is missing add it to sets_of_line with key value as the y coordinate of the entire line
		if(cv2.arcLength(c, True)<1200):
			sets_of_lines.setdefault(c[0][0][1], [])
			sets_of_lines[c[0][0][1]].append((c[0][0][0],c[3][0][0]))

	# Get the labelled missing parts
	horizontal_roads_under_construction=get_road_points_horizontal(sets_of_lines)
	##################################################
	
	return horizontal_roads_under_construction	

def detect_vertical_roads_under_construction(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list
	containing the missing vertical links

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`vertical_roads_under_construction` : [ list ]
			list containing missing vertical links
	
	Example call:
	---
	vertical_roads_under_construction = detect_vertical_roads_under_construction(maze_image)
	"""    
	vertical_roads_under_construction = []

	##############	ADD YOUR CODE HERE	##############
	#  Convert image to grayscale
	gray = cv2.cvtColor(maze_image,cv2.COLOR_BGR2GRAY)
	thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
 
	# Detect vertical lines
	vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,20))
	detect_vertical = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
	cnts = cv2.findContours(detect_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if len(cnts) == 2 else cnts[1]
 
	# Form a dictionary of lines that have missing parts
	sets_of_lines={}
	for c in cnts:
		
		# If any part of a line is missing add it to sets_of_line with key value as the x coordinate of the entire line
		if(cv2.arcLength(c, True)<1200):
			sets_of_lines.setdefault(c[0][0][0], [])
			sets_of_lines[c[0][0][0]].append((c[0][0][1],c[1][0][1]))
   
	# Get the labelled missing parts
	vertical_roads_under_construction=get_road_points_vertical(sets_of_lines)
	##################################################
	
	return vertical_roads_under_construction


def detect_medicine_packages(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a nested list of
	details of the medicine packages placed in different shops

	** Please note that the shop packages should be sorted in the ASCENDING order of shop numbers 
	   as well as in the alphabetical order of colors.
	   For example, the list should first have the packages of shop_1 listed. 
	   For the shop_1 packages, the packages should be sorted in the alphabetical order of color ie Green, Orange, Pink and Skyblue.

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`medicine_packages` : [ list ]
			nested list containing details of the medicine packages present.
			Each element of this list will contain 
			- Shop number as Shop_n
			- Color of the package as a string
			- Shape of the package as a string
			- Centroid co-ordinates of the package
	Example call:
	---
	medicine_packages = detect_medicine_packages(maze_image)
	"""    
	medicine_packages = []

	##############	ADD YOUR CODE HERE	##############
	# Converting into Grayscale
	gray = cv2.cvtColor(maze_image, cv2.COLOR_BGR2GRAY)
 
	# getting only shapes and setting threshold of gray image
	_, with_shapes = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
	_, without_shapes = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)
	only_shapes = cv2.bitwise_xor(with_shapes,without_shapes)

	# using a findContours() function
	contours, _ = cv2.findContours(only_shapes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	
	# here we are ignoring first coutours because
	# findcontour function detects whole image as shape
	contours =  contours[1:]
	
	# Putting Values into list
	for contour in contours:   
		
		# Ignoring the extra contours
		area = cv2.contourArea(contour)
		if area < 200:
			continue

		# finding Shape
		approx = cv2.approxPolyDP(contour, 0.03 * cv2.arcLength(contour, True), True)
		
		# if the shape is a triangle, it will have 3 vertices
		if (len(approx) == 3):
			shape = 'Triangle'

		# if the shape has 4 vertices, it is a square
		elif (len(approx) == 4):
			shape = 'Square'

		# otherwise, we assume the shape is a circle
		else:
			shape = 'Circle'
   
		# finding center point of shape
		M = cv2.moments(contour)
		t=()
		if M['m00'] != 0.0:
			x = int(M['m10']/M['m00'])
			y = int(M['m01']/M['m00'])
		t=(x,y)
  
		# finding color
		color=""
		b, g, r= maze_image[y, x]
		# for sky blue 
		if ((b>250) & (g>250) & (r<5)):
			color="Skyblue"
		# for pink 
		elif ((b<5) & (g<150) & (r>250)):
			color="Orange"
		# for orange
		elif ((b<200) & (g<5) & (r>250)):
			color="Pink"
		# for green 
		elif ((b<5) & (g>250) & (r<5)):
			color="Green"
		
		# finding shop number
		shop=get_shop(t)

		# Add to list
		medicine_packages.append([shop,color,shape,t])
	medicine_packages.sort()
	##################################################

	return medicine_packages

def detect_arena_parameters(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a dictionary
	containing the details of the different arena parameters in that image

	The arena parameters are of four categories:
	i) traffic_signals : list of nodes having a traffic signal
	ii) horizontal_roads_under_construction : list of missing horizontal links
	iii) vertical_roads_under_construction : list of missing vertical links
	iv) medicine_packages : list containing details of medicine packages

	These four categories constitute the four keys of the dictionary

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`arena_parameters` : { dictionary }
			dictionary containing details of the arena parameters
	
	Example call:
	---
	arena_parameters = detect_arena_parameters(maze_image)
	"""    
	arena_parameters = {}

	##############	ADD YOUR CODE HERE	##############
	arena_parameters={'traffic_signals':detect_traffic_signals(maze_image), 'horizontal_roads_under_construction':detect_horizontal_roads_under_construction(maze_image), 'vertical_roads_under_construction':detect_vertical_roads_under_construction(maze_image),'medicine_packages_present':detect_medicine_packages(maze_image)}
	##################################################
	
	return arena_parameters

######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########	

if __name__ == "__main__":

    # path directory of images in test_images folder
	img_dir_path = "public_test_images/"

    # path to 'maze_0.png' image file
	file_num = 0
	img_file_path = img_dir_path + 'maze_' + str(file_num) + '.png'
	
	# read image using opencv
	maze_image = cv2.imread(img_file_path)
	
	print('\n============================================')
	print('\nFor maze_' + str(file_num) + '.png')

	# detect and print the arena parameters from the image
	arena_parameters = detect_arena_parameters(maze_image)

	print("Arena Prameters: " , arena_parameters)

	# display the maze image
	cv2.imshow("image", maze_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	choice = input('\nDo you want to run your script on all test images ? => "y" or "n": ')
	
	if choice == 'y':

		for file_num in range(1, 15):
			
			# path to maze image file
			img_file_path = img_dir_path + 'maze_' + str(file_num) + '.png'
			
			# read image using opencv
			maze_image = cv2.imread(img_file_path)
	
			print('\n============================================')
			print('\nFor maze_' + str(file_num) + '.png')
			
			# detect and print the arena parameters from the image
			arena_parameters = detect_arena_parameters(maze_image)

			print("Arena Parameter: ", arena_parameters)
				
			# display the test image
			cv2.imshow("image", maze_image)
			cv2.waitKey(2000)
			cv2.destroyAllWindows()