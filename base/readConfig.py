import configparser

filePath = '/Users/zhuyadong/PycharmProjects/test/base/donfig'

# 读取配置文件
cf = configparser.ConfigParser()
cf.read(filePath)


def getConfig(test):
    host = cf.get(test, 'host')
    post = int(cf.get(test, 'post'))
    user = cf.get(test, 'user')
    pwd = cf.get(test, 'pwd')

    return host, post, user, pwd


print(getConfig('test'))
