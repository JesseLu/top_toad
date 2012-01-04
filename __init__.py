from marionette.units import Unit
import math
import random 
class Toad(Unit):
    def act(self):

        # Eat if we can
        if self.inventory.get('grutonium', 0) > 0:
            return 'eat', {
                'typename': 'grutonium',
                'amount': self.inventory['grutonium']
            }

        # Grab an item if we can
        items = self.items_in_view
        for item in items:
            if item.pos == self.pos:
                return 'grab', {
                    'uid': item.uid,
                    'amount': item.amount
                }

        # Move to an item if we see one (not necessarily closest)
        if len(items) > 0:
           target = get_closest_item(self.pos, items)
           return 'move', {
                'pos': target.pos
            }


        # Move "randomly"
        step = 100
        return 'move', {
            'pos': self.pos 
#             'pos': (self.pos[0] + step * math.cos(self.health/30), \
#                 self.pos[1] + step * math.sin(self.health/30))
        }

def get_closest_item(pos, items):
    mindist = 1e9
    for item in items:
        dist = math.hypot(item.pos[0]-pos[0],\
            item.pos[1]-pos[1])
        if dist < mindist:
            target = item
            mindist = dist
    return target
