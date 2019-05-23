import os #讀取作業系統
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續,跳到下一迴圈
			name, price = line.strip().split(',') 
			products.append([name, price])
	return products

# 讀取檔案並檢查是否存在
#strip去除換行,split切割 #切割完後直接存成name跟price
#讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		products.append([name, price])
	return products
#上面這行為的縮寫
#p = []	
#p.append(name)
#p.append(price)
#products.append(p)
#print(products[0][1]) #意思為進去products[0]取[1]資料

# 印出購買紀錄
def print_products(products):
	for product in products:
		print(product[0], '的價格是', product[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')
def main():
	filename = 'product.csv'
	if os.path.isfile(filename):
		print('讀取成功')
		print('輸入q為離開')
		products = read_file(filename)
	else:
		print('找不到檔案')
	products = user_input(products)
	print_products(products)
	write_file('product.csv', products)

main()