#! /usr/bin/env python3
"""
Deploy all scripts to:
/home/[username]/Scripts/bin/deployed
"""

import os
from pathlib import Path

HOME_PATH = "/home/"
DEPLOY_PATH = "Scripts/bin/deployed"
def deploy():
    """
    Deploys scripts to destination folder.
    """

# TODO get the username of the current user
    cwd = Path(os.getcwd())
    print(cwd)
    # src_path = cwd + "/src"
    # category_dirs = os.listdir(src_path)
    # for category_dir in category_dirs:
    #     script_folder = src_path "/" + category_dir + "/"
    ...


def main():
    """
    main function
    """
    deploy()
    ...


if __name__ == '__main__':
    main()
    ...
