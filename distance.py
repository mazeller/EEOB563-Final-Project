# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 10:14:06 2018

@author: michael.zeller
"""

import sys
import getopt
import pandas as pd

def main():
	#Get arguments
	argv = sys.argv[1:]

	try:
		opts, args = getopt.getopt(argv,"i:h",["input=","help"])
	except getopt.GetoptError:
		sys.exit(2)
	
	for opt, arg in opts:
		if opt in ('-h',"help"):
			sys.exit()	#No help for you
		elif opt in ("-i", "--ifile"):
			inputfile = arg
			
	#Open input file as a dataframe
	#format name, {ingred}
	df = pd.read_csv(inputfile)
	
	#Grab recipes & create a dataframe (you shouldn't create empty dataframes as it is slow to fill them)
	recipes = df.iloc[:,0].unique()
	distanceDf = pd.DataFrame(0, index=recipes, columns=recipes)

	#Compute distances per every two recipes
	for indexi, rowi in df.iterrows():
		for indexj, rowj in df.iterrows():
			#Reset distance
			dist = 0
			
			for i in range(1,224):
				if(rowi[i] != rowj[i]):
					dist += 1
				
			distanceDf.loc[rowi[0],rowj[0]] = dist
		print(rowi[0]," ",dist)
	print(distanceDf)

	#Save output	
	distanceDf.to_csv("distances.csv")
	print(distanceDf)


			

if __name__ == "__main__": main()