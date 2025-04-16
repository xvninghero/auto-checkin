from miniprograms.changtai import ChangtaiMiniProgram
from miniprograms.lalaport import LalaportMiniProgram
import json

def main():
    with open("config/accounts.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    programs = [
        # ChangtaiMiniProgram(config.get("changtai", [])),
        LalaportMiniProgram(config.get("lalaport", []))
    ]

    for prog in programs:
        prog.run_all()

if __name__ == "__main__":
    main()