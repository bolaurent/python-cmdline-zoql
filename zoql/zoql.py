# -*- coding: utf-8 -*-


__version__ = "0.1.0-dev"



"""zoql.zoql: provides entry point main().

A command line loop that interprets Zuora Object Query Language

Results are either displayed on the console or pushed to Excel 

If a query includes a period in the field names, the zuora data export query feature is used;
you can query any of the datasources defined by Zuora.

"""

import os
import sys
import argparse
import getpass

import csv
import json
from cmd2 import Cmd


from zuora_restful_python.zuora import Zuora



def zuora_object_keys(zoura_object):
    if zoura_object:
        return zoura_object.keys()


class Interpreter(Cmd):

    zuora_connection = None
    excel = False

    prompt = "zoql> "
    intro = "Enter zuora queries (terminated with semicolon)!"
    multilineCommands = ['select']
    sheet_number = 0


    def do_select(self, line):
        try:
            if '.' in line:
                csv_data = self.zuora_connection.query_export('select ' + line).split('\n')
                records = [record for record in csv.DictReader(csv_data)]
            else:
                records = self.zuora_connection.query_all('select ' + line)
            self.dump_records(records)
        except Exception as ex:
            print('Error: q', repr(ex))

    def do_q(self, line):
        return self.do_eof(line)

    def do_eof(self, line):
        return True

    def dump_to_excel(self, records):
        zoql_dataframe = pd.DataFrame(records)

        zoql_sheet = wb.sheets.add('zoql{}'.format(self.sheet_number if self.sheet_number else ''))
        self.sheet_number += 1
        zoql_sheet.range('A1').value = zoql_dataframe

    def dump_to_stdout(self, records):
        first_record = records[0]
        keys = [key for key in zuora_object_keys(first_record) if first_record[key]]

        print(','.join(keys))

        for record in records:
            print(','.join(str(record[key]) for key in keys))

        print(len(records), 'records')


    def dump_records(self, records):
        if records:
            if Interpreter.excel:
                self.dump_to_excel(records)
            else:
                self.dump_to_stdout(records)


def main():
    parser = argparse.ArgumentParser(description='Interpret Zuora zoql queries')
    parser.add_argument('--excel', action="store_true", default=False)
    parser.add_argument('--sandbox', action="store_true", default=False)
    parser.add_argument("-u", "--user", type=str)
    args = parser.parse_args()

    sys.argv = sys.argv[0:1]

    if args.sandbox:
        zuora_instance = 'sandbox'
        Interpreter.prompt = 'zoql (sandbox)> '
        ZUORA_CONFIGFILE = os.path.expanduser('~') + '/.zuora-sandbox-config.json'
    else:
        zuora_instance = 'production'
        ZUORA_CONFIGFILE = os.path.expanduser('~') + '/.zuora-production-config.json'

    if args.user:
        zuora_config = {}
        zuora_config['password'] = getpass.getpass('password:')
        zuora_config['user'] = args.user
        
    else:
        with open(ZUORA_CONFIGFILE, 'r') as f:
            zuora_config = json.load(f)

    Interpreter.zuora_connection = Zuora(zuora_config['user'], zuora_config['password'], zuora_instance)

    if args.excel:
        Interpreter.excel = True
        import pandas as pd
        import xlwings as xw
        wb = xw.Book()


    Interpreter().cmdloop()
