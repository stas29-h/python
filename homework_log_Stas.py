import csv

syslog = "C:\\Users\\halaimov.stanislav\\Desktop\\PythonWorkshop\\syslog"

final_results = list()

with open(syslog, 'r', encoding= 'utf8') as f:
    rich_text = f.readlines()

for line in rich_text:
    if 'INFO kernel:' in line:
       split_lines = line.split('INFO kernel:')
       time_list = split_lines[0].split(',')
       final_results.append([time_list[0], split_lines[1]])

with open('C:\\Users\\halaimov.stanislav\\Documents\\results_log_Stas.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Message'])
    writer.writerows(final_results)
