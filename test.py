# import requests
# import json
# import random
# import math

from multilinguist import Multilinguist
from mathgenius import MathGenius
from quotecollector import QuoteCollector

speaker = Multilinguist()
#This is the language the speaker is speaking.
# print(speaker.language_in('Canada')) #en
# print()

#This is the language the message will be translated into.
# print(speaker.travel_to('Canada')) #en
# print(speaker.travel_to('Japan')) #ja
# print(speaker.travel_to('Ireland')) #ga #Gaelic
# print(speaker.travel_to('France')) #fr
# print()

# print(speaker.say_in_local_language('This is my message.')) #en
# print(speaker.say_in_local_language('This is my message.')) #ja
# print(speaker.say_in_local_language('This is my message.')) #ga #Gaelic
# print(speaker.say_in_local_language('This is my message.')) #fr
# print()


mathematician = MathGenius()
# mathematician.travel_to("Canada")
# print(mathematician.report_total([23,45,676,34,5778,4,23,5465])) # The total is 12048
# mathematician.travel_to("India")
# print(mathematician.report_total([6,3,6,68,455,4,467,57,4,534])) # है को कुल 1604
# mathematician.travel_to("Italy")
# print(mathematician.report_total([324,245,6,343647,686545])) # È Il totale 1030767
# print()

print(mathematician.factorial(7))
print()



quotist = QuoteCollector()
quotist.add_new_quote('It is what it is.', 'nonsense')
quotist.add_new_quote('You can’t trade shoes with a barefoot monkey.', 'shoes')
quotist.add_new_quote('You can’t fill a hat with maybes.', 'Carly Rae Jepson')
quotist.add_new_quote('A pit in a peach is worth six in a bucket.', 'peaches')
quotist.add_new_quote('There’s never enough time to chew all the ice.', 'ice')
quotist.add_new_quote('A paperclip won’t make the dog sit up.', 'paperclips')
quotist.add_new_quote('He folded like a wet watermelon.', 'sports')
quotist.add_new_quote('It feels like we’re walking towards Cleveland with this one.', 'Cleveland')
quotist.add_new_quote('Every pig gets twisted some weeks.', 'pigs')
quotist.add_new_quote('You can’t bend steel with tears.', 'tears')
quotist.add_new_quote('It’s worth all you’ve got plus five pizzas.', 'pizza')
quotist.add_new_quote('As far as I’m concerned, she hangs the moon and neatly folds the sun.', 'the moon')

print(quotist.share_quote_by_topic('pizza'))
print(quotist.share_quote_by_topic('werewolves'))
print()
print(quotist.get_random_quote())


