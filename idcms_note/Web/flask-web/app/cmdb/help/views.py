#coding=utf-8
import os
import sys
import copy

from flask import render_template, request
from flask.ext.login import login_required

from .. import cmdb
from ..sidebar import start_sidebar

workdir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, workdir + "/../../../")

from app.utils.utils import init_sidebar

#初始化参数
sidebar_name = 'help'

@cmdb.route('/cmdb/help',  methods=['GET'])
@login_required
def help():
    '''帮助'''
    sidebar = copy.deepcopy(start_sidebar)
    sidebar = init_sidebar(sidebar, sidebar_name,'usage')
    return render_template('cmdb/help.html', sidebar=sidebar)
