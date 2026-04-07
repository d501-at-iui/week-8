import numpy as np
from collections import defaultdict

class MarkovText:
    
    def __init__(self, corpus):
        self.corpus = corpus
        self.tokens = corpus.split()
        self.term_dict = None
    
    def get_term_dict(self):
        term_dict = defaultdict(list)
        
        for i in range(len(self.tokens) - 1):
            current_word = self.tokens[i]
            next_word = self.tokens[i + 1]
            term_dict[current_word].append(next_word)
        
        self.term_dict = dict(term_dict)
        return self.term_dict
    
    def generate(self, term_count=20, seed_term=None):
        if self.term_dict is None:
            self.get_term_dict()
        
        if seed_term is None:
            current_word = np.random.choice(list(self.term_dict.keys()))
        else:
            if seed_term not in self.term_dict:
                raise ValueError(f"Seed term '{seed_term}' not found in corpus")
            current_word = seed_term
        
        result = [current_word]
        
        for _ in range(term_count - 1):
            if current_word not in self.term_dict or len(self.term_dict[current_word]) == 0:
                current_word = np.random.choice(list(self.term_dict.keys()))
            else:
                current_word = np.random.choice(self.term_dict[current_word])
            
            result.append(current_word)
        
        return ' '.join(result)