class Scorer:
    def parse(self, input):
        '''Parse a Yahtzee input string.
        
        params:
        input: a string of the form "(1, 3, 3, 2, 5) fullhouse" describing
                a Yahtzee roll and chosen category

        returns:
        a tuple containing: a list of 5 die values, and a category string

        '''
        category = input.split()[-1]
        dice_input = input[:input.rfind(' ')]
        dice = dice_input[1:-1].split(', ')
        return (dice, category)

    def add(self, x, y):
        return x + y
