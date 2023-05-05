import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

@pytest.fixture
def burger():
    bn = BurgerMachine()
    return bn

@pytest.fixture
def check():
    bn = BurgerMachine()
    return bn

def test_bun_is_the_first (machine):
    with pytest.raises (InvalidStageException): 
        machine.handle_patty("turkey") 
        machine.handle_patty("beef") 
        machine.handle_patty("next") 
        machine.handle_toppings("bbq")
        machine.handle_toppings("mayo") 
        machine.handle_toppings("cheese") 




def test_toppings_in_stock (check): 
    # UCID is ar2565 and date is  23/03/2023
    check.toppings[0].quantity = 0 
    with pytest.raises (OutOfStockException): 
        check.handle_bun("lettuce wrap") 
        check.handle_patty("turkey")
        check.handle_patty("next")
        check.handle_toppings("lettuce")

def test_patty_in_stock(machine):
    # UCID is ar2565 and date is  23/03/2023
    machine.patties[1].quantity=0
    with pytest.raises(OutOfStockException):
        machine.handle_bun("lettuce wrap")
        machine.handle_patty("veggie")
        
        
def test_patty_is_three (machine):
# UCID is ar2565 and date is  23/03/2023 
    with pytest.raises (ExceededRemainingChoicesException): 
        machine.handle_bun("no bun")
        machine.handle_patty("beef")
        machine.handle_patty("turkey")
        machine.handle_patty("turkey")
        machine.handle_patty("beef")

def test_toppings_are_three (machine): 
    # UCID is ar2565 and date is  23/03/2023 
    with pytest.raises (ExceededRemainingChoicesException): 
        machine.handle_bun("wheat burger bun") 
        machine.handle_patty("beef")
        machine.handle_patty("beef")
        machine.handle_patty("beef")
        machine.handle_patty("next") 
        machine.handle_toppings("mayo") 
        machine.handle_toppings("mayo")
        machine.handle_toppings("mustard")
        machine.handle_toppings("cheese")


def test_cost_of_burger (burger): 
# UCID is ar2565 and date is  23/03/2023    
    burger.handle_bun("wheat burger bun") 
    burger.handle_patty("turkey")
    burger.handle_patty("next")
    burger.handle_toppings("mustard") 
    burger.handle_toppings("pickles")
    burger.handle_toppings("tomato")
    burger.handle_toppings("done")
    price1= burger.calculate_cost()
    assert price1 == "$4.00"
    burger.handle_pay(price1,"$4.00") 

    burger.handle_bun("no bun") 
    burger.handle_patty("beef")
    burger.handle_patty("turkey")
    burger.handle_patty("beef")
    burger.handle_patty("next")
    burger.handle_toppings("tomato") 
    burger.handle_toppings("cheese")
    burger.handle_toppings("done")
    price2= burger.calculate_cost()
    assert price2 == "$3.50"
    burger.handle_pay(price2,"$3.50") 

    burger.handle_bun("lettuce wrap") 
    burger.handle_patty("beef")
    burger.handle_patty("beef")
    burger.handle_patty("next")
    burger.handle_toppings("ketchup") 
    burger.handle_toppings("ketchup")
    burger.handle_toppings("done")
    price3= burger.calculate_cost()
    assert price3 == "$4.00"
    burger.handle_pay(price3,"$4.00") 


def test_total_number_of_burgers (machine): 
# UCID is ar2565 and date is  23/03/2023      
    machine.handle_bun("no bun")
    machine.handle_patty("turkey") 
    machine.handle_patty("beef") 
    machine.handle_patty("next")
    machine.handle_toppings("mustard") 
    machine.handle_toppings("mustard") 
    machine.handle_toppings("bbq")
    machine.handle_toppings("done") 
    machine.handle_pay("$3.50","$3.50")
    
    machine.handle_bun("lettuce wrap") 
    machine.handle_patty("beef")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("mayo")
    machine.handle_toppings("mayo")
    machine.handle_toppings("done")
    machine.handle_pay("$3.50","$3.50")
    assert machine.total_burgers == 2

def test_total_number_of_sales(machine): 
# UCID is ar2565 and date is  23/03/2023    
    machine.handle_bun("white burger bun")
    machine.handle_patty("beef")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("mayo") 
    machine.handle_toppings("pickles")
    machine.handle_toppings("cheese")
    machine.handle_toppings("done")
    price1 = machine.calculate_cost() 
    machine.handle_pay(price1,price1)
    
    machine.handle_bun("no bun")
    machine.handle_patty("turkey")
    machine.handle_patty("beef")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("tomato")
    machine.handle_toppings("done")
    price2 = machine.calculate_cost() 
    machine.handle_pay(price2,price2)

    machine.handle_bun("no bun") 
    machine.handle_patty("next") 
    machine.handle_toppings("pickles")
    machine.handle_toppings("pickles")
    machine.handle_toppings("pickles")
    machine.handle_toppings("done")
    price3= machine.calculate_cost()
    machine.handle_pay(price3,price3)
    assert machine.total_sales == float(price1[1:])+float(price2[1:])+float(price3[1:])

"""
