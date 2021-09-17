# writer by fengjianguang
# time: 2021/7/19 4:15 下午

#生成genkey
import os

#指定服务地址
print('fns setup -S https://prod-testnet.prod.findora.org')
os.system('fns setup -S https://prod-testnet.prod.findora.org')
walletkey = open('/home/admin/testscript/walletkey.txt', 'w')
print('创建压力测试钱包信息中...请等待...')
for i in range(2000):
    output = os.popen('fns genkey')
    print(output.read(), file=walletkey)
walletkey.close()

# 遍历文件
file_object = open('/home/admin/testscript/walletkey.txt', 'r')
pub_key = open('/home/admin/testscript/pub_key.txt', 'w')
sec_key = open('/home/admin/testscript/sec_key.txt', 'w')
try:
    for line in file_object:
        if line[3:10] == 'pub_key':
            print(line[14:58], file=pub_key)
        elif line[3:10] == 'sec_key':
            print(line[14:58], file=sec_key)
finally:
    file_object.close()
    pub_key.close()
    sec_key.close()
    print('创建完成')

