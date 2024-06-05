from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

origin_airports = ['BMV', 'CAH', 'VCA', 'VCS', 'DLI', 'DAD', 'DIN', 'VDH', 'VDO', 'HPH', 'HAN', 'SGN', 'HUI', 'CXR', 'PQC', 'PXU', 'UIH', 'VKG', 'VCL', 'THD', 'TBB', 'VII']
destination_airports = ['BMV', 'CAH', 'VCA', 'VCS', 'DLI', 'DAD', 'DIN', 'VDH', 'VDO', 'HPH', 'HAN', 'SGN', 'HUI', 'CXR', 'PQC', 'PXU', 'UIH', 'VKG', 'VCL', 'THD', 'TBB', 'VII']
dates = ['2024-06-13', '2024-06-14', '2024-06-15', '2024-06-16', '2024-06-17', '2024-06-18', '2024-06-19', '2024-06-20']

for origin in origin_airports:
    flights_info = []  # Initialize the list here to collect all flights for the current origin

    for destination in destination_airports:
        for date in dates:
            if origin != destination:
                url = f'https://www.google.com/travel/flights?q=Flights%20to%20{destination}%20from%20{origin}%20on%20{date}%20oneway%20nonstop&curr=VND'
                print(f"Processing URL: {url}")
                driver = webdriver.Chrome()
                driver.get(url)

                try:
                    wait = WebDriverWait(driver, 10)
                    
                    # Wait until the elements are present
                    wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[@role="text" and contains(@aria-label, "Departure time: ")]')))
                    
                    departure_elements = driver.find_elements(By.XPATH, '//span[@role="text" and contains(@aria-label, "Departure time: ")]')
                    arrival_elements = driver.find_elements(By.XPATH, '//span[@role="text" and contains(@aria-label, "Arrival time: ")]')
                    airline_elements = driver.find_elements(By.XPATH, '//div[@class="sSHqwe tPgKwe ogfYpf"]/span')
                    flight_times = driver.find_elements(By.XPATH, '//div[@class= "gvkrdb AdWm1c tPgKwe ogfYpf"]')
                    flight_prices = driver.find_elements(By.XPATH, '//div[@class="BVAVmf I11szd POX3ye"]//span[@role="text"]')

                    # Check if all lists have the same length
                    for i in range(len(departure_elements)):
                        departure_time = departure_elements[i].text
                        arrival_time = arrival_elements[i].text
                        airline = airline_elements[i].text
                        flight_time = flight_times[i].text
                        flight_price = flight_prices[i].text
                        flights_info.append([origin, destination, departure_time, arrival_time, airline, flight_time, date, flight_price])
                
                except Exception as e:
                    print(f"An error occurred for {origin} to {destination} on {date}: {str(e)}")
                
                finally:
                    driver.quit()
    
    if flights_info:
        df = pd.DataFrame(flights_info, columns=['Origin_Airport', 'Destination_Airport', 'Departure_Time', 'Arrival_Time', 'Airline', 'Duration', 'Date', 'Price'])
        file_name = f"flights_['{origin}'].csv"

        # Save to a single CSV file for each origin
        if os.path.exists(file_name):
            print(f"The file '{file_name}' already exists. Appending new data.")
            df.to_csv(file_name, mode='a', index=False, header=False)
        else:
            print(f"The file '{file_name}' does not exist. Creating a new file.")
            df.to_csv(file_name, index=False)
    else:
        print(f"No flight information found for {origin}.")
