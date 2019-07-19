############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing) 


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType(
        'musk',
        1998, 
        'green', 
        True, 
        True, 
        'Muskmelon')
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)

    casaba = MelonType(
        'cas', 
        2003, 
        'orange',
        False,
        False,
        'Casaba')
    casaba.add_pairing('mint')
    casaba.add_pairing('strawberries')
    all_melon_types.append(casaba)

    crenshaw = MelonType(
        'cren',
        1996,
        'green',
        False, 
        False, 
        'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)


    yellow_watermelon = MelonType(
        'yw',
        2013,
        'yellow',
        False,
        True,
        'Yellow Watermelon',
        )
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)


    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")

        for pairing in melon.pairings:
            print(f'- {pairing}')

        print() # Blank line for separator.


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dictionary = {}
    for melon in melon_types:
        key = melon.code
        melon_dictionary[key] = melon

    return melon_dictionary


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field_number, harvested_by):
        self.type = melon_type
        self.shape_rating = int(shape_rating)
        self.color_rating = int(color_rating)
        self.field_number = int(field_number)
        self.harvested_by = harvested_by
        

    def is_sellable(self):
        return (self.shape_rating > 5 and
                self.color_rating > 5 and
                self.field_number != 3)


def make_melons(melon_dictionary,file_path):
    """Returns a list of Melon objects."""
    
    list_of_melons = []
    melon_file = open(file_path)

    for line in melon_file:
        tokens = (line.rstrip()).split('|')
        # Melon | type | shape_rating | color_rating | field_num | harvested_by
        new_melon = Melon(melon_dictionary[tokens[1]],
                          tokens[2],
                          tokens[3], 
                          tokens[4], 
                          tokens[5])
        list_of_melons.append(new_melon)

    return list_of_melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            sellability = '(CAN BE SOLD)'
        else:
            sellability = '(NOT SELLABLE)'

        print(f'Harvested by {melon.harvested_by}', end ='')
        print(f' from Field {melon.field_number} {sellability}')

if __name__ == '__main__':
    dictionary_of_melons = make_melon_type_lookup(make_melon_types())
    get_sellability_report((make_melons(dictionary_of_melons, 'melons.txt')))