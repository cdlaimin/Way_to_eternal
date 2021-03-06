import math
import os
import time
import random
import threading
import re

from prettytable import *

from variable import *
from FDLB import *
from MTLB import *
from SPLB import *


class Archive:
    def __init__(self, name, password):
        self.password = password
        self.name = name
        self.HP = HP
        self.HP_MAX = HP_MAX
        self.DF = DF
        self.AT = AT
        self.HV = HV
        self.HV_MAX = HV_MAX
        self.EXP = EXP
        self.EXP_MAX = EXP_MAX
        self.BAG_List = BAG_List
        self.LV = LV
        self.coin = coin
        self.realm = realm
        self.BAG_List = BAG_List

    def save_Archive(self):
        cwd = os.getcwd()
        f = open(cwd + '\\UserConfig.config', 'w')
        f.write(str(self.name) + '\n')
        f.write(str(self.password) + '\n')
        f.write(str(self.HP) + '\n')
        f.write(str(self.HP_MAX) + '\n')
        f.write(str(self.DF) + '\n')
        f.write(str(self.AT) + '\n')
        f.write(str(self.HV) + '\n')
        f.write(str(self.HV_MAX) + '\n')
        f.write(str(self.EXP) + '\n')
        f.write(str(self.EXP_MAX) + '\n')
        f.write(str(self.BAG_List) + '\n')
        f.write(str(self.LV) + '\n')
        f.write(str(self.coin) + '\n')
        f.write(self.realm + '\n')
        f.write(str(Buffer_LV) + '\n')
        f.close()

    def read_Archive(self):
        global HP
        global HV
        global DF
        global EXP
        global EXP_MAX
        global BAG
        global BAG_Used  # 变量全局化
        global LV
        global AT
        global HP_MAX
        global HV_MAX
        global coin
        global realm
        global BAG_List
        global name
        global password
        global Buffer_LV
        f = open('UserConfig.config', 'r')
        name = str(f.readline().strip())
        password = str(f.readline().strip())
        HP = float(f.readline().strip())
        HP_MAX = int(f.readline().strip())
        DF = int(f.readline().strip())
        AT = int(f.readline().strip())
        HV = int(f.readline().strip())
        HV_MAX = int(f.readline().strip())
        EXP = float(f.readline().strip())
        EXP_MAX = float(f.readline().strip())
        BAG_List = eval(f.readline().strip())
        LV = int(f.readline().strip())
        coin = int(f.readline().strip())
        realm = str(f.readline().strip())
        Buffer_LV = int(f.readline().strip())

    def judgment(self):
        global name
        global password
        if os.path.exists('UserConfig.config'):
            time.sleep(0.2)
            print('欢迎回来,\033[1;36m' + str(name) + '\033[0m')
            time.sleep(0.3)
            input_password = input('请输入密码<')
            if input_password == password:
                print('登陆成功')
            else:
                print('密码错误,你还有一次机会')
                input_password = input('请输入密码<')
                if input_password == password:
                    print('登陆成功')
                else:
                    print('密码错误')
                    exit()

        else:
            print('欢迎新玩家')
            input_name = input('请输入你的姓名<')
            name = input_name
            input_password = input('请输入密码<')
            password = input_password
            print('登陆成功')
            save = Archive(name, password)
            save.save_Archive()


def update_announcement():
    print('\033[1;35m--------------更新公告--------------\033[0m')
    print('版本:5w-2d1a')
    print('-- 注意！新版本/w改为/f,战斗过程中使用/r逃跑')
    print('-- 添加了提示')
    print('-- 修复了诸多bug')
    print('-- 没了')


def poem_w(text, width):
    seq = [c for c in text if c.strip()]
    # print (seq)
    seq_len = len(seq)
    # print (seq_len)
    line = math.ceil(seq_len / width)
    for i in range(0, line):
        for j in range(0, width):
            if j * line + i < seq_len:
                print(' | ', end='')
                print(seq[j * line + i], end=' | ')
                time.sleep(0.2)
        print()


def operation():  # 帮助文档
    print('/pc或/personal centre来打开个人中心')
    time.sleep(1)
    print('/f或/fight进入战斗界面')
    time.sleep(1)
    print('/shop打开商店')
    time.sleep(1)
    print('/map打开地图,/go 东南西北英文首字母(n s e w)进行移动')
    time.sleep(1)
    print('在战斗中,/r可以逃跑（50%）')
    time.sleep(1)
    print('介绍完毕，尽情游玩吧')
    print('输入/help再次观看')
    print('输入/help <物品名>可以查看数据')


