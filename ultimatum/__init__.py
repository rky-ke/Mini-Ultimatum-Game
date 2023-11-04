from otree.api import *

doc = """
Mini-Ultimatum Game
"""

class Constants(BaseConstants):
    name_in_url = 'ultimatum'
    players_per_group = 3
    num_rounds = 1
    endowment = cu(200)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    amount_sent = models.CurrencyField(
        min=0, max=Constants.endowment,
        doc="Amount sent to Player 2"
    )
    punish = models.BooleanField(
        doc="Punish Player 1 (True) or Not Punish (False)"
    )
    capital_city = models.StringField(
        choices=["Kisumu", "Nairobi", "Mombasa"],
        doc="Capital city of Kenya"
    )
    math_answer = models.IntegerField(
        min=0,
        doc="Math answer (14 + 15)"
    )
    population = models.IntegerField(
        min=0,
        doc="Population of Kenya"
    )

class Player1Decision(Page):
    form_model = 'player'
    form_fields = ['amount_sent']

    def is_displayed(self):
        return self.id_in_group == 1
    def vars_for_template(self):
        return {
            'endowment': Constants.endowment
        }
    
    
class WaitForPlayer1(WaitPage):
    def is_displayed(self):
        return self.id_in_group != 1

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
    def is_displayed(self):
        return self.id_in_group != 3
    
class Results(Page):
    def vars_for_template(self):
        player1 = self.group.get_player_by_id(1)
        player2 = self.group.get_player_by_id(2)
        punisher = self.group.get_player_by_id(3)
        
        if punisher.punish:
            player1_payout = 0
            player2_payout = 0
        else:
            player1_payout = Constants.endowment - player1.amount_sent
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


class FinalResults(Page):
    pass

page_sequence = [
    Player1Decision,
    WaitForPlayer1,
    PunisherDecision,
    WaitForPunisher,
    Results,
    ExitSurvey,
    FinalResults,
]
