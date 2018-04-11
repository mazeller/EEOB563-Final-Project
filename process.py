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
	#format name, id, origin, ingred
	df = pd.read_csv(inputfile)
	
	#Grab recipes & ingredients and create a  (you shouldn't create empty dtaaframes as it is slow to fill them)
	recipes = df.iloc[:,0].unique()
	ingredients = df.iloc[:,3].unique()
	characterDf = pd.DataFrame(0, index=recipes, columns=ingredients)

	
	#Slowly fill the dataframe
	for index, row in df.iterrows():
		characterDf.loc[row[0],row[3]] = 1

	#Save output	
	characterDf.to_csv("characters.csv")
	print(characterDf)


			

if __name__ == "__main__": main()