def weather(velocityOfFlow):
    global w_time
    while 1:
        time.sleep(int(velocityOfFlow))
        w_time = w_time + 1
        if w_time == 50:
            print('\n \033[1;33m红红的太阳慢慢地从山尖上冒了出来，不一会儿，朝霞就洒满了大地。 \n')
        elif w_time == 100:
            print('\n \033[1;33m金色的阳光透过缝隙，洒在褐色土地滋生的小草上。\n ')
        elif w_time == 200:
            print('\n \033[1;33m烈日当头，阴影变成蓝色，野草在酷热中昏睡，而飕飕寒气，却从浓林密叶下掠过。\n ')
        elif w_time == 300:
            print('\n \033[1;31m日光正值韶华盛极，殊不知盛极反趋于衰朽，绚烂之极反归于涣灭，阳光逐渐斜照\n ')
        elif w_time == 350:
            print('\n \033[1;31m天边的云朵被绚丽的霞光映照得更加耀目，倒映在清澈的江水里，微波荡漾，仿佛天在晃动。\n ')
        elif w_time == 400:
            print('\n \033[1;35m黄昏已经谢去，夜幕早已铺开。\n ')
        elif w_time == 600:
            print('\n \033[1;35m天上缀满了闪闪发光的星星，像细碎的流沙铺成的银河斜躺在青色的天宇上。\n ')
        elif w_time >= 601:
            w_time = 0
        weather_r = random.randint(0, 10000)
        if weather_r == 872 or weather_r == 389:
            print('不知怎的，天上下起了稀稀拉拉的小雨，周围笼上了一层雾')
            weather_r = random.randint(0, 10000)
            if weather_r == 832 or weather_r == 237:
                print('渐渐地，雨停了')
        elif weather_r == 7428 or weather_r == 562:
            print('天上刮起了大风，树叶从枝头上掉落，沙沙作响')
            if weather_r == 2398 or weather_r == 8429:
                print('风逐渐变小了，一切归于宁静')


Buffer_LV = LV


def pc():  # 个人界面
    global fun
    for i in range(0, random.randint(1, random.randint(2, 8))):
        fun = random.randint(0, 100)
    global HP
    global HV
    global EXP
    global EXP_MAX
    global BAG
    global BAG_Used  # 变量全局化
    global LV
    global AT
    global Buffer_LV
    global HP_MAX
    global HV_MAX
    global coin
    global realm
    global BAG_List_Buffer
    global realm_LV
    if LV != Buffer_LV:
        Buffer_LV = LV
        HP_MAX = int(HP_MAX * (1 + (int(LV) / 20)))
        HP = HP_MAX
    else:
        HP = HP
    print('\033[1;33m【气血】' + str(HP) + '/' + str(HP_MAX))
    print('【护甲】' + str(DF))
    AT = int(AT * (1 + (LV / 5))) + int(ETLY[hand][0])
    print('【功力】' + str(AT))
    print('【饥饿】' + str(HV) + '/' + str(HV_MAX))
    if BAG_List_Buffer != BAG_List:
        for BAG_Used_key in FDLB.keys():
            if BAG_Used_key in list(BAG_List.keys()):
                BAG_Used = BAG_Used + (FDLB[BAG_Used_key][2] * int(BAG_List[BAG_Used_key]))
                BAG_List_Buffer = BAG_List
            else:
                pass
    else:
        pass
    print('\033[1;34m【背包】' + str(BAG_Used) + '/' + str(BAG) + 'kg')
    ET = ['【头部】' + str(head), '【躯体】' + str(body), '【腿部】' + str(leg), '【脚部】' + str(foot), '【手部】' + str(hand)]  # 装备总览
    for i in range(0, 5):
        print(ET[i])
    while EXP >= EXP_MAX:
        if EXP >= EXP_MAX:
            LV = LV + 1
            realm_LV = realm_LV + 1
            EXP = EXP - EXP_MAX
            EXP_MAX = int(EXP_MAX * (1 + (0.2 * LV)))
    print('\033[1;33m【经验】' + str(EXP) + '/' + str(EXP_MAX))
    if 0 < LV <= 5:
        realm = '炼体'
        realm_LV = 1
    elif 5 < LV <= 15:
        realm = '锻神'
        realm_LV = 1
    elif 15 < LV <= 25:
        realm = '小生'
        realm_LV = 1
    elif 25 < LV <= 35:
        realm = '结丹'
        realm_LV = 1
    print('【境界】' + str(realm) + str(realm_LV) + '段')
    print('\033[1;36m【铜钱】' + str(coin))
    print('\033[0m/bag 可以打开背包')


