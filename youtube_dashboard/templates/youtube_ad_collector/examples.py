
dates = set()
with open('expl_data.tsv') as fl:
    reader = csv.DictReader(fl,delimiter='\t')
    for row in reader:
        print row
        dat = row['day'].split('/')
        dat = (int(dat[2]),int(dat[1])-1,int(dat[0]))
        dates.add(dat)


#first
import numpy as np
for date in sorted(dates):
    for tag in ["'Advertisers'","'Behavioral/Demographics'","'Interests'","'Likes'"]:
        keep = np.random.binomial(1,1/3.)
        if keep==0: continue
        print "[{}, new Date{}, new Date{},{}],".format(tag,date,date,"createCustomHTMLContent('https://upload.wikimedia.org/wikipedia/commons/2/28/Flag_of_the_USA.svg', 1, 2, 3)")


#second
import numpy as np
arr = ["'Advertisers'","'Behavioral/Demographics'","'Interests'","'Likes'"]
print "['Date', "+",".join(arr)+"],"
for date in sorted(dates):
    dat = [str(x) if  np.random.binomial(1,1/3.) else 'NaN' for x in np.arange(1,len(arr)+1).tolist()]
    new_dat = list()
    for d in dat: 
        new_dat.append(d)
        new_dat.append("createCustomReport(new Date{})".format(date))
    print "[new Date{},{}],".format(date,",".join(new_dat))
    

