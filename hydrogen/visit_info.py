# -*- coding: utf-8 -*-
# @Author: Jonathan fu
# @Date:   2018-08-15 09:43:22
# @Last Modified by:   jonathan fu
# @Last Modified time: 2018-08-15 14:47:50
from .models import VisitNumber,Userip

#自定义的函数，不是视图
def refresh_visitnumber(request,page_name):       #修改网站访问量和访问ip等信息
    # 每一次访问，网站总访问次数加一
    count_nums = VisitNumber.objects.filter(page_name=page_name)
    count_nums_pagename = count_nums[0]
    count_nums_pagename.count += 1
    count_nums_pagename.save()

def get_Userip(request):
    # 记录访问ip和每个ip的次数
    if 'HTTP_X_FORWARDED_FOR' in request.META:  # 获取ip
        client_ip = request.META['HTTP_X_FORWARDED_FOR']
        client_ip = client_ip.split(",")[0]  # 所以这里是真实的ip
    else:
        client_ip = request.META['REMOTE_ADDR']  # 这里获得代理ip

    ip_exist = Userip.objects.filter(ip=str(client_ip))
    if ip_exist:  # 判断之前是否存在该ip
        uobj = ip_exist[0]
        uobj.count += 1
    else:
        uobj = Userip()
        uobj.ip = client_ip
        uobj.count = 1
    uobj.save()