def woods_low_level(name):
    global fun
    for i in range(0, random.randint(1, random.randint(2, 8))):
        fun = random.randint(0, 100)
    global HP
    global EXP
    global AT
    global HV
    global if_run
    global menpai_can
    if place == '树林':
        if AT <= 4:
            print('你蹑手蹑脚地走进森林，等待着猎物的出现')
        else:
            print('你大摇大摆地走进森林，这里的野兽已经不足为惧')
        print('等待中.', end='')
        rm = random.randint(0, 5)
        for i in range(0, rm):
            time.sleep(1)  # 等待怪物
            print('.', flush=False)
        if LV < 5:
            rm = str(random.randint(0, 3))  # 随机怪物
            ml = str(random.randint(1, (int(LV) + 2)))  # 随机怪物等级
            me = int(ml) * 1.5  # 怪物经验
            mh = int(ml) * 10  # 怪物血量
        elif LV == 5:
            rm = '4'
            ml = 6
            me = 50
            mh = 1000
        elif 10 > LV > 5:
            print('你已经不适合在这种小地方呆着了，出去闯荡吧')
            ml = 0
            return 1
        else:
            print('宁搁这儿玩儿呢？')
            ml = 0
            return 1
    else:
        print('这儿似乎没有什么可以让你打的')

    print('\033[1;33m「' + str(ml) + '」\033[0m' + MTLB[rm] + str(random.choice(ZYC)), flush=True)  # 打印信息
    mh_max = int(ml) * 10

    md = int(ml) * 0.25  # 怪物防御
    ma = int(ml) * 1.5  # 怪物攻击
    c_pa = 0  # 玩家总伤害
    print(name)
    while mh != 0 and HP != 0 and ml != 0:
        if if_run:
            if_run_possibility = random.randint(0, 100)
            if if_run_possibility <= 50:
                print('\033[1;31m你狼狈地逃跑了\033[0m')
                if_run = False
                break
            else:
                print('\033[1;36m' + MTLB[rm] + '挡在了你面前，你跑不掉了\033[0m')
                time.sleep(0.5)
                if_run = False
        time.sleep(random.uniform(0.8, 1.2))  # 攻击间隙
        pa = (AT * 2) * random.randint(1, 2)  # 玩家伤害计算
        M_sp = random.randint(0, 100)  # 怪物闪避
        if M_sp <= int(ml) * 0.5:  # 闪避几率 = 等级 * 1.5
            print('\033[1;33m' + MTLB[rm] + '惊险地躲过了这一击！\033[0m')
        else:
            print(
                '\033[0m 你用' + '\033[1;32m' + hand + '\033[0m' + str(random.choice(PATSE[ETLY[hand][1]])) + MTLB[
                    rm] + str(
                    random.choice(PATSE_1)) + '     造成了' + str(
                    (pa - md)) + '点伤害！')  # 打印信息
            mh = mh - pa + md  # 怪物扣血
            c_pa = c_pa + pa - md  # 玩家总伤害计算
            if mh / mh_max >= 0.9:
                print('\033[1;32m' + MTLB[rm] + '看起来气势汹汹，精神抖擞\n \n')
            elif 0.7 <= mh / mh_max < 0.9:
                print('\033[1;33m' + MTLB[rm] + '看起来受了点轻伤，不过不成大碍\n \n')
            elif 0.5 <= mh / mh_max < 0.7:
                print('\033[1;34m' + MTLB[rm] + '看起来气喘吁吁，大汗淋漓\n \n ')
            elif 0.2 <= mh / mh_max < 0.5:
                print('\033[1;31m' + MTLB[rm] + '摇摇欲坠，就快要倒下了\n \n ')
            elif mh / mh_max < 0.2:
                print('\033[1;35m' + MTLB[rm] + ' 的鲜血四溅，离死不远了\n \n ')
            time.sleep(random.uniform(1.0, 2.0))  # 攻击间隙
            sp = random.randint(0, 100)  # 玩家闪避

            if sp <= int(LV) * 2:  # 闪避几率 = 等级*2
                print('\033[1;34m你灵巧地躲过了这一击！\033[0m \n \n')
            elif mh <= 0:
                if mh <= 0:
                    print('你胜利了！ 获得了' + '\033[1;34m ' + str(me) + ' \033[0m' + '经验！')
                    EXP = EXP + me  # 加经验
                    HV = HV - 3  # 扣饥饿
                    print('现在经验为' + str(EXP))
                    if MTLB[rm] == '野熊':
                        menpai_can = True
                    fun_1 = random.randint(0, 100)
                    if BAG_Used < BAG:
                        if fun_1 == fun:
                            for dpn in range(0, len(MTDP[MTLB[rm]])):
                                if str(MTDP[MTLB[rm]][dpn]) not in BAG_List:
                                    BAG_List[str(MTDP[MTLB[rm]][dpn])] = 1
                                else:
                                    BAG_List[str(MTDP[MTLB[rm]][dpn])] = int(BAG_List[str(MTDP[MTLB[rm]][0])]) + 1
                        elif abs(int(fun) - int(fun_1)) <= 10 and fun_1 != fun:
                            dp = random.randint(0, 100)
                            if dp <= 90:
                                for dpn in range(0, len(MTDP[MTLB[rm]])):
                                    if str(MTDP[MTLB[rm]][dpn]) not in BAG_List:
                                        BAG_List[str(MTDP[MTLB[rm]][dpn])] = 1
                                    else:
                                        BAG_List[str(MTDP[MTLB[rm]][dpn])] = int(BAG_List[str(MTDP[MTLB[rm]][0])]) + 1

                            else:
                                print('你没有获得任何物品！')
                        elif 20 >= abs(int(fun) - int(fun_1)) > 10:
                            dp = random.randint(0, 100)
                            if dp <= 70:
                                for dpn in range(0, len(MTDP[MTLB[rm]])):
                                    if str(MTDP[MTLB[rm]][dpn]) not in BAG_List:
                                        BAG_List[str(MTDP[MTLB[rm]][dpn])] = 1
                                    else:
                                        BAG_List[str(MTDP[MTLB[rm]][dpn])] = int(BAG_List[str(MTDP[MTLB[rm]][0])]) + 1

                            else:
                                print('你没有获得任何物品！')
                        elif 50 >= abs(int(fun) - int(fun_1)) > 20:
                            dp = random.randint(0, 100)
                            if dp <= 40:
                                for dpn in range(0, len(MTDP[MTLB[rm]])):
                                    if str(MTDP[MTLB[rm]][dpn]) not in BAG_List:
                                        BAG_List[str(MTDP[MTLB[rm]][dpn])] = 1
                                    else:
                                        BAG_List[str(MTDP[MTLB[rm]][dpn])] = int(BAG_List[str(MTDP[MTLB[rm]][0])]) + 1

                            else:
                                print('你没有获得任何物品！')
                        elif 80 >= abs(int(fun) - int(fun_1)) > 50:
                            dp = random.randint(0, 100)
                            if dp <= 20:
                                for dpn in range(0, len(MTDP[MTLB[rm]])):
                                    if str(MTDP[MTLB[rm]][dpn]) not in BAG_List:
                                        BAG_List[str(MTDP[MTLB[rm]][dpn])] = 1
                                    else:
                                        BAG_List[str(MTDP[MTLB[rm]][dpn])] = int(BAG_List[str(MTDP[MTLB[rm]][0])]) + 1

                            else:
                                print('你没有获得任何物品！')
                        break
                    else:
                        print('你的背包太满了。')
            else:

                if ma > DF:  # 若怪物攻击》玩家防御
                    print('\033[0m' + MTLB[rm] + str(random.choice(MATSE)) + '你' + str(
                        random.choice(MATSE_1)) + '     造成了' + str(
                        (ma - DF)) + '点伤害！')  # 打印信息
                    HP = HP - ma + DF  # 玩家扣血
                if ma <= DF:  # 若怪物伤害无法破防
                    print('\033[0m' + MTLB[rm] + str(random.choice(MATSE)) + '你' + str(
                        random.choice(MATSE_1)) + '     未造成伤害！')
                    # 未造成伤害
                if HP / HP_MAX >= 0.9:
                    print('\033[1;32m你看起来毫发无损，精神抖擞\n \n ')
                elif 0.7 <= HP / HP_MAX < 0.9:
                    print('\033[1;33m你看起来受了点轻伤，不过不成大碍\n \n ')
                elif 0.5 <= HP / HP_MAX < 0.7:
                    print('\033[1;34m你气喘吁吁，大汗淋漓\n \n')
                elif 0.3 <= HP / HP_MAX < 0.5:
                    print('\033[1;31m你摇摇欲坠，就快要倒下了\n \n ')
                elif HP / HP_MAX < 0.3:
                    print('\033[1;35m你的鲜血四溅，离死不远了\n \n')

        if HP <= 0:
            print('你失败了！ 你对' + MTLB[rm] + '总共造成了' + str(c_pa) + '点伤害！')
            print('请升级再战!')
            HV = HV - 6  # 扣饥饿
            break


