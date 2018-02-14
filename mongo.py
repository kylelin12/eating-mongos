import pymongo

connection = pymongo.MongoClient("149.89.150.100")

restdb = connection.test

restaurants = restdb.restaurants

def query_borough(borough):
    results = restaurants.find("{'borough': %s}", borough)
    print(results)
    return results

def query_zip(zipcode):
    results = restaurants.find("{'address.zipcode': %s}", zipcode)
    print(results)
    return results