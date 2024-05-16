# First needs to import the relevant libraries 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# The iris.data has no headings for columns, so I need to define them
irisdata = 'iris.data'
colums = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Species']
iris = pd.read_csv(irisdata, names = colums)

# Creating a text file where all results will be kept.
datasummary = open('summary.txt','w')
print("In this file you can find the different statistics of Iris dataset.", file = datasummary)
print("\n", file = datasummary)

# Summary of dataset
print("\nThis statistics will display first 5 and last 5 rows of the dataset and gives the total of rows and columns.\n", file = datasummary)
print(iris, file = datasummary) 
print("\n", file = datasummary)

# This will print just third row from dataset
print("\n\nShowing the 3rd row of data set.\n", file = datasummary)
print(iris.iloc[3], file = datasummary)

# This is summary for flower species
print("\n\nOverall summary statistics for the four variables of all 3 species.\n", file = datasummary)
print(iris.describe(), file = datasummary)

# This will print the statement groups the summary for each species
print("\n\nThis will show the statement groups for each species.\n", file = datasummary)
print(iris.groupby(['Species']).describe(), file = datasummary)

# This will show just a mean value for each species separately
print("\n\nThis will show the mean value for each species.\n", file = datasummary)
print(iris.groupby(['Species']).mean(), file = datasummary)


# This will show the mean value for all 4 variables of 3 species as bar charts
# Sepal Length
plt.figure(figsize=(7,5))
iris.groupby(['Species'])['Sepal Length'].mean().plot(kind = 'bar', color =['indianred','steelblue','forestgreen'])
plt.title('Sepal Length(cm) vs Species', color ='darkslategray')
plt.xlabel('Species', color ='darkslategray')
plt.xticks(rotation = 0)
plt.ylabel('Sepal Length', color = 'darkslategray')
plt.savefig('Sepal Length Bar Chart.png')
plt.show()

# Sepal Width
plt.figure(figsize=(7,5))
iris.groupby(['Species'])['Sepal Width'].mean().plot(kind = 'bar', color =['indianred','steelblue','forestgreen'])
plt.title('Sepal Width(cm) vs Species', color ='darkslategray')
plt.xlabel('Species', color ='darkslategray')
plt.xticks(rotation = 0)
plt.ylabel('Sepal Width', color = 'darkslategray')
plt.savefig('Sepal Width Bar Chart.png')
plt.show()

# Petal Length
plt.figure(figsize=(7,5))
iris.groupby(['Species'])['Petal Length'].mean().plot(kind = 'bar', color =['indianred','steelblue','forestgreen'])
plt.title('Petal Length(cm) vs Species', color ='darkslategray')
plt.xlabel('Species', color ='darkslategray')
plt.xticks(rotation = 0)
plt.ylabel('Petal Length', color = 'darkslategray')
plt.savefig('Petal Length Bar Chart.png')
plt.show()

# Petal Width
plt.figure(figsize=(7,5))
iris.groupby(['Species'])['Petal Width'].mean().plot(kind = 'bar', color =['indianred','steelblue','forestgreen'])
plt.title('Petal Width(cm) vs Species', color ='darkslategray')
plt.xlabel('Species', color ='darkslategray')
plt.xticks(rotation = 0)
plt.ylabel('Petal Width', color = 'darkslategray')
plt.savefig('Petal Width Bar Chart.png')
plt.show()


#sorting the species, variables and other parameters
setosa_sl = iris[iris.Species == 'Iris-setosa']['Sepal Length']
versicolor_sl = iris[iris.Species == 'Iris-versicolor']['Sepal Length']
virginica_sl = iris[iris.Species == 'Iris-virginica']['Sepal Length']

setosa_sw = iris[iris.Species == 'Iris-setosa']['Sepal Width']
versicolor_sw = iris[iris.Species == 'Iris-versicolor']['Sepal Width']
virginica_sw = iris[iris.Species == 'Iris-virginica']['Sepal Width']

setosa_pl = iris[iris.Species == 'Iris-setosa']['Petal Length']
versicolor_pl = iris[iris.Species == 'Iris-versicolor']['Petal Length']
virginica_pl = iris[iris.Species == 'Iris-virginica']['Petal Length']

setosa_pw = iris[iris.Species == 'Iris-setosa']['Petal Width']
versicolor_pw = iris[iris.Species == 'Iris-versicolor']['Petal Width']
virginica_pw = iris[iris.Species == 'Iris-virginica']['Petal Width']

lab = ['Iris Setosa', 'Iris Versicolor', 'Iris Virginica']
col = ['yellowgreen', 'skyblue', 'mediumvioletred']
leg = ['Setosa', 'Versicolor', 'Virginica']

# Creating function for each variables for all 3 species using the paramenters set up above.
# Sepal Length - this function will output the histogram for all 3 species based on the sepal length
def his_sl():
    plt.figure(figsize=(7,5))
    plt.hist([setosa_sl, versicolor_sl, virginica_sl], color = col,  label = lab, edgecolor = 'darkslategray')
    plt.title('Sepal Length', color ='darkslategray')
    plt.xlabel('Sepal Length(cm)', color ='darkslategray')
    plt.ylabel('Count', color = 'darkslategray')
    plt.legend(leg)
    plt.savefig('Sepal Length Hist.png')
    plt.show()

