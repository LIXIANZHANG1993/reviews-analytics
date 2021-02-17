data = []
count = 0
with open ('reviews.txt' , 'r') as f :
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

print(data[0])

wc = {} #word_count
for d in data:
    words = d.split() #split的預設值就是空白鍵，如果是手動寫成.split(' ')，就會遇到連續空白鍵而形成的空字串
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #新增新的Key進字典

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
    word = input('請輸入查詢的字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為:' , wc[word] )
    else:
        print('查無此字')

print('感謝您使用此查詢功能')


#sum_len = 0
#for d in data:
	#sum_len += len(d)
#print('每筆留言的平均長度為', sum_len/len(data), '個字' )




