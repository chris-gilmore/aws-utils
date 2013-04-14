#!/usr/bin/env python

import sys
import boto

def main():
    tag_Name = sys.argv[1]
    autoscale = boto.connect_autoscale()
    tags = autoscale.get_all_tags()
    for tag in tags:
        if tag.key == 'Name' and tag.value == tag_Name:
            print tag.resource_id

if __name__ == "__main__":
    main()
