# Using the url "https://restcountries.com/v3.1/all" write python program which will do the following.
# 1. Using the OOPS concepts for the following task.

# 2. Use the class constructor for taking the input of the mentioned URL for the task.
import requests

class Conductor:
    def __init__(self, url):
        self.url = url

    def fetch_url_content(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return response.text
            else:
                return f"Failed to fetch content. Status code: {response.status_code}"
        except requests.exceptions.RequestException as e:
            return f"Error fetching URL: {e}"

if __name__ == "__main__":
    # Example usage:
    url = input("Enter a URL: ")
    conductor = Conductor(url)
    content = conductor.fetch_url_content()
    print(content)




# 3.  Create a method that will fetch all the Json data from the mentioned url
import requests

class shruti:
    def __init__(self,web_url):
        self.url=web_url

    def fetch_data(self):
        response=requests.get(self.url)
        print(url)
        return response.json()
    
url="https://restcountries.com/v3.1/all"

s=shruti(url)
print(s.fetch_data())

# 4.Create a method that will display the name of the countries, currencies and currency symbols
import requests

class Shruti:
    def __init__(self, web_url):
        self.url = web_url

    def fetch_data(self):
        store_data = requests.get(self.url)
        return store_data.json()

    def fetch_name_currency_symbol(self):
        data_n_c_s = []
        for country_data in self.fetch_data():
            common_name = country_data.get('name', {}).get('common', '')
            currencies = country_data.get('currencies', {})
            symbols = []

            for currency_key, currency_info in currencies.items():
                symbol_name = currency_info.get('symbol', '')
                symbols.append(symbol_name)

            data_n_c_s.append({'name': common_name, 'currencies': list(currencies.keys()), 'symbols': symbols})

        return data_n_c_s

url = "https://restcountries.com/v3.1/all"
s = Shruti(url)
result = s.fetch_name_currency_symbol()


for country_info in result:
    print("Common Name:", country_info['name'])
    print("Currencies:", country_info['currencies'])
    print("Currency Symbols:", country_info['symbols'])
    print("="*30)

# 5. Write a method that will display all the countries that have dollar as its currency.
import requests

class Shruti:
    def __init__(self, web_url):
        self.url = web_url

    def fetch_data(self):
        store_data = requests.get(self.url)
        return store_data.json()

    def countries_with_dollar(self):
        data = self.fetch_data()
        dollar_countries = []

        for entry in data:
            name_info = entry.get('name')
            common_name = name_info.get('common')
            currencies = entry.get('currencies')
            
            if currencies:
                for currency in currencies:
                    currency_name = currencies[currency].get('name', '').lower()
                    
                    if 'dollar' in currency_name:
                        dollar_countries.append(common_name)

        return dollar_countries
    
url = "https://restcountries.com/v3.1/all"
s = Shruti(url)
result = s.countries_with_dollar()

for country_with_dollar in result:
    print("Common Name:", country_with_dollar)
    # You can't access 'country_info' here as it's not defined in your code
    print("=" * 30)


# 6. Write a method that will display all the countries that have euro as its currency.
import requests

class Shruti:
    def __init__(self, web_url):
        self.url = web_url

    def fetch_data(self):
        store_data = requests.get(self.url)
        return store_data.json()

    def countries_with_euro(self):
        data = self.fetch_data()
        euro_countries = []

        for entry in data:
            name_info = entry.get('name')
            common_name = name_info.get('common')
            currencies = entry.get('currencies')
            
            if currencies:
                for currency in currencies:
                    currency_name = currencies[currency].get('name', '').lower()
                    
                    if 'euro' in currency_name:
                        euro_countries.append(common_name)

        return euro_countries
    
url = "https://restcountries.com/v3.1/all"
s = Shruti(url)
result = s.countries_with_euro()

for country_with_euro in result:
    print("Common Name:", country_with_euro)
    # You can't access 'country_info' here as it's not defined in your code
    print("=" * 30)

# Visit the Url "https://www.openbrewerydb.org/" and write the python script which will do the following:
# 1. List the names of all breweries present in the states of Alaska, Maine and New York.
import requests

def fetch_breweries_in_states(states):
    base_url = "https://api.openbrewerydb.org/breweries"
    brewery_data = []

    for state in states:
        params = {"by_state": state}
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()  # Raise an exception if the request fails
            brewery_data.extend(response.json())
        except requests.exceptions.RequestException as e:
            print(f"Error fetching brewery data for {state}:", e)

    return brewery_data

# Define a list of states you want to fetch data for
states_to_fetch = ["Alaska", "Maine", "New_York"]
brewery_data = fetch_breweries_in_states(states_to_fetch)

if brewery_data:
    for brewery in brewery_data:
        print("Brewery Name:", brewery.get('name'))
        print("State:", brewery.get('state'))
        # Print other relevant brewery information here
        print("=" * 30)
else:
    print("Brewery data not found for the specified states.")

# 2. What is the count of breweries in the states mentioned above.
import requests

def fetch_breweries_in_states(states):
    base_url = "https://api.openbrewerydb.org/breweries"
    brewery_data = []

    for state in states:
        params = {"by_state": state}
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()  # Raise an exception if the request fails
            brewery_data.extend(response.json())
        except requests.exceptions.RequestException as e:
            print(f"Error fetching brewery data for {state}:", e)

    return brewery_data

# Define a list of states you want to fetch data for
states_to_fetch = ["Alaska", "Maine", "New_York"]
brewery_data = fetch_breweries_in_states(states_to_fetch)

if brewery_data:
    count = len(brewery_data)  # Calculate the count of breweries
    print(f"Total number of breweries in the specified states: {count}")
else:
    print("Brewery data not found for the specified states.")

# 3. Count the number of types of breweries present in the individual cities of the states mentioned above.