# Machine-Learning-Linear-Regression

###### The project

This project is an example of using datasets to perform a linear regression analysis in python with the help of matplotlib, numpy and sklearn. A diabetes dataset is used to perform linear regression to find the best fit line through the data. In the dataset used, the last 20 observations are used for testing and the rest of the data is used for training the model. Instead of using **linear_model.LinearRegression()** from **sklearn**, a function was written to make use of numpy to calculate the gradient and the y-intercept of the line of best fit, which has the equation _y = mx + b_. The equations below describe how both the gradient and the y-intercept can be calculated from the training data and labels. 

The calculated values are used to produce a figure with the following:
* Scatter plot of training data colored red.
* Scatter plot of testing data colored green.
* Line graph for the best-fit line colored blue.
* Legend.

###### Usefulness

This project is useful in the sense that it provides a base understanding of how a dataset can be used for testing a model, trainging a model and performing a linear regression analysis that is necessary in understanding the relationship between two variables.

###### Maintainers and contributers 

Egor Zakharov

###### Running the program

Getting the program to work is fairly simple and works as follows:

* You will need to install SciPy, Numpy, Matplotlib and Sci-Kit Learn. For more information on installing python packages see https://packaging.python.org/tutorials/installing-packages/
* Download linearRegression.py
* Run the code in an IDE that supports python
* A new window will open up with a figure containing the aspects outlined above
