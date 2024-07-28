# VietFlight
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

##Introduction
The flightfare in Vietnam in recent year has changed dramatically, making it crucial for passengers to be able to predict ticket price for their upcoming trips. This project's primary objective is to analyze and suggest what are the best ways to plan their trip effectively. I also develop a model capable of predicting flight fares with 92% accuracy using historical flight data. The model will empower the decision-making process for passengers to optimize their schedule.

## About the project

The data in this project is collected using Selenium library from Python. A script is developed and gathered from **Google Flights**, with 5 major airlines, spanning in the period of 38 days (from 26 Jun to 15 Jul, and 30 Jul to 17 Aug), and all is non-stop routes between airport in Vietnam.

Columns in CSV file:
- Origin_Airport: Airport of origin
- Destination_Airport: Airport of destination
- Departure_time: Departure time
- Arrival_time: Arrival time
- Airline: Carrier
- Duration: Flight time
- Date: Date
- Price: Flight price
- ** Note**: All flights in this project are non-stop flights.

## Model Building 

The data was split into 70% training and 30 % test set. 5 models were tested and the results are of following:

| Model | Accuracy Rate | R2 Score |
|:---:|:---:|:---:|
| ExtraTreesRegressor Model | 91.01% | 69.81%|
| Linear Regression Model | 82.52%  | 29.59%|
| Random Forest Model| 91.13% |	62.52%|
|Ridge Model| 82.53%| 29.58%|
|Lasso Model| 82.53%| 29.59%|

Therefore, Random Forest model is able to predict flight ticket prices within around  ≈ 163,004 VND (≈ 6.43 USD)

## Installation
This project is written in Python 3.12.2. You are expected to have Python installed already before cloning this project from Github.

To install the required packages and libraries for this project, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

Raw, unmerged dataset can be found **[here](https://github.com/quanquejztr/VietFlight/tree/main/raw_data)**, while cleaned, merged can be found **[here](https://github.com/quanquejztr/VietFlight/blob/main/flights.csv)**.

## Directory Tree 
```
├── Images  
|	└── raw_data.png 
├── Raw Data 
│ 	├── flights['BMV'].csv 
│ 	├── flights['CAH'].csv 
│ 	├── flights['CXR'].csv 
│ 	├── flights['DAD'].csv 
│ 	├── flights['DIN'].csv 
│ 	├── flights['DLI'].csv 
│ 	├── flights['HAN'].csv 
│ 	├── flights['HPH'].csv 
│ 	├── flights['HUI'].csv 
│ 	├── flights['PQC'].csv 
│ 	├── flights['PXU'].csv 
│ 	├── flights['SGN'].csv 
│ 	├── flights['TBB'].csv 
│ 	├── flights['THD'].csv 
│ 	├── flights['UIH'].csv 
│ 	├── flights['VCA'].csv 
│ 	├── flights['VCL'].csv 
│ 	├── flights['VCS'].csv 
│ 	├── flights['VDH'].csv 
│ 	├── flights['VDO'].csv 
│ 	├── flights['VII'].csv 
│ └── flights['VKG'].csv 
├── Data Cleaning.ipynb 
├── Flight Analysis.ipynb 
├── Flight Price Prediction.ipynb 
├── Flights.csv 
├── LICENSE 
├── README.md 
└── Web Scraping.py
```
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
## Contact Information
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/stephenluong04/)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://www.instagram.com/ltcunnn/)
