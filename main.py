
from variables import lottery_guru_url, lotto_max_prizes, \
    bet_amount, lotto_name, group_picks, lottery_played, bet_amount, lotto_max_picks

import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
import datetime as dt
import pytz
import lxml

## Get the lottery cards from the website
def scrape_lottery_cards(url):
    lottery_guru = requests.get(url)

    if lottery_guru.status_code == 200:
        print(f"SCRAPE SUCCESSFUL {lottery_guru.status_code}")

        soup_guru = BS(lottery_guru.text, "lxml")

        ## Retrieve all the cards from the site
        lottery_cards = soup_guru.find_all('div', class_ = 'lg-card lg-link')

    else:
        print(lottery_guru.status_code)

    return lottery_cards


## Get the results of the lotto max lottery
def lotto_max_numbers():
    lottery_cards = scrape_lottery_cards(lottery_guru_url)

    results = dict()
    for n in [0, 1]:

        lotto_max_card = lottery_cards[n]
        name = lotto_max_card.find("div", class_="column is-10 lg-name")
        name = name.text
        jackpot = lotto_max_card.find("div", class_="lg-sum")
        jackpot = jackpot.text.strip()
        numbers = lotto_max_card.find_all("ul", class_="lg-numbers")

        if name == "Lotto Max":
            print("Match")

            lotto_max_numbers = list()
            for num in numbers[0].find_all("li"):
                lotto_max_numbers.append(int(num.text))
                draw_dates = lotto_max_card.find_all("div", class_="lg-time")
                last_result_date = draw_dates[0].text.strip()
                last_result_date = last_result_date.split("\n")
                next_result_date = draw_dates[1].text.strip()
                next_result_date = next_result_date.split("\n")

            results[f"card_{n}"] = [lotto_max_numbers, last_result_date, next_result_date]

            return results[f"card_{n}"][0], results[f"card_{n}"][1], results[f"card_{n}"][2], jackpot


def matched_numbers(picks, lotto_played):
    last_winning_numbers, last_draw_date, next_draw_date, jackpot = lotto_max_numbers()
    bonus_number = last_winning_numbers[-1]
    last_winning_numbers = last_winning_numbers[0:-1]

    matches = dict()

    for e, nums in enumerate(picks):
        matches[f"Line_{e + 1}"] = dict()
        matched_picks = [x for x in nums if x in last_winning_numbers]
        matched_bonus = [x for x in nums if x == bonus_number]
        # print(f"Regular Pick Matches: {matched_picks}")
        # print(f"Bonus Number Matched: {matched_bonus}")
        matches[f"Line_{e + 1}"][f"Number_Matches_{e + 1}"] = matched_picks
        if len(matched_bonus) == 1:
            matches[f"Line_{e + 1}"][f"Bonus_Match_{e + 1}"] = matched_bonus
        else:
            matches[f"Line_{e + 1}"][f"Bonus_Match_{e + 1}"] = []
    return matches, last_winning_numbers, bonus_number, last_draw_date, next_draw_date, jackpot


def correct_vs_incorrect(matches_from_picks):
    correct_vs_incorrect = []
    for key, val in matches_from_picks.items():
        keys = list(val.keys())
        correct = len(matches_from_picks[key][keys[0]])
        bonus = len(matches_from_picks[key][keys[1]])
        if bonus == 1:
            c_i = f"{correct}/{lotto_max_picks}+Bonus"
        else:
            c_i = f"{correct}/{lotto_max_picks}"

        correct_vs_incorrect.append(c_i)

    return correct_vs_incorrect


def prizes(correct_picks_incorrect_picks):
    prizes = []
    for picks in correct_picks_incorrect_picks:
        try:
            p = lotto_max_prizes[picks]
        except:
            p = 0
        prizes.append(p)
    return prizes


def load_df(filename):
    import pandas as pd
    df = pd.read_csv(filename)
    return df


def new_row(group_picks, lottery_played):
    df = load_df(filename="data/lotto_max_stats2.csv")

    matches, last_winning_numbers, bonus_number, last_draw_date, next_draw_date, jackpot = matched_numbers(
        picks=group_picks, lotto_played=lottery_played)

    c_i = correct_vs_incorrect(matches_from_picks=matches)

    group_prizes = prizes(correct_picks_incorrect_picks=c_i)

    add_new_row = {
        df.columns[0]: last_draw_date[-1],
        df.columns[1]: last_draw_date[-2],
        df.columns[2]: lotto_name,
        df.columns[3]: last_winning_numbers,
        df.columns[4]: bonus_number,
        df.columns[5]: lottery_played,
        df.columns[6]: group_picks,
        df.columns[7]: bet_amount,
        df.columns[8]: matches,
        df.columns[9]: c_i,
        df.columns[10]: group_prizes,
        df.columns[11]: sum(group_prizes),
        df.columns[12]: -(sum(bet_amount)) - sum(group_prizes)

    }

    return add_new_row


def update_csv(group_picks, lottery_played, file_name):
    row_to_add = new_row(group_picks=group_picks, lottery_played=lottery_played)

    df = load_df(filename=file_name)

    last_winning_numbers = df.iloc[-1]["Numbers Drawn"]
    last_winning_numbers = last_winning_numbers.replace("[", "", 3)
    last_winning_numbers = last_winning_numbers.replace("]", "", 2)
    last_winning_numbers = [int(e) for e in last_winning_numbers.split(",")]
    print(last_winning_numbers, type(last_winning_numbers))
    print(row_to_add["Numbers Drawn"])

    new_row_series = pd.Series(row_to_add)
    df2 = pd.concat([df, new_row_series.to_frame().T], ignore_index=True)

    if last_winning_numbers == row_to_add["Numbers Drawn"]:
        print("Nothing to add")
    else:
        print("Adding new row to file")

        # df = df.append(row_to_add, ignore_index=True)

        new_row_series = pd.Series(row_to_add)
        df2 = pd.concat([df, new_row_series.to_frame().T], ignore_index=True)

        df2.to_csv("lotto_max_stats2.csv",
                   lineterminator='\n',
                   index=False)



if __name__ == '__main__':
    print("Running")
    print(dt.datetime.now(tz=pytz.timezone('EST')))
    update_csv(group_picks=group_picks, lottery_played=lottery_played, file_name="data/lotto_max_stats2.csv")

