# Hint:  use Google to find python function
from datetime import datetime

datetime_converter = lambda x,y: datetime.strptime(x, y)
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

date_format = '%m-%d-%Y'
# d0 = datetime.strptime(date_start, date_format)
d0 = datetime_converter(date_start, date_format)
d1 = datetime_converter(date_stop, date_format)
difference = d1 - d0
print difference.days

####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_format = '%m%d%Y'
d0 = datetime_converter(date_start, date_format)
d1 = datetime_converter(date_stop, date_format)
difference = d1 - d0
print difference.days

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_format = '%d-%b-%Y'
d0 = datetime_converter(date_start, date_format)
d1 = datetime_converter(date_stop, date_format)
difference = d1 - d0
print difference.days
