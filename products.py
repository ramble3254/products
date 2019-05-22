import os #讀取作業系統

# 讀取檔案並檢查是否存在
products = []
print('輸入q為離開')
if os.path.isfile('product.csv'):
	print('讀取成功')
	with open('product.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續,跳到下一迴圈
			name, price = line.strip().split(',') 
			products.append([name, price])
	print(products)
else:
	print('找不到檔案')





#strip去除換行,split切割 #切割完後直接存成name跟price

#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
#上面這行為的縮寫
#p = []	
#p.append(name)
#p.append(price)
#products.append(p)
#print(products[0][1]) #意思為進去products[0]取[1]資料

# 印出購買紀錄
for product in products:
	print(product[0], '的價格是', product[1])

#寫入檔案
with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')