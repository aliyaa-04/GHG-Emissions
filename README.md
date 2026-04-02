#Greenhouse Gas Emission Analytics & Prediction

#Overview: This project explores and analyzes greenhouse gas (GHG) emissions using two primary datasets: "Supply Chain Greenhouse Gas Emission Factors" and the "EPA Greenhouse Gas Reporting Program 2023". The study examines emission patterns across different facilities, the role of specific facility attributes, and the carbon intensity of the petroleum industry.

#Tech Stack Languages: Python, R, SQL.
#Cloud Platform: AWS (S3, EC2, RDS, and Glue DataBrew).
#Machine Learning: Random Forest Regression and K-Means Clustering.

#Key Findings: 
Emission Profiles- Leveraged K-Means clustering to identify three distinct facility behaviors: Low Emission (majority), High Methane, and High CO_{2}/Nitrous Oxide. 
Carbon Intensity: Analysis revealed that petroleum-related industries are twice as carbon-intensive as other sectors, emitting approximately 0.6 kg CO_{2}e per $1.

#AI Feasibility: Determined that current static facility datasets are insufficient for high-accuracy AI prediction, highlighting the critical need for real-time operational data and continuous monitoring.
Primary Pollutants: Identified Methane (CH_{4}) as the primary contributor to total emissions across the analyzed industrial facilities.

#Project Structure: ashaik33_Report.pdf: The full technical research paper.
#Project_Codes: Contains Python scripts for visualization, R scripts for Random Forest modeling, and SQL queries used for data exploration.

#Methodology: The workflow followed a multi-tool analytical approach- 
Data Ingestion: Hosted datasets in AWS S3 and RDS (MariaDB) for scalability.
Preprocessing: Utilized AWS Glue DataBrew and Python for data cleaning and handling missing values.
Analytics: Performed univariate and multivariate analysis to correlate facility attributes (State, Latitude, Industry Type) with emission outputs.
