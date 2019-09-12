import libtcodpy as libtcod
from game_states import GameStates

def heal(*args, **kwargs):
    entity = args[0]
    amout = kwargs.get('amount')

    results = []

    if entity.fighter.hp == entity.fighter.max_hp:
        results.append({'consumed': False, 'message': Message('You are already at full health', libtcod.yellow)})
    else:
        entity.fighter.heal(amount)
        results.append({'consumed': True, 'message': Message('Your wounds start to heal. You feel better!', libtcod.green)})