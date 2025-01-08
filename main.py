import requests


DOUBLE_CHEST = 3456
INVENTORY = 2240
STACK = 64
SINGLE_ORDER = 7964


def main():
    while True:
        print("Choices:\n\t1 - Null Ovoid\n\t2 - Whale Bait\n\t3 - Enchanted Golden Carrot\n\t4 - Revenant "
              "Viscera\n\t5 - Tarantula Silk\n\t6 - Booster Cookie Margins\n\t7 - Quit")
        choice = input("Enter your choice. ")
        if choice == "1":
            null_ovoid()
        elif choice == "2":
            whale_bait()
        elif choice == "3":
            golden_carrot()
        elif choice == "4":
            revenant_viscera()
        elif choice == "5":
            tarantula_silk()
        elif choice == "6":
            booster_cookie_margins()
        elif choice == "7":
            break
        else:
            print("Please enter a valid choice.")
            continue
        choice = 'n'
        while True:
            choice = input("Enter 'y' to continue or 'n' to quit. ")
            if choice == 'y':
                break
            elif choice == 'n':
                exit()
            else:
                print("Please enter a valid choice.")



def print_info(unit_buy_price, unit_sell_price, amount):
    total_cost = unit_buy_price*amount
    total_revenue = unit_sell_price*amount
    profit = total_revenue-total_cost
    profit_percentage = (profit / total_cost)*100
    print('You are crafting {:,} items at ${:,.1f} per item.'.format(amount, unit_buy_price))
    print('Your total cost is ${:,.1f}'.format(total_cost))
    print('Your total profit is ${:,.1f} ({:.1f}% profit)'.format(profit, profit_percentage))


def get_buy_order_price(path_extension):
    json = requests.get('https://api.hypixel.net/v2/skyblock/bazaar').json()
    return float(json['products'][path_extension]['sell_summary'][0]['pricePerUnit'])


def get_sell_order_price(path_extension):
    json = requests.get('https://api.hypixel.net/v2/skyblock/bazaar').json()
    return float(json['products'][path_extension]['buy_summary'][0]['pricePerUnit'])


def get_amt():
    while True:
        print("Either enter a number or one of these keywords:\n\tSTACK = 64\n\tINVENTORY = "
              "2240\n\tDOUBLE_CHEST = 3456\n\tSINGLE_ORDER = 7964\n\tAdd a number before any keyword to craft that "
              "many of the keyword value.")
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
        elif choice.find(' ') == -1:
            print(choice.find(' '))
        elif choice[choice.index(' ')+1:] == 'DOUBLE_CHEST':
            num = int(choice[:choice.index(' ')])
            amt = num*DOUBLE_CHEST
            break
        elif choice[choice.index(' ')+1:] == 'STACK':
            num = int(choice[:choice.index(' ')])
            amt = num*STACK
            break
        elif choice[choice.index(' ')+1:] == 'INVENTORY':
            num = int(choice[:choice.index(' ')])
            amt = num*INVENTORY
            break
        elif choice[choice.index(' ')+1:] == 'SINGLE_ORDER':
            num = int(choice[:choice.index(' ')])
            amt = num*SINGLE_ORDER
            break
    return amt


def null_ovoid():
    null_sphere = get_buy_order_price('NULL_SPHERE')
    ench_obsidian = get_buy_order_price('ENCHANTED_OBSIDIAN')
    unit_price = round(null_sphere*128 + ench_obsidian*32, 1)
    ovoid = get_sell_order_price('NULL_OVOID')
    amt = get_amt()
    print_info(unit_price, ovoid, amt)


def whale_bait():
    fish = get_buy_order_price('RAW_FISH')
    salmon = get_buy_order_price('RAW_FISH:1')
    gold = get_buy_order_price('GOLD_INGOT')
    ink = get_buy_order_price('INK_SACK')
    prismarine = get_buy_order_price('PRISMARINE_CRYSTALS')
    whale = get_sell_order_price('WHALE_BAIT')
    unit_price = fish*5 + salmon + gold*9 + ink + prismarine*3
    amt = get_amt()
    print_info(unit_price, whale, amt)


def golden_carrot():
    ench_carrot = get_buy_order_price('ENCHANTED_CARROT')
    gold_carrot = 15
    unit_price = ench_carrot*128 + gold_carrot*32
    ench_golden_carrot = get_sell_order_price('ENCHANTED_GOLDEN_CARROT')
    amt = get_amt()
    print_info(unit_price, ench_golden_carrot, amt)


def revenant_viscera():
    rev_flesh = get_buy_order_price('REVENANT_FLESH')
    ench_string = get_buy_order_price('ENCHANTED_STRING')
    unit_price = rev_flesh*128 + ench_string*32
    viscera = get_sell_order_price('REVENANT_VISCERA')
    amt = get_amt()
    print_info(unit_price, viscera, amt)


def tarantula_silk():
    tara_web = get_buy_order_price('TARANTULA_WEB')
    ench_flint = get_buy_order_price('ENCHANTED_FLINT')
    unit_price = tara_web*128 + ench_flint*32
    silk = get_sell_order_price('TARANTULA_SILK')
    amt = get_amt()
    print(unit_price, silk)
    print_info(unit_price, silk, amt)


def booster_cookie_margins():
    buy_order = get_buy_order_price("BOOSTER_COOKIE")
    sell_order = get_sell_order_price("BOOSTER_COOKIE") * 0.99
    margin = sell_order-buy_order
    print("Margin: ${:,.1f}".format(margin))


if __name__ == "__main__":
    main()
