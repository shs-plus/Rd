import logging
import random
import itertools

class Core:
    def __init__(self, settings):
        self.settings = settings
        self.rc = self.random_choice()
        next(self.rc)
    

    def random_choice(self):
        '''
        A different choosing algorithm.
        For each iteration, normalize the probabilities, choose one, then multiply the probability of the choosed one by .5 (for example)
        Then the results would be more mixed together, rather than chunks of 35 (for example) pieced together
        '''
        n = dict(zip(set(range(1, self.settings.n + 1)) - set(self.settings.exception), itertools.repeat(1)))
        logging.debug(f'Setting n')
        while True:
            t = sum(n)
            for p in n:
                n[p] /= t
            yield (p := random.choices(list(n), list(n.values()))[0])
            n[p] *= self.settings.rec
            logging.debug(f'Random choice: {p}')
            self.label['text'] = p
            self.label.config(font=("Arial", 20))