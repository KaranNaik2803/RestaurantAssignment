# Restuarant Scraping :
--------------
## Modules used : Requests, Os, BeautifulSoup and Json

### PREREQUISITES NEEDED:
- Installation of different modules using pip:  
`pip install requests / pip3 install requests`<br>
`pip install BeautifulSoup / pip3 install BeautifulSoap`

### STEPS INVOLVED:
### User Input: 
- The script prompts the user to input the name of the *city* { For eg.: Goa, Bengaluru}

### Web Scraping with requests and bs4: 
- It then searches for the top 10 restaurants in that city using a Google search query. 
- The search URL is constructed by combining the base Google search URL, along with the city name.

### Parsing HTML: 
- The *requests* library fetches the HTML content of the Google search result page. 
- Then, *BeautifulSoup* parses this HTML to extract the restaurant information, like the restaurant name, rating, and review count.

### Storing in JSON: 
- The extracted restaurant details are stored in a Python dictionary and then saved into a JSON file. 
- The restaurant names are used as keys, and details such as ratings and reviews are stored as values.