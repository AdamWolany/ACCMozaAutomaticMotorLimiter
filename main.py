import time
import psutil

from acc_reader import ACCReader
from cars import CAR_LOCKS
from moza import MozaController
#from moza import set_steering_angle
from datetime import datetime


def log(message):
    with open("acc_moza.log", "a", encoding="utf-8") as file:
        file.write(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {message}\n")

def is_acc_running():
    for process in psutil.process_iter(["name"]):
        try:
            if process.info["name"] == "AC2-Win64-Shipping.exe":
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def main():
    acc_reader = ACCReader()
    moza = MozaController()
    
    last_car = None
    try:
        while True:
            if not is_acc_running():
                last_car = None
                time.sleep(5)
                continue
            current_car = acc_reader.get_current_car()
            if current_car != last_car:
                angle = CAR_LOCKS.get(current_car)

                if angle is not None:
                    if moza.set_steering_angle(angle):
                        last_car = current_car
                    log(f"{current_car} -> {angle}°")
                else:
                    log(f"{current_car} not found in CAR_LOCKS")
                last_car = current_car
            time.sleep(3)
    finally:
        moza.close()


if __name__ == "__main__":
    main()