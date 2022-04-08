try:
    TEXT = requests.get('https://pastebin.com/raw/Gsdk2fKV').text
    GetIP = requests.get('https://api.ipify.org?format=json').text
    GETIP = re.findall('{"ip":"(.*?)"}', GetIP)
    IP = " ".join(GETIP)
    if IP in TEXT:
        pass
    else:
        input(f'Sorry You Can Not Access To This Tool [{IP}]')
        os._exit(1)
except:
    os._exit(1)
good = "  [ + ]"
ctypes.windll.kernel32.SetConsoleTitleW(f'#Lost Monitor - By @7zb8')
os.system('mode con: cols=76 lines=25')
bad = "  [ - ]"
qs = "  [ ? ]"
print("""

                 ██╗ ██╗ ██╗      ██████╗ ███████╗████████╗
                ████████╗██║     ██╔═══██╗██╔════╝╚══██╔══╝
                ╚██╔═██╔╝██║     ██║   ██║███████╗   ██║   
                ████████╗██║     ██║   ██║╚════██║   ██║   
                ╚██╔═██╔╝███████╗╚██████╔╝███████║   ██║   
                 ╚═╝ ╚═╝ ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   
                                           
                                                                                   
""")
def RandomStringUpper(n=10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))


def RandomString(n=10):
    letters = string.ascii_lowercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))


def RandomStringUpper(n=10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))


def RandomStringChars(n=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))


def randomStringWithChar(stringLength=10):
    letters = string.ascii_lowercase + '1234567890'
    result = ''.join(random.choice(letters) for i in range(stringLength - 1))
    return RandomStringChars(1) + result


###########################################################login#######################################################
def generateUSER_AGENT():
    Devices_menu = ['HUAWEI', 'Xiaomi', 'samsung', 'OnePlus']
    DPIs = [
        '480', '320', '640', '515', '120', '160', '240', '800'
    ]
    randResolution = random.randrange(2, 9) * 180
    lowerResolution = randResolution - 180
    DEVICE_SETTINTS = {
        'system': "Android",
        'Host': "Instagram",
        'manufacturer': f'{random.choice(Devices_menu)}',
        'model': f'{random.choice(Devices_menu)}-{randomStringWithChar(4).upper()}',
        'android_version': random.randint(18, 25),
        'android_release': f'{random.randint(1, 7)}.{random.randint(0, 7)}',
        "cpu": f"{RandomStringChars(2)}{random.randrange(1000, 9999)}",
        'resolution': f'{randResolution}x{lowerResolution}',
        'randomL': f"{RandomString(6)}",
        'dpi': f"{random.choice(DPIs)}"
    }
    return '{Host} 155.0.0.37.107 {system} ({android_version}/{android_release}; {dpi}dpi; {resolution}; {manufacturer}; {model}; {cpu}; {randomL}; en_US)'.format(
        **DEVICE_SETTINTS)
nospam = (''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(16)))
ssss = []
ssss1 = []
def exit_():
    input(f'{bad} Enter To Exit : ')
    os._exit(1)
