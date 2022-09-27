import random
import datetime

sub = 10
miss = 2
count = 3
moji_lst = [chr(n+65) for n in range(26)]
row = True

for i in range(count):
    st = datetime.datetime.now()
    print(f"チャレンジ回数は{count-i}回です")
    sub_moji = random.sample(moji_lst,sub)
    dis_moji = random.sample(sub_moji,(sub-miss))
    miss_moji = list(set(sub_moji)^set(dis_moji))
    num_ans = input("対象文字:"+"\n"+str(sub_moji)+"\n"+"=="*30+
                "\n"+"表示文字:"+"\n"+str(dis_moji)+"\n\n"+"欠損文字はいくつあるでしょうか?:")
    if int(num_ans) == miss:
        print("正解です。具体的に欠損文字を1つずつ入力してください")
        moji_ans1 = input("１つ目の文字を入力してください:")
        if moji_ans1 in miss_moji:
            miss_moji.remove(moji_ans1)
            moji_ans2 = input("２つ目の文字を入力してください:")
            if moji_ans2 in miss_moji:
                print("正解です。")
                break
            else:
                print("不正解です。またチャレンジしてください。")
        else:
            print("不正解です。またチャレンジしてください。")
    else:
        print("不正解です。またチャレンジしてください。")
ed = datetime.datetime.now()
print(f"掛かった時間は{(ed-st).seconds}秒です")