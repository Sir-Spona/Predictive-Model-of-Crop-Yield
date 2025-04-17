# Predictive-Model-of-Crop-Yield

This App is built by me to predict crop yield based on environmental factors and farm features
The dataset was optained from Kaggle, designed for the prediction of crop yield in agricultural farms. It includes 3000 data points generated through a set of simulated environmental and farming features. These features—such as rainfall, soil quality, farm size, sunlight hours, and fertilizer usage—have been carefully selected to represent key factors that affect crop productivity.

The crop yield values (in tons per hectare) are generated using a predefined equation that combines the effects of these factors. This dataset is ideal for exploring regression models, testing machine learning algorithms, or building predictive models for agricultural analysis.

MACHINING LEARNING PROCESS
#Import Libriarires and Data
The process of building a machine learning began with importing the necessary libraries like pandas, numpy, scikilearn etc and the the data

#Data Cleaning and Preprocessing
The data was already cleaned from the source, so there was no cleaning, hence, I went further to seperate the data into train and test. 
The next thing was feature scaling and selection

#Model Training and Evaluation
The model was fisrt trained using RandomForestRegressor but I was not satisfied with the outcome. I later trained it with LinearRegression model.

#STREAMLIT
After training the model, I later used streamlit to build a predictive model by loading sterialized model and creating logic for prediction.

#DEPLOYMENT
The model was finally deploy using GitHub.
