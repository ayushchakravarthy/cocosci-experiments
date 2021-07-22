"""Bartlett's transmission chain experiment from Remembering (1932)."""

import logging

from dallinger.config import get_config
from dallinger.experiments import Experiment
from dallinger.networks import Empty
try:
    from .bots import Bot
    Bot = Bot
except ImportError:
    pass

logger = logging.getLogger(__file__)


def extra_parameters():
    config = get_config()
    types = {
        'custom_variable': bool,
        'num_participants': int,
    }

    for key in types:
        config.register(key, types[key])


class IGG(Experiment):
    """Define the structure of the experiment."""
    num_participants = 1

    def __init__(self, session=None):
        """Call the same parent constructor, then call setup() if we have a session.
        """
        super(IGG, self).__init__(session)

        self.experiment_repeats = 5
        self.initial_recruitment_size = 10

        if session:
            self.setup()

    @classmethod
    def extra_parameters(cls):
        config = get_config()

        # can extend if needed
        types = {
            'num_participants': int
        }
        
        for key in types:
            config.register(key, types[key])

    def configure(self):
        config = get_config()
        super(IGG, self).configure()
        self.num_participants = config.get('num_participants')

    def create_network(self):
        """Return a new network."""
        return Empty(max_size=self.num_participants)
