from Game import Game
from Field import Field
from Card import Card
from MonsterCard import MonsterCard
from SpecialyCard import SpecialyCard

def player_select_card(g:Game, p:Player, name=None):
    if name is None:
        print("Select one of the following cards:")
        i = 0
        for c in game.field[p]:
            printf("Position %d: %s"%(i, c.name))
            i += 1