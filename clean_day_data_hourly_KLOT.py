import csv 

with open('KLOT_clean.csv','r') as source:
    
    csv_reader = csv.reader(source)
    next(csv_reader)

    with open('KLOT_clean_count.csv','a') as dest:
        csv_writer = csv.writer(dest)
        
        old_mm_dd = ''
        old_date = ''
        count = 1
        flag = False

        for line in csv_reader:
            new_mm_dd = line[0][5:]
            new_date = line[0]
            if new_mm_dd != old_mm_dd:
                if flag:
                    csv_writer.writerow([old_date,count])
                    flag = False
                count = 1
            else:
                count = count + 1
                flag = True
            old_mm_dd = new_mm_dd
            old_date = new_date

