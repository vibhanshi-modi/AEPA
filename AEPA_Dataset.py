import json
import requests
import os

#class HackerRankDataset:
#	def get_all_users():\
url_sol="https://www.hackerrank.com/rest/contests/master/challenges/mini-max-sum/hackers/{name}/download_solution"
url_users="https://www.hackerrank.com/rest/contests/master/challenges/mini-max-sum/leaderboard/filter?offset={offset_value}&limit=100&include_practice=true&language=c&filter_kinds=language"
#obj=requests.get("https://www.hackerrank.com/rest/contests/master/challenges/simple-array-sum/leaderboard/filter?offset=0&limit=100&include_practice=true&language=c&filter_kinds=language",auth=("vibhanshimodi@gmail.com","#1Ambition"))
#users=obj.json()
#user_details=users["models"]
parent_dir="mini-max"
if not os.path.exists(parent_dir):
    os.makedirs(parent_dir)
for i in range(0,20000,100):
	obj=requests.get(url_users.format(offset_value=i),auth=("vibhanshimodi@gmail.com","#1Ambition"))
	users=obj.json()
	user_details=users["models"]
	for j in range(0,100,10):
		new_dir=parent_dir+"/"+ "Correct"
		if not os.path.exists(new_dir):
			os.makedirs(new_dir)
		filename=new_dir + "/"+ user_details[j]["hacker"] + ".c"
		fo=open(filename,"w")
		code=requests.get(url_sol.format(name=user_details[j]["hacker"]),auth=("vibhanshimodi@gmail.com","#1Ambition"))
		fo.write(code.text)	
	


