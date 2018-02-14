import pymongo, pprint

# Server
connection = pymongo.MongoClient("149.89.150.100")

# Document
restdb = connection.test

# Collection
restaurants = restdb.restaurants

# Query from borough
def query_borough(borough):
    borough_qdoc = {'borough': borough}
    results = restaurants.find(borough_qdoc)
    for result in results:
        pprint.pprint(result)
    return results

# Query from zipcode
def query_zip(zipcode):
    zip_qdoc = {'address.zipcode': zipcode}
    results = restaurants.find(zip_qdoc)
    for result in results:
        pprint.pprint(result)
    return results

# Query from borough + grade
def query_bgrade(borough, grade):
    bgrade_qdoc = {"$and": [{'borough': borough}, {'grades.grade': grade}]}
    results = restaurants.find(bgrade_qdoc)
    for result in results:
        pprint.pprint(result)
    return results

# Query from borough + max score
def query_bltscore(borough, score):
    bltscore_qdoc = {"$and": [{'borough': borough}, {'grades.score': {'$lt': score}}]}
    results = restaurants.find(bltscore_qdoc)
    for result in results:
        pprint.pprint(result)
    return results

if __name__ == "__main__":
    # Test borough query
    #query_borough("Manhattan")

    # Test zip query
    #query_zip("11215")

    # Test borough + grade query
    #query_bgrade("Manhattan", "A")

    # Test borough + max score query
    query_bltscore("Manhattan", 2)