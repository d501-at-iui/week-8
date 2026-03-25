from collections import defaultdict
import numpy as np

class MarkovText:
   """Generates text using a first-order Markov chain model."""
   def __init__(self, corpus):
       self.corpus = corpus
       self.term_dict = None
   def get_term_dict(self):
       """Here I have built a transition dictionary which maps each word to its possible successors."""
       term_dict = defaultdict(list)
       tokens = self.corpus.split()
       for i in range(len(tokens) - 1):
           current_word = tokens[i]
           next_word = tokens[i + 1]
           term_dict[current_word].append(next_word)
       self.term_dict = dict(term_dict)
   def generate(self, seed_term=None, term_count=15):
       """
       Generating text using the Markov chain.
       Args:
           seed_term (str, optional): Starting word. Words are randomly chosen if not provided.
           term_count (int): Number of words to generate. Defaults to 15.
       Returns:
           str: Generated text as a single string.
       Raises:
           ValueError: If term_dict not built or seed_term not in corpus.
       """
       if self.term_dict is None:
           raise ValueError(
               "Term dictionary not built. Run get_term_dict() first."
           )
       if seed_term:
           if seed_term not in self.term_dict:
               raise ValueError("Seed term not in corpus.")
           current_word = seed_term
       else:
           current_word = np.random.choice(list(self.term_dict.keys()))
       generated_words = [current_word]
       for _ in range(term_count - 1):
           if current_word not in self.term_dict:
               break
           next_word = np.random.choice(self.term_dict[current_word])
           generated_words.append(next_word)
           current_word = next_word
       return " ".join(generated_words)