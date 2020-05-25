import json


class Storage:
    """A class to manage the data."""

    def __init__(self):
        self.file = 'db/data.json'

    def get_score(self):
        try:
            with open(self.file) as f:
                score = json.load(f)
        except FileNotFoundError:
            return 0
        else:
            return score

    def set_score(self, score):
        with open(self.file, 'w') as f:
            json.dump(score, f)