# Sepal Width - this function will output the histogram for all 3 species based on the sepal width
def his_sw():
    plt.figure(figsize=(7,5))
    plt.hist([setosa_sw, versicolor_sw, virginica_sw], color = col,  label = lab, edgecolor = 'darkslategray')
    plt.title('Sepal Width', color ='darkslategray')
    plt.xlabel('Sepal Width(cm)', color ='darkslategray')
    plt.ylabel('Count', color = 'darkslategray')
    plt.legend(leg)
    plt.savefig('Sepal Width Hist.png')
    plt.show()

# Petal Length - this function will output the histogram for all 3 species based on the petal length
def his_pl():
    plt.figure(figsize=(7,5))
    plt.hist([setosa_pl, versicolor_pl, virginica_pl], color = col,  label = lab, edgecolor = 'darkslategray')
    plt.title('Petal Length', color ='darkslategray')
    plt.xlabel('Petal Length(cm)', color ='darkslategray')
    plt.ylabel('Count', color = 'darkslategray')
    plt.legend(leg)
    plt.savefig('Petal Length Hist.png')
    plt.show()

# Petal Width - this function will output the histogram for all 3 species based on the petal width
def his_pw():
    plt.figure(figsize=(7,5))
    plt.hist([setosa_pw, versicolor_pw, virginica_pw], color = col,  label = lab, edgecolor = 'darkslategray')
    plt.title('Petal Width', color ='darkslategray')
    plt.xlabel('Petal Width(cm)', color ='darkslategray')
    plt.ylabel('Count', color = 'darkslategray')
    plt.legend(leg)
    plt.savefig('Petal Width Hist.png')
    plt.show()

# Merging all previous function to one
def his():
    his_sl()
    his_sw()
    his_pl()
    his_pw()

# This is a scatter plot chart using all information from dataset of all 3 species comparing Sepal Length and Width.
# It has the trend lines for all data points for each species so I could see the correlation between the species.
# I addedd the trend line for all data points combined to show the general overview of dataset for specific variables.

plt.figure(figsize=(7,5))
sns.scatterplot(x='Sepal Length', y='Sepal Width', data=iris, hue='Species')

# Add trend lines for all data points

sns.regplot(x='Sepal Length', y='Sepal Width', data=iris, scatter=False, lowess=True, color='yellow')

# Separating the trend lines for each species.
species_list = iris['Species'].unique()
for species in species_list:
    block = iris[iris['Species'] == species]
    sns.regplot(x='Sepal Length', y='Sepal Width', data=block, scatter=False, logx=True, label=species)
plt.title('Sepal Length vs Width', color ='darkslategray')
plt.xlabel('Sepal Length (cm)', color='darkslategray')
plt.ylabel('Sepal Width (cm)', color='darkslategray')
plt.legend()
plt.savefig('Scatter plot Sepal Length vs Width.png')
plt.show()

# This is a scatter plot chart using all information from dataset of all 3 species comparing Petal Length and Width.

plt.figure(figsize=(7,5))
sns.scatterplot(x='Petal Length', y='Petal Width', data=iris, hue='Species')

# Add trend lines for all data points

sns.regplot(x='Petal Length', y='Petal Width', data=iris, scatter=False, lowess=True, color='yellow')

# Separating the trend lines for each species.
species_list = iris['Species'].unique()
for species in species_list:
    block = iris[iris['Species'] == species]
    sns.regplot(x='Petal Length', y='Petal Width', data=block, scatter=False, logx=True, label=species)
plt.title('Petal Length vs Width', color ='darkslategray')
plt.xlabel('Petal Length (cm)', color='darkslategray')
plt.ylabel('Petal Width (cm)', color='darkslategray')
plt.legend()
plt.savefig('Scatter plot Petal Length vs Width.png')
plt.show()

# This is pair plot

sns.pairplot(data = iris, hue = 'Species', palette = 'Set2')
plt.savefig('Pair Plot.png')
plt.legend()
plt.show()

# Box plot for Sepal Length by Species
plt.figure(figsize=(7,5))
plt.subplot(1,2,1)
sns.boxplot(x = 'Species', y = 'Sepal Length', data = iris, palette = 'Set2')
plt.title('Sepal Length(cm) vs Species', color ='darkslategray')
plt.xlabel('Species', color ='darkslategray')
plt.ylabel('Sepal Length', color = 'darkslategray')

plt.subplot(1,2,2)
sns.boxplot(x = 'Species', y = 'Sepal Width', data = iris, palette = 'Set2')
plt.title('Sepal Width(cm) vs Species', color ='darkslategray')
plt.xlabel('Species', color ='darkslategray')
plt.ylabel('Sepal Width', color = 'darkslategray')
plt.tight_layout()
plt.savefig('Sepal Box Chart.png')
plt.show()

# Box plot for Petal Length by Species
plt.subplot(1,2,1)
sns.boxplot(x = 'Species', y = 'Petal Length', data = iris, palette = 'Set2')
plt.title('Petal Length(cm) vs Species', color ='darkslategray')
plt.xlabel('Species', color ='darkslategray')
plt.ylabel('Petal Length', color = 'darkslategray')

plt.subplot(1,2,2)
sns.boxplot(x = 'Species', y = 'Petal Length', data = iris, palette = 'Set2')
plt.title('Petal Width(cm) vs Species', color ='darkslategray')
plt.xlabel('Species', color ='darkslategray')
plt.ylabel('Petal Width', color = 'darkslategray')
plt.tight_layout()
plt.savefig('Petal Box Chart.png')
plt.show()

