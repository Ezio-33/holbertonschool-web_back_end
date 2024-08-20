#!/usr/bin/env python3
"""
Module pour mettre à jour les sujets d'une école dans MongoDB
"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Change tous les sujets d'une école dans une collection MongoDB

    :param mongo_collection: Un objet collection PyMongo
    :param name: Le nom de l'école à mettre à jour
    :param topics: La liste des nouveaux sujets
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
