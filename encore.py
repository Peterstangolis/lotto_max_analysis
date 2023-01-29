

from main import scrape_lottery_cards
from variables import lottery_guru_url, encore_played, encore_picks, \
    lotto_49_prizes, lotto_encore, bet_amount_encore, next_encore_date, group_encore_picks




def encore_numbers():
    lottery_cards = scrape_lottery_cards(lottery_guru_url)

    results = dict()
    for n in [10,11,12]:

        encore_card = lottery_cards[n]
        name = encore_card.find("div", class_="column is-10 lg-name")
        name = name.text
        numbers = encore_card.find_all("ul", class_="lg-numbers")


        if name == "Encore":
            print("Match")

            encore_numbers = list()
            for num in numbers[0].find_all("li"):
                encore_numbers.append(int(num.text))
                draw_dates = encore_card.find_all("div", class_="lg-time")
                last_result_date = draw_dates[0].text.strip()
                last_result_date = last_result_date.split("\n")
                next_result_date = draw_dates[1].text.strip()
                next_result_date = next_result_date.split("\n")

            results[f"card_{n}"] = [encore_numbers, last_result_date, next_result_date]

            return results[f"card_{n}"][0], results[f"card_{n}"][1], results[f"card_{n}"][2]


if encore_played:

    def load_df(filename):
        import pandas as pd
        df = pd.read_csv(filename)
        return df


    def new_row_encore(group_picks, lottery_played, ticket_date):
        df = load_df(filename="data/encore_analysis.csv")

        a, b, c = encore_numbers()
        encore_drawn = a
        Last_draw_date = b[-2]
        Last_draw_time = b[-1]
        Next_draw_date = c[-2]
        Next_draw_time = c[-1]

        add_new_row = {
            df.columns[0]: Last_draw_date,
            df.columns[1]: next_encore_date,
            df.columns[2]: Last_draw_time,
            df.columns[3]: lotto_encore,
            df.columns[4]: encore_drawn,
            df.columns[5]: encore_played,
            df.columns[6]: group_encore_picks,
            df.columns[7]: bet_amount_encore,
            df.columns[8]: None


        }
        return add_new_row

    def update_encore_csv(group_picks, lottery_played, file_name, ticket_date):
        import pandas as pd
        row_to_add = new_row_encore(group_picks=group_encore_picks, lottery_played=encore_played, ticket_date=next_encore_date)
        print(row_to_add)

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

            df2.to_csv("data\encore_analysis.csv",
                       lineterminator='\n',
                       index=False)

            df2.to_pickle("data\encore_analysis.pkl")
        else:
            print(row_to_add["Draw Date"], row_to_add["Ticket Date"])


    update_encore_csv(group_picks=group_encore_picks, lottery_played=encore_played,
                  file_name="data/encore_analysis.csv", ticket_date=next_encore_date)







