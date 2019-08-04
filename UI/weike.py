#!/usr/bin/env python
#coding:utf-8

#Author:WuYa

import  requests
import  unittest_1
import  warnings

def getHeaders():
	headers={
		'Content-Type':'application/x-www-form-urlencoded',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'}
	return headers

def getData():
	dict1={'formhash':'b4ba6e','txt_account':'13484545195','pwd_password':'60e52c87966078c0b3fab7debb0fc892','login_type':3,'ckb_cookie':0,
	       'hdn_refer':'http://www.epwk.com/','txt_code':'','pre':'login','inajax':1}
	return dict1

class SessionTest(unittest_1.TestCase):
   def login(self):
      r = requests.post(
         url='https://www.epwk.com/index.php?do=login',
         data=getData(),
         headers=getHeaders())
      return r.cookies

   def test_task(self):
      '''我的发布任务'''
      r = requests.post(
         url='http://i.epwk.com/home/employer/index.html',
         data={'model': 'xsrw', 'status': 'all'},
         headers=getHeaders(),
         cookies=self.login())
      self.assertEqual(r.status_code,200)

if __name__ == '__main__':
    unittest_1.main(verbosity=2)
