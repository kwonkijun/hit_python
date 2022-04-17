import sys
import os
import win32com.shell.shell as shell

# 관리자 권한을 얻어야 할때
if sys.argv[-1] != 'asadmin':
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + ['asadmin'])
    shell.ShellExecuteEx(
        lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)