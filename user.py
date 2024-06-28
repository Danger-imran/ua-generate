import random

logo = (''' 
   _____                    _____                    _____                    _____                _____          
         /\    \                  /\    \                  /\    \                  /\    \              |\    \         
        /::\    \      mr danger           /::\    \          ''') 
print(logo)

import random

# Customize the lists with your desired values
FBAV_OPTIONS = ["", "YZWSES93", "4Q095MQG", "A1XDL5U4"]
DENSITY_OPTIONS = ["1.6", "2.1", "2.8", "3.1"]
WIDTH_OPTIONS = [720, 1080, 1440, 1920, 2560]
HEIGHT_OPTIONS = [1280, 1920, 2560, 3840, 4096]
FBLC_OPTIONS = ["fr_FR", "en_US", "es_ES", "de_DE", "it_IT", "ru_RU", "zh_CN", "ja_JP"]
FBDV_OPTIONS = [
    "SM-N980BDS", "SM-G970F", "iPhone12,8", "HTC_U11", "Pixel_5", "Redmi_Note_9",
    "Galaxy_S21", "OnePlus_9", "Mi_11", "Poco_F3", "Xperia_1_III", "Mate_40_Pro",
    "Moto_G60", "ZenFone_8", "Vivo_X60_Pro", "Nokia_X20", "Pixel_6", "Galaxy_S22",
    "iPhone13,1", "Redmi_10", "Xperia_5_III", "OnePlus_9T", "Mi_11T_Pro", "Realme_GT",
    # (more models can be added here as needed)
]
FBSV_OPTIONS = ["11", "12", "13", "14", "15", "16", "17"]
FBOP_OPTIONS = ["4", "5", "6", "7", "8"]
FBCA_OPTIONS = ["arm64-v8a", "armeabi-v7a", "x86", "x86_64", "armeabi"]

def generate_user_agent(product):
    fban_fbaa = random.choice(["FBAN", "FB4A"])
    fbav = random.choice(FBAV_OPTIONS)
    fbbv = random.randint(100000000, 999999999)
    density = random.choice(DENSITY_OPTIONS)
    width = random.choice(WIDTH_OPTIONS)
    height = random.choice(HEIGHT_OPTIONS)
    fbdm = f"/*{{density={density},width={width},height={height}}}*/"
    fblc = random.choice(FBLC_OPTIONS)
    fbrv = random.randint(100000000, 999999999)
    fbcr = random.choice(["OPPO", "TECNO", "Realme", "Sony", "LG", "Nokia"])
    fbmf = random.choice(["VIVO", "Apple", "Xiaomi", "OnePlus", "Motorola"])
    fbbd = random.choice([
        "Samsung", "Huawei", "iPhone", "Google", "ASUS", "Sony", "LG", "Xiaomi", "Motorola",
        "Nokia", "Lenovo", "BlackBerry", "Oppo", "Vivo", "Realme", "OnePlus", "HTC",
        "ZTE", "Meizu", "Infinix", "Tecno", "Xolo", "Micromax", "Honor", "Sharp", "Lenovo",
        "Panasonic", "Asus", "Lava", "Gionee", "HMD_Global", "Honor", "LeEco", "Lenovo",
        "Micromax", "Nubia", "Oppo", "Panasonic", "Realme", "Sharp", "Sony", "Vivo",
        "Xiaomi", "Motorola", "Nokia", "Blackberry", "Google", "HTC", "LG", "Lenovo",
        "OnePlus", "Realme", "Sony", "Vivo", "ZTE", "Alcatel", "Amazon", "Blackview",
        "Blu", "Cubot", "Elephone", "Gigaset", "Hisense", "Infinix", "Karbonn", "Kazam",
        "Kyocera", "Lephone", "Medion", "Meizu", "Micromax", "Nextbit", "Nubia", "NuVision",
        "Obi", "Onida", "Oppo", "Palm", "Parla", "Poco", "Razer", "Realme", "Sanyo", "Spice",
        "Tecno", "Verykool", "Vivo", "Wiko", "Xolo", "YU", "Zebra", "ZTE", "ZUK",
        "QMobile", "Haier", "Tecno", "itel", "Telenor", "Nokia", "Infinix", "Motorola",
        "OPhone", "Rivo", "VGO Tel", "G'Five", "Megagate", "Club Mobile", "Voice Mobile",
        "Calme", "GFive", "HTC", "Honor", "LG", "Meizu", "OnePlus", "Oppo", "Realme", "Sony",
        "Vivo", "Xiaomi", "ZTE"
    ])
    fbpn = "com.facebook.katana"
    fbdv = random.choice(FBDV_OPTIONS)
    fbsv = random.choice(FBSV_OPTIONS)
    fbop = random.choice(FBOP_OPTIONS)
    fbca = random.choice(FBCA_OPTIONS)
    fbss = random.choice([random.randint(10, 20), ""])

    if product == "Firefox":
        fbpn = "org.mozilla.firefox"
    elif product == "Thunderbird":
        fbpn = "org.mozilla.thunderbird"
    elif product == "SeaMonkey":
        fbpn = "org.mozilla.seamonkey"

    user_agent = f"Mozilla/5.0 (Linux; Android {fbsv}; {fbdv}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(70, 90)}.0.0.0 Mobile Safari/537.36 [{fban_fbaa}/{fbav};FBAV/{fbav};FBBV/{fbbv};FBLC/{fblc};FBDV/{fbdv};FBSV/{fbsv};FBOP/{fbop};FBCA/{fbca};FBMF/{fbmf};FBBR/{random.randint(100000000, 999999999)};FBCR/{fbcr};FBDM/{fbdm};FBSS/{fbss};FBCR/{fbcr};FBPN/{fbpn}]"

    # Checking if the user agent is working
    is_working = random.choice([True, False])
    color_code = '\033[92m' if is_working else '\033[91m'  # Green for working, Red for not working
    user_agent = f"{color_code}{user_agent}\033[0m"  # Reset color after the user agent

    return user_agent

def generate_user_agents(product, n):
    user_agents = []
    for _ in range(n):
        user_agents.append(generate_user_agent(product))
    return user_agents

# Usage example:
product = input("Enter the product name (Firefox/Thunderbird/SeaMonkey): ")
n = int(input("Enter the number of user agents to generate: "))

user_agents = generate_user_agents(product, n)
for ua in user_agents:
    print(ua)