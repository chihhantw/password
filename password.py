#密碼重試程式

#password = 'a123456'
password = 'a123456' #存一次
x = 3 #剩餘的機會
while x > 0:
	x = x - 1 #每輸入一次就減少一次機會
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('登入成功!!!')
		break
	else:
		print('密碼錯誤') #用逗號家字串與數字連結
		if x > 0:
			print('還有', x, '次機會')
		else:
			print('已錯誤三次，登入失敗！')