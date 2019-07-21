import random #Needed to use random.choice.
import requests #Needed to send the request to the API.
import json #Needed to convert the request from JSON.

from multilinguist import Multilinguist #Needed to inherit Multilinguist class.

class QuoteCollector(Multilinguist):
  """The multilinguist documentation tells us that 
  class represents a world-traveller who speaks many 
  languages. The QuoteCollect class represents a 
  represents a person who loves to memorize quotes and 
  then travel the world, unleashing poor translations 
  of them to unsuspecting passers-by.
  """
  list_of_quotes = []

  def report_quote(self, numbers_list):
    pass
    # return f"{speaker.say_in_local_language('The total is')} {sum(numbers_list)}"

  def add_new_quote(self, new_quote, topic):
    self.list_of_quotes.append({'quote': new_quote, 'topic': topic})
    return new_quote

  def is_quote_real(self, desired_topic):
    for quote in self.list_of_quotes:
      if quote['topic'] == desired_topic:
        return quote['quote']
    return False

  def share_quote_by_topic(self, desired_topic):
    quote_exists = self.is_quote_real(desired_topic)

    if quote_exists:
      return(f"\"{quote_exists}\" - a quote about {desired_topic}.")
    else:
      return (f'I don\'t have a quote about {desired_topic}.')

  def get_random_quote(self):
    random_quote = random.choice(self.list_of_quotes)
    # return(f"\"{random_quote['quote']}\" - a quote about {random_quote['topic']}.")
    return(speaker.say_in_local_language(random_quote['quote']))

  def get_quote_length(self, desired_topic):
    quote_exists = self.is_quote_real(desired_topic)

    if quote_exists:
      return(f"Your quote is {len(quote_exists)} characters long.")
    else:
      return (f'I don\'t have a quote about {desired_topic}.')