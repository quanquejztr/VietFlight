# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

# Define lists of airports and dates
origin_airports = ['BMV', 'CAH', 'VCA', 'VCS', 'DLI', 'DAD', 'DIN', 'VDH', 'VDO', 'HPH', 'HAN', 'SGN', 'HUI', 'CXR', 'PQC', 'PXU', 'UIH', 'VKG', 'VCL', 'THD', 'TBB', 'VII']
destination_airports = ['BMV', 'CAH', 'VCA', 'VCS', 'DLI', 'DAD', 'DIN', 'VDH', 'VDO', 'HPH', 'HAN', 'SGN', 'HUI', 'CXR', 'PQC', 'PXU', 'UIH', 'VKG', 'VCL', 'THD', 'TBB', 'VII']
dates = ['2024-06-26','2024-06-27','2024-06-28','2024-06-29', '2024-06-30', '2024-07-01', '2024-07-02', '2024-07-03', '2024-07-04', '2024-07-05', '2024-07-06','2024-07-07','2024-07-08','2024-07-09','2024-07-10','2024-07-11','2024-07-12','2024-07-13','2024-07-14','2024-07-15']

# Iterate over origin airports
for origin in origin_airports:
    flights_info = []  # Initialize the list to collect all flights for the current origin

    # Iterate over destination airports and dates
    for destination in destination_airports:
        for date in dates:
            # Skip if the origin and destination are the same
            if origin != destination:
                # Construct the Google Flights URL
                url = f'https://www.google.com/travel/flights?q=Flights%20to%20{destination}%20from%20{origin}%20on%20{date}%20oneway%20nonstop&curr=VND'

                # Initialize the Selenium WebDriver
                driver = webdriver.Chrome()
                driver.get(url)

                try:
                    # Initialize the WebDriverWait object
                    wait = WebDriverWait(driver, 2)

                    # Wait until the departure time elements are present
                    wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[@role="text" and contains(@aria-label, "Departure time: ")]')))

                    # Find the departure time, arrival time, airline, flight time, and flight price elements
                    departure_elements = driver.find_elements(By.XPATH, '//span[@role="text" and contains(@aria-label, "Departure time: ")]')
                    arrival_elements = driver.find_elements(By.XPATH, '//span[@role="text" and contains(@aria-label, "Arrival time: ")]')
                    airline_elements = driver.find_elements(By.XPATH, '//div[@class="sSHqwe tPgKwe ogfYpf"]/span')
                    flight_times = driver.find_elements(By.XPATH, '//div[@class= "gvkrdb AdWm1c tPgKwe ogfYpf"]')
                    flight_prices = driver.find_elements(By.XPATH, '//div[@class="BVAVmf I11szd POX3ye"]//span[@role="text"]')

                    # Iterate over the lists and extract the flight information
                    for i in range(len(departure_elements)):
                        departure_time = departure_elements[i].text
                        arrival_time = arrival_elements[i].text
                        airline = airline_elements[i].text
                        flight_time = flight_times[i].text
                        flight_price = flight_prices[i].text
                        flights_info.append([origin, destination, departure_time, arrival_time, airline, flight_time, date, flight_price])
                
                # Handle exceptions
                except Exception as e:
                    print(f"An error occurred for {origin} to {destination} on {date}: {str(e)}")
                
                finally:
                    # Quit the WebDriver
                    driver.quit()
    
    # If there is flight information for the origin
    if flights_info:
        # Create a DataFrame from the flight information
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

