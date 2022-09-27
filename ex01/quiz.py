from multiprocessing.connection import answer_challenge
import random

q_lst = ["サザエさんの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
a_lst = [["マスオ","ますお",],["わかめ","ワカメ"],["甥","おい","甥っ子",]]

q = random.randint(0,2)
answer = input(q_lst[q]+":")
if answer in a_lst[q]:
    print("正解")
else:
    print("不正解")