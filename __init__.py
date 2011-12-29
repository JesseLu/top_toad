from marionette.units import Unit
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
            target = items[0]
            return 'move', {
                'pos': target.pos
            }
        # Move to (0, 0) if there's nothing better to do
        return 'move', {
            'pos': (0, 0)
        }
