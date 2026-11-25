"""Till Firmware Do Us Part — entry for make.fun.

Writes one line to /output/entry.txt. The line is one funny, heartfelt wedding vow a robot says at its own wedding, under 200 characters.
"""
import os

LINE = "I take you to be my lawfully wedded update, to have and to hold, in low battery and in full charge, till the factory reset do us part."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
