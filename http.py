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

# code
def getCodeInfo(code):
    codelist =[
            [200, 'OK'],
            [300, 'Multiple Choices: 重定向'],
            [400, 'Bad Request: 参数错误'],
            [401, 'Unauthorized: 未授权'],
            [500, 'Internal Server Error: 服务器错误'],
    ]
    for tmp in codelist:
        if tmp[0] == int(code):
            wfAdd(tmp[1], tmp[0])

def wfAdd(title, subtitle):
    info = ''
    wf.add_item(title,
            subtitle,
            arg=info,
            valid=True)
    return

def logger(log):
    wf.logger.debug(log)

def main(wf):
    args = wf.args
    if len(args) > 1:
        userInput = args[1]
    else:
        userInput = ''
    logger('user input : '+userInput)
    getCodeInfo(userInput)
    wf.send_feedback()

if __name__ == '__main__':
    # Create a global `Workflow3` object
    wf = Workflow3()
    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    sys.exit(wf.run(main))
