import json
import sys
import tkinter
from tkinter import messagebox

sys.path.append(sys.path[0] + "\\common")
from Constants import Areas, KeyDict
sys.path.append(sys.path[0] + "\\browser")
import FileLoder


def callWin():
    window = tkinter.Tk()
    # 标题
    window.title("疫情查询程序")
    # 尺寸
    window.geometry("400x300")

    data = FileLoder.inventedBrowser()
    valueTree = json.loads(data)

    # 标题替换
    firstTitle = "全国今日新增确诊：C1人，共计：C2人\n全国今日新增疑似：S1人，共计S2人"
    firstTitle = firstTitle.replace("C1", str(valueTree[KeyDict.CHINAADD.value][KeyDict.CONFIRM.value]))
    firstTitle = firstTitle.replace("C2", str(valueTree[KeyDict.CHINATOTAL.value][KeyDict.CONFIRM.value]))
    firstTitle = firstTitle.replace("S1", str(valueTree[KeyDict.CHINAADD.value][KeyDict.SUSPECT.value]))
    firstTitle = firstTitle.replace("S2", str(valueTree[KeyDict.CHINATOTAL.value][KeyDict.SUSPECT.value]))

    # 创建label可替换对象
    secondTitleValue = tkinter.StringVar()

    # 内容布局
    title = tkinter.Label(window, text=firstTitle, font=('仿宋', 12), bg='Orange')
    selectText = tkinter.Label(window, text="选择城市", font=('Arial', 16))
    listValue = tkinter.Listbox(window, height=3)
    secondTitle = tkinter.Label(window, font=('仿宋', 12), fg='red', textvariable=secondTitleValue)

    count = 0
    for area in Areas.areas:
        count += 1
        listValue.insert(count, Areas.areas.get(area))

    # 确认选择传递参数
    def confirm():
        selectArea = listValue.get(listValue.curselection())
        print(selectArea)
        cityConfirm, citySuspect = getCityValue(selectArea, valueTree[KeyDict.AREATREE.value][0])
        secondValue = selectArea + "总计确诊：" + str(cityConfirm) + "人，总计疑似" + str(citySuspect) + "人"
        print(secondValue)
        secondTitleValue.set(secondValue)

    confirmButton = tkinter.Button(window, text="确认", command=confirm)

    # 放置布局
    title.pack()
    selectText.pack()
    listValue.pack()
    confirmButton.pack()
    secondTitle.pack()

    # 进入消息循环
    window.mainloop()


# 获取选择城市的值
def getCityValue(selectArea, valueTree):
    location = str(selectArea).split("-")
    provinces = valueTree[KeyDict.CHILDREN.value]
    try:
        for province in provinces:
            provinceName = province[KeyDict.NAME.value]
            # 判断是否为查询省份
            if (provinceName == location[0]):
                # 判断是否为直辖市
                if provinceName == "重庆":
                    cityConfirm = province[KeyDict.TOTAL.value][KeyDict.CONFIRM.value]
                    citySuspect = province[KeyDict.TOTAL.value][KeyDict.SUSPECT.value]
                    return cityConfirm, citySuspect
                else:
                    # 非直辖市查询指定城市
                    citys = province[KeyDict.CHILDREN.value]
                    for city in citys:
                        cityName = city[KeyDict.NAME.value]
                        if (cityName == location[1]):
                            cityConfirm = city[KeyDict.TOTAL.value][KeyDict.CONFIRM.value]
                            citySuspect = city[KeyDict.TOTAL.value][KeyDict.SUSPECT.value]
                            return cityConfirm, citySuspect
    except:
        messagebox.showinfo("查询失败", "查询信息失败！")
