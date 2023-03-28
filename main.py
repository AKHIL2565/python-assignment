
from burger_machine import BurgerMachine

bm = BurgerMachine()

bm.make_burger('hamburger')
bm.make_burger('cheeseburger')
bm.make_burger('chickenburger')

bm.add_ingredients('bun', 5)
bm.add_ingredients('beef patty', 2)

bm.make_burger('hamburger')
bm.make_burger('cheeseburger')

bm.restock()

bm.make_burger('hamburger')
