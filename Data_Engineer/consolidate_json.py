import json 
import os 
import pandas 
import numpy 
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file,'r') as f:
        data = js