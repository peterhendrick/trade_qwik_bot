A www.tradeqwik.com bot to automate your trades!
=======

This TradeQwik bot was written using python 3.6.0

This bot will create VIVA/BTC ask offers if the last VIVA/BTC tradeqwik exchange trade is over .005 VIVA/BTC in price,
or if there are any existing bid offers on the exchange over .005 VIVA/BTC, it will attempt to fulfill them.

It will create VIVA/BTC bid offers if the last VIVA/BTC tradeqwik exchange trade is under .001 VIVA/BTC in price,
or if there are any existing ask offers on the exchange under .001 VIVA/BTC, it will attempt to fulfill them.

It will cancel any of your pending orders if they are 10% different from the last traded price on the exchange.

It will also print out any recent VIVA/BTC tradeqwik exchange trades as well as your trade history and your BTC balance.

The bot will make requests every 60 seconds when running

All api calls are all held within the trade.py file, while the bot itself operates within the trade_qwik.py file.


To download:

```bash
git clone https://github.com/peterhendrick/trade_qwik_bot && cd trade_qwik_bot
```

Then add a config file for your API_KEY, type:

```bash
touch config.py && echo 'API_KEY="your api key"' > config.py
```

To install dependencies type:

```bash
pip install -r requirements.txt
```

To run type:

```bash
python3 trade_qwik.py
```


If you would like to verify your download, you can use the SHASUMS file and the gpg SHASUMS.sig file.

To verify the integrity of the SHASUMS file, first import my public pgp key:

```bash
gpg --keyserver pgp.mit.edu --recv EC3ED53D
```

Then, to verify my signature of the SHASUMS file, type:

```bash
gpg --verify SHASUMS.sig SHASUMS
```

If you see "Good signature", then that is my file.


To verify your downloaded files, type:

```bash
shasum -a 256 trade.py && cat SHASUMS | grep trade.py
```

If the lines match exactly, you have verified your download hashes match. Now just get the hash from the other file.

```bash
shasum -a 256 trade_qwik.py && cat SHASUMS | grep trade_qwik.py
```
