from miniprograms.changtai import ChangtaiMiniProgram
from miniprograms.lalaport import LalaportMiniProgram
from miniprograms.jinqiaotaimao import TaimaoMiniProgram
from miniprograms.huizhiguoji import HuizhiMiniProgram
import json
import os

# ✅ 获取 config/accounts.json 的绝对路径
def get_config_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "config", "accounts.json")

def main():
    config_path = get_config_path()
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    programs = [
        ChangtaiMiniProgram(config.get("changtai", [])),
        LalaportMiniProgram(config.get("lalaport", [])),
        TaimaoMiniProgram(config.get("taimao", [])), 
        HuizhiMiniProgram(config.get("huizhi", []))
    ]

    for prog in programs:
        prog.run_all()

# ✅ 腾讯云函数入口
def main_handler(event, context):
    main()

if __name__ == "__main__":
    main()
