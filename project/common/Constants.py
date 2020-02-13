from enum import Enum


class ProjectPath(Enum):
    NETINFO = "docs\\InternetInfo.yml"
    BROWSER = "project\\browser"


class InternetInfo(Enum):
    URI = "source_url"
    HEADER = "chrome_header"


class KeyDict(Enum):
    # 全国总数
    CHINATOTAL = "chinaTotal"
    # 今日
    TODAY = "today"
    # 总计
    TOTAL = "total"
    # 全国今日更新
    CHINAADD = "chinaAdd"
    # 更新时间
    LASTUPDATETIME = "lastUpdateTime"
    # 地区数据树
    AREATREE = "areaTree"
    # 确诊
    CONFIRM = "confirm"
    # 疑似
    SUSPECT = "suspect"
    CHILDREN = "children"
    NAME = "name"


class Areas():
    areas = {"CQ": "重庆-重庆", "HZ": "陕西-汉中", "WH": "湖北-武汉"}
