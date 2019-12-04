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
    time_local = time.localtime(timestamp)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    return dt

# 跳转到LeetCode
def goLeetcode(info):
    if info:
        url = 'https://leetcode.com/problemset/all/?difficulty=Medium&status=Todo&search='+info
    else:
        url = 'https://leetcode.com/problemset/all/?difficulty=Medium&status=Todo'
    return url

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
        wf.send_feedback()
    elif action == 'leetcode':
        wf.add_item(title='搜索',
                arg=goLeetcode(userInput),
                valid=True)
        wf.send_feedback()

if __name__ == '__main__':
    # Create a global `Workflow3` object
    wf = Workflow3()
    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    sys.exit(wf.run(main))
