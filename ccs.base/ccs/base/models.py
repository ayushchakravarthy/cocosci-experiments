from dallinger.nodes import Source
import numpy as np

class RandomSource(Source):
    """A source that generates a random number between 0 and 10"""

    __mapper_args__ = {"polymorphic_identity": "random_source"}

    def _contents(self):
        return f"This is the first generation!"
