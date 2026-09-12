from pyaccsharedmemory import accSharedMemory


class ACCReader:
    def __init__(self):
        self.acc = accSharedMemory()

    def get_current_car(self):
        data = self.acc.read_shared_memory()

        if data is None:
            return None

        return data.Static.car_model.rstrip("\x00") # Remove null bytes from the string