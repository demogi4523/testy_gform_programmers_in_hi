from typing import List, Union

def get_inductees(names: List[str], dates: List[Union[int, None]], genders: List[Union[str, None]]) -> None:
	cur_year = 2021
	def create_humans(names: List[str], dates: List[Union[int, None]], genders: List[Union[str, None]]) -> List[dict]:
		res = []
		for i in range(len(names)):
			human = {
				"name": names[i],
			}
			if dates[i] is not None:
				human["birth_year"] = dates[i]
			if genders[i] is not None:
				human["gender"] = genders[i]
			res.append(human)
		return res
	humans = create_humans(names, dates, genders)

	def q(humans: List[dict], cur_year=cur_year):
		"""Фильтрация военнообязанных"""
		return [
			human for human in humans
			if (
				cur_year - human.get("birth_year", 2023) >= 18
				and
				human.get("gender") == "Male")
			]

	def q2(humans: List[dict], cur_year=cur_year):
		"""Фильтрация военнообязанных под вопросом"""
		# Проверка исполнена муторно, но верно
		return [
			human for human in humans
			if (
					(human.get("gender") is None and human.get("birth_year") is None)
					or
					(human.get("gender") is None and cur_year - human.get("birth_year") >= 18)
					or
					(human.get("gender") == "Male" and human.get("birth_year") is None)
				)
			]

	searching_man = q(humans)
	unsure_man = q2(humans)

	def pf(man: List[dict], is_sure=True):
		"""Вспомогательная функция печати"""
		man_str_form = []
		sure_str_form = '' if is_sure else '- под вопросом'
		for men in man:
			man_str_form.append(f'{men["name"]}, {men.get("birth_year", "неизвестного")} года рождения {sure_str_form}')
		print("\n".join(man_str_form))

	pf(searching_man)
	print("=" * 40)
	pf(unsure_man, False)
