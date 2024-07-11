

def get_population(country_data):
  population_per_year = {
    '1970' : int(country_data['1970 Population']),
    '1980' : int(country_data['1980 Population']),
    '1090' : int(country_data['1990 Population']),
    '2000' : int(country_data['2000 Population']),
    '2010' : int(country_data['2010 Population']),
    '2015' : int(country_data['2015 Population']),
    '2020' : int(country_data['2020 Population']),
    '2022' : int(country_data['2022 Population'])
  }
  return population_per_year.keys(), population_per_year.values()

def data_by_country(data, country):
  country_data = list(filter(lambda item : item['Country/Territory'] == country, data))
  return country_data