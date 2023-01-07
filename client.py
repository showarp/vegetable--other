import socket               # 导入 socket 模块
import sys
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 6918                # 设置端口号
s.connect((host, port))
parment = sys.argv
sp=parment[1]
dp=parment[2].split('\\')
filename=dp[-1]
dp='\\'.join(dp[:-1])
s.send(f'{sp}|{dp}|{filename}'.encode('utf8'))
print (s.recv(1024).decode('utf8'))
s.close()
