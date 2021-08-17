#!/usr/bin/env python
"""This script prompts a user to enter a message to encode or decode
    using a classic Caeser shift substitution (3 letter shift)"""

import glob
from pathlib import Path
import re
from kaggle.api.kaggle_api_extended import KaggleApi


class Kaggle:
    """This script prompts a user to enter a message to encode or decode
        using a classic Caeser shift substitution (3 letter shift)"""

    def __init__(self):
        self.api = KaggleApi()
        self.api.authenticate()

    def create_dataset_dir(self, dataset, path):
        """ convert dataset in owner / dataset_name set and create directory structure

        usage: kaggle.create_dataset_dir(dataset="owner/dataset-name", path="./")

        Parameters
        ==========
        dataset:    the string identified of the dataset should be in format [owner]/[dataset-name]
        file_name:  the dataset configuration file
        path:       if defined, download to this location
        """

        split_ds = dataset.split("/")
        owner = split_ds[0]
        dataset_name = split_ds[1]

        path = re.sub('/$', '', path)
        path = str(path + "/" + owner + "/" + dataset_name)

        filepath = Path(path)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        return path

    def parse_size(self, human_readable_size="0B"):
        """ This Methode convert human readable File Size to bytes.
        Usage: parse_size(human_readable_size="1337 MB")
        """
        human_readable_size = human_readable_size.upper()
        units = {"B": 1, "KB": 2**10,
                 "MB": 2**20, "GB": 2**30, "TB": 2**40}

        if not re.match(r' ', human_readable_size):
            human_readable_size = re.sub(
                r'([KMGT]?B)', r' \1', human_readable_size)

        number, unit = [string.strip()
                        for string in human_readable_size.split()]

        return int(float(number)*units[unit])


class Datasets(Kaggle):
    """This script prompts a user to enter a message to encode or decode
        using a classic Caeser shift substitution (3 letter shift)"""

    def list_datasets(
        self, search="", tag_ids="", file_type="all", user="",
        mine=False, license_name="all", sort_by="hottest", min_size="0B",
        max_size="999TB", page=1
    ):
        """ return a list of datasets!

        usage: kaggle.list_datasets(
            search="Anything", file_type="json", license_name="gpl")

        Parameters
        ==========
        search:         Term(s) to search for (default is empty string)
        tag_ids:        Search for datasets that have specific tags. Tag list should be comma separated
        file_type:      Search for datasets with a specific file type.
                        Default is 'all'. Valid options are 'all', 'csv', 'sqlite', 'json', 'bigQuery'.
        user:           Find public datasets owned by a specific user or organization
        mine:           Display only my items (default is False) (Cannot specify both mine and a user)
        license_name:   Search for datasets with a specific license. Default is 'all'.
                        Valid options are 'all', 'cc', 'gpl', 'odb', 'other'
        sort_by:        Sort list results. Default is 'hottest'.
                        Valid options are 'hottest', 'votes', 'updated', 'active', 'published'
        max_size:       The maximum size of the Dataset to return (bytes)
        min_size:       The minimum size of the Dataset to return (bytes)
        page:           Page number for results paging (default is 1)
        """

        datasets_list = self.api.dataset_list(
            search=str(search), tag_ids=list(tag_ids), file_type=str(file_type), user=str(user),
            mine=bool(mine), license_name=str(license_name), sort_by=str(sort_by),
            min_size=self.parse_size(min_size), max_size=self.parse_size(max_size),
            page=int(page),
        )

        datasets_list = [str(i) for i in datasets_list]

        return datasets_list

    def list_dataset_files(self, dataset):
        """ list files for a dataset

        usage: kaggle.list_dataset_files(dataset="owner/dataset-name")

        Parameters
        ==========
        dataset:    the string identified of the dataset should be in format [owner]/[dataset-name]
        """

        dataset_file_list = self.api.dataset_list_files(str(dataset)).files

        if isinstance(dataset_file_list, list):
            return [str(i) for i in dataset_file_list]
        else:
            return []

    def get_dataset_files(self, dataset, path="."):
        """ download all files for a dataset

        usage: kaggle.get_dataset_files(
            dataset="owner/dataset-name", path="./", unzip=True)

        Parameters
        ==========
        dataset:    the string identified of the dataset should be in format [owner]/[dataset-name]
        path:       the path to download the dataset to
        """

        list_dataset = self.list_datasets(search=str(dataset))

        if len(list_dataset) == 1:
            dataset = str(list_dataset[0])

            path = self.create_dataset_dir(dataset=dataset, path=path)

            self.api.dataset_download_files(
                str(dataset), str(path), True, True, True)

            dl_lst = [str(i)
                      for i in glob.iglob(path + '**/**', recursive=True)]

            return dl_lst

    def get_dataset_file(self, dataset, file_name, path="."):
        """ download a single file for a dataset

        usage: kaggle.list_dataset_files(dataset="owner/dataset-name")

        Parameters
        ==========
        dataset:    the string identified of the dataset should be in format [owner]/[dataset-name]
        file_name:  the dataset configuration file
        path:       if defined, download to this location
        """

        path = self.create_dataset_dir(dataset=dataset, path=path)
        df_lst = self.list_dataset_files(dataset=dataset)

        if str(file_name) in df_lst:
            self.api.dataset_download_file(
                str(dataset), str(file_name), str(path), True, True)

            return file_name