def runAway(name):
    global if_run
    print(name)
    in2 = input('')
    if in2 == '/r':
        if_run = True
    else:
        if_run = False


def fight(place):  # 战斗界面
    if HV <= 2:
        print('你饿得快要昏过去了，你应该找点东西填饱肚子再说。')
    else:
        if place == '树林':
            f1 = threading.Thread(target=woods_low_level, args=('',))
            f1_run = threading.Thread(target=runAway, args=('',))
            f1.start()
            f1_run.start()
        else:
            print('这儿似乎没有什么可以让你打的')
            print('\033[1;33m 提示：使用/go n/s/w/e 在地图中行走，/map打开地图\033[0m')

def bag():
    global fun
    for i in range(0, random.randint(1, random.randint(2, 8))):
        fun = random.randint(0, 100)
    bag_p = PrettyTable()
    bag_p.field_names = ['名称', '数量']
    if bool(BAG_List):
        for bag_key in list(FDLB.keys()):
            if bag_key in list(BAG_List.keys()):
                if int(BAG_List[bag_key]) == 0:
                    del BAG_List[bag_key]
                else:
                    bag_p.add_row([bag_key, int(BAG_List[bag_key])])
        for bag_key in list(ETLY.keys()):
            if bag_key in list(BAG_List.keys()):
                if int(BAG_List[bag_key]) == 0:
                    del BAG_List[bag_key]
                else:
                    bag_p.add_row([bag_key, int(BAG_List[bag_key])])


            else:
                pass
        print('\033[1;33m')
        print(bag_p)
        print('\033[0m')
        print('/use <物品名> 可以使用物品')
    else:
        print('你嘛都没有')


