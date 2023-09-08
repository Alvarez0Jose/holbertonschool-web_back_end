#!/usr/bin/env python3
"""
Module that changes the topics of a school
doctument based on the names
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Function thata updates the topics
    """

    query: dict = {"name": name}

    mongo_collection.update_many(query, {"$set": {"topics": topics}})
