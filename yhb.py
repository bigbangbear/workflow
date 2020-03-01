#!/usr/bin/python
# encoding: utf-8

import sys
import re
import os
import time
import urllib

# Workflow3 supports Alfred 3's new features. The `Workflow` class
# is also compatible with Alfred 2.
from workflow import Workflow3, ICON_INFO, ICON_HOME, ICON_USER, ICON_WEB, ICON_GROUP, ICON_NETWORK, ICON_ACCOUNT
from workflow.notify import notify
from workflow import web

# 时间戳转换
def timeToDate(timestampStr):
    timestamp = float(timestampStr)
    if timestamp > 1000000000:
        timestamp = timestamp / 1000;
    time_local = time.localtime(timestamp)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    return dt

# 跳转到LeetCode
def goLeetcode(info):
    if info:
        if info == 'sb':
            url = 'https://www.yuque.com/qingling-w9d0v/davayg'
            wfAdd('语雀', url)
        else:
            url = 'https://leetcode.com/problemset/all/?search='+info
            wfAdd('搜索', url)
    else:
        url = 'https://leetcode.com/problemset/all/?difficulty=Medium&status=Todo'
        wfAdd('随机', url)
    return url

def wfAdd(title, info):
    wf.add_item(title,
            arg=info,
            valid=True)
    return

def main(wf):
    args = wf.args
    if len(args) > 1:
        userInput = args[1]
    else:
        userInput = ''
    action = args[0]
    wf.logger.debug('user input : '+userInput)

    if action == 'time':
        wf.add_item(title='时间戳',
                subtitle=timeToDate(userInput),
                valid=True)
    elif action == 'leetcode':
        goLeetcode(userInput)
    wf.send_feedback()

if __name__ == '__main__':
    # Create a global `Workflow3` object
    wf = Workflow3()
    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    sys.exit(wf.run(main))
