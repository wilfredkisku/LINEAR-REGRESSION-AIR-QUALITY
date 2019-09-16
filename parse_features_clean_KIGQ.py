import csv

with open('KIGQ_clean_count.csv','r') as clean_data:
    csv_reader_1 = csv.reader(clean_data)
    next(csv_reader_1)
    with open('KIGQ_clean.csv','r') as consolidated_read:
        csv_reader_2 = csv.reader(consolidated_read)
        next(csv_reader_2)
        with open('consolidated_features_KIGQ_final.csv', 'a') as consolidated_write:
            csv_writer = csv.writer(consolidated_write)
            for row in csv_reader_1:
                if row[1]=='24':
                    count = 0
                    for line in csv_reader_2:
                        csv_writer.writerow(line)
                        count = count + 1
                        if count == 24:
                            break
                else:
                    count = 0
                    for line in csv_reader_2:
                        count = count + 1
                        if count == int(row[1]):
                            break
