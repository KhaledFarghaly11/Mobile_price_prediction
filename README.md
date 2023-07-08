# **Mobile Price Classification**
This repository contains a machine learning project that focuses on predicting the price range of mobile phones based on various attributes. The dataset used in this project includes features such as battery power, Bluetooth availability, camera specifications, memory capacity, screen dimensions, and more.

## **Dataset Description**
The dataset includes the following features:

* `Id`: ID
* `battery_power`: Total energy a battery can store in one time (mAh)
* `blue`: Has Bluetooth or not (0: No, 1: Yes)
* `clock_speed`: Speed at which the microprocessor executes instructions
* `dual_sim`: Has dual SIM support or not (0: No, 1: Yes)
* `fc`: Front Camera megapixels
* `four_g`: Has 4G network support or not (0: No, 1: Yes)
* `int_memory`: Internal memory in gigabytes
* `m_dep`: Mobile depth in centimeters
* `mobile_wt`: Weight of the mobile phone
* `n_cores`: Number of cores of the processor
* `pc`: Primary Camera megapixels
* `px_height`: Pixel resolution height
* `px_width`: Pixel resolution width
* `ram`: Random Access Memory in megabytes
* `sc_h`: Screen height of the mobile in centimeters
* `sc_w`: Screen width of the mobile in centimeters
* `talk_time`: Longest time that a single battery charge will last
* `three_g`: Has 3G network support or not (0: No, 1: Yes)
* `touch_screen`: Has touch screen or not (0: No, 1: Yes)
* `wifi`: Has WiFi or not (0: No, 1: Yes)
* `price_range`: Target variable with values 0 (low cost), 1 (medium cost), 2 (high cost), and 3 (very high cost)

## **Objective**
The objective of this classification task is to develop a machine learning model that accurately predicts the price range of mobile phones based on their attributes. By following the machine learning workflow, this project covers various steps such as data exploration, data visualization, feature engineering, feature selection, model training with hyperparameter tuning, evaluation of models, and selection of the best model.

## **Project Workflow**
1. Data Exploration: Explore the dataset and provide descriptive statistics to gain insights into the data.

2. Data Visualization: Perform data visualization to visualize the relationships and distributions of various features. Provide comments on each graph to explain the observations.

3. Data Transformations and Feature Engineering: Apply necessary data transformations and feature engineering techniques to preprocess the data. Provide justification for each step taken.

4. Feature Selection: Select the most relevant features for the prediction task. Discuss the reasons behind the selection.

5. Model Training and Hyperparameter Tuning: Train multiple classification models using the provided train.csv dataset. Perform hyperparameter tuning to optimize the models' performance.

6. Model Evaluation: Evaluate the trained models on the training and testing data using classification scores such as accuracy, precision, recall, and F1-score. Provide comments on the results and discuss the model performance.

7. Selecting the Best Model: Select the best-performing model based on the evaluation results. Save the selected model as a pickle (.pkl) file for future use.

8. Serving Predictions as an API: Implement a Flask framework to serve predictions as an API for easy integration with other applications.

Feel free to explore the code, datasets, and results in this repository. Follow the README instructions within each directory for more details on the specific steps of the project.

For any questions or suggestions, please reach out. Happy coding!
