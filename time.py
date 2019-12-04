import sys
from workflow import Workflow, ICON_WEB, web
# To use Alfred 3+ feedback mechanism:
# from workflow import Workflow3

def main(wf):
    args = wf.args
    wf.logger.debug('yhb'+ args)
    wf.add_item(title='title',
            subtitle='source',
            arg='url',
            valid=True,
            icon=ICON_DEFAULT)
    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
