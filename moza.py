import ctypes
import time
import sys
from pathlib import Path

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / relative_path

    return Path(__file__).parent / relative_path

class MozaController:
    def __init__(self):
        dll_path = resource_path("sdk/MOZA_SDK.dll")

        self.dll = ctypes.WinDLL(str(dll_path))

        self.install_sdk = getattr(
            self.dll,
            "?installMozaSDK@moza@@YAXXZ"
        )

        self.remove_sdk = getattr(
            self.dll,
            "?removeMozaSDK@moza@@YAXXZ"
        )

        self.set_motor_limit_angle = getattr(
            self.dll,
            "?setMotorLimitAngle@moza@@YA?AW4ERRORCODE@@HH@Z"
        )

        self.install_sdk.argtypes = []
        self.install_sdk.restype = None

        self.remove_sdk.argtypes = []
        self.remove_sdk.restype = None

        self.set_motor_limit_angle.argtypes = [
            ctypes.c_int,
            ctypes.c_int,
        ]

        self.set_motor_limit_angle.restype = ctypes.c_int

        self.install_sdk()

        # Dajemy SDK chwilę na wykrycie bazy
        time.sleep(3)

    def set_steering_angle(self, angle):
        result = self.set_motor_limit_angle(angle, 2000)

        if result != 0:
            print(f"Failed to set motor limit angle: {result}")
            return False

        print(f"Motor limit angle set to {angle}°")
        return True

    def close(self):
        self.remove_sdk()