# **Iris data set - Project**
***
### **<ins>Table of Contents</ins>**
* **Introduction** 
    * Aims
    * Iris Flowers
    * Iris data set
* **Investigation** 
    * Set up 
    * Data download 
    * Data insight
* **Data visualization**
    * Variables relation 
    * Histograms
    * Scatter plot
    * Pair plot
    

---


## **Introduction**

### **Aims**
This project aims to use the Iris dataset to demonstrate different analysis using Python with the level of skills acquired during the course. I show the research and 
exploration done on the dataset and, as a result, display/render the data to better understand the data within it, the differences, and how they compare. 

### **Iris flowers**

Iris is the largest genus of the family Iridaceae with up to 300 species. [Plants of the World Online](https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:326330-2) 
lists 312 accepted species from this genus as of 2024. 
In general, the Iris’ meaning is sent to present faith, hope and wisdom, but it can vary depending on the variety and colour of the flowers.
These classic flowers derive their name from the Greek goddess of the rainbow and come in a stunning array of vibrant colours.

### **Iris flower data set**

![6874747073c6561726e696e672e706e67)](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png)

Three of Iris varieties (_Iris Setosa_, _Iris Virginica_ and _Iris Versicolor_) are used in the [Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set)  
outlined by the British statistician and biologist [Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) in his 1936 paper '[The use of multiple measurements in taxonomic 
problems](https://digital.library.adelaide.edu.au/dspace/bitstream/2440/15227/1/138.pdf)' as an example of linear discriminant analysis.

The data set consist of 50 samples from each of three species, representing a total of 150 observation. Four attributes are measured from each sample: sepal length, sepal 
width, petal length, and petal width. The measurement was made in centimetres.

---

## **Investigation**

### **Set up**

We need to set up environment to be able to write and run the code for any analysis we want to explore.

I would suggest using below programs:
* [Visual studio code (VSC)](https://code.visualstudio.com/) – is a free, open-source code editor used for coding.
* [Python](https://www.python.org/downloads/) – is a general-purpose programming language, not specialized for any specific problems, and used to create a various program.
* [GitHub](https://github.com/) - it is a repository that helps developers store, manage track, and make a change to their codes.

### **Import libraries**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
I used the numpy for working with arrays. To be able to download, read, manipulate and analysis the iris data set I used pandas’ function. The matplotlib.pyplot is module which has many different functions for plotting. I used it to create and customise my plots. Seborn is a library that uses Matplotlib underneath to plot graphs. It's another visualization tool I've used because it provides a beautiful default style and colour palettes.

### **Data download**

The data set was downloaded from [https://archive.ics.uci.edu/dataset/53/iris](https://archive.ics.uci.edu/dataset/53/iris). 

### **Data insight**

After I download aniris dataset, I want to review the data to get an overview of what's in the dataset.
To run the python program, use the **'analysis.py'** and run through the Visual Studio Code. All outputs are written in **'summary.txt'** file or saved as individual **png** files.

The overal iris dataset statistic display the top 5 and last 5 rows and provide the total account of rows and columns.

![image]()

The iloc function below displays the third row from dataset.

![image]()

The describe() method returns summary statistics of the numeric values for each variable. Below are summary rows returned:
 * count - total number of the values, which are not-empty
 * mean - this is an average value
 * std - this is standard deviation
 * min - this is minimum value
 * 25% - shows the 25% - how many of the values in dataset are less than given percentile
 * 50% - shows the 50% - how many of the values in dataset are less than given percentile
 * 75% - shows the 75% - how many of the values in dataset are less than given percentile
 * max - this is maximum value

 ![image]()

 This shows the mean value of all 4 variables for each 3 species.

 ![image]()

---

 ## **Data Visualization**

### **Variables relation**

Below are 4 bar charts represending relationship between each variable (Sepal Length, Sepal Width, Petal Length, Petal Width) and 3 different species based on mean (averaga) value.

![image1](Sepal Length)
![image2](Sepal Width)
![image3](Petal Length)
![image4](Petal Width)

The species Iris-virginica has the largest Sepal & Petal length. Iris-setosa has the largest Sepal width, but the smallest length and width of the Petals. In the case of Iris-versicolor, there is not much difference between all 4 variables.

### **Histograms**

I created 4 different histograms for all 3 species based on 4 variables.

![image1](hist Sepal Length)
![image2](hist Sepal Width)
![image3](hist Petal Length)
![image4](hist Petal Width)

The highest number / frequency of length Sepal has the species Iris-setosa.
The highest number / frequency of Sepal Width has the species Iris-setosa and Iris-virginica.
The highest number / frequency of Petal Length has Iris-setosa, lower Iris-virginica.
The highest number / frequency of Petal Width again has Iris-setosa and lower Iris-virginica.

### **Scatter plot**

Below is a scattered graph comparing the length and width of Sepal for all 3 species.

![image](scatter plot Sepal Length & Width)

This is a scatterred graph comparing the length and width of Petal for all 3 species.

![image](scatter plot Petal Length & Width)

### **Pair plot**

A pair plot is a matrix of scatter plots that allow us easily to take a dataset and generate a relationship between each pair of variables. It consists of histograms and scatter plots that create a nice visualization and summarize a large amount of data in a single image.

![image](Pair Plot)

### **Box plot**






