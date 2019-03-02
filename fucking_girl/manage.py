#!/usr/bin/env python
import os

from migrate.versioning.shell import main

if __name__ == '__main__':
    main(repository='migrations', debug='False', url=os.environ['DB_URL'])
