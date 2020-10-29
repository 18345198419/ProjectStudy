import configparser

filePath = '/db_donfig.ini'

# 读取配置文件
cf = configparser.ConfigParser()
cf.read(filePath)


def getConfig(test):
    host = cf.get(test, 'host')
    post = int(cf.get(test, 'post'))
    user = cf.get(test, 'user')
    pwd = cf.get(test, 'pwd')

    return host, post, user, pwd


# print(getConfig('exchange'))


# 加载地址

def getaddr():
    addr_path = '/Users/zhuyadong/PycharmProjects/test/base/wbf/address.ini'
    addrlist = []
    with open(addr_path, 'r+') as f:
        for line in f.readlines():
            addrlist.append(line.strip())
    return addrlist


print(getaddr())
