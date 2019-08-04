#!/usr/bin/env python
#-*-coding:utf-8-*-

#author:wuya


from selenium import  webdriver
from selenium.webdriver.common.by import By
from UI.base.base import  *
import  time as t
from appium import  webdriver

class SinaLogin(AppUi):
	# tiYan_loc=(By.XPATH,"//android.widget.Button[@text='立即体验']")
	# shaohou_loc=(By.ID,"android:id/button1")
	login_loc=(By.XPATH,"//android.widget.Button[@text='登录']")
	username_loc=(By.ID,"com.sina.mail:id/etAccount")
	password_loc=(By.ID,"com.sina.mail:id/etPassword")
	loginButton_loc=(By.ID,"com.sina.mail:id/btnLogin")
	menu_loc=(By.ID,'com.sina.mail:id/btnMenu')
	nick_loc=(By.ID,'com.sina.mail:id/tvEmail')
	set_loc=(By.ID,'com.sina.mail:id/btnSet')
	exit_loc=(By.ID,'com.sina.mail:id/setting_btn_exit')
	exitSure_loc=(By.ID,'android:id/button1')


	@property
	def clickTiYan(self):
		self.findElement(*self.tiYan_loc).click()

	@property
	def clickLogin(self):
		self.findElement(*self.login_loc).click()

	def typeUsername(self,username):
		t.sleep(3)
		self.findElement(*self.username_loc).send_keys(username)

	def typePasswd(self,password):
		t.sleep(3)
		self.findElement(*self.password_loc).send_keys(password)

	@property
	def clickLoginButton(self):
		self.findElement(*self.loginButton_loc).click()

	@property
	def clickMenu(self):
		self.findElement(*self.menu_loc).click()

	@property
	def getNick(self):
		return  self.findElement(*self.nick_loc).text

	@property
	def clickSet(self):
		self.findElement(*self.set_loc).click()

	@property
	def clickExit(self):
		self.findElement(*self.exit_loc).click()

	@property
	def clickExitSure(self):
		self.clickExit
		self.findElement(*self.exitSure_loc).click()

	def exit(self):
		self.clickSet
		self.clickExitSure

	def login(self,username,password):
		self.clickLogin
		self.typeUsername(username)
		self.typePasswd(password)
		self.clickLoginButton
		t.sleep(6)