lottery_played_lotto_max = False
lottery_played_649 = True
encore_played = False
ontario_49_played = False

lottery_guru_url = 'https://lotteryguru.com/ontario-lottery-results'

lotto_max_range = list(range(1,51))
lotto_649_range = list(range(1,50))

encore_number_options = []

lotto_max_picks = 7
lotto_649_picks = 6
ontario_64_picks = 6
encore_picks = 7

time = '22:30 EST'

days = ['Tuesday', 'Friday']

ticket_date = '7-Apr-2023'

next_649_draw_date = '06 May 2023'
next_49_draw_date = '08 Apr 2023'
next_encore_date = '29 Mar 2023'


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

lotto_49_prizes = {
    "2/6" : "Free Play",
    "2/6+Bonus" : 5.00,
    "3/6" : 10.00,
    "4/6" : 83.60,
    "5/6" : 859.90,
    "5/6+Bonus" : 206832.30,
    "6/6" : 5000000.00,
}

encore_prizes_right_left = {
    "Last_Digit" : 2.00,
    "Last_2" : 5.00,
    "Last_3" : 10.00,
    "Last_4" : 100.00,
    "Last_5" : 1000.00,
    "Last_6" : 100000.00,
    "7/7" : 1000000.00,
}

encore_prizes_left_right = {
    "First_2" : 2.00,
    "First_3" : 5.00,
    "First_4" : 10.00,
    "First_5" : 100.00,
    "First_6" : 1000.00
}
encore_combination = {

}


## Variables for lottery number picks of the group
lotto_name = "Lotto Max"
lotto_649_name = "Lotto 6/49"
lotto_49_name = "Ontario 49"
lotto_encore = "Encore"

draw_date = " "

group_picks = [
    [8,17,23,33,42,47,49],
    [9,32,42,43,46,48,50],
    [1,2,9,19,20,35,45]
]

group_649_picks = [
    [2,10,34,43,47,48],
    [5,7,31,35,45,49],
    [1,11,29,36,42,43],
    [9,15,24,30,32,35]


]

group_49_picks = [
    [9,15,27,34,39,43],
    [1,9,13,18,24,30]

]

group_encore_picks = [
    [5,3,5,2,1,3,2]
]

lines_picked = len(group_picks)

bet_amount = [
    5.00
]

bet_amounts_649 = [
    4.00
    ]

bet_amounts_49 = [
    1.00
]

bet_amount_encore = [
1.00
]

group_funding_balance = None