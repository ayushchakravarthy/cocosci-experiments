"""Bartlett's transmission chain experiment from Remembering (1932)."""

import logging

from dallinger.config import get_config
from dallinger.experiments import Experiment
from dallinger.networks import Chain
try:
    from .bots import Bot
    Bot = Bot
except ImportError:
    pass

logger = logging.getLogger(__file__)


class IGG(Experiment):
    """Define the structure of the experiment."""

    def __init__(self, session=None):
        """Call the same parent constructor, then call setup() if we have a session.
        """
        super(IGG, self).__init__(session)
        from . import models

        self.models = models
        self.experiment_repeats = 1
        self.initial_recruitment_size = 1

        if session:
            self.setup()

    @classmethod
    def extra_parameters(cls):
        config = get_config()
        config.register("num_participants", int)

    def configure(self):
        config = get_config()
        self.num_participants = config.get('num_participants')

    def create_network(self):
        """Return a new network."""
        return Chain(max_size=self.num_participants)
    
    def add_node_to_network(self, node, network):
        """Add node to the chain and receive transmissions"""
        network.add_node(node)
        parents = node.neighbors(direction="from")
        if len(parents):
            parent = parents[0]
            parent.transmit()
        node.receive()

    def recruit(self):
        if self.networks(full=False):
            self.recruiter.recruit(n=1)
        else:
            self.recruiter.close_recruitment()
    
    def setup(self):
        if not self.networks():
            super(IGG, self).setup()
            for net in self.networks():
                self.models.RandomSource(network=net)

    
