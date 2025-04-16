import requests
from .base import MiniProgramBase

class ChangtaiMiniProgram(MiniProgramBase):
    def sign(self, account):
        headers = {
            "x-app-token": account["token"],
            "x-app-marketid": "1",
            "x-app-platform": "wxapp",
            "x-app-version": "2.1.1",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12...)",
            "Referer": "https://servicewechat.com/wx2a4be1a19e10933/49/page-frame.html"  # 替换为真实 Referer
        }

        response = requests.post(
            "https://api.crm.chamshare.cn/daySign",  # 如果接口不同，请替换
            headers=headers,
            json={}
        )
        result = response.json()
        if result.get("code") == 0:
            print(f"[长泰广场] {account['name']} 签到成功，积分 +{result['data'].get('integral', 0)}")
        else:
            print(f"[长泰广场] {account['name']} 签到失败：{result}")
