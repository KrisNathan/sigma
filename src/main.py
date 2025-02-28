import random
    
class Mobil:
    speed: int = 0
    accel: int

    def __init__(self, accel: int):
        self.accel = accel

    def forward(self):
        self.speed += self.accel

class Toyota(Mobil):
    asuransi_astra: bool = False

    def apply_insurance(self):
        self.asuransi_astra = True

def main():
    # random.seed()
    # print(f"1-100: {random.randint(1, 100)}")
    # print(f"{Math.add(69, 420)}")

    mobi = Toyota(10)
    print(f"{mobi.accel} {mobi.speed}")
    mobi.forward()
    mobi.forward()
    print(f"{mobi.accel} {mobi.speed}")

    print(f"Is insured: {mobi.asuransi_astra}")
    mobi.apply_insurance()
    print(f"Is insured: {mobi.asuransi_astra}")



if __name__ == "__main__":
    main()
