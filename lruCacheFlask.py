import sys
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

capacity=0 # capacity of the cache
recency=[] # most recent data appended at the end (least recent data @ beginning)
kvCache={} # dictionary representing the cache
# all keys in "kvCache" must necessarily be in "recency",
# and must also be ordered by their recency of being accessed,
# and "recency" should have no keys other than those in "kvCache"

def initialize(cacheCap):
    print("Initializing...")
    global capacity
    global recency
    global kvCache
    capacity=cacheCap
    recency=[]
    kvCache={}
    print("lruCache capacity set to " + str(capacity))

@app.route('/api/v1/get/<int:k>', methods=['GET'])
def getLRUC(k):
    global capacity
    global recency
    global kvCache
    if k not in kvCache:
        abort(404)
    # if key is in the cache, update recency and return the key-value pair
    recency.remove(k)
    recency.append(k)
    res="200 " + "{k: " + str(k) + "; v: " + str(kvCache[k]) + "}"
    return res

@app.route('/api/v1/put/<int:k>', methods=['PUT'])
def putLRUC(k):
    v=int(request.data.decode('utf-8').split("=")[1])
    global capacity
    global recency
    global kvCache
    # If key passed already exists in cache, just update value and recency 
    if k in kvCache:
        kvCache[k]=v
        recency.remove(k)
        recency.append(k)
        res="200 {}"
        return res
    # if key passed is not in the cache, and cache capacity not yet full
    if len(kvCache)<capacity:
        kvCache[k]=v
        recency.append(k)
        res="200 {}"
        return res
    # if key passed is not in the cache, and cache completely filled up
    kvCache[k]=v
    recency.append(k)
    # remove 1st elem (least recently used) from the recency list, and even from kvCache
    lruKey=recency.pop(0)
    lruKeyVal=kvCache[lruKey]
    del kvCache[lruKey]
    res="200 " + "{k: " + str(lruKey) + "; v: " + str(lruKeyVal) + "}"
    return res

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__=='__main__':
    if len(sys.argv)<2:
        print("You must pass an integer representing the cache capacity")
        sys.exit()
    cacheCap=int(sys.argv[1])
    initialize(cacheCap)
    app.run(debug=True)
