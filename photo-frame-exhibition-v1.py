
"""import RPi.GPIO as GPIO"""
import time
import psutil
import random


# blinking function: note that it is only one blink if you want to perform more 
#blinks at once you have to use a for loop

"""def blink(pin):
        # to use Raspberry Pi board pin numbers
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        # set up GPIO output channel  
        GPIO.setup(16, GPIO.OUT)
        # blink GPIO17 50 tim
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(0.5)
        return
 """
#the ammount of delay for mimicing the usuage of internet
def random_delay():
  base_value = random.randint(0, 100)
  print "base is "+str(base_value)
  if base_value<10:
    delay=(1+base_value)
  elif base_value>90:
    delay=(1+(100-base_value))
  elif base_value>10 and base_value<90:
    delay=1+(100-base_value)*1.5
  else:
    delay=5
  print "dealy is "+str(delay)
  return delay



#the random ammount for mimicing the cycle of each response
def random_cycle():
  cycle=random.randint(4,10)
  print "cycle is "+str(cycle)
  return cycle

 
 
#main program
def main():
  old_value = 0
 
  #main loop
  while True:
        #sum of the send and receive 
    new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
 
    if old_value:
        a=new_value - old_value
        if a<100000:
                  #programming guide print
              #print "nothing"
              #print "the network traffic usuage is "+str(a)
              """for i in range(0,random_cycle()):
                blink(16)
                GPIO.cleanup()"""
              dd= random_delay()
              time.sleep (dd)
              print random_cycle()

        else:
                  #programming guide print 
              print "sth"
              print "the network traffic usuage is"+str(a)
              #for performing 5 blinks
              """for i in range(0,5):
                  blink(16)
                  GPIO.cleanup()"""
 
    old_value = new_value
 
    time.sleep(1)
        #GPIO.cleanup()
 
b= main()
print "a value equals:"+ b
