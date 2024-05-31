from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os

origin_airports = ['BMV', 'CAH', 'VCA', 'VCS', 'DLI', 'DAD', 'DIN', 'VDH', 'VDO', 'HPH', 'HAN', 'SGN', 'HUI', 'CXR', 'PQC', 'PXU', 'UIH', 'VKG', 'VCL', 'THD', 'TBB', 'VII']
destination_airports = ['BMV', 'CAH', 'VCA', 'VCS', 'DLI', 'DAD', 'DIN', 'VDH', 'VDO', 'HPH', 'HAN', 'SGN', 'HUI', 'CXR', 'PQC', 'PXU', 'UIH', 'VKG', 'VCL', 'THD', 'TBB', 'VII']
dates = ['2024-06-12', '2024-06-13', '2024-06-14', '2024-06-15', '2024-06-16', '2024-06-17', '2024-06-18', '2024-06-19', '2024-06-20']

flights_info = []

for origin in origin_airports:
    for destination in destination_airports:
        for date in dates:
            if origin != destination:
                
                    #Constructing url
                    url = f'https://www.google.com/travel/flights?q=Flights%20to%20{destination}%20from%20{origin}%20on%20{date}%20oneway%20nonstop&curr=VND'
                    
                    #Loading webpage in Chrome
                    driver = webdriver.Chrome()
                    driver.get(url)
                    time.sleep(1)
                    
                    try:
                        #Locating for elements to extract data from HTML
                        departure_times = driver.find_elements(By.XPATH, '//span[@role="text" and contains(@aria-label, "Departure time: ")]')
                        arrival_times = driver.find_elements(By.XPATH, '//span[@role="text" and contains(@aria-label, "Arrival time: ")]')
                        airliners = driver.find_elements(By.XPATH, '//div[@class="sSHqwe tPgKwe ogfYpf"]/span')
                        flight_times = driver.find_elements(By.XPATH, '//div[@class= "gvkrdb AdWm1c tPgKwe ogfYpf"]')
                        flight_prices = driver.find_elements(By.XPATH, '//div[@class="BVAVmf I11szd POX3ye"]//span[@role="text"]')

                        for i in range(len(departure_time)):
                            departure_time = departure_times[i].text
                            arrival_time = arrival_times[i].text
                            airline = airliners[i].text
                            flight_time = flight_times[i].text
                            flight_price = flight_prices[i].text
                            flights_info.append([origin, destination, departure_time, arrival_time, airline, flight_time, date, flight_price])
                    except Exception as e:
                        print(f"An error occurred for {origin} to {destination} on {date}: {str(e)}")
                        continue

                    driver.quit()
#Save data into a dataframe
df = pd.DataFrame(flights_info, columns=['Origin_Airport', 'Destination_Airport', 'Departure_Time', 'Arrival_Time', 'Airline', 'Duration', 'Date', 'Price'])

# Check if the file already exists
if os.path.exists('flights_data.csv'):
    print(f"The file 'flights_{origin_airports}.csv' already exists.")
    # Append new data to existing CSV file
    df.to_csv(f'flights_{origin_airports}.csv', mode='a', index=False, header=False)
else:
    print(f"The file 'flights_{origin_airports}.csv' does not exist. Creating a new file.")
    # Create a new CSV file and write data to it
    df.to_csv(f'flights_{origin_airports}.csv', index=False)
