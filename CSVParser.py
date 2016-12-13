import csv
import os
import queue
import threading
import time
import elasticsearch
from elasticsearch import helpers
#pip install elasticsearch
#Written with Python 3.5

class parserThread(threading.Thread):
    def __init__(self, ID, name, q):
        threading.Thread.__init__(self)
        self.thread = ID
        self.name = name
        self.q = q

    def run(self):
        print("\nStart " + self.name)
        self.parseCSV()
        print("\nEnd " + self.name)

    def parseCSV(self):
        while endFlag:
            #start = time.time()
            queueLock.acquire()
            if not csvQueue.empty():
                filename = self.q.get()
                queueLock.release()
                print("Thread-%s processing %s\n" % (self.thread, filename))
                populateDB(filename)
                #print("Time: %s" % (time.time()-start))
            else:
                queueLock.release()

def populateDB(filename):
    with open(path + filename) as csvfile:
        reader = csv.DictReader(csvfile)
        bulkdata = []
        if (filename == 'perform-summary.csv'):
            for row in reader:
                data = {
                    "_index": "test",
                    "_type": "raw",
                    "_id": (str(row['serialNumberInserv']) + '.0'),
                    "_source": row
                }
                bulkdata.append(data)
        else:
            i = 0
            for row in reader:
                i += 1
                data = {
                    "_index": "test",
                    "_type": "raw",
                    "_id": (str(row['systemId']) + '.' + str(i)),
                    "_source": row
                }
                bulkdata.append(data)
    helpers.bulk(es,bulkdata)


es = elasticsearch.Elasticsearch()
path = "./perform-csv/"
start = time.time()
#Please change this to the number of threads according to CPU
numThreads = 2
queueLock = threading.Lock()
csvQueue = queue.Queue(0)
threads = []
threadID = 1

endFlag = 1

if es.indices.exists('test'):
    res = es.indices.delete(index='test')
    print("Response: '%s'" % res)


for num in range(numThreads):
    thread = parserThread(threadID, "Thread-" + str(threadID), csvQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

queueLock.acquire()
for filename in os.listdir(path):
    csvQueue.put(filename)
queueLock.release()

while not csvQueue.empty():
    pass

endFlag = 0

for t in threads:
    t.join()
endTime = time.time() - start

print("Parser Finished. Time: " + str(endTime))
