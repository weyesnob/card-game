from MonsterCard import MonsterCard
from SpecialyCard import SpecialyCard
from EventHandlers import EventHandlersDict
from Frontend import player_select_card

class BasicMubarrachka(MonsterCard):
    hp = 100
    strength = 27
    name = "Basic Mubarrachka"

    def __init__(self, g:Game, p:Player):
        super().__init__(hp=hp, strength=strength, g=g, p=p)
        self.name = name

class MubarrachkaCool(MonsterCard):
    hp = 200
    strength = 37
    name = "Mubarrachka (Cool)"

    def __init__(self, g:Game, p:Player):
        super().__init__(hp, strength, g, p)
        self.name = name
        self.handled_events["start_of_turn"] = True
    
    def summon_check(self, g: Game):
        can_summon = False
        cards = g.field.get_cards()[self.player]
        for card in cards:
            if card != None:
                can_summon = can_summon or card.name == "Basic Mubarrachka"
        return can_summon
    
    def summon_preparation(self):
        c = player_select_card(self.game, self.player, name="Basic Mubarrachka")
        self.game.field.remove_card(c)
        c.on_tribute()



