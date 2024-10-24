# Used-Car-Price-Prediction
* Created a tool capable of predicting the price of used cars based on features such as KM driven, mileage, etc.
* Data was sourced from Kaggle.
* Data link: [Kaggle Dataset](https://www.kaggle.com/datasets/sukritchatterjee/used-cars-dataset-cardekho)
* Developed a pipeline using DVC that includes data extraction, data cleaning, data processing, and model training.
* Optimized Gradient Boosting Regressor, AdaBoost Regressor, Ridge Regressor, Linear Regressor, Random Forest Regressor, and XGBoost Regressor to identify the best model.
* Utilized MLFlow for model versioning.


## Code and Resources Used 
**Python Version:** 3.12.1  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, flask, joblib, xgboost, dvc, mlflow, 

## DATA CLEANING
This step involved the following: 
* Removing Duplicate Row and Columns.
* Cleaning the misspelled data in the categorical columns. For eg: in Fuel_Supply Column: Values like "mpfi", "multi-point injection", "mpfi+lpg", "mpfi+cng", should all be categorized as Multi-Point Fuel Injection.
* Converting features which should be numerical, to numerical. For eg: Engine Capacity has values like 1800cc. This should be a numerical feature.

        
## DATA PROCESSING
This step involved the following: 
* Handling Null Values.
* Removing Un-important columns based on statistical tests.
* Encoding Categorical Features.

## MODEL TRAINING
This step involved creating a comprehensive pipeline that processes the data and trains models including Gradient Boosting Regressor, AdaBoost Regressor, Ridge Regressor, Linear Regressor, Random Forest Regressor, and XGBoost Regressor. The models were optimized and hyperparameters were fine-tuned using GridSearchCV. The best model was then saved for prediction.

## Data Versioning
Data versioning and pipeline management were handled using DVC. At each stage, such as data cleaning and data processing, the output dataframe was stored in the artifacts folder, which was tracked using DVC.

## MLFlow
Model versioning was managed with MLFlow. All created models were tracked and analyzed using MLFlow, which facilitated the selection of the best model.

Random Forest Regressor emerged as the best model with an R² score of 0.95


## Deployment and Productionization

### Dockerization
* The model was deployed via a Flask API and containerized using Docker to ensure consistency across environments. This allows for seamless deployment and version control across different systems.
* Docker ensures that the environment, libraries, and dependencies remain consistent, simplifying the process of deploying the model to different servers or cloud platforms.

### Logging Pipeline
* Integrated a logging pipeline using Python and MySQL Database.
* The logs capture key events during model inference and API usage, providing insights into API requests, prediction outcomes, and potential errors.
* This setup enhances system monitoring and performance tracking in production, making it easier to identify bottlenecks and improve user experience.

### End-User Application
* Built a Flask API hosted on a local server.
* The end-user application accepts input variables such as Car Model Name, KM Driven, and other relevant features.
* Based on this data, the car price is predicted using the Random Forest model.

## Set Up Project Locally

To set up the project locally, follow these steps:

* Clone the repository:
   ```bash
   git clone https://github.com/ArnabMitra0408/Used-Car-Price-Prediction.git

* Go to the cloned directory:
    ```bash
   cd Used-Car-Price-Prediction

* Install the required packages:
  ```bash
   pip install -r requirements.txt

* Run the DVC pipeline:
  ```bash
   dvc repro
* Build the docker image:
  ```bash
   docker build -t car-app .
* Pull mysql image:
  ```bash
   docker pull mysql
* Run Docker Compose:
  ```bash
  docker compose up
