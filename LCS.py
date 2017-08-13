# Longest common substring 
# 采用匹配性和承接型状态矩阵, 打印非连续最长公子串
# 根据两个矩阵的状态结合, 判断公子串
# 增加回溯方向矩阵, 找出所有最长路径

def goback(D, i, j, S1, S2, path, depth=0):
	global numsub
	global L
	global SubStr
	if(D[i][j] == 'o'):
		# numsub += 1
		# print("%d: "% numsub, end='')
		str = ""
		for k in range(L-1,-1,-1):
			# print(path[k], end='')
			str = str + path[k]
		# print()
		SubStr.append(str)
		return
	if(D[i][j] == '\\'):
		depth += 1
		path[depth-1] = S1[i-1]
		goback(D, i-1, j-1, S1, S2, path, depth)
		depth -= 1
	elif(D[i][j] == 'A'):
		goback(D, i-1, j, S1, S2, path, depth)
	elif(D[i][j] == '<'):
		goback(D, i, j-1, S1, S2, path, depth)
	elif(D[i][j] == 'X'):
		goback(D, i-1, j, S1, S2, path, depth)
		goback(D, i, j-1, S1, S2, path, depth)

# ======================================================

def PrintMatrix(M, S1, S2):
	L1 = len(S1)
	L2 = len(S2)
	print(end=" "*7)
	for j in range(L2):
		print("%-2s" % S2[j], end=" ")
	print()
	for i in range(L1+1):
		if(i>0):
			print("%-2s" % S1[i-1], end=" ")
		else:
			print(end=" "*3)
		for j in range(L2+1):
			if(isinstance(M[i][j], int)):
				print("%2d" % M[i][j], end=" ")
			else:
				print("%2c" % M[i][j], end=" ")
		print()
	
	print()
	return

# ======================================================	

def lcs(S1, S2):
	L1 = len(S1)
	L2 = len(S2)
	print("L1 = %d, L2 = %d" % (L1,L2))
	M = [[0]*(L2+1) for i in range(L1+1)]	# 承接型矩阵 Max
	S = [[0]*(L2+1) for i in range(L1+1)]	# 状态型矩阵 State
	D = [['o']*(L2+1) for i in range(L1+1)]	# 回溯方向矩阵 Direction
	global L	# 最长公子串长度
	for i in range(1,L1+1):
		for j in range(1,L2+1):
			if(S1[i-1] == S2[j-1]):
				M[i][j] = M[i-1][j-1] + 1
				S[i][j] = M[i-1][j-1] + 1
				D[i][j] = '\\'	#  最大值从左上角得来, 故左上回溯
				if(M[i][j]>L):
					L = M[i][j]	# 记录当前公子串长度
			else:
				if(M[i-1][j]>M[i][j-1]):
					M[i][j] = M[i-1][j]
					D[i][j] = 'A'	# 最大值从上行得来, 故上回溯
				elif(M[i-1][j]<M[i][j-1]):
					M[i][j] = M[i][j-1]
					D[i][j] = '<'	# 最大值从左列得来, 故左回溯
				elif(M[i-1][j]==M[i][j-1] and M[i-1][j] != 0):
					M[i][j] = M[i][j-1]
					D[i][j] = 'X'	# 最大值从左列或上列得来, 故开叉
				S[i][j] = 0
	print()
	
	PrintMatrix(M, S1, S2)
	
	PrintMatrix(S, S1, S2)
	
	PrintMatrix(D, S1, S2)

	
	global numsub		# 最长公子串数目
	global SubStr
	
	
	path = ['' for n in range(L)]
	
	goback(D, L1, L2, S1, S2, path, numsub)	
	
	SubStr2 = [SubStr[0]]
	for str in SubStr:
		iflag = 1
		for str2 in SubStr2:
			if(str == str2):
				iflag = 0
				break
		if(iflag):
			SubStr2.append(str)
	
	n = 0
	for str2 in SubStr2:
		n += 1
		print("%d: " % n, end='')
		print(str2)
	
	print("num. of LCS: n = %d" % n)
	print("len. of LCS: L = %d" % L)
	
	return
# ======================================================

# ========= main() =========
# S1 = "sadstory"
# S2 = "adminsorry"

# S1 = "ABABDABAB"
# S2 = "BABACBABA"

# S1 = "ABCABCAB"
# S2 =  "BCADBCA"

# S2 = "ABAB"
# S1 = "BABA"

# S1 = "abcdefabcdefaaa"
# S2 = "cdxabcaaa"

# S1 = "aaabbbccc"
# S2 = "cccbbbaaa"

# S1 = "aaabbbcccdddeeefffggg"
# S2 = "gggfffeeedddcccbbbaaa"

# S1 = "aaabbbcccdddeeefffggghhhiiijjjkkklllmmmnnn"
# S2 = "nnnmmmlllkkkjjjiiihhhgggfffeeedddcccbbbaaa"

# S1 = "aaabbbccc"
# S2 = "abc"

# S1 = "aabbcc"
# S2 = "abxbcxaaxccxbb"

# S1 = "1234567890"
# S2 = "2468013579"

# S1 = "123456789"
# S2 = "213546879"

# 一个起点, 中间开叉
# S1 = "123456789"
# S2 = "214365879"

# S1 = "x123"
# S2 = "x213"

# S1 = "ABCDE"
# S2 = "BADCE"

# S1 = "DABC123"
# S2 = "DBAC213"

# S1 = "XABCDE12345"
# S2 = "XBADCE21435"

# S1 = "BDCABA"
# S2 = "ABCBDAB"

# S1 = "GCCCTAGCG"
# S2 = "GCGCAATG"

# S1 = "ABCDEFG";
# S2 = "BBADGFE";

# S1 = "ABCDEFGB";
# S2 = "AGFEDCBB";

# S2 = "查询北京咳咳咳天气"
# S1 = "查天气"

# S1 = "我准备考到中国科学院大学攻读博士学位"
# S2 = "我到中科院读博"

# numsub = 0

# L = 0

# SubStr = []

# ret = lcs(S1, S2)

while(input("Press any key to continue ... (x for end) ") != "x"):
	S1 = input("S1 = ")
	S2 = input("S2 = ")
	numsub = 0
	L = 0
	SubStr = []
	ret = lcs(S1, S2)


