from bs4 import BeautifulSoup
import requests
DOUBLE_CHEST = 3456
INVENTORY = 2240
STACK = 64
SINGLE_ORDER = 7964
def main():
    while True:
        print("Choices:\n\t1 - Null Ovoid\n\t"
              "2 - Whale Bait\n\t3 - Enchanted Golden Carrot")
        choice = input("Enter your choice.")
        if choice == "1":
            null_ovoid()
        elif choice == "2":
            whale_bait()
        elif choice == "3":
            golden_carrot()
        else:
            print("Please enter a valid choice.")
            continue
        choice = input("Enter 'y' to continue.")
        if choice != 'y':
            break


def whale_bait():
    whale = whale_price()
    fish = fish_price()
    salmon = salmon_price()
    prismarine = prismarine_price()
    gold = gold_price()
    ink = ink_price()
    unit_price = round(fish*5 + salmon + prismarine*3 + gold*9 + ink, 1)
    amt = get_amt()
    print_profit(unit_price, whale, amt)

def get_amt():
    while True:
        print("Either enter a number or one of these keywords:\n\tSTACK = 64\n\tINVENTORY = "
              "2240\n\tDOUBLE_CHEST = 3456\n\tSINGLE_ORDER = 7964")
        choice = input("How much would you like to craft? ")
        if choice.isdigit():
            amt = int(choice)
            break
        elif choice == 'STACK':
            amt = STACK
            break
        elif choice == 'DOUBLE_CHEST':
            amt = DOUBLE_CHEST
            break
        elif choice == 'INVENTORY':
            amt = INVENTORY
            break
        elif choice == 'SINGLE_ORDER':
            amt = SINGLE_ORDER
            break
        elif choice[choice.index(' ')+1:] == 'DOUBLE_CHEST':
            num = int(choice[:choice.index(' ')])
            amt = num*DOUBLE_CHEST
            break

        print("Please enter a valid amount.")
    return amt


def print_profit(unit_cost, unit_profit, amt):
    total_cost = round(unit_cost*amt, 1)
    total_revenue = round(unit_profit*amt, 1)
    profit = round(total_revenue-total_cost, 1)
    profit_percentage = round((profit / total_cost) * 100, 2)
    print('You are crafting {:,} items, at ${:,} per item.'.format(amt, unit_cost))
    print('Total Cost: ${:,}'.format(total_cost))
    print('Total Profit: ${:,} ({:.2f}% profit)'.format(profit, profit_percentage))


def whale_price():
    html_text = requests.get('https://www.skyblock.bz/product/WHALE_BAIT').text
    soup = BeautifulSoup(html_text, 'lxml')
    divs = soup.find_all('td', class_="svelte-f7mtyj")[13].text
    return float(divs.replace(',', '')[:divs.index(' ')])


def fish_price():
    html_text = requests.get('https://www.skyblock.bz/product/RAW_FISH').text
    soup = BeautifulSoup(html_text, 'lxml')
    divs = soup.find_all('td', class_="svelte-f7mtyj")[1].text
    return float(divs.replace(',', '')[:divs.index(' ')])


def salmon_price():
    html_text = requests.get('https://www.skyblock.bz/product/RAW_FISH:1').text
    soup = BeautifulSoup(html_text, 'lxml')
    divs = soup.find_all('td', class_="svelte-f7mtyj")[1].text
    return float(divs.replace(',', '')[:divs.index(' ')])


def prismarine_price():
    html_text = requests.get('https://www.skyblock.bz/product/PRISMARINE_CRYSTALS').text
    soup = BeautifulSoup(html_text, 'lxml')
    divs = soup.find_all('td', class_="svelte-f7mtyj")[1].text
    return float(divs.replace(',', '')[:divs.index(' ')])


def gold_price():
    html_text = requests.get('https://www.skyblock.bz/product/GOLD_INGOT').text
    soup = BeautifulSoup(html_text, 'lxml')
    divs = soup.find_all('td', class_="svelte-f7mtyj")[1].text
    return float(divs.replace(',', '')[:divs.index(' ')])


def ink_price():
    html_text = requests.get('https://www.skyblock.bz/product/INK_SACK').text
    soup = BeautifulSoup(html_text, 'lxml')
    divs = soup.find_all('td', class_="svelte-f7mtyj")[1].text
    return float(divs.replace(',', '')[:divs.index(' ')])


def null_ovoid():
    spheres = sphere_price()
    obsidian = obsidian_price()
    ovoid = ovoid_price()
    unit_price = round(spheres*128 + obsidian*32, 1)
    amt = get_amt()
    print_profit(unit_price, ovoid, amt)


def sphere_price():
    html_text = requests.get('https://www.skyblock.bz/product/NULL_SPHERE').text
    soup = BeautifulSoup(html_text, 'lxml')
    divs = soup.find_all('td', class_="svelte-f7mtyj")[1].text
    return float(divs.replace(',', '')[:divs.index(' ')])


def obsidian_price():
    html_text = requests.get('https://www.skyblock.bz/product/ENCHANTED_OBSIDIAN').text
    soup = BeautifulSoup(html_text, 'lxml')
    divs = soup.find_all('td', class_="svelte-f7mtyj")[1].text
    return float(divs.replace(',', '')[:divs.index(' ')])


def ovoid_price():
    html_text = requests.get('https://www.skyblock.bz/product/NULL_OVOID').text
    soup = BeautifulSoup(html_text, 'lxml')
    divs = soup.find_all('td', class_="svelte-f7mtyj")[13].text
    return float(divs.replace(',', '')[:divs.index(' ')])


def golden_carrot():
    print(1)


if __name__ == "__main__":
    main()
