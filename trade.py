import requests
import json
from config import api_key

url = "https://www.tradeqwik.com/api/1/"


def get_ticker():
    tickerURL = url + "ticker"
    return requests.request('GET', tickerURL)


def get_recent_trades(base, counter):
    recentTradesURL = url + "recent_trades/" + base + "/" + counter
    return requests.request("GET", recentTradesURL)


def get_open_trades(base, counter):
    openTradesURL = url + "open_trades/" + base + "/" + counter
    return requests.request("GET", openTradesURL)


def make_bid_order(base, counter, amount, price):
    bidURL = url + "bid"
    bidReqBody = {
        'api_key': api_key,
        'base': base,
        'counter': counter,
        'amount': amount,
        'price': price
    }
    return requests.request('POST', bidURL, json=bidReqBody)


def make_ask_order(base, counter, amount, price):
    askURL = url + "ask"
    askReqBody = {
        'api_key': api_key,
        'base': base,
        'counter': counter,
        'amount': amount,
        'price': price
    }
    return requests.request('POST', askURL, json=askReqBody)


def cancel_order(orderNumber):
    cancelURL = url + "cancel"
    cancelReqBody = {
        'api_key': api_key,
        'order': orderNumber
    }
    return requests.request('POST', cancelURL, json=cancelReqBody)


def pending_trades():
    listURL = url + "pending_trades"
    listReqBody = {
        'api_key': api_key
    }
    return requests.request('POST', listURL, json=listReqBody)


def trade_history(before, limit, lastId):
    historyURL = url + "trade_history"
    historyReqBody = {
        'api_key': api_key,
        'before': before,
        'limit': limit,
        'lastId': lastId
    }
    return requests.request('POST', historyURL, json=historyReqBody)


def get_balance():
    balanceURL = url + "balance"
    balanceReqBody = {
        'api_key': api_key
    }
    return requests.request("POST", balanceURL, json=balanceReqBody)
