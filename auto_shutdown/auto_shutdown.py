import os, time, re

#获取用户指定关机时间
print('1,输入关机时间，格式如：小时:分钟 举个栗子：20:21 然后敲回车 即可\n'+
      '2,取消定时关机 再次双击打开程序 输入 off 敲回车 即可\n'+
      '3,退出程序，输入exit敲回车 即可\n')

while True:
    input_time = input('请输入：')
    input_time.replace('：', ':')#将中文字符下的'：'替换成英文的':'。
    if input_time == 'off':#取消定时关机
        os.system('shutdown -a')
        print('已为您取消定时, 3秒后自动关闭程序!')
        time.sleep(3)
        break
    elif input_time == 'exit':#取消操作
        os.system('exit')
        break
    elif re.fullmatch(r'^\d{1,2}:\d{2}$', input_time) is not None:
        #If the whole string matches the regular expression pattern, return a corresponding match object.
        # Return None if the string does not match the pattern; note that this is different from a zero-length match.
        #处理非法时间：
        # 处理4:03这种小时为个位数的情况,转为04:03。
        if len(input_time)==4:
            input_time = '0'+input_time
        #提取时分秒
        h1 = int(input_time[0:2])
        m1 = int(input_time[3:5])

        #获取当前系统时间
        mytime = time.strftime('%H:%M:%S')
        h2 = int(mytime[0:2])
        m2 = int(mytime[3:5])

        #对用户输入数据进行整理 防止出现25:76:66这样的时间数据
        if h1 > 24:
            h1 = 24
            m1 = 0
        if m1 > 60:
            m1 = 60
        #只要定时关机时间小于当前时间，就加24个小时。
        if h1 < h2:
            h1 = h1 + 24
        if h1 == h2 and m1 < m2:
            h1 = h1 + 24

        #计算秒数
        s1=(h1+(m1/60.0)-h2-(m2/60.0))*3600

        print('距离关机还有 %d 秒' %s1)
        os.system('shutdown -s -t %d' % s1)
        print('3秒后自动关闭程序!')
        time.sleep(3)
        break
    else:
        print('亲，输入不合法，请重新输入！')