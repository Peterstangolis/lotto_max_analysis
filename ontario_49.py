

from main import scrape_lottery_cards
from variables import lottery_guru_url, ontario_49_played, group_49_picks, \
    lotto_49_prizes, lotto_49_name, bet_amounts_49, next_49_draw_date, ontario_64_picks



def lotto_49_numbers():
    lottery_cards = scrape_lottery_cards(lottery_guru_url)

    results = dict()
    for n in [5,6]:

        lotto_49_card = lottery_cards[n]
        name = lotto_49_card.find("div", class_="column is-10 lg-name")
        name = name.text
        jackpot = lotto_49_card.find("div", class_="lg-sum")
        jackpot = jackpot.text.strip()
        numbers = lotto_49_card.find_all("ul", class_="lg-numbers")

        if name == "Ontario 49":
            print("Match")

            lotto_649_numbers = list()
            for num in numbers[0].find_all("li"):
                lotto_649_numbers.append(int(num.text))
                draw_dates = lotto_49_card.find_all("div", class_="lg-time")
                last_result_date = draw_dates[0].text.strip()
                last_result_date = last_result_date.split("\n")
                next_result_date = draw_dates[1].text.strip()
                next_result_date = next_result_date.split("\n")

            results[f"card_{n}"] = [lotto_649_numbers, last_result_date, next_result_date]

            return results[f"card_{n}"][0], results[f"card_{n}"][1], results[f"card_{n}"][2], jackpot

if ontario_49_played:

    def matched_numbers_49(picks, lotto_played):
        last_winning_numbers, last_draw_date, next_draw_date, jackpot = lotto_49_numbers()
        bonus_number = last_winning_numbers[-1]
        last_winning_numbers = last_winning_numbers[0:-1]

        if len(picks) >= 1:
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
        else:
            matches = []

        return matches, last_winning_numbers, bonus_number, last_draw_date, next_draw_date, jackpot

    def correct_vs_incorrect_49(matches_from_picks):
        correct_vs_incorrect = []
        for key, val in matches_from_picks.items():
            keys = list(val.keys())
            correct = len(matches_from_picks[key][keys[0]])
            bonus = len(matches_from_picks[key][keys[1]])
            if bonus == 1:
                c_i = f"{correct}/{ontario_64_picks}+Bonus"
            else:
                c_i = f"{correct}/{ontario_64_picks}"

            correct_vs_incorrect.append(c_i)

        return correct_vs_incorrect

    def prizes_49(correct_picks_incorrect_picks):
        prizes = []
        for picks in correct_picks_incorrect_picks:
            try:
                p = lotto_49_prizes[picks]
            except:
                p = 0
            prizes.append(p)
        return prizes

    def load_df(filename):
        import pandas as pd
        df = pd.read_csv(filename)
        return df


    def new_row_49(group_picks, lottery_played, ticket_date):
        df = load_df(filename="data/lotto_49_analysis.csv")

        matches, last_winning_numbers, bonus_number, last_draw_date, next_draw_date, jackpot = matched_numbers_49(
            picks=group_49_picks, lotto_played=ontario_49_played)

        c_i = correct_vs_incorrect_49(matches_from_picks=matches)

        group_prizes = prizes_49(correct_picks_incorrect_picks=c_i)
        money = []
        freeplay = []
        for p in group_prizes:
            if p == 'Free Play':
                freeplay.append(1)
            else:
                money.append(p)

        add_new_row = {
            df.columns[0]: last_draw_date[-1],
            df.columns[1]: ticket_date,
            df.columns[2]: last_draw_date[-2],
            df.columns[3]: lotto_49_name,
            df.columns[4]: last_winning_numbers,
            df.columns[5]: bonus_number,
            df.columns[6]: ontario_49_played,
            df.columns[7]: group_49_picks,
            df.columns[8]: bet_amounts_49,
            df.columns[9]: matches,
            df.columns[10]: c_i,
            df.columns[11]: group_prizes,
            df.columns[12]: sum(money),
            df.columns[13]: len(freeplay),
            df.columns[14]: -(sum(bet_amounts_49)) - sum(money)

        }
        return add_new_row


    def update_49_csv(group_picks, lottery_played, file_name, ticket_date):
        import pandas as pd
        row_to_add = new_row_49(group_picks=group_picks, lottery_played=lottery_played, ticket_date=ticket_date)

        df = load_df(filename=file_name)

        try:
            last_winning_numbers = df.iloc[-1]["Numbers Drawn"]
            last_winning_numbers = last_winning_numbers.replace("[", "", 3)
            last_winning_numbers = last_winning_numbers.replace("]", "", 2)
            last_winning_numbers = [int(e) for e in last_winning_numbers.split(",")]
            print(last_winning_numbers, type(last_winning_numbers))
            print(row_to_add["Numbers Drawn"])
        except:
            last_winning_numbers = []

        new_row_series = pd.Series(row_to_add)
        df2 = pd.concat([df, new_row_series.to_frame().T], ignore_index=True)

        if last_winning_numbers == row_to_add["Numbers Drawn"]:
            print("Nothing to add")
        elif row_to_add["Draw Date"] == row_to_add["Ticket Date"]:
            print("Adding new row to file")

            # df = df.append(row_to_add, ignore_index=True)

            new_row_series = pd.Series(row_to_add)
            df2 = pd.concat([df, new_row_series.to_frame().T], ignore_index=True)

            df2.to_csv("data\lotto_49_analysis.csv",
                       lineterminator='\n',
                       index=False)

            df2.to_pickle("data\lotto_49_analysis.pkl")
        else:
            print(row_to_add["Draw Date"], row_to_add["Ticket Date"])


    update_49_csv(group_picks=group_49_picks, lottery_played=ontario_49_played,
                   file_name="data/lotto_49_analysis.csv", ticket_date=next_49_draw_date)