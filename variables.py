lottery_played_lotto_max = True
lottery_played_649 = True
encore_played = False
ontario_49_played = True

lottery_guru_url = 'https://lotteryguru.com/ontario-lottery-results'

lotto_max_range = list(range(1,51))
lotto_649_range = list(range(1,50))

encore_number_options = ["1,1,1,1,1,1,1", "9,9,9,9,9,9,9"]

lotto_max_picks = 7
lotto_649_picks = 6
ontario_64_picks = 6
encore_picks = 7

time = '22:30 EST'

days = ['Tuesday', 'Friday']

ticket_date = '31-Jan-2023'

next_649_draw_date = '01 Feb 2023'
next_49_draw_date = '01 Feb 2023'
next_encore_date = '28 Jan 2023'


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
    [4,5,6,9,12,23,24],
    [13,14,15,19,34,48,50],
    [10,31,34,36,37,41,46],
    [7,20,21,26,31,35,46],
    [3,4,14,15,25,32,45],
    [7,15,25,31,32,45,50]
]

group_649_picks = [
    [17,21,30,35,46,48]

]

group_49_picks = [
    [1,27,29,30,37,41],
    [1,15,19,32,47,49]
]

group_encore_picks = [
    [3,4,7,6,1,1,9]
]

lines_picked = len(group_picks)

bet_amount = [
5.00, 5.00
]

bet_amounts_649 = [
    3.00, 3.00
]

bet_amounts_49 = [
0.00
]

bet_amount_encore = [

]

group_funding_balance = None