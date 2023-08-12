"""

Menu Item Combinations

Your task is to process the following menu of food items, and determine which combination of food items could be purchased for the receipt values below.
The Menu: (I'll try to provide this in a hash or map data structure as an input)

1- veggie sandwich: 6.85
2- extra veggies: 2.20
3- chicken sandwich: 7.81 
4- cheese: 1.25
5- chips: 1.40
6- nachos: 3.45
7- soda: 2.05
8- extra chicken: 3.20

The receipt values to test, also provided as an input:

4.85, 11.05, 13.75, 17.75, 18.25, 19.40, 28.25, 40.30, 75.00 21

Key elements to follow:
1- Your script should process as many of these receipt values as possible in under 30 seconds
2- You must use 100% of the money, we don't want any money left over 24 - you can order any quantity of any menu item
3- None of the receipt values are "tricks", they all have combinations that add up to exactly their money amount

Part One:

Find a single combination of menu items that add up to exactly these amounts o money, and output them as your script runs. Output format is up to you, but here are a few examples:

13.75, 3 items, ['veggie sandwich', 'nachos', 'nachos']
13.75, 3 items, {'veggie sandwich': 1, nachos: 2}


Part Two:

Each receipt value above has many possible combinations. Next, refactor your algorithm to identify which combination contains fewer total items than other answers.

Example:

4.85 receipt has three combinations:

- best: nachos, chips (2 total items)
- extra veggies, chips, cheese (3 total times)
- chips, chips, soda (3 total items)

"""


class Solution(object):
    def __menu_item_combinations_helper(self, result, menu, receipt):
        if receipt < 0:
            return False

        if receipt == 0:
            return True

        for key in menu.keys():
            result.append(key)

            diff = round(receipt * 100 - menu[key] * 100) / 100

            if self.__menu_item_combinations_helper(result, menu, diff):
                return True

            result.pop()

        return False

    def menu_item_combinations(self, menu, receipts):

        menu = dict(sorted(menu.items(), key=lambda item: item[1], reverse=True))

        print(menu)

        for i in range(len(receipts)):
            result = []
            self.__menu_item_combinations_helper(result, menu, receipts[i])
            print(receipts[i], ":", len(result), "items :", result)


menu = {
    "veggie sandwich": 6.85,
    "extra veggies": 2.20,
    "chicken sandwich": 7.85,
    "extra chicken": 3.20,
    "cheese": 1.25,
    "chips": 1.40,
    "nachos": 3.45,
    "soda": 2.05,
}

receipts = [4.85, 11.05, 13.75, 17.75, 18.25, 19.40, 28.25, 48.30, 75.00]

Solution().menu_item_combinations(menu, receipts)
