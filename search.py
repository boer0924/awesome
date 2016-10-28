#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--boer', help='Just a test.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
    help='an integer for the count')
parser.add_argument('--sum', dest='account', action='store_const',
    const=sum, default=max, help='sum the integers(default: find the max)')

args = parser.parse_args()
print args.account(args.integers)
