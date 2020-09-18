"""Reinforcement Learning (Chapter 21)
"""

from __future__ import absolute_import
from .utils import *
from . import agents

class PassiveADPAgent(agents.Agent):
    """Passive (non-learning) agent that uses adaptive dynamic programming
    on a given MDP and policy. [Fig. 21.2]"""
    NotImplementedError

class PassiveTDAgent(agents.Agent):
    """Passive (non-learning) agent that uses temporal differences to learn
    utility estimates. [Fig. 21.4]"""
    NotImplementedError
