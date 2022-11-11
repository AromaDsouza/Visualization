# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:33:46 2022

@author: Aroma
"""

import pandas as pd  #To open the files
import matplotlib.pyplot as plt  #Used for vizualizations

#Defining a function for the line graph with three parameters and plotting the line graph

def line_graph(age,drug_use,drug_name):
    plt.plot(age,drug_use,label=drug_name)

#To read the csv file
data = pd.read_csv('drug-use-by-age.csv')

#Printing the file
print(data)

#Dropping the columns that will not be considered for plotting the line graph
data = data.drop(['n','alcohol-frequency','marijuana-frequency','cocaine-frequency','crack-frequency','heroin-frequency','hallucinogen-frequency','inhalant-frequency','pain-releiver-frequency','oxycontin-frequency','tranquilizer-frequency','stimulant-frequency','meth-frequency','sedative-frequency'], axis=1)

#Selecting the 9 rows from the first column i.e age to make the line plot look neat
data1 = data.iloc[0:10]
print(data1)

'''
For plotting the image and mentioning the figure size.
dpi is dots per inch i.e to set the resolution of the image
'''
plt.figure(figsize=(6,4),dpi=144)

#Calling the above define function for the line graph and labelling the lines
line_graph(data1["age"],data1["alcohol-use"],"Alcohol")
line_graph(data1["age"],data1["marijuana-use"],"Marijuana")
line_graph(data1["age"],data1["cocaine-use"],"Cocaine")
line_graph(data1["age"],data1["sedative-use"],"Sedative")

plt.xlabel("Age (Years)")  #To label the x-axis 
plt.ylabel("Percentage of drug usage")  #To label the y-axis
plt.title("Line graph representing the consumption of drugs")  #To mention the title for the line graph
plt.legend()  #To show the label names in form of a box
plt.savefig('Line graph.png') #Saving the image of the line graph
plt.show()  #To display the image of the line graph

#Defining a function for the stacked bar graph with three parameters and plotting the line graph
def stacked_bar_graph(age,drug_use,drug_name):
    plt.bar(age,drug_use,label=drug_name)

'''
For plotting the image and mentioning the figure size.
dpi is dots per inch i.e to set the resolution of the image
'''
plt.figure(figsize=(6,4),dpi=144)

#Calling the above define function for the stacked bar graph and labelling the bars
stacked_bar_graph(data1["age"],data1["alcohol-use"],"Alcohol")
stacked_bar_graph(data1["age"],data1["marijuana-use"],"Marijuana")
stacked_bar_graph(data1["age"],data1["cocaine-use"],"Cocaine")
stacked_bar_graph(data1["age"],data1["sedative-use"],"Sedative")

plt.xlabel("Age (Years)")  #To label the x-axis
plt.ylabel("Percentage of drug usage")  #To label the y-axis
plt.title("Stacked bar graph representing the consumption of drugs")  #To mention the title for stacked bar graph
plt.legend()  #To show the label names in form of a box
plt.savefig('Bar graph.png') #Saving the image of the line graph
plt.show()  #To display the image of the line graph

#Defining a function for the pie chart with three parameters and plotting the pie chart
def pie_chart(drug_use, age):
    plt.pie(drug_use, labels=age, autopct="%2.1f%%")  #autopct is to display the plot in terms of percentage

'''
Selecting the next 7 rows starting from the 10th row in the first column i.e age 
Since the rows 10 to 16 are in the form of strings.
'''
data = data.iloc[10:,:]
print(data)

#To calculate the totals of all the columns
data["total"] = data["alcohol-use"]+data["marijuana-use"]+data["cocaine-use"]+data["crack-use"]+\
                data["heroin-use"]+ data["hallucinogen-use"]+data["inhalant-use"]+data["pain-releiver-use"]+\
                data["oxycontin-use"]+data["tranquilizer-use"]+data["stimulant-use"]+data["meth-use"]+data["sedative-use"]
print(data)

'''
For plotting the image and mentioning the figure size.
dpi is dots per inch i.e to set the resolution of the image
'''
plt.figure(figsize=(6,4),dpi=144)

#Plotting the pie chart with columnns 'age' and 'total'
pie_chart(data["total"],data["age"])

plt.title("Pie chart representing the consumption of drugs based on age")  #To display the image of the pie graph
plt.savefig('Pie chart.png') #Saving the image of the line graph

plt.show()









