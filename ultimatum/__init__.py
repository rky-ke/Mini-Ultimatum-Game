from otree.api import *

doc = """
Mini-Ultimatum Game
"""

class C(BaseConstants):
    NAME_IN_URL = 'my_trust'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    ENDOWMENT = cu(200)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    amount_sent = models.CurrencyField(
        min=cu(0),
        max=C.ENDOWMENT,
        label="How much do you want to send to Player 2?"
    )
    punish = models.BooleanField(
        label="Do you want to punish Player 1?"
    )
    capital_city = models.StringField(
        choices=["Kisumu", "Nairobi", "Mombasa"],
        label="What is the capital city of Kenya?"
    )
    math_answer = models.IntegerField(
        label="What is 15 + 14?"
    )
    population = models.IntegerField(
        label="What is the population of Kenya?"
    )
# PAGES
class Player1Decision(Page):
    form_model = 'player'
    form_fields = ['amount_sent']

    def is_displayed(self):
        return self.id_in_group == 1
    
    
class WaitForPlayer1(WaitPage):
    pass

class PunisherDecision(Page):
    form_model = 'player'
    form_fields = ['punish']
    
    def is_displayed(self):
        return self.id_in_group == 3
    def vars_for_template(self):
        return {
            'amount_sent': self.group.get_player_by_id(1).amount_sent
        }

class WaitForPunisher(WaitPage):
    pass
    
class Results(Page):
    @staticmethod
    def vars_for_template(self):
        player1 = self.group.get_player_by_id(1)
        punisher = self.group.get_player_by_id(3)
        
        if punisher.punish:
            player1_payout = 0
            player2_payout = 0
        else:
            player1_payout = C.ENDOWMENT - player1.amount_sent
            player2_payout = player1.amount_sent

        return {
            'player1_amount_sent': player1.amount_sent,
            'punisher_decision': "Punish" if punisher.punish else "Not Punish",
            'player1_payout': player1_payout,
            'player2_amount_received': player2_payout,
        }
    
class ExitSurvey(Page):
    form_model = 'player'
    form_fields = ['capital_city', 'math_answer', 'population']

    def error_message(self, values):
        if values['math_answer'] != 29:
            return 'Your answer to the math question is incorrect. Please provide the correct answer to continue.'


class TheEnd(Page):
    pass

page_sequence = [
    Player1Decision,
    WaitForPlayer1,
    PunisherDecision,
    WaitForPunisher,
    Results,
    ExitSurvey,
    TheEnd,
]
