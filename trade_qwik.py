import trade
import time
import json
from pydash import py_


def main():
    requests = make_requests()
    response_content = []
    for request in requests:
        response_content.append(json.loads(request.content))
    process_responses(response_content)


def make_requests():
    ticker_request = trade.get_ticker()
    recent_trades_request = trade.get_recent_trades('VIVA', 'BTC')
    open_btc_trades_request = trade.get_open_trades('VIVA', 'BTC')
    my_pending_trades = trade.pending_trades()
    my_trade_history = trade.trade_history(None, None, None)
    my_balance = trade.get_balance()
    return [ticker_request, recent_trades_request, open_btc_trades_request, my_pending_trades, my_trade_history, my_balance]


def process_responses(responses):
    btc_dict = py_.find(responses[0], lambda x: x['counter'] == 'BTC')
    current_price = float(btc_dict['last'])
    process_ticker_response(responses[0])
    process_recent_trades_response(responses[1])
    process_open_btc_trades_response(responses[2])
    process_my_pending_trades_response(responses[3], current_price)
    process_my_trade_history(responses[4])
    process_my_balance_response(responses[5])


def process_ticker_response(ticker_response):
    btc_dict = py_.find(ticker_response, lambda x: x['counter'] == 'BTC')
    if float(btc_dict['last']) > .005:
        ask_request = trade.make_ask_order('VIVA', 'BTC', '100', '0.005')
        print(ask_request.status_code)
    if float(btc_dict['last']) < .001:
        bid_request = trade.make_bid_order('VIVA', 'BTC', '100', '0.001')
        print(bid_request.status_code)


def process_recent_trades_response(recent_trades_response):
    btc_list = py_.filter(recent_trades_response, lambda x: x['counter'] == 'BTC')
    print(btc_list)


def process_open_btc_trades_response(open_btc_trades_response):
    ask_list = py_.order_by(open_btc_trades_response['asks'], ['price'])
    bid_list = py_.order_by(open_btc_trades_response['bids'], ['price'])
    lowest_ask = py_.head(ask_list)
    highest_bid = py_.last(bid_list)
    if float(highest_bid['price']) > .005:
        amount = highest_bid['amount']
        price = highest_bid['price']
        print("Highest bid is: " + highest_bid['price'] + ", making ask offer for " + amount + " VIVA at " + price +
              " BTC/VIVA")
        ask_request = trade.make_ask_order('VIVA', 'BTC', str(amount), str(price))
        print(ask_request.status_code)
    if float(lowest_ask['price']) < .001:
        amount = lowest_ask['amount']
        price = lowest_ask['price']
        print("Lowest ask is: " + highest_bid['price'] + ", making bid offer for " + amount + " VIVA at " + price +
              " BTC/VIVA")
        bid_request = trade.make_bid_order('VIVA', 'BTC', str(amount), str(price))
        print(bid_request.status_code)


def process_my_pending_trades_response(my_pending_trades_response, current_price):
    for single_trade in my_pending_trades_response:
        if (float(single_trade['price']) < current_price * .9) or (float(single_trade['price']) > current_price * 1.1):
            print("Canceling order because it is more than 10% different than current price")
            cancel_order = trade.cancel_order(int(single_trade['order']))
            print(cancel_order.status_code)


def process_my_trade_history(my_trade_history_response):
    print("My Trade History: " + str(my_trade_history_response))


def process_my_balance_response(my_balance_response):
    btc_dict = py_.find(my_balance_response, lambda x: x['currency'] == 'BTC')
    print("My BTC balance: " + str(btc_dict))


while True:
    main()
    print("Will wait 60 secs for next requests")
    time.sleep(60)
