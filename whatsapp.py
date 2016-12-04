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
		msg = "Hello, Ashish is currently unavailable , I am his virtual assistant.Kindly leave your message to me, I will inform him once he is free."
		
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


		
		

