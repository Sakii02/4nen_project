# coding: utf-8

import csv
import re


from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer

#削除する単語のリストを作成
f_dictionary = open('NegativeWordsDictionary.txt', 'r')
# array_stop_words = f_dictionary.readlines()
array_stop_words = []

while True:
  line = f_dictionary.readline().replace('\n', '')
  if line:
    array_stop_words.append(line)
  else:
    break

# print(array_stop_words)

with open('ComfortHotelHakata_review_3660.tsv', mode='r', newline='', encoding='utf-8') as f_input:
    tsv_reader = csv.reader(f_input, delimiter='\t')
    read_data = [row for row in tsv_reader]

# 入力ファイルからレビューごとにread_dataに格納
# with open('Sample_review.tsv', mode='r', newline='', encoding='utf-8') as f_input:
#     tsv_reader = csv.reader(f_input, delimiter='\t')
#     read_data = [row for row in tsv_reader]



tokenizer = Tokenizer()
a = Analyzer(tokenizer=tokenizer)
for review_and_star in read_data:
    
    review = review_and_star[1]

    #一人のレビューを一文ずつ格納した配列
    # sentences = re.split(r'[。?\n]', review)

    #形態素解析してから抜く
    # for sentence in sentences:
    #     # 形態素解析
    #     # test_tokens = a.analyze(sentence)

    #     # for word in test_tokens:
    #     #     if word.surface in array_stop_words:
    #     #         review_and_star[1] = review.replace(sentence + '。','')
    #     #         # print("stopWordを検出")
    #     #         break
    #     #     # for stop_word in array_stop_words:
    #     #     #     if word in array_stop_words:
    #     #     #         review_and_star[1] = review.replace(sen + '。','')
    #     #     #         print("stopWordを検出")
    #     #     #         break
    #     #     # break
    #     # # print("stopWordなし")

    #     # 形態素解析なし
    #     # for word in array_stop_words:
    #     #     if word in sentence:
    #     #         review_and_star[1] = review.replace(sentence + '。','')
    #     #         # print("stopWordを検出")
    #     #         break

    #     print(sentence)
    

    for word in array_stop_words:
        if word in review:
            review_and_star[1] = review.replace(review,'')
    print(review)


# f_output = open('Sample_output.tsv', 'w', encoding='UTF-8')
# f_output = open('ComfortHotelHakata_output.tsv', 'w', encoding='UTF-8')
# for index in range(len(read_data)):
#     line = read_data[index]
#     f_output.write(line[0] + '\t' + line[1]+ '\n')


# str = '過去比較的新しい建物の「コンフォートホテル」にしか宿泊した事がなかったので少々驚きました、建物の古さに・・・。室内も古く少々がっかり。私の中での「コンフォートホテル」のイメージが崩れてしまいました。以前あったホテルを買い取ったのですかね？？？まあ全体的に可もなく不可もなくですね、寝るだけと考えたら。照明の融通の利かなさ（真っ暗かピーカンか究極の選択・・・）、トイレの水量が少なく流れない（大をすると流れず３回くらい流さないと流れない。しかもタンクに貯まるのが遅い。）、など少々（？？？）の事は我慢できました。（我慢するのも変ですが・・・）朝食会場での中国人のマナーの悪さには絶句。食べ物を容器に入れて持ち帰ってましたよ。係りの人は見て見ぬふり？それとも気づいていない？何処に行ってもいる中国人を眺めながらの朝食は朝から不愉快になる。会場を分けたら如何でしょうか。（中国人とそれ以外の人種で。'
# sentences = re.split(r'[。?\n]', str)
# print(sentences)