def use_things(name):
    global fun
    for i in range(0, random.randint(1, random.randint(2, 8))):
        fun = random.randint(0, 100)
    global HV
    global HP
    global HP_MAX
    global HV_MAX
    global DF
    global AT
    global head
    global body
    global leg
    global foot
    global hand

    if name in list(BAG_List.keys()) and name in list(FDLB.keys()) and int(BAG_List[name]) >= 1:
        BAG_List[name] = int(BAG_List[name]) - 1
        if HP + FDLB[name][1] < HP_MAX:
            HP = HP + FDLB[name][1]
            print('你用' + name + '回复了\033[1;34m' + str(FDLB[name][1]) + '\033[0m点生命')
        elif HP + FDLB[name][1] >= HP_MAX:
            HP = HP_MAX
            print('\033[1;33m你重新变得神采奕奕！\033[0m')
        if HV + FDLB[name][0] < HV_MAX:
            HV = HV + FDLB[name][0]
            print('你用' + name + '回复了\033[1;34m' + str(FDLB[name][0]) + '\033[0m点饥饿值')
        elif HV + FDLB[name][0] >= HV_MAX:
            HV = HV_MAX
            print('\033[1;33m你的肚子被填饱了\033[0m')
    elif name in list(ETLY.keys()) and name in list(BAG_List.keys()) and int(BAG_List[name]) >= 1:
        BAG_List[name] = int(BAG_List[name]) - 1
        if ETLY[name][1] == 'head':
            head = name
            DF = int(ETLY[head][0]) + int(ETLY[body][0]) + int(ETLY[foot][0]) + int(ETLY[leg][0])  # 防御值计算（利用字典
            print('你装备了' + str(name))
        elif ETLY[name][1] == 'body':
            body = name
            DF = int(ETLY[head][0]) + int(ETLY[body][0]) + int(ETLY[foot][0]) + int(ETLY[leg][0])  # 防御值计算（利用字典
            print('你装备了' + str(name))
        elif ETLY[name][1] == 'leg':
            leg = name
            DF = int(ETLY[head][0]) + int(ETLY[body][0]) + int(ETLY[foot][0]) + int(ETLY[leg][0])  # 防御值计算（利用字典
            print('你装备了' + str(name))
        elif ETLY[name][1] == 'foot':
            foot = name
            DF = int(ETLY[head][0]) + int(ETLY[body][0]) + int(ETLY[foot][0]) + int(ETLY[leg][0])  # 防御值计算（利用字典
            print('你装备了' + str(name))
        elif ETLY[name][1] == 'sword' or ETLY[name][1] == 'knife':
            hand = name
            AT = int(ETLY[hand][0])  # 攻击
            print('你装备了' + str(name))

    else:
        print('你没有介玩意儿！')


def shop():
    global shop_enter
    if AT <= 10:
        print('你走进了店铺，里面人满为患，不乏一些强大的气息。你决定低调一点')
        shop_enter = 1
    else:
        print('你大摇大摆地走进店铺，挤开了许多顾客')
        shop_enter = 1
    print('/buy l 打开购买菜单,/rec l 打开回收菜单')
    print('/buy <物品名> 购买物品,/rec <物品名>回收物品')


def shop_sl():  # 售卖菜单
    global shop_enter
    if shop_enter == 0:
        if AT <= 10:
            print('你走进了店铺，里面人满为患，不乏一些强大的气息。你决定低调一点')
            shop_enter = 1
        else:
            print('你大摇大摆地走进店铺，挤开了许多顾客')
            shop_enter = 1
    else:
        pass
    shop_sl_p = PrettyTable()
    shop_sl_p.field_names = ['名称', '描述', '售卖价']
    for name in list(shop_sell_list.keys()):
        shop_sl_p.add_row([str(name), shop_sell_list[name][0], shop_sell_list[name][1]])

    print(shop_sl_p)
    shop_enter = 0


def shop_s(thing):
    global coin
    if type(thing) == str:
        if str(thing) in list(shop_sell_list.keys()):
            if coin >= shop_sell_list[str(thing)][1]:
                if str(thing) in list(BAG_List.keys()):
                    BAG_List[str(thing)] = BAG_List[str(thing)] + 1
                else:
                    BAG_List[str(thing)] = 1
                coin = coin - shop_sell_list[thing][1]
                print('你购买了\033[1;32m' + str(thing) + '\033[0m')
            else:
                print('太可怜了，你居然连这个都买不起')
        else:
            print('店小二想了想：这里没有这种东西，您去别的地方看看吧')


def shop_rl():  # 回收菜单
    global shop_enter
    if shop_enter == 0:
        if AT <= 10:
            print('你走进了店铺，里面人满为患，不乏一些强大的气息。你决定低调一点')
            shop_enter = 1
        else:
            print('你大摇大摆地走进店铺，挤开了许多顾客')
            shop_enter = 1
    else:
        pass
    shop_rl_p = PrettyTable()
    shop_rl_p.field_names = ['名称', '描述', '回收价']
    for name_r in list(shop_recycle_list.keys()):
        shop_rl_p.add_row([str(name_r), shop_recycle_list[name_r][0], shop_recycle_list[name_r][1]])

    print(shop_rl_p)
    shop_enter = 0


def shop_r(thing):
    global coin
    if str(thing) in list(shop_recycle_list.keys()):
        if str(thing) in list(BAG_List.keys()) and int(BAG_List[thing]) > 0:
            BAG_List[thing] = BAG_List[thing] - 1
            coin = coin + shop_recycle_list[thing][1]
            print('你把' + str(thing) + '递给了店小二，他高兴地给了你' + str(shop_recycle_list[thing][1]) + '个铜钱')
        else:
            print('你掏了掏背包，你似乎没有这种东西')
    else:
        print('店小二似乎不认识这种东西')


