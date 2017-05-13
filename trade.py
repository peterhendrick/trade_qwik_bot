import requests
from config import API_KEY

URL = "https://www.tradeqwik.com/api/1/"


def get_ticker():
    ticker_url = URL + "ticker"
    return requests.request('GET', ticker_url)


def get_recent_trades(base, counter):
    recent_trades_url = URL + "recent_trades/" + base + "/" + counter
    return requests.request("GET", recent_trades_url)


def get_open_trades(base, counter):
    open_trades_url = URL + "open_trades/" + base + "/" + counter
    return requests.request("GET", open_trades_url)


def make_bid_order(base, counter, amount, price):
    bid_url = URL + "bid"
    bid_req_body = {
        'api_key': API_KEY,
        'base': base,
        'counter': counter,
        'amount': amount,
        'price': price
    }
    return requests.request('POST', bid_url, json=bid_req_body)


def make_ask_order(base, counter, amount, price):
    ask_url = URL + "ask"
    ask_req_body = {
        'api_key': API_KEY,
        'base': base,
        'counter': counter,
        'amount': amount,
        'price': price
    }
    return requests.request('POST', ask_url, json=ask_req_body)


def cancel_order(order_number):
    cancel_url = URL + "cancel"
    cancel_req_body = {
        'api_key': API_KEY,
        'order': order_number
    }
    return requests.request('POST', cancel_url, json=cancel_req_body)


def pending_trades():
    list_url = URL + "pending_trades"
    list_req_body = {
        'api_key': API_KEY
    }
    return requests.request('POST', list_url, json=list_req_body)


def trade_history(before, limit, last_id):
    history_url = URL + "trade_history"
    history_req_body = {
        'api_key': API_KEY,
        'before': before,
        'limit': limit,
        'lastId': last_id
    }
    return requests.request('POST', history_url, json=history_req_body)


def get_balance():
    balance_url = URL + "balance"
    balance_req_body = {
        'api_key': API_KEY
    }
    return requests.request("POST", balance_url, json=balance_req_body)
