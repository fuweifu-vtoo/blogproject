# -*- coding: utf-8 -*-
# @Author: Jonathan fu
# @Date:   2018-07-27 23:03:17
# @Last Modified by:   jonathan fu
# @Last Modified time: 2018-07-28 11:56:29
from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "blogproject"

env.user = 'dc2-user'
env.password = 'FuWeiFu123'

# 填写你自己的主机对应的域名
env.hosts = ['www.vtoo.pro']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '22'


def deploy():
    source_folder = '/home/dc2-user/sites/demo.vtoo.pro/blogproject'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py makemigrations &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('systemctl start bg.service')
    sudo('service nginx reload')