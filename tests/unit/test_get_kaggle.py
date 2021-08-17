#!/usr/bin/python3
"""This script prompts a user to enter a message to encode or decode
    using a classic Caeser shift substitution (3 letter shift)"""

from lib.sourcing_kaggle_datasets.sourcing.get_kaggle import Datasets

ds = Datasets()


def test_list_datasets():
    """ list files for a dataset

    usage: kaggle.list_dataset_files(dataset="owner/dataset-name")

    Parameters
    ==========
    dataset:    the string identified of the dataset should be in format [owner]/[dataset-name]
    """
    list_datasets = ds.list_datasets(search='Python')
    assert isinstance(list_datasets, list) is True
    return list_datasets


def test_list_dataset_files():
    """ list files for a dataset

    usage: kaggle.list_dataset_files(dataset="owner/dataset-name")

    Parameters
    ==========
    dataset:    the string identified of the dataset should be in format [owner]/[dataset-name]
    """
    list_datasets = ds.list_datasets(search='Python')
    list_dataset_files = ds.list_dataset_files(dataset=list_datasets[1])
    assert isinstance(list_dataset_files, list) is True
    return list_dataset_files


def test_get_dataset_files():
    """ list files for a dataset

    usage: kaggle.list_dataset_files(dataset="owner/dataset-name")

    Parameters
    ==========
    dataset:    the string identified of the dataset should be in format [owner]/[dataset-name]
    """

    list_datasets = ds.list_datasets(search='Python', max_size="100MB")
    list_dataset_files = ds.get_dataset_files(
        dataset=list_datasets[1], path="./data/")
    assert isinstance(list_dataset_files, list) is True


def test_get_dataset_file():
    """ list files for a dataset

    usage: kaggle.list_dataset_files(dataset="owner/dataset-name")

    Parameters
    ==========
    dataset:    the string identified of the dataset should be in format [owner]/[dataset-name]
    """

    list_datasets = ds.list_datasets(search='Python', max_size="10MB")

    list_dataset_files = ds.list_dataset_files(dataset=list_datasets[1])

    get_dataset_file = ds.get_dataset_file(
        dataset=list_datasets[1], file_name=list_dataset_files[0], path="./data/")
    assert isinstance(get_dataset_file, str) is True
