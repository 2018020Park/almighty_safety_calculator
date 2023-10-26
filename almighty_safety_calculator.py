class Safety_Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def safety(self):
        z = self.x / self.y
        if z > 1:
            print(f"안전율이 {z}이므로 1보다 높습니다. 허용 가능합니다.")
        elif z < 1:
            print(f"안전율이 {z}이므로 1보다 낮습니다. 허용 할 수 없습니다. 재입력 하십시오.")
            while True:
                a = int(input("기준강도를 입력하십시오."))
                b = int(input("허용응력을 입력하십시오."))
                c = a / b
                if c < 1:
                    print(f"안전율이 {c}이므로 1보다 낮습니다. 허용 할 수 없습니다. 재입력 하십시오.")
                elif c > 1:
                    print(f"안전율이 {c}이므로 1보다 높습니다. 허용 가능합니다.")
                    break

    def stress(self):
        print(f"허용응력은 {self.y / self.x}입니다.")

    def strength(self):
        print(f"기준강도는 {self.x * self.y}입니다.")

m = input("계산기 입력. ('안전율 계산기', '허용응력 계산기', '기준강도 계산기' 중 택1)")

if m == "안전율 계산기" or m == "안전율계산기":
    k = int(input("기준강도 입력"))
    l = int(input("허용응력 입력"))
    safety_factor = Safety_Calculator(k, l)
    safety_factor.safety()

elif m == "허용응력 계산기" or m == "허용응력계산기":
    o = int(input("안전율 입력"))
    p = int(input("기준강도 입력"))
    allowable_stress = Safety_Calculator(o, p)
    allowable_stress.stress()

elif m == "기준강도 계산기" or m == "기준강도계산기":
    u = int(input("안전율 입력"))
    e = int(input("허용응력 입력"))
    basic_strength = Safety_Calculator(u, e)
    basic_strength.strength()