def move(direction):
    global place
    if str(direction) == 'n':
        if place_l[place][0] == '无' or '':
            print('那边没路了')
        elif place == '树林':
            pass
        else:
            place = place_l[place][0]
            print('你来到了\033[1;33m' + place + '\033[0m')

    elif str(direction) == 'e':
        if place_l[place][1] == '无' or '':
            print('那边没路了')
        else:
            place = place_l[place][1]
            print('你来到了\033[1;33m' + place + '\033[0m')

    elif str(direction) == 's':
        if place_l[place][2] == '无' or '':
            print('那边没路了')
        else:
            place = place_l[place][2]
            print('你来到了\033[1;33m' + place + '\033[0m')

    elif str(direction) == 'w':
        if place_l[place][3] == '无' or '':
            print('那边没路了')
        else:
            place = place_l[place][3]
            print('你来到了\033[1;33m' + place + '\033[0m')

    else:
        print('咋地？你想上哪儿去？')


def bbq(thing):
    if coin >= 3:
        if thing in list(BAG_List.keys()) and BAG_List[thing] >= 1:
            BAG_List[thing] = int(BAG_List[thing]) - 1
            if '烤' + thing in list(BAG_List.keys()):
                BAG_List['烤' + thing] += 1
            else:
                BAG_List['烤' + thing] = 1
        else:
            print('人家可不免费给你食材')
    else:
        print('太可怜了，你居然连这个都吃不起')


def menpai_list_out(property):
    if property == 'k':
        menpai_kind_p = PrettyTable()
        for menpai_k in range(0, len(list(menpai_list_kind.keys()))):
            menpai_kind_p.field_names = ['序号', '门派']
            menpai_kind_p.add_row([str(menpai_k + 1), menpai_list_kind[str(menpai_k + 1)]])
        print(menpai_kind_p)
    if property == 'n':
        menpai_neutral_p = PrettyTable()
        for menpai_n in range(0, len(list(menpai_list_neutral.keys()))):
            menpai_neutral_p.field_names = ['序号', '门派']
            menpai_neutral_p.add_row([str(menpai_n + 1), menpai_list_neutral[str(menpai_n + 1)]])
        print(menpai_neutral_p)
    if property == 'e':
        menpai_evil_p = PrettyTable()
        for menpai_e in range(0, len(list(menpai_list_evil.keys()))):
            menpai_evil_p.field_names = ['序号', '门派']
            menpai_evil_p.add_row([str(menpai_e + 1), menpai_list_evil[str(menpai_e + 1)]])
        print(menpai_evil_p)


def exp(number):
    global EXP
    EXP = EXP + number


def AT_add(number):
    global AT
    AT = AT + number


def DF_add(number):
    global DF
    DF = DF + number


