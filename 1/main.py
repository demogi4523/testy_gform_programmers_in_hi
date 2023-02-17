from typing import List
from functools import cmp_to_key

def find_top(cands: List[dict], amount, safe_mode=False):
	# Проверка тривиального случая
	if len(cands) <= amount:
		return cands

	# Производим глубокое копирование по необходимости
	if safe_mode:
		from copy import deepcopy
		cands = deepcopy(cands)
  
	def cmp(cand: dict, other_cand: dict):
		def get_score(cand: dict):
			# Честно говоря, было лень обрабатывать ошибку, поэтому так
			mock_scores = {
				"math": 0,
				"russian_language": 0,
				"computer_science": 0,
			}
			scores = cand.get("scores", mock_scores)

			informatics_score = scores.get("computer_science", 0)
			math_score = scores.get("math", 0)
			rl_score = scores.get("russian_language", 0)

			extra_score = cand.get("extra_scores", 0)
			
			return (informatics_score + math_score + rl_score + extra_score, (informatics_score, math_score, rl_score))

		cand_score, cand_metrics = get_score(cand)
		other_cand_score, other_cand_metrics = get_score(other_cand)
	
		if cand_score != other_cand_score:
			return cand_score - other_cand_score
		if cand_metrics[0] != other_cand_metrics[0]:
			return cand_metrics[0] - other_cand_metrics[0]
		if cand_metrics[1] != other_cand_metrics[1]:
			return cand_metrics[1] - other_cand_metrics[1]
		if cand_metrics[2] != other_cand_metrics[2]:
			return cand_metrics[2] - other_cand_metrics[2]
		# Проверять дополнительные баллы не имеет смысла, 
		# т.к. они равны - иначе сработало бы одно из ветвлений выше
		# В данной ситуации оставляем текущий порядок - это место слабое в алгоритме,
		# т.к. у кто-то из равных кандидатов может не пройти
		return 1
  
	cands.sort(key=cmp_to_key(cmp), reverse=True)
	return cands[:amount]

def find_top_20(cands: List[dict], safe_mode=False):
	# Используем частный случай более общей функции find_top
	return find_top(cands, 20, safe_mode)
