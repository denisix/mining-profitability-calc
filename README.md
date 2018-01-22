# mining-profitability-calc

Calculators:
1) Ethereum - calc_profit_ethereum.py


Example usage:
```
$ python calc_profit_ethereum.py
```

Output example:
```
1. data:  ethereumStats = {"blockTime": 14.7802293511395, "lastUpdate": 1516660202.166973, "priceUsd": 940.88, "difficulty": 2390878600435750}; 

2. repl:  {"blockTime": 14.7802293511395, "lastUpdate": 1516660202.166973, "priceUsd": 940.88, "difficulty": 2390878600435750} 

3. json: difficulty =  2390878600435750  blocktime =  14.7802293511 

4. nethash =  161761.941823 

> Mh/s: 23.2
> Price for 1 GPU: 360
> GPU count: 6
> Watt: 125
- Details:
	hash = 139.200000
	earn_day = 23.664629
	Watts = 750.000000
	efficiency = 5.387931 W/hash
	efficiency = 0.161858 price/hash
- Earn (real):
	day = 22.530629
	week = 157.714401
	month = 675.918860
- ROI:
	days to 1 ETH = 39.758917
	days to zero = 95.869495
- Risk:
	current profitability = 20.868279 X of electicity price
	minimal ETH price = $90.173223 (for 2X electicity price)
```
