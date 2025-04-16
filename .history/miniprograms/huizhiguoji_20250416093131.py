import requests
from .base import MiniProgramBase

class TaimaoMiniProgram(MiniProgramBase):
    def sign(self, account):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12...)",
            "Referer": "https://servicewechat.com/wx6074aac511d8888e/19/page-frame.html"
        }

        payload = {
            "MallID": 11641,
            "pageIndex": 1,
            "pageSize": 100,
            "LotteryVersion": 0,
            "LotteryUrl": None,
            "Header": {
                "Token": account["token"],
                "systemInfo": {
                    "model": "M2102J2SC",
                    "SDKVersion": "3.4.10",
                    "system": "Android 12",
                    "version": "8.0.49",
                    "miniVersion": "2.73.1"
                }
            }
        }

        response = requests.post(
            "https://m.mallcoo.cn/api/user/User/CheckinV2",
            headers=headers,
            json=payload
        )
        result = response.json()
        if result.get("code") == 0:
            print(f"[金桥太茂] {account['name']} 签到成功，积分 +{result['data'].get('integral', 0)}")
        else:
            print(f"[金桥太茂] {account['name']} 签到失败：{result}")