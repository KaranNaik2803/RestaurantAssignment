'''
Author: Karan Naik
Date: 23-10-2024
'''

import requests 
from bs4 import BeautifulSoup
import json
import os

# Define a function to fetch restaurant data
def get_restaurants(city):
    
    # Set up the search query to find top restaurants in the city
    search_url = f"https://www.google.com/search?sca_esv=9ee8fdcc760d43dd&rlz=1C1UEAD_enIN1080IN1080&tbm=lcl&sxsrf=ADLYWILyt6aGHLWra4zqgCbWsVY_bZTjKg:1729712715663&q=top+10+restaurants+in+{city.replace(' ', '+')}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }

    response = requests.get(search_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML response with BeautifulSoup
        latest_soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all relevant restaurant information
        restaurant_cards = latest_soup.find_all('div', {'class' : 'dbg0pd'})
        
        # Prepare a list to store restaurant data
        restaurants = {}

        # Extract up to 10 restaurant details
        for index, card in enumerate(restaurant_cards[:10]):
            name = card.get_text()
            rating = None
            review_count = None

            # Extract rating if available, by inspecting the HTML structure around the restaurant name
            rating_tag = card.find_next('span', {'class': 'yi40Hd YrbPuc'})
            if rating_tag:
                rating = rating_tag.get_text()

            # Extract review count, if available
            review_tag = rating_tag.find_next('span', {'class': 'RDApEe YrbPuc'}) if rating_tag else None
            if review_tag:
                review_count = review_tag.get_text()

            # Add the restaurant details to the dictionary
            restaurants[name] = {
                'Rating': rating,
                'Reviews': review_count
            }

        return restaurants
    else:
        print(f"Failed to retrieve data for {city}. Status Code: {response.status_code}")
        return None



# ------- Main script ---------------------
def main():
    
    # Prompt the user to enter a city
    city = input("Enter the name of a city: ").strip()

    # Fetch restaurant data for the specified city
    restaurants = get_restaurants(city)

    if restaurants:
        folder_name = "json_report"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            
        # Save the restaurant data to a JSON file
        filename = f"{city}_restaurants.json"
        folder_path = os.path.join(folder_name, filename)
        
        with open(folder_path, 'w') as json_file:
            json.dump(restaurants, json_file, indent=4)
        
        print(f"Top 10 restaurants in {city} saved to {folder_path}")
    else:
        print("No data available for the specified city.")


# Run the script
if __name__ == "__main__":
    main()