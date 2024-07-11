from utils import get_population, data_by_country
from read_csv import read_csv
from charts import generate_bar_chart, generate_pie_chart


def run():
  data = read_csv('./app/data.csv')
  world_population_percentage = {
    country['Country/Territory'] : \
    country['World Population Percentage'] for country in data \
    if country['Continent'] == 'South America'
  }
  countries, population = world_population_percentage.keys(), \
  world_population_percentage.values()
  generate_pie_chart(countries, population)

'''
def run():
  data = read_csv('./app/data.csv')
  country = input('Insert a country: ')
  
  country_data = data_by_country(data, country)

  if len(country_data) > 0:
    country = country_data[0]
    labels, values = get_population(country)
    generate_bar_chart(labels, values)
'''

if __name__ == '__main__':
  run()
