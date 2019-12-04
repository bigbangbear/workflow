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

def timeToDate(timestampStr):
    timestamp = float(timestampStr)
    time_local = time.localtime(timestamp)
    #转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    return dt

def main(wf):
    args = wf.args
    wf.logger.debug(args)
    wf.add_item(title='时间戳',
            subtitle=timeToDate(args[0]),
            arg='url',
            valid=True,
            )
    wf.send_feedback()

if __name__ == '__main__':
    # Create a global `Workflow3` object
    wf = Workflow3()
    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    sys.exit(wf.run(main))
