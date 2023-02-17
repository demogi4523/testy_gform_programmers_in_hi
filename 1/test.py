from pprint import pprint
from main import find_top

candidates = [
 {"name": "Vasya",  "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
 {"name": "Petya",  "scores": {"math": 92, "russian_language": 33, "computer_science": 34},  "extra_scores":1}
]

def gen_cands(amount):
	from random import randint
	r = lambda: randint(0, 100)
	cands = [
		{
			"name": f"cand{[i]}",
			"scores": {
				"math": r(),
				"russian_language": r(),
				"computer_science": r()
			},
			"extra_scores":r()
		} for i in range(1, amount + 1)
	]
	return cands

candidates2 = gen_cands(10)

pprint(find_top(candidates, 4))
# pprint(candidates2)
print()
pprint(find_top(candidates2, 3))
