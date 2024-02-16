import schedule
import time 

def tarea_programada():
	print("I wanna be yours")


schedule.every(1).minutes.do(tarea_programada)

while True:
	schedule.run_pending()
	time.sleep(1)
