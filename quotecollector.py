import random #Needed to use random.choice.

from multilinguist import Multilinguist #Needed to inherit Multilinguist class.

class QuoteCollector(Multilinguist):
  list_of_quotes = []

  def report_quote(self, numbers_list):
    return f"{speaker.say_in_local_language('The total is')} {sum(numbers_list)}"

  def add_new_quote(self, new_quote, topic):
    self.list_of_quotes.append({'quote': new_quote, 'topic': topic})
    return new_quote

  def share_quote_by_topic(self, desired_topic):
  
    for quote in self.list_of_quotes:
      if (quote['topic'] == desired_topic):
        return(f"\"{quote['quote']}\" - a quote about {quote['topic']}.")
    return (f'I don\'t have a quote about {desired_topic}.')

  def get_random_quote(self):
    random_quote = random.choice(self.list_of_quotes)

    return(f"\"{random_quote['quote']}\" - a quote about {random_quote['topic']}.")