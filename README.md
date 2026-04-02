# Greenhouse Gas Emission Analytics & Prediction

# Project Overview
This project analyzes greenhouse gas (GHG) emissions across U.S. industrial facilities using data from the EPA Greenhouse Gas Reporting Program (GHGRP) and the Supply Chain Greenhouse Gas Emission Factors dataset.
The objective of this analysis is to explore emission patterns, understand the carbon intensity of petroleum-related industries, and evaluate the feasibility of applying machine learning models to predict emission behavior.
The project demonstrates an end-to-end data analytics pipeline, including data ingestion, preprocessing, exploratory analysis, and machine learning modeling.

# Datasets
1. Supply Chain Greenhouse Gas Emission Factors
This dataset provides emission factors associated with economic activity across different industries based on NAICS classification.

2. EPA Greenhouse Gas Reporting Program (GHGRP) 2023
This dataset contains facility-level emission data reported by industrial facilities across the United States.

# Key attributes include:
State, Latitude and Longitude, Industry Type, CO₂ emissions, Methane emissions, Nitrous Oxide emissions, Total GHG emissions

# Technologies Used
Programming Languages: Python, R, SQL
Cloud Tools: AWS S3 (data storage), AWS EC2 (analysis environment), AWS RDS / MariaDB (data management), AWS Glue DataBrew (data cleaning and preprocessing)
Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn

# Methodology
The analysis followed a multi-stage data science workflow:

Data Ingestion
The datasets were uploaded to AWS S3 and stored in MariaDB using AWS RDS to enable structured querying and scalable data access.

Data Preprocessing
Data cleaning and transformation were performed using: Python and AWS Glue DataBrew

This included:
Handling missing values
Renaming and restructuring variables
Preparing datasets for statistical analysis

# Exploratory Data Analysis
Exploratory analysis was conducted to identify patterns and relationships between facility attributes and greenhouse gas emissions.
Examples of analysis performed:
Distribution of emissions across industries
Correlation analysis between different gas types
Facility emission patterns across states

# Machine Learning Models
Two machine learning approaches were applied: 
Random Forest Regression- Used to evaluate the predictive potential of facility attributes on emission levels.
K-Means Clustering- Used to identify patterns in emission behavior across facilities.

# Key Findings
Emission Profiles- Using K-Means clustering, three major facility emission patterns were identified:

Low Emission Facilities (majority of facilities)
High Methane Emission Facilities
High CO₂ / Nitrous Oxide Emission Facilities
Carbon Intensity

Petroleum-related industries were found to be significantly more carbon intensive, emitting approximately: 0.6 kg CO₂e per $1 of economic activity. This is nearly twice the emission intensity compared to many other sectors.

# Primary Pollutants
Methane (CH₄) was identified as the largest contributor to total emissions across many facilities.

# AI Prediction Feasibility
The analysis found that current facility-level datasets lack sufficient operational variables for accurate AI prediction models.

# Future predictive models would require:
Real-time operational data
Process-level variables
Continuous monitoring data
