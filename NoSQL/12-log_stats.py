#!/usr/bin/env python3
"""Script pour fournir des statistiques sur les logs Nginx stockés dans MongoDB"""

from pymongo import MongoClient


def log_stats():
    """Affiche les statistiques des logs Nginx"""
    client = MongoClient()
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")

if __name__ == "__main__":
    log_stats()