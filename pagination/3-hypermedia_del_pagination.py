#!/usr/bin/env python3
"""
Delete Resisielent  Pagination module
"""
import csv
from typing import List, Dict
import math


class Server:
    """
    Server class that paginates a database of popular names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting positions
        """

        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Method that gets hyper index
        """

        result_dataset = []
        index_data = self.indexed_dataset()
        keys_list = list(index_data.keys())

        assert index + page_size < len(keys_list)
        assert index < len(keys_list)

        if index not in index_data:
            start_index = keys_list[index]
        else:
            start_index = index

        for i in range(start_index, start_index + page_size):
            if i not in index_data:
                result_dataset.append(index_data[keys_list[i]])
            else:
                result_dataset.append(index_data[i])

        next_index: int = index + page_size

        if index in keys_list:
            next_index
        else:
            next_index = keys_list[next_index]

        hyper_dict = {
            'index': index,
            'next_index': next_index,
            'page_size': len(result_dataset),
            'data': result_dataset}

        return hyper_dict
