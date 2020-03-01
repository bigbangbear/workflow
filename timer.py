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

def getTime(time):
    minus = 60 * 1000;
    return time * minus

def countDown(time):
    time.sleep(time);

def wfAdd(title, info):
    wf.add_item(title,
            arg=info,
            valid=True)

def main(wf):
    args = wf.args
    userInput = args[0]
    wf.logger.debug('user input : '+userInput)

    wf.add_item(title='倒计时',
                subtitle=timeToDate(userInput),
                valid=True)
    wf.send_feedback()
    #开始倒计时
    timeout = getTime(userInput)
    countDown(timeout)

    wf.add_item(title='完成',
                subtitle=timeToDate(userInput),
                valid=True)


    wf.send_feedback()

if __name__ == '__main__':
    # Create a global `Workflow3` object
    wf = Workflow3()
    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
