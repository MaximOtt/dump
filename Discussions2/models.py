from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import time

author = 'Maxim Ott'

doc = """
A group of people has to find a consensus on task.
"""


class Constants(BaseConstants):
    name_in_url = 'Discussions2'
    players_per_group = 2
    num_rounds = 1
    reward_beauty = c(10)
    reward_NASA = c(20)
    
    # This is technically unnecessary timer stuff
    starting_time = 15000
    extra_time = 15000

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    BeautyGroupResult = models.IntegerField()
    
    # This is technically unnecessary timer stuff
    auctionstartdate = models.FloatField()
    auctionenddate = models.FloatField()
    def time_left(self):
        now = time.time()
        time_left = self.auctionenddate - now
        time_left = round(time_left) if time_left > 0 else 0
        return time_left

    def set_payoffs(self):
        for p in self.get_players():
            p.payoff = 15 # Just do whatever you want here

class Player(BasePlayer):
    BeautyFirstAnswer = models.IntegerField(min=0, max=100, label="")
    BeautyCurrentAnswer = models.IntegerField(min=0, max=100, label="")
    BeautyChangeHistory = models.StringField()

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)