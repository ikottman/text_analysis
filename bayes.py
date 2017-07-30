import os
from fractions import Fraction

class Category:
  def __init__(self, name, examples, total_examples):
    self.name = name
    self.examples = examples
    self.words = self.__clean_words()
    self.p = Fraction(len(examples), total_examples)

  def __clean_words(self) -> list:
    return list(map(lambda x: x.lower(), " ".join(self.examples).split()))

def unique_word_count(words: list) -> int:
  return len(set(words))

# Find probability a word belongs in a category. Applies Laplace smoothing to prevent 0 probability.
def P(word: str, category: Category, unique_word_count: int) -> Fraction:
  instances = category.words.count(word)
  total = len(category.words)
  return laplace_smooth(instances, total, unique_word_count)
  
def laplace_smooth(numerator, denominator, unique_word_count) -> Fraction:
  return Fraction(numerator + 1, denominator + unique_word_count)


# read in example data
sports_examples = open("sports.txt").readlines()
not_sports_examples = open("not_sports.txt").readlines()
sports = Category("Sports", sports_examples, 5)
not_sports = Category("Not Sports", not_sports_examples, 5)
categories = (sports, not_sports)

all_words = sports.words + not_sports.words
unique_words = unique_word_count(all_words)

test = 'a very close game'

for category in categories:
  probability = 0
  for word in test.split():
    if probability == 0:
      probability = P(word, category, unique_words) 
    else:
      probability*= P(word, category, unique_words)
  p = float(probability * category.p)
  print("Probability of being in {} is {:f}".format(category.name, p))
