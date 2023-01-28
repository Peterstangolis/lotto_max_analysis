

from main import scrape_lottery_cards
from variables import lottery_guru_url, encore_played, encore_picks, \
    lotto_49_prizes, lotto_encore, bet_amount_encore, next_encore_date, group_encore_picks




def encore_numbers():
    lottery_cards = scrape_lottery_cards(lottery_guru_url)

    results = dict()
    for n in [11,12]:

        encore_card = lottery_cards[n]
        name = encore_card.find("div", class_="column is-10 lg-name")
        name = name.text
        numbers = encore_card.find_all("ul", class_="lg-numbers")
        print(numbers)

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

