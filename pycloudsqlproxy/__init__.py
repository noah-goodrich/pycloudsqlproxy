import logging
import os
import subprocess
import sys
import time
import signal

log = logging.getLogger()
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler(sys.stdout))

def connect(instances):
    log.info('>> cloud_sql_proxy called')

    log.info('>> cloud_sql_proxy starting')
    cmd = ['{}/cloud_sql_proxy'.format(os.path.dirname(__file__)),
            '-instances={}=tcp:3306'.format(instances)]
    print(cmd)
    proxy = subprocess.Popen(cmd)
    pid = proxy.pid

    log.info('>> cloud_sql_proxy pid: {}'.format(pid))
    log.info('>> cloud_sql_proxy finished connecting')
    return pid

def disconnect(pid):
    log.info('>> cloud_sql_proxy disconnect called')
    if (pid != None):
        log.info('>> cloud_sql_proxy killing pid {}'.format(pid))
        os.kill(pid, signal.SIGKILL)
    else:
        log.info('>> cloud_sql_proxy no pid found to kill')
