# #creating thead without any class

from threading import *
import time

def display():
	for i in range(10):
		print("child thread-1")

t=Thread(target=display)
t.start()
for j in range(10):
	print("main thread-2")

print()

#create  a thrad using run mehof

class Test(Thread):
	def run(self):
		for i in range(10):
			print("1-->1")

t=Test()
t.start()

for j in range(10):
	print("main thread")

print()

#create  a thread without extending Thread class


class Test:
	def display(self):
		for i in range(10):
			print("1-->1")
o1=Test()
t=Thread(target=o1.display)
t.start()

for j in range(10):
	print("main thread")


################################################################
################################################################
############# isAlive(), enumerate(), active_acount() ##########
################################################################
################################################################


def Test():
	print(current_thread().getName(),"Start..")
	time.sleep(3)
	print(current_thread().getName(),"end..")

print(current_thread().getName(),'start..')
print("the number of active thread",active_count())

t1=Thread(target=Test,name="childthread1")
t2=Thread(target=Test,name="childthread2")
t3=Thread(target=Test,name="childthread3")

t1.start()
t2.start()
t3.start()

l=enumerate()
for t in l:
	print("thread name:",t.name)

print()

print(t1.name,'is alive: ',t1.isAlive())
print(t2.name,'is alive: ',t1.isAlive())
print(t3.name,'is alive: ',t1.isAlive())

print("the number of active acount" , active_count())

time.sleep(5)

print()

print(t1.name,'is alive: ',t1.isAlive())
print(t2.name,'is alive: ',t1.isAlive())
print(t3.name,'is alive: ',t1.isAlive())

l=enumerate()
for t in l:
	print("thread name:",t.name)

print("the number of active thread", active_count())



########################################################
################### join(), isDaemon() #################
########################################################




class Test(Thread):
	def run(self):
		for i in range(10):
			print("child start..")
			time.sleep(1)
			
t=Test(name="childThread1")
t.setDaemon(True)

t.start()
time.sleep(2)
print("main thread..")

print(t.name,"thread is daemon :",t.isDaemon())