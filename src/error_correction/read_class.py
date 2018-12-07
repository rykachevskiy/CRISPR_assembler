from src.utils import utils
from src.error_correction.error_correction import ErrorCorrector

import os

class Read:
    def __init__(self, path, names=None):
        if names is None:
            names = os.listdir(path)

        self.pairs = [self._load_pairs_from_path(path + name, ' ') for name in names]

        self._get_spacers_set()

    def _load_pairs_from_path(self, path, split = '\t', limit = None):
        if limit is None:
            limit = 1000 #TODO fix shit

        with open(path) as f:
            pairs = [[y[:limit] for y in x[:-1].split(split)] for x in f.readlines()]

        return pairs

    def _get_spacers_set(self):
        self.spacers = set(utils.unwrap_nested(self.pairs))

    def correct_errors(self, threshold=5):
        self.corrector = ErrorCorrector(threshold=threshold)

        self.corrector.fit(self.pairs)
        self.corrected_pairs = list(map(self.corrector.transform, self.pairs)) #TODO questionable