def cedn():  # 总检测
    global HP
    global HP_MAX
    global place
    global fi_enter
    global menpai

    in1 = input('\033[0m>')
    if in1 == '/help':
        operation()
    if in1 == '/pc' or in1 == '/personal centre':
        pc()
    if in1 == '/f' or in1 == '/fight':
        fight(place)
    if in1 == '/bag':
        bag()
    if '/use' in in1:
        use_things(in1[5:])
    if '/debug' in in1:
        if in1[7:8] == 'AT':
            AT_add(int(in1[10:]))
        if in1[7:8] == 'DF':
            DF_add(int(in1[10:]))
        if in1[7:9] == 'EXP':
            exp(int(in1[11:]))
    if '/help ' in in1:
        if str(in1[6:]) in FDLB:
            print(str(in1[6:]) + '的数据：')
            print('回复' + str(FDLB[str(in1[6:])][0]) + '点饱食')
            print('回复' + str(FDLB[str(in1[6:])][1]) + '点气血')
        elif str(in1[6:]) in ETLY:
            print(str(in1[6:]) + '的数据：')
            print('提升' + str(ETLY[str(in1[6:])][0]) + '点防御/攻击')
    if in1 == '/version':
        f = open('ChangeLog.md', 'r', encoding='utf-8')
        while True:
            line = f.readline()

            if len(line) == 0:
                break

            print(line, end='')
    if in1 == '/map':
        f = open('map.txt', 'r', encoding='utf-8')
        while True:
            line = f.readline()

            if len(line) == 0:
                break

            print(line, end='')
        print('\n你现在位于\033[1;31m', place, '\n')

    if in1 == '/shop':
        shop()
    if in1 == '/buy l':
        shop_sl()
    if in1 == '/rec l':
        shop_rl()
    if '/rec' in in1 and 'l' not in in1:
        number = re.compile(r'\d')
        rec_if = number.search(str(in1))
        if rec_if:
            rec_str = re.sub(r'\d', '', in1)
            rec_str = re.sub(r'\s', '', rec_str)
            for i in range(0, int(rec_if.group())):
                shop_r(re.sub(r'[^\u4e00-\u9fa5]', '', in1))
        else:
            shop_r(re.sub(r'[^\u4e00-\u9fa5]', '', in1))
    if '/buy' in in1 and 'l' not in in1:
        shop_s(in1[5:])
    if in1 == '/save':
        save = Archive(name, password)
        save.save_Archive()
        print('存档完毕，可退出')
    if in1 == '/rf':
        rf = Archive('霖', '20080826')
        rf.read_Archive()
        print('读档成功')
    if '/go ' in in1:
        # print(place)
        if len(in1) > 6:  # 判断输入字符串长度
            for i in range(0, int(in1[6:])):  # 重复执行
                move(in1[4:5])
        else:  # 若未输入数字
            move(in1[4:])  # 只执行一次
        # print(place)
    if place == '熟食铺':
        if not fi_enter:
            print('\033[0m这里肉香漫天，你忍不住咽了咽口水')
            print('输入/fi <物品名>烤肉(收费三铜币）')
            fi_enter = True
        else:
            pass
        if '/fi' in in1 and place == '熟食铺':
            bbq(in1[4:])
        elif '/fi' in in1 and place != '熟食铺':
            print('你觉得你能烤好吗？')
    if '/go n' in in1 and place == '树林':
        if menpai_can:
            place = '门派接待使者'
        else:
            print('你的功力太低了，人家看不上你')
    if place == '门派接待使者':
        menpai_admit_enter = True
        if menpai_admit_enter:
            if len(menpai) == 0:
                print('\033[0m一位慈祥的老人走过来')
                print('‘小兄弟，你可否想过闯荡江湖?’')
                time.sleep(2)
                print('我现在给你一个机会，你可以加入任意一个门派')
                time.sleep(2)
                print('注:输入k打开正派列表,n打开中庸列表,e打开邪门列表')
                time.sleep(1)
                menpai_goodAndEvil = input('你想救国济民，还是闯荡江湖，亦或者天下唯我独尊？')
                time.sleep(2)
                if menpai_goodAndEvil == 'k':
                    print('\033[1;32m 你的心中升起一股浩然正气，你决定投身于名门正派\033[0m')
                    time.sleep(1)
                    menpai_list_out('k')
                    print('注：输入序号决定门派')
                    menpai_choose = input('你想加入哪个门派？')
                    menpai = menpai_list_kind[str(menpai_choose)]
                    print('你加入了\033[1;32m', menpai, '\033[0m')
                elif menpai_goodAndEvil == 'n':
                    print('\033[1;33m 你想了想，还是中庸之道最适合自己')
                    time.sleep(1)
                    menpai_list_out('n')
                    print('注：输入序号决定门派')
                    menpai_choose = input('你想加入哪个门派？')
                    menpai = menpai_list_neutral[str(menpai_choose)]
                    print('你加入了\033[1;33m', menpai, '\033[0m')
                elif menpai_goodAndEvil == 'e':
                    print('\033[1;31m你嘿嘿一笑，令人毛骨悚然。你决定加入江湖邪派')
                    time.sleep(1)
                    menpai_list_out('e')
                    print('注：输入序号决定门派')
                    menpai_choose = input('你想加入哪个门派？')
                    menpai = menpai_list_evil[str(menpai_choose)]
                    print('你加入了\033[1;31m', menpai, '\033[0m')
                menpai_admit_enter = False
            else:
                print('背叛师门不是件好事')
        else:
            pass
    if HP <= 0:
        HP = 0
        time.sleep(1)
        print('你吐出一大口鲜血，倒在地上抽搐几下就死了。')
        time.sleep(2)
        print('你来到了鬼门关')
        place = '鬼门关'
        print('白无常伸出长长长的舌头舔了舔手指')
        time.sleep(1)
        print('‘新来的，你叫什么名字？’')
        time.sleep(2)
        print('白无常死死盯着你，仿佛要把你的一切都看穿')
        time.sleep(3)
        print('白无常眉头紧蹙：阳寿未尽？怎么可能！')
        time.sleep(2)
        print('白无常叹了口气：罢了罢了，你走吧')
        time.sleep(3)
        print('你摇摇晃晃的站了起来，仿佛做了一场梦')
        place = '中央广场'
        HP = int(HP_MAX / 100)
        print(HP)
        BAG_List = {}
