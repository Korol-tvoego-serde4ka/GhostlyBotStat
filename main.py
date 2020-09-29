import os
import json

def statistic(delete):
	dir = "statistic"

	ques = {}
	
	files = os.listdir(dir)
	
	for file in files:
		f = open(dir+"/"+file)
		data = json.load(f)
		ques.update({data["Command"]: data["Count"]})
	
	list_d = list(ques.items())
	list_d.sort(key=lambda i: i[1], reverse=True)
	
	for que in list_d:
		print(que[0] + " - " + str(que[1]))
	
	if delete:
		os.delete(dir)


def statQue(delete, num):
	dir = "stat_que"
	
	ques = {}
	
	files = os.listdir(dir)
	
	for file in files:
		f = open(dir+"/"+file)
		data = json.load(f)
		ques.update({data["Que"]: data["Count"]})
	
	list_d = list(ques.items())
	list_d.sort(key=lambda i: i[1], reverse=True)
	
	if num > 0:
		list_d = list_d[0:num]
	
	print()
	print()
	print("Топ из {0} запросов: ".format(num))
	print()
	
	for que in list_d:
		print(que[0] + " - " + str(que[1]))
	
	print()
	
	if delete:
		os.delete(dir)

def main():
	proc = input("Что будем получать? (0 - статистика по командам, 1 - статистика по запросам)\n> ")
	if proc == "0":
		delete = True if input("Удалить данные [y/n] (n - по умолчанию)\n> ") == "y" else False
		statistic(delete)
	elif proc == "1":
		delete = True if input("Удалить данные [y/n] (n - по умолчанию)\n> ") == "y" else False
		num = int(input("Сколько постов вернуть? (число, если нужно получить все запросы, то - 0)\n> "))
		statQue(delete, num)
	else:
		print("Error! Странное значение")
		input()

if __name__ == "__main__":
	main()