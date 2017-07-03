from collections import OrderedDict
stocks = {
	'goog' : 78,
	'fb' : 56,
	'amz' : 32,
	'apl' :190,
	'ntfx' : 89 
}
print (OrderedDict(sorted(stocks.items(), key=lambda t: t[1])))
print (sorted(stocks.items()), key = lambda t : t[1])
