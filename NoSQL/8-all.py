#!/usr/bin/env python3
"""
Module pour lister tous les documents dans une collection MongoDB
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Liste tous les documents dans une collection MongoDB
    
    :param mongo_collection: Un objet collection PyMongo
    :return: Une liste de tous les documents dans la collection
    """
    documents = []
    for doc in mongo_collection.find():
        documents.append(doc)
    return documents
