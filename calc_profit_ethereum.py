#!/usr/bin/python
import json
import urllib2
import re
import socket
import csv
import sys
import os.path
import time

res = urllib2.urlopen('https://alpha61.com/ethereum.json')
data = res.read()
print "1. data: ", data, "\n"

data = re.sub(r'ethereumStats = ', '', data)
data = re.sub(r';$', '', data)

print "2. repl: ", data, "\n"

eth = json.loads(data)
print "3. json: difficulty = ", eth['difficulty'], " blocktime = ", eth['blockTime'], "\n"

netHash = (eth['difficulty'] / eth['blockTime']) / 1e9;
print "4. nethash = ", netHash, "\n"


def hash_to_usd_day( userHash ):
	userRatio = (userHash * 1e6) / (netHash * 1e9)
	blocksPerMin = 60.0 / eth['blockTime']
	ethPerMin = blocksPerMin * 5.0
	earn_min = userRatio * ethPerMin
	earn_hour = earn_min * 60
	earn_day = earn_hour * 24
	earn_mon = earn_day * 30
	#print "- hash = ", userHash, "  earn_day = ", earn_day * eth['priceUsd'], " $/day\n"
	return earn_day * eth['priceUsd'];

gpu_hash = float(input("> Mh/s: "))
gpu_price = float(input("> Price for 1 GPU: "))
gpu_cnt = int(input("> GPU count: "))

gpu_price = gpu_price * gpu_cnt
gpu_hash_one = gpu_hash
gpu_hash = gpu_hash * gpu_cnt
earn_day = hash_to_usd_day(gpu_hash)
K_en = 0.063 # $/kWt = 1.68 UAH
W = float(input("> Watt: "))
W_one = W
W = W*gpu_cnt
earn_day_real = earn_day - (W/1000) * 24 * K_en

Whash = W / gpu_hash
Phash = earn_day_real / gpu_hash
print "- Details:\n\thash = %f\n\tearn_day = %f\n\tWatts = %f\n\tefficiency = %f W/hash\n\tefficiency = %f price/hash" % (gpu_hash, earn_day, W, Whash, Phash)

print "- Earn (real):\n\tday = %f\n\tweek = %f\n\tmonth = %f" % (earn_day_real, earn_day_real*7, earn_day_real*30)

print "- ROI:\n\tdays to 1 ETH = %f\n\tdays to zero = %f" % ( (1 / (earn_day/eth['priceUsd']) ), (gpu_price / earn_day_real) )

print "- Risk:\n\tcurrent profitability = %f X of electicity price\n\tminimal ETH price = $%f (for 2X electicity price)" % (earn_day / ( (W/1000) * 24 * K_en ), (2 * ((W/1000) * 24 * K_en) / (earn_day/eth['priceUsd']))) 
