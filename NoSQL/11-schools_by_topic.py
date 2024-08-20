#!/usr/bin/env python3
"""
Module pour trouver les écoles par sujet dans MongoDB
"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Retourne la liste des écoles ayant un sujet spécifique

    :param mongo_collection: Un objet collection PyMongo
    :param topic: Le sujet recherché
    :return: Liste des écoles ayant le sujet spécifié
    """
    return list(mongo_collection.find({"topics": topic}))
