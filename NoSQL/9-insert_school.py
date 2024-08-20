#!/usr/bin/env python3
"""
Module pour insérer un nouveau document dans une collection MongoDB
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Insère un nouveau document dans une collection MongoDB
    
    :param mongo_collection: Un objet collection PyMongo
    :param kwargs: Les paires clé-valeur à insérer dans le document
    :return: L'ID du nouveau document inséré
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
