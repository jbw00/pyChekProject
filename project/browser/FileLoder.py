import json
import os
import sys

import requests
import yaml

sys.path.append(sys.path[0] + "\\common")
from Constants import ProjectPath, InternetInfo


# 获取配置文件路径
def getYmlPath():
    currentPath = os.path.split(os.path.realpath(__file__))[0]
    ymlPath = currentPath.replace(ProjectPath.BROWSER.value, ProjectPath.NETINFO.value)
    return ymlPath


# 读取配置文件
def getYmlValue(key, ymlPath):
    ymlFail = open(ymlPath, "r", encoding='utf-8').read()
    yml = yaml.load(ymlFail, Loader=yaml.FullLoader)
    return yml[key]


# 通过参数虚拟浏览器
def inventedBrowser():
    ymlPath = getYmlPath()
    url = getYmlValue(InternetInfo.URI.value, ymlPath)
    header = getYmlValue(InternetInfo.HEADER.value, ymlPath)
    response = requests.get(url, header).text
    value = json.loads(response, encoding="utf-8")["data"]
    return value

