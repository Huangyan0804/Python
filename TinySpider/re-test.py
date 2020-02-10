import re

text = r"<font style=\"display: inline;white-space:nowrap;\" color=\"red\">请先登录系统</font>"

cp = re.compile(r"请先登录系统")

login_status = False
if re.match(re.compile('.*请先登录系统.*'), text) is None:
    login_status = True

print(login_status)
