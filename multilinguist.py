import requests
import json

class Multilinguist:
  """This class represents a world traveller who knows 
  what languages are spoken in each country around the world
  and can cobble together a sentence in most of them
  (but not very well)
  """

  translatr_base_url = "http://bitmakertranslate.herokuapp.com"
  countries_base_url = "https://restcountries.eu/rest/v2/name"
  #{name}?fullText=true
  #?text=The%20total%20is%2020485&to=ja&from=en

  def __init__(self):
    """Initializes the multilinguist's current_lang to 'en'
    
    Returns
    -------
    Multilinguist
        A new instance of Multilinguist
    """
    self.current_lang = 'en'

  def language_in(self, country_name):
    """Uses the RestCountries API to look up one of the languages
    spoken in a given country

    Parameters
    ----------
    country_name : str
         The full name of a country.

    Returns
    -------
    bool 
        2 letter iso639_1 language code.
    """
    params = {'fullText': 'true'}
    response = requests.get(f"{self.countries_base_url}/{country_name}", params=params)
    json_response = json.loads(response.text)
    return json_response[0]['languages'][0]['iso639_1']

  def travel_to(self, country_name):
    """Sets current_lang to one of the languages spoken
    in a given country

    Parameters
    ----------
    country_name : str
        The full name of a country.

    Returns
    -------
    str
        The new value of current_lang as a 2 letter iso639_1 code.
    """
    local_lang = self.language_in(country_name)
    self.current_lang = local_lang
    return self.current_lang

  def say_in_local_language(self, msg):
    """(Roughly) translates msg into current_lang using the Transltr API

    Parameters
    ----------
    msg : str
        A message to be translated.

    Returns
    -------
    str
        A rough translation of msg.
    """
    params = {'text': msg, 'to': self.current_lang, 'from': 'en'}
    response = requests.get(self.translatr_base_url, params=params)
    json_response = json.loads(response.text)





    try: #Tries to run this.
      return json_response['translationText']
    except: #If it fails then it returns something else. This prevents the app from crashing.
      return "Nope!"
    pass




speaker = Multilinguist()

# print(speaker.language_in('Canada')) #en
# print(speaker.language_in('Japan')) #ja
# print(speaker.language_in('Ireland')) #ga #Gaelic
# print(speaker.language_in('France')) #fr
# print()

# print(speaker.travel_to('Canada')) #en
# print(speaker.travel_to('Japan')) #ja
# print(speaker.travel_to('Ireland')) #ga #Gaelic
# print(speaker.travel_to('France')) #fr
# print()

# print(speaker.say_in_local_language('This is my message.')) #en
# print(speaker.say_in_local_language('This is my message.')) #ja
# print(speaker.say_in_local_language('This is my message.')) #ga #Gaelic
# print(speaker.say_in_local_language('This is my message.')) #fr





class MathGenius(Multilinguist):

  def report_total(self, numbers_list):
    return f"{speaker.say_in_local_language('The total is')} {sum(numbers_list)}"
    pass
  pass



class QuoteCollector(Multilinguist):
  list_of_quotes = []

  def add_new_quote(self, new_quote):
    return new_quote




mathematician = MathGenius()
# mathematician.travel_to("Canada")
# print(mathematician.report_total([23,45,676,34,5778,4,23,5465])) # The total is 12048
# mathematician.travel_to("India")
# print(mathematician.report_total([6,3,6,68,455,4,467,57,4,534])) # है को कुल 1604
# mathematician.travel_to("Italy")
# print(mathematician.report_total([324,245,6,343647,686545])) # È Il totale 1030767



quotist = QuoteCollector()
