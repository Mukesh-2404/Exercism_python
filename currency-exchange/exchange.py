def exchange_money(budget, exchange_rate):
    return budget/exchange_rate
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    pass

def get_change(budget, exchanging_value):
    return budget - exchanging_value
    """
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    pass

def get_value_of_bills(denomination, number_of_bills):
    return int(number_of_bills*denomination)
    """
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    pass

def get_number_of_bills(amount, denomination):
    return amount//denomination
    """
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    pass

def get_leftover_of_bills(amount, denomination):
    return amount % denomination
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    pass

def exchangeable_value(budget, exchange_rate, spread, denomination):
    new_rate = exchange_rate + 0.01*spread*exchange_rate
    max_currency=exchange_money(budget, new_rate)
    no_of_bills=max_currency//denomination
    return no_of_bills*denomination
    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    pass
