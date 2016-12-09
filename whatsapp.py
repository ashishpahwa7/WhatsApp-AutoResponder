'''
MIT License

Copyright (c) 2016 Ashish Pahwa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from lxml import html
from selenium import webdriver
from pyvirtualdisplay import Display  
import os
import time
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

display = Display(visible=1, size=(1920, 1080))
display.start()


class Whatsapp:

	def __init__(self):
		self.browser = webdriver.Firefox()

	def sendMessage(self, people):
		msg = "Hello, Ashish is currently unavailable, Please leave your message after next beep ....*Beep* :P "
		
		for name in people:
			try:
				elem = self.browser.find_element_by_xpath(
				'//span[contains(text(),"%s")]'%name
				)			
				elem.click()
				elem1 = self.browser.find_elements_by_class_name('input')
				elem1[1].send_keys(msg)
				self.browser.find_element_by_class_name('send-container').click()
			except:
				print 'Unable to read name'

	def login(self):
		self.browser.get('http://web.whatsapp.com')
		raw_input('Press any key whenever you are ready')

	def read(self):

		while(1):

			#self.browser.get('http://web.whatsapp.com')
			#time.sleep(15)
						
			try:
				page = self.browser.page_source
			except:
				print "Unable to load page"

			tree = html.fromstring(page)

			unread = tree.xpath(
				'//div[contains(@class, "infinite-list-item")]/div[1]/div[contains(@class, "unread chat")]//div[contains(@class, "chat-body")]/div[contains(@class, "chat-main")]/div[contains(@class, "chat-title")]/span/@title'
				)
			print 'You have unread message from :'
	
			for person in unread:
				print person

			self.sendMessage(unread)
			time.sleep(10)  


		
		