class Main:
    def __init__(self):
        self.LISTL = []
        self.SESSIONSL = []
        self.NM = 0
        self.SSS = 0
        self.ddd = 0
        self.NOSP = 0
        self.DONE = 0
        self.ERROR = 0
        self.counting_pr , self.counting_li , self.counting_ses , self.counting_pr2 = 0,0,0,0
        self.dn , self.erro , self.mn = 0,0,0
        try:
            self.webhook = open('webhook.txt','r').read().splitlines()
            self.PROXIES = open('proxies.txt','r').read().splitlines()
            for i in self.PROXIES:
                self.counting_pr+=1
            print(f'{good} {self.counting_pr} Proxies Have Been Grabbed')
            self.LIST = open('list.txt', 'r').read().splitlines()
            for i in self.LIST:
                self.LISTL.append(i)
            print(f'{good} Usernames List Have Been Grabbed')
            self.SESSIONS = open('sessions.txt', 'r').read().splitlines()
            for i in self.SESSIONS:
                self.counting_ses+=1
            print(f'{good} {self.counting_ses} Sessions Have Been Grabbed')
            for i in self.SESSIONS:
                self.SESSIONSL.append(i)
            self.PROXIES_SWAP = open('proxies-swap.txt','r').read().splitlines()
            for i in self.PROXIES_SWAP:
                self.counting_pr2+=1
            print(f'{good} {self.counting_pr2} Swap Proxies Have Been Grabbed')
        except Exception as eeer : input(f'{bad} {eeer}');exit_()
        print('  ---------------------------------------------------------------------')
        self.MODE = input(f'  [ 1 ] Monitor skip 14 days\n  [ 2 ] Monitoring target\n  [ 3 ] Monitoring target With Auto Claim\n  [ ? ] Enter Mode : ')
        self.Target = input(f'{qs} Enter Target (if you chose [1] press enter) : ')
        self.MODE_PR = input(f'  [ 1 ] Http/s\n  [ 2 ] Socks4\n  [ ? ] Enter Proxies Mode : ')
        self.THE = input(f'{qs} Enter Threading : ')
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('mode con: cols=75 lines=15')
        if self.MODE == '1':
            threading.Thread(target=self.counting).start()
            threads1 = []
            TR = int(self.THE)
            for i in range(TR):
                thread1 = threading.Thread(target=self.M_1)
                thread1.start()
                threads1.append(thread1)
            for thread in threads1:
                thread.join()
        elif self.MODE == '2':
            threading.Thread(target=self.counting).start()
            threads1 = []
            TR = int(self.THE)
            for i in range(TR):
                thread1 = threading.Thread(target=self.M_2)
                thread1.start()
                threads1.append(thread1)
            for thread in threads1:
                thread.join()
        elif self.MODE == '3':
            threading.Thread(target=self.counting).start()
            threads1 = []
            TR = int(self.THE)
            for i in range(TR):
                thread1 = threading.Thread(target=self.M_3)
                thread1.start()
                threads1.append(thread1)
            for thread in threads1:
                thread.join()

    def counting(self):
        while True:
            ctypes.windll.kernel32.SetConsoleTitleW(f'[monitored : {self.mn}] [checked : {self.dn}] [error : {self.erro}]')
    def M_1(self):
        while True:
            for Target in self.LISTL:
                if Target in ssss:
                    pass
                else:
                    ssss.append(Target)
                    if self.MODE_PR == '1':
                        proxq = random.choice(self.PROXIES)
                        proxy = {'http': f"http://{proxq}", 'https': f"http://{proxq}"}
                    elif self.MODE_PR == '2':
                        proxq = random.choice(self.PROXIES)
                        proxy = {'http': f"socks4://{proxq}", 'https': f"socks4://{proxq}"}
                    self.url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
                    self.head = {'x-csrftoken': 'pp9UV9pirx3thkCos80JzKj7wbeZfwha','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
                    self.data = {
                        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:',
                        'email': f"{(''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(16)))}@gmail.com",
                        'username': Target,
                        'first_name': '',
                        'client_id': 'YisYKgALAAF0qjQcjA3DYLPTWVsL',
                        'seamless_login_enabled': '1',
                        'opt_into_one_tap': 'false',
                    }
                    try:
                        self.reqq = requests.post(url=self.url,data=self.data,headers=self.head,proxies=proxy).text
                        if ("Please try another.") in self.reqq:
                            self.mn+=1
                            print(f'  [ + ] Trying To Skip 14 days : {Target} | {datetime.datetime.now()}')
                            try:
                                mUrl = self.webhook[0]
                            except:""
                            data = {}
                            data["embeds"] = [
                                {
                                    "description": f"\n[+] @{Target} Trying To Skip 14 Day",
                                    "color": random.choice([0x3498db]), "thumbnail": {"url": ""},
                                    "author": {"name": "#Lost Monitor"}}]
                            try:
                                response2 = requests.post(mUrl, json=data)
                            except:
                                pass
                            with open('monitored.txt','a') as wr:
                                wr.write(f'{Target}\n')
                            self.LISTL.remove(Target)
                        elif ("This username isn't available.") in self.reqq:self.dn+=1
                        else:self.erro+=1
                    except:self.erro+=1
            ssss.clear()
    def CM(self):
        while True:
            if self.MODE_PR == '1':
                proxq = random.choice(self.PROXIES)
                proxy = {'http': f"http://{proxq}", 'https': f"http://{proxq}"}
            elif self.MODE_PR == '2':
                proxq = random.choice(self.PROXIES)
                proxy = {'http': f"socks4://{proxq}", 'https': f"socks4://{proxq}"}
            self.urla = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            self.heada = {'x-csrftoken': 'pp9UV9pirx3thkCos80JzKj7wbeZfwha','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
            self.dataa = {
                'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:',
                'email': f"{(''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(16)))}@gmail.com",
                'username': self.Target,
                'first_name': '',
                'client_id': 'YisYKgALAAF0qjQcjA3DYLPTWVsL',
                'seamless_login_enabled': '1',
                'opt_into_one_tap': 'false',
            }
            while True:
                try:
                    berr = requests.post(url=self.urla, data=self.dataa, headers=self.heada, proxies=proxy).text
                    if ("Please try another.") in berr:
                        if self.NM == 0:
                            self.NM += 1
                            self.mn += 1
                            print(f'  [ + ] Trying To Skip 14 days : {self.Target} | {datetime.datetime.now()}')
                           
                            try:
                                mUrl = self.webhook[0]
                            except:
                                ""
                            data = {}
                            data["embeds"] = [
                                {
                                    "description": f"\n[+] @{self.Target} Trying To Skip 14 Day",
                                    "color": random.choice([0x3498db]), "thumbnail": {"url": ""},
                                    "author": {"name": "#Lost Monitor"}}]
                            try:
                                response2 = requests.post(mUrl, json=data)
                            except:
                                pass
                            with open('monitored.txt', 'a') as wr:
                                wr.write(f'{self.Target}\n')
                        exit_()
                        break
                    elif ("This username isn't available.") in berr:
                        self.dn += 1
                    else:self.erro+=1
                except:
                 self.erro += 1
    def M_2(self):
        while True:
            if self.MODE_PR == '1':
                proxq = random.choice(self.PROXIES)
                proxy = {'http': f"http://{proxq}", 'https': f"http://{proxq}"}
            elif self.MODE_PR == '2':
                proxq = random.choice(self.PROXIES)
                proxy = {'http': f"socks4://{proxq}", 'https': f"socks4://{proxq}"}
            self.url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            self.head = {'x-csrftoken': 'pp9UV9pirx3thkCos80JzKj7wbeZfwha','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
            self.data = {
                'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:',
                'email': f"yusdbbfyevhh4e@gmail.com",
                'username': self.Target,
                'first_name': '',
                'client_id': 'YisYKgALAAF0qjQcjA3DYLPTWVsL',
                'seamless_login_enabled': '1',
                'opt_into_one_tap': 'false',
            }
            try:
                self.reqq = requests.post(url=self.url, data=self.data, headers=self.head, proxies=proxy).text
                if ("Please try another.") in self.reqq:
                    self.dn+=1
                elif ("This username isn't available.") in self.reqq:
                    threads1 = []
                    TR = int(self.THE)
                    for i in range(TR):
                        thread1 = threading.Thread(target=self.CM)
                        thread1.start()
                        threads1.append(thread1)
                    for thread in threads1:
                        thread.join()
                else:
                    self.erro += 1
            except :self.erro+=1
    def cc(self):
        while True:
            print(f'  AT : {self.DONE} | ER : {self.ERROR}')
    def claim(self):
        while True:
            for SES in self.SESSIONSL:
                if SES in ssss1:
                    pass
                else:
                    try:
                        ssss1.append(SES)
                        if self.MODE_PR == '1':
                            proxq = random.choice(self.PROXIES_SWAP)
                            proxy = {'http': f"http://{proxq}", 'https': f"http://{proxq}"}
                        elif self.MODE_PR == '2':
                            proxq = random.choice(self.PROXIES_SWAP)
                        url2 = 'https://i.instagram.com/api/v1/accounts/set_username/'
                        data2 = {'username': self.Target}
                        SwapS = requests.post(url2, headers={'User-Agent': generateUSER_AGENT(), "Accept": "*/*",
                                                             "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US",
                                                             "X-IG-Capabilities": "3brTvw==",
                                                             "X-IG-Connection-Type": "WIFI",
                                                             "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                                             'Host': 'i.instagram.com', 'Connection': 'keep-alive'},
                                              data=data2, cookies={'sessionid': f'{SES}'}, proxies=proxy)
                        if ('"status":"ok"') in SwapS.text:
                            if self.NOSP == 0:
                                GetUrl = 'https://i.instagram.com/api/v1/accounts/current_user/?edit=true'
                                self.NOSP = 1
                                mUrl = self.webhook[0]
                                data = {}
                                data["embeds"] = [
                                    {
                                        "description": f"\n[+] @{self.Target} Trying To Skip 14 Day & Claimed",
                                        "color": random.choice([0x3498db]), "thumbnail": {"url": ""},
                                        "author": {"name": "#Lost Monitor"}}]
                                try:
                                    response2 = requests.post(mUrl, json=data)
                                except:
                                    pass
                                try:
                                    requests.post('https://i.instagram.com/api/v1/accounts/set_biography/',
                                                  data={"raw_text": ''},
                                                  headers={'User-Agent': generateUSER_AGENT(), "Accept": "*/*",
                                                           "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US",
                                                           "X-IG-Capabilities": "3brTvw==", "X-IG-Connection-Type": "WIFI",
                                                           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                                           'Host': 'i.instagram.com', 'Connection': 'keep-alive'},
                                                  cookies={'sessionid': f'{SES}'})
                                    requests.post('https://i.instagram.com/api/v1/accounts/set_phone_and_name/',
                                                  data={"first_name": '#Lost Monitor'},
                                                  headers={'User-Agent': generateUSER_AGENT(), "Accept": "*/*",
                                                           "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US",
                                                           "X-IG-Capabilities": "3brTvw==", "X-IG-Connection-Type": "WIFI",
                                                           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                                           'Host': 'i.instagram.com', 'Connection': 'keep-alive'},
                                                  cookies={'sessionid': f'{SES}'})
                                except:
                                    pass
                                try:
                                    headerss = {
                                        'User-Agent': generateUSER_AGENT(),
                                        "Accept": "*/*",
                                        "Accept-Encoding": "gzip, deflate",
                                        "Accept-Language": "en-US",
                                        "X-IG-Capabilities": "3brTvw==",
                                        "X-IG-Connection-Type": "WIFI",
                                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                        'Host': 'i.instagram.com',
                                        'Connection': 'keep-alive'}
                                    GetUrl = 'https://i.instagram.com/api/v1/accounts/current_user/?edit=true'
                                    gett = requests.get(GetUrl, headers=headerss,cookies={'sessionid': f'{SES}'}).json()
                                    email = gett['user']['email']
                                    with open(f'@{self.Target}.txt', 'a') as dee:
                                        dee.write(f'username : {self.Target}\nsessionid : {SES}\ne-mail : {email}')

                                except:
                                    pass
                                ctypes.windll.user32.MessageBoxW(0, f'Claimed @{self.Target}\nby #Lost Monitor', '#Lost Monitor')
                                try:
                                    os._exit(1)
                                except:
                                    exit(1)
                        elif SwapS.status_code == 400:
                            self.DONE += 1
                        else:
                            self.ERROR += 1
                    except:self.ERROR+=1
            self.SESSIONSL.clear()
    def M_3(self):
            while True:
                if self.MODE_PR == '1':
                    proxq = random.choice(self.PROXIES)
                    proxy = {'http': f"http://{proxq}", 'https': f"http://{proxq}"}
                elif self.MODE_PR == '2':
                    proxq = random.choice(self.PROXIES)
                    proxy = {'http': f"socks4://{proxq}", 'https': f"socks4://{proxq}"}
                self.url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
                self.head = {'x-csrftoken': 'pp9UV9pirx3thkCos80JzKj7wbeZfwha',
                             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
                self.data = {
                    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:',
                    'email': f"yusdbbfyevhh4e@gmail.com",
                    'username': self.Target,
                    'first_name': '',
                    'client_id': 'YisYKgALAAF0qjQcjA3DYLPTWVsL',
                    'seamless_login_enabled': '1',
                    'opt_into_one_tap': 'false',
                }
                try:
                    self.reqq = requests.post(url=self.url, data=self.data, headers=self.head, proxies=proxy).text
                    if ("Please try another.") in self.reqq:
                        self.dn += 1
                    elif ("This username isn't available.") in self.reqq:
                        while True:
                            self.reqq_ = requests.post(url=self.url, data=self.data, headers=self.head,
                                                       proxies=proxy).text
                            if ("Please try another.") in self.reqq_:
                                if self.NM == 0:
                                    self.NM += 1
                                    print(f'  [ + ] Trying To Skip 14 days : {self.Target} | {datetime.datetime.now()}')
                                    print("")
                                    print(f'  [ + ] Trying To Claim : @{self.Target}')
                                    print("")
                                    threading.Thread(target=self.cc)
                                    threads12 = []
                                    TRq = int(1200)
                                    for i in range(TRq):
                                        thread1q = threading.Thread(target=self.claim)
                                        thread1q.start()
                                        threads12.append(thread1q)
                                    for threadq in threads12:
                                        threadq.join()
                    else:
                        self.erro += 1
                except:
                    self.erro += 1


Main()
