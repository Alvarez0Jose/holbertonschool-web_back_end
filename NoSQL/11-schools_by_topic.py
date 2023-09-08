#!/usr/bin/env python3
"""
Module that returns a list of school
"""
import pymongo


def schools_by_topic(mongo_collection, topic: str) -> list:
    """
    Function that returns a list of schools
    """
    schools: list = []
    query = {"topics": topic}

    for school in mongo_collection.find(query):
        schools.append(school)

    return schools
