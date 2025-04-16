import requests
import datetime
import hashlib
from .base import MiniProgramBase

class LalaportMiniProgram(MiniProgramBase):
    def sign(self, account):
        url = "https://weixinnew.lalaport-jq.com:42211/api/Sign/SignIn"
        app_id = "api.app.member"
        buildingid = "ST0001"
        open_id = "oHFYW5MHocGxOd7qfgvYisTD6ENw"
        authorization = account["authorization"]

        app_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        app_sign = hashlib.md5((app_id + app_time + "abc123456789").encode()).hexdigest().upper()  # 签名逻辑仅示意

        headers = {
            "authorization": authorization,
            "buildingid": buildingid,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; ...)",
            "Referer": "https://servicewechat.com/wx8f8b976e0c4a82e2/33/page-frame.html"
        }

        body = {
            "requestId": "v5.app.member.wechat",
            "openId": open_id
        }

        response = requests.post(url, headers=headers, json=body)
        result = response.json()
        if result.get("success"):
            print(f"[Lalaport] {account['name']} 签到成功， +{result['msg']}")
        else:
            print(f"[Lalaport] {account['name']} 签到失败：{result}")