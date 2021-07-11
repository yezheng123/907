import time
import random
import easygui




List = ['']
n32 = ''
n33 = ''
name2 = ['陈凯', '陈斯楠', '陈学庆', '陈梓钧', '冯志扬', '邓文莹', '郭子豪', '胡博昊', '叶政', '成金政', '雷雨晴', '梁伟新', '凌少东', '刘冠成', '罗诗瑞', '刘宏湘', '刘永豪', '聂俊杰', '欧铭懿', '欧阳铭昱', '司徒', '谭竣文', '王定邦', '王梓洋', '伍迪', '吴俊鑫', '谢伟聪', '颜玉绮', '杨天赐', '叶子君', '尹佳倩', '余琪安', '唐嘉耀', '邹庆竟', '洪伟珩', '钟正标', '曾力多', '汤全旭', '刘钰莹', '林灿恩', '丘文滔', '肖锦程', '张瑞华', '潘可盛', '王家祥', '张炜']
cis = 0
print('=====点名器v1.0 作者yezheng1340=====')
print('加载中...')
time.sleep(2.3333344445555)
print('正在检查版本更新...')
print('=====点名器v1.0 作者yezheng1340=====')
sethello = ['(1)检查更新', '(2)当前设备信息', '(3)开始点名', '(4)查看点名数据的列表及每人的点名概率', '============================']
for __count in range(5):
    print(sethello[cis])
    cis += 1
number = int(input('选项'))
if (number == 1):
    print('正在检查更新')
    time.sleep(2)
    print('错误：403 可能是服务器处于关闭状态')
elif (number == 2):
    print('版本号：1.0')
    print('作者：yezheng1340')
elif (number == 3):
    ciname1 = int(input('抽几个？'))
    for __count in range(ciname1):
        cut = random.choice(name2)
        List.insert(0, cut)
        xy = name2.index(cut)
        del name2[xy]
        print(cut)
        time.sleep(0.08791)
    del List[-1]
    easygui.msgbox(List, '907 Roll call system-Author:yezheng1340', 'Ok,I know')
elif (number == 4):
    print('正在查找...')
    time.sleep(1)
    print('名字列表：', name2)
    print('')
    print('每人抽奖概率：', round((100 / len(name2)), 6), '%')
    print('一共有：', len(name2), '个人')
else:
    print('对不起，我好像不明白')
