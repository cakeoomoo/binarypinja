#!/usr/bin/python3

import pandas as pd
import os.path
from pinja.color.color import *

class CsvImprivement:

    KEYWORD1 = "call"
    IMPROVEMENT_STR1 = "call 0x0"
    extension = ".csv"
    new_tailname_extension = "_TRANS.csv"
    new_file_name = ""

    def create_improvement_csv(self, input_csv_file_path):

        input_csv = pd.read_csv(input_csv_file_path)
        output_data_list = []
        output_data_frame = None

        for row in input_csv.itertuples():

            output_row_list = []

            for i in range(len(row)):
                if self.KEYWORD1 in str(row[i]):

                    output_row_list.append(self.IMPROVEMENT_STR1)

                else:
                    output_row_list.append(row[i])

            output_data_list.append(output_row_list)

        output_data_frame = pd.DataFrame(output_data_list)

        self.create_csv_file_name(input_csv_file_path)

        temp_newfilename = self.new_file_name + self.new_tailname_extension

        output_data_frame.to_csv(temp_newfilename)
        print_green('OUTPUT >>>>>>>>  {} '.format(temp_newfilename))

    def create_csv_file_name(self, input_csv_file_path):
        name, ext = os.path.splitext(input_csv_file_path)
        self.new_file_name = name

