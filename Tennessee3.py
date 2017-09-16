import queue
from threading import Thread
import requests
import timeit

startTime = timeit.default_timer()
csl = []
entryQueue = queue.Queue()

q = queue.Queue()

for x in range(100):
    q.put(x)


# make list
def getEntry(int):
    string = "http://maps.googleapis.com/maps/api/geocode/json?address=" + str(int)
    requestLine = requests.get(string)
    entryQueue.put(requestLine)


# process list
def processEntry(Response):
    list = (Response.json()['results'])
    i = 0
    j = 0
    for y in range(len(list)):
        comparator = Response.json()['results'][j]['formatted_address']
        if 'Tennessee' in comparator:
            lat = (Response.json()['results'][j]['geometry']['bounds']['northeast']['lat'])
            lng = (Response.json()['results'][j]['geometry']['bounds']['northeast']['lng'])
            entry = comparator + ': ' + str(lat) + ',' + str(lng)
            csl.append(entry)

        j += 1
    i += 1
    j = 0


# thread to make list
class worker1(Thread):
    def __init__(self):
        super(worker1, self).__init__()

    def run(self):
        while q:
            item = q.get()
            getEntry(item)
            q.task_done()


# thread to process list
class worker2(Thread):
    def __init__(self):
        super(worker2, self).__init__()

    def run(self):
        while entryQueue:
            item = entryQueue.get()
            processEntry(item)
            entryQueue.task_done()


# make 10 threads that serve to get requests
for i in range(10):
    t = worker1()
    t.daemon = True
    t.run()

# make 10 threads that will go through the requests to search for applicable coordinates
for j in range(10):
    t = worker2()
    t.daemon = True
    t.run()

q.join()
print(csl)

endTime = timeit.default_timer()
print(endTime - startTime)
