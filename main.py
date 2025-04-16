from miniprograms.changtai import ChangtaiMiniProgram
from miniprograms.lalaport import LalaportMiniProgram
from miniprograms.jinqiaotaimao import TaimaoMiniProgram
from miniprograms.huizhiguoji import HuizhiMiniProgram
import json
import os

# ✅ 新增 Kivy 相关导入
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

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

# ✅ 安卓 APK 主入口（新增 GUI）
class CheckinApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.status_label = Label(text="欢迎使用签到助手", font_size=18)
        checkin_btn = Button(text="立即签到", font_size=20)
        checkin_btn.bind(on_press=self.do_signin)
        layout.add_widget(self.status_label)
        layout.add_widget(checkin_btn)
        return layout

    def do_signin(self, instance):
        try:
            main()
            self.status_label.text = "✅ 签到完成"
        except Exception as e:
            self.status_label.text = f"❌ 出错了：{str(e)}"

# ✅ 判断入口（区分云函数或 GUI 模式）
if __name__ == "__main__":
    try:
        from kivy import __version__  # 判断是否运行在 APK 内部
        CheckinApp().run()
    except ImportError:
        main()
