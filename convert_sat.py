#!/usr/bin/env python

#-----------------------------------------------------------------------------
# 
# Name:			convert_sat.py
# Product:		SAT.SCR fixed length to CSV
# Version:		Version: 1.0.0 (August 16, 2010)
# Author:		Kevin Risden < compuwizard123@gmail.com >
# Copyright:		Copyright 2010, Kevin Risden
# Licence:		GPL
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
# 
#-----------------------------------------------------------------------------

"""SAT.SCR fixed length to CSV conversion utility

Usage: convert_sat.py [options] 

Options:
	-h
	--help
		Print this message and exit

	-i
	--input
		Pathname to the input file

	-o
	--output
		Pathname to the output directory

"""

import getopt
import os
import csv
import string
import sys

# Global Defaults
bool_convert_date = False

def read_input (str_opt_input):
    obj_input_filehandle = open(str_opt_input, 'r')
    list_input = obj_input_filehandle.read().splitlines()
    obj_input_filehandle.close()
    return list_input

def convert_date (str_date):
    if bool_convert_date:
        length = len(str_date)
        new_date = str_date[0:2] + "/" + str_date[2:4]
        if length == 4:
            return new_date
        elif length == 6:
            new_date = new_date + "/" + str_date[4:6]
            return new_date
    return str_date

def main():
    # Defaults
    str_opt_input = "SAT.SCR"
    str_opt_output = "SAT.csv"
    
    # Get arguments, if any
    try:
        list_opts, list_args = getopt.getopt(sys.argv[1:], 'io:hv', ['input=', 'output=', 'convert-dates', 'help'])
    except getopt.error, str_error:
        usage(1, str_error)
        
    # Process arguments
    for str_opt, str_arg in list_opts:
        if str_opt in ('-i', '--input'):
            str_opt_input = str_arg
        elif str_opt in ('-o', '--output'):
            str_opt_output = str_arg
        elif str_opt in ('--convert-dates'):
            global bool_convert_date
            bool_convert_date = True
        elif str_opt in ('-h', '--help'):
            usage(0)
                
    # Check input file
    if not os.path.exists(str_opt_input):
        print 'The input file could not be found.'
        sys.exit()
    
    writer = csv.writer(open(str_opt_output, 'wb'))
    category_titles = ["College Code", "Last Name", "First Name", "Middle Initial", "Sex", "Date of Birth", "Social Security Number", "Street Address", "City", "Street", "Zip Code + 4", "Residence Code", "Telephone Number", "HS Graduation Date", "SAT Test Date", "Sat Educational Level", "Critical Reading Score", "Math Score", "Writing Score", "Essay Subscore", "Multiple-Choice Subscore", "Subject Test Date", "Subject Educational Level", "Subject Test 1 Code", "Subject Test 1 Score", "Subject Test 2 Code", "Subject Test 2 Score", "Subject Test 3 Code", "Subject Test 3 Score"]
    writer.writerow(category_titles)

    # Read input file into a list
    list_input = read_input(str_opt_input)
                    
    # Read and convert each line
    for line in list_input:
        str_student = ''
        
        college_code = string.rstrip(line[0:6])
        last_name = string.rstrip(line[6:21])
        first_name = string.rstrip(line[21:33])
        middle_initial = string.rstrip(line[33:34])
        sex = string.rstrip(line[34:35])
        dob = convert_date(string.rstrip(line[35:41]))
        ssn = string.rstrip(line[41:50])
        street_address = string.rstrip(line[50:75])
        city = string.rstrip(line[75:90])
        state = string.rstrip(line[91:93])
        zip_code = string.rstrip(line[94:103])
        residence_code = string.rstrip(line[106:111])
        telephone = string.rstrip(line[116:126])
        hs_grad_date = convert_date(string.rstrip(line[126:130]))
        sat_test_date = convert_date(string.rstrip(line[139:143]))
        sat_educational_lvl = string.rstrip(line[143:144])
        critical_reading_score = string.rstrip(line[146:149])
        math_score = string.rstrip(line[149:152])
        writing_score = string.rstrip(line[152:155])
        essay_subscore = string.rstrip(line[155:157])
        multiple_choice_subscore = string.rstrip(line[157:159])
        sat_subject_test_date = convert_date(string.rstrip(line[259:263]))
        sat_subject_educational_lvl = string.rstrip(line[263:264])
        subject_test_1_code = string.rstrip(line[266:268])
        subject_test_1_score = string.rstrip(line[268:271])
        subject_test_2_code = string.rstrip(line[277:279])
        subject_test_2_score = string.rstrip(line[279:282])
        subject_test_3_code = string.rstrip(line[288:290])
        subject_test_3_score = string.rstrip(line[290:293])
        
        category_list = [college_code, last_name, first_name, middle_initial, sex, dob, ssn, street_address, city, state, zip_code, residence_code, telephone, hs_grad_date, sat_test_date, sat_educational_lvl, critical_reading_score, math_score, writing_score, essay_subscore, multiple_choice_subscore, sat_subject_test_date, sat_subject_educational_lvl, subject_test_1_code, subject_test_1_score, subject_test_2_code, subject_test_2_score, subject_test_3_code, subject_test_3_score]
        
        for category in category_list:
            str_student = str_student + ", " + category

        writer.writerow(category_list)


if __name__ == '__main__':
    main()
