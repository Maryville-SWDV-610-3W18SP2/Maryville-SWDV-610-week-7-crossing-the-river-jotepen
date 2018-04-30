
def print_state(dct1, dct2, dct3):
    """
    Prints each boat trip result
    """
    repeated_message = """
    Bank 1: {} cannibal(s), {} missionaries
    Bank 2: {} cannibal(s), {} missionaries
    Boat: {} cannibal(s), {} missionaries
    """
    
    print(repeated_message.format(dct1['cannibals'], dct1['missionaries'], dct2['cannibals'], dct2['missionaries'],
                     dct3['cannibals'], dct3['missionaries']))


def cross_river(bank1, bank2, boat):

    if all(empty == 0 for empty in bank2.values()):  # bank 2 is empty
        print_state(bank1, bank2, boat)
        # 1 cannibal boards the boat and leaves bank 1
        bank1['cannibals'] -= 1 
        boat['cannibals'] += 1
        
    # 1 missionary boards the boat and leaves bank 1.
    bank1['missionaries'] -= 1  
    boat['missionaries'] += 1
    print_state(bank1, bank2, boat)

    if all(empty == 0 for empty in bank1.values()):  # bank 1 is empty
        #The cannibal and missionary get on the boat
        boat['cannibals'], boat['missionaries'] = 0, 0  
        # 1 cannibal and 1 missionary setp onto bank 2
        bank2['cannibals'] += 1
        bank2['missionaries'] += 1
        print_state(bank1, bank2, boat)
        return  # final condition is met

    # 1 missionary steps onto bank 2
    boat['missionaries'] -= 1 
    bank2['missionaries'] += 1
    print_state(bank1, bank2, boat)

    # 1 cannibal boards the boat and leaves bank 1.
    bank1['cannibals'] -= 1
    boat['cannibals'] += 1 
    print_state(bank1, bank2, boat)

    # 1 cannibal boards the boat and leaves bank 2.
    boat['cannibals'] -= 1
    bank2['cannibals'] += 1 
    print_state(bank1, bank2, boat)
    
    
    #Calling the cross_river function for additonal crossings
    cross_river(bank1, bank2, boat)


def main():
    # Start with 3 missionaries and 3 cannibals on bank 1
    bank1 = {'cannibals': 3, 'missionaries': 3}
    bank2 = {'cannibals': 0, 'missionaries': 0}
    boat = {'cannibals': 0, 'missionaries': 0}
    
    cross_river(bank1, bank2, boat)

main()