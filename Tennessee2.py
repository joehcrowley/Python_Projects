import timeit
import requests
from threading import Thread

startTime = timeit.default_timer()

# list containing each response from Google Map's API

# iterators
i = 0
j = 0
# comma separated list to hold lat, lng values
csl = []
counter = 0

threads = []

class MyThread(Thread):
    def __init__(self):
        pass
    def run(self):
        counter = self
        for x in range(10):
            string = "http://maps.googleapis.com/maps/api/geocode/json?address=" + str(counter)
            requestLine = requests.get(string)
            list = (requestLine.json()['results'])
            i = 0
            j = 0
            for y in range(len(list)):
                comparator = requestLine.json()['results'][j]['formatted_address']
                if 'Tennessee' in comparator:
                    lat = (requestLine.json()['results'][j]['geometry']['bounds']['northeast']['lat'])
                    lng = (requestLine.json()['results'][j]['geometry']['bounds']['northeast']['lng'])
                    entry = comparator + ': ' + str(lat) + ',' + str(lng)
                    csl.append(entry)

                j += 1
            i += 1
            j = 0
            counter += 10



t0 = MyThread(0)
t1 = MyThread(1)
t2 = MyThread(2)
t3 = MyThread(3)
t4 = MyThread(4)
t5 = MyThread(5)
t6 = MyThread(6)
t7 = MyThread(7)
t8 = MyThread(8)
t9 = MyThread(9)
t10 = MyThread(10)

t0.start()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()


threads.append(t0)
threads.append(t1)
threads.append(t2)
threads.append(t3)
threads.append(t4)
threads.append(t5)
threads.append(t6)
threads.append(t7)
threads.append(t8)
threads.append(t9)

for t in threads:
    t.join()

print(csl)
print(len(csl))


endTime = timeit.default_timer()
print(endTime - startTime)
