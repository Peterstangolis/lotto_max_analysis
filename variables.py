lottery_played_lotto_max = True
lottery_played_649 = False
encore_played = False

lottery_guru_url = 'https://lotteryguru.com/ontario-lottery-results'

lotto_max_range = list(range(1,51))
lotto_649_range = list(range(1,50))

encore_number_options = ["1,1,1,1,1,1,1", "9,9,9,9,9,9,9"]

lotto_max_picks = 7

time = '22:30 EST'

days = ['Tuesday', 'Friday']

ticket_date = '20-Jan-2023'


lotto_max_prizes = {
    "3/7" : "Free Play",
    "3/7+Bonus" : 20.00,
    "4/7" : 20.00,
    "4/7+Bonus" : 45.5,
    "5/7" : 99.30,
    "5/7+Bonus" : 995.60,
    "6/7" : 3845.5,
    "6/7+Bonus" : 80754.8,
    "7/7" : 60000000.00
}

lotto_649_prizes = {
    "2/6" : "Free Play",
    "2/6+Bonus" : 5.00,
    "3/6" : 10.00,
    "4/6" : 83.60,
    "5/6" : 859.90,
    "5/6+Bonus" : 206832.30,
    "6/6" : 5000000.00,
}

## Variables for lottery number picks of the group
lotto_name = "Lotto Max"

draw_date = " "

group_picks = [
    [2,20,22,24,36,39,46],
    [3,25,26,30,28,45,50],
    [24,26,32,38,39,41,42],
    [3,6,13,22,38,40,49],
    [11,12,24,27,30,36,42],
    [4,11,23,28,32,37,43]
]

group_649_picks = [
    [],
    []
]

encore_picks = [
    []
]

lines_picked = len(group_picks)

bet_amount = [

]

bet_amounts_649 = [
5.00, 5.00
]

encore_amount = [

]

group_funding_balance = None