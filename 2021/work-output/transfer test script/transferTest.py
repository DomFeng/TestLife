# writer by fengjianguang
# time: 2021/7/20 11:33 上午
import os
import time

# 2000用户给test父账户转账
# testnet
# os.system('fn setup -S https://prod-testnet.prod.findora.org')
# qa01
os.system('fn setup -S https://dev-qa01.dev.findora.org')
# 调试私钥
# sec_key = open('/home/ubuntu/testscript/sec_key_test.txt', 'r')
sec_key = open('/home/ubuntu/testscript/sec_key.txt', 'r')
transferlog = open('/home/ubuntu/testscript/translog.txt', 'w')
counter = 1
i = 0
print('开始发送交易：')
datetest = os.popen('date')
print('开始时间：' + datetest.read(), file=transferlog)
os.system('date')
for line in sec_key:
    print('第' + str(counter) + '个钱包开始转账:', file=transferlog)
    os.system('echo -n \'' + line.strip() + '\' > tempsec')
    print('echo -n \'' + line.strip() + '\' > tempsec', file=transferlog)
    print(
        'fn transfer -n $((1 * 1000000)) -f tempsec -t \'AdjFthQc3w2mAQxDTptJRzNZIcFPwj7fE5ggVvw1Wnk=\'',
        file=transferlog)
    output = os.popen(
        'fn transfer -n $((1 * 1000000)) -f tempsec -t \'AdjFthQc3w2mAQxDTptJRzNZIcFPwj7fE5ggVvw1Wnk=\'')
    print(output.read(), file=transferlog)
    counter += 1
    # 发起交易每笔间隔时间
    time.sleep(0.2)

print('发送交易完成！')
datetest = os.popen('date')
print('发送交易结束时间：' + datetest.read(), file=transferlog)
os.system('date')
# 判断转账进度：
while i != 1:
    progressw = open('/home/ubuntu/testscript/progresslog.txt', 'w')
    output1 = os.popen('fn show')
    print('fn show')
    print(output1.read(), file=progressw)
    print('写入文件')
    progressw.close()
    progressr = open('/home/ubuntu/testscript/progresslog.txt', 'r')
    print('------开始遍历------')
    for fra in progressr:
        if fra[16:25] == 'FRA units':
            print(fra)
            # 校验最终收款金额，确认所有金额都到账
            if fra[0:9] == '997002002':
                datetest = os.popen('date')
                print('交易处理完成！')
                print('交易处理完成：' + datetest.read(), file=transferlog)
                i = 1
    progressr.close()
    time.sleep(2)

sec_key.close()
transferlog.close()
