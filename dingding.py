from dingtalkchatbot.chatbot import DingtalkChatbot


def create_monitor_flow(content):
    # webhook 通过钉钉群添加机器人可获取
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=c4b683fc690522b94fc8d0c1b8eb4076166223a186daa0621b321d408f317c3b'
    xiaoding = DingtalkChatbot(webhook)
    xiaoding.send_markdown(title='数据监控', text=content, is_at_all=True)


def send(mark_available=list):
    if mark_available is None:
        return

    if isinstance(mark_available, list):

        if len(mark_available) <= 0:
            return

        for single in mark_available:
            hos_name = single["hosName"]
            first_dept_name = single["firstDeptName"]
            second_dept_name = single["secondDeptName"]
            yuyue = single["yuyue"]
            url = single["url"]

            if len(yuyue) <= 0:
                continue

            content = '#### ****[114] 可预约提醒 %s**** \n  *****%s***** - *****%s***** \n' % (hos_name, first_dept_name, second_dept_name)
            content = content + "".join(yuyue)
            content = content + "".join(url)

            create_monitor_flow(content)
