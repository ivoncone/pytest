home = {
	'name': 'casa',
	'offers': {
		'offer_one': {'price': 1600},
		'offer_two': {'price': 1800},
		'offer_three': {'price': 1200}
	}
}

max_val = max(home.map('offers.price'))

print(str(max_val))