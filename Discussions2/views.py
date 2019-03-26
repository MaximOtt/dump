from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
# Timer stuff
import time
import datetime


class WelcomePage(Page):
    pass
class BeautyRules(Page):
    pass
class BeautyIndividual(Page):
    form_model = 'player'
    form_fields = ['BeautyFirstAnswer']
    
    def before_next_page(self):
        self.player.BeautyCurrentAnswer = self.player.BeautyFirstAnswer
class BeautyDiscussion(Page):
    # This is probably something for the timer again
    def is_displayed(self):
        # Not really sure what it does here
        # Tutorial says it should return TRUE or FALSE, so ....?
        return self.group.time_left()
    
    # Again, technically not required, but REALLY good idea to call it sometime
    def before_next_page(self):
        self.group.set_payoffs()
    
    def vars_for_template(self):
        return {'some_list': ['first element','second element','third element'],
                'time_left': self.group.time_left()}
        
    def vars_for_template(self):
        return {'CurrentAnswersById': [player.BeautyCurrentAnswer for player in self.group.get_players()]}
class RulesNASA(Page):
    pass
class TaskNASA(Page):
    pass

# Strictly speaking not needed, but it is usually a good idea to start at the same time
# Only need in this example for the timer 
class MyWaitPage(WaitPage):
    def after_all_players_arrive(self):
        
        # This is technically unnecessary timer stuff
        now = time.time()
        self.group.auctionstartdate = now
        self.group.auctionenddate = now + Constants.starting_time

class Results(Page):
    pass


page_sequence = [
#    WelcomePage,
#    BeautyRules,
    BeautyIndividual,
    MyWaitPage,
    BeautyDiscussion,
    MyWaitPage,
    RulesNASA,
    TaskNASA,
    Results
]
