
import threading

'''
threading:Python中线程的使用
'''

class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(100):
            print(threading.current_thread().getName())

x=BuckysMessenger(name="Send out Messages")
y=BuckysMessenger(name="Receive messages")
x.start()
y.start()