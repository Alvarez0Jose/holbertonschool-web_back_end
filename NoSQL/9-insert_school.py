#!/usr/bin/env python3
"""
Module that inserts a new document
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Function that adds the document
    """

    new_school = mongo_collection.insert_one(kwargs)

    return new_school.inserted_id
