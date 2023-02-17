import os
import sys
import csv
from typing import List

def make_report_about_top3(students_avg_scores:dict) -> str:
	link = os.getcwd() + os.sep + 'top3.csv'

	def define_top3(students_avg_scores: dict) -> List[dict]:
		students = [
			{
				"name": name,
				"avg_score": avg_score,
			} for (name, avg_score) in students_avg_scores.items()
		]
		students.sort(key=lambda s: s["avg_score"], reverse=True)
		return students[:3]

	top3 = define_top3(students_avg_scores)

	with open(link, 'w', newline='') as xsl:
		writer = csv.writer(xsl, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for top in top3:
			writer.writerow([top["name"], top["avg_score"]])
	return link
