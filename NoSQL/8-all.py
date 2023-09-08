#!/usr/bin/env python3
"""
Module that lists all the documents in a collection
"""
import pymongo


def list_all(mongo_collection) -> list:
    """
    Fucntion that lists all documents
    """

    docs: list = []

    for documents in mongo_collection.find():
        docs.append(documents)

    return docs
