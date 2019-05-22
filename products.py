products = []
print('輸入q為離開')
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
print(products)
print(products[0][1]) #意思為進去products[0]取[1]資料
for product in products:
	print(product[0], '的價格是', product[1])
