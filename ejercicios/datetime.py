# -*- coding: utf-8 -*-
from datetime import datetime
myDate = datetime.now()
formatedDate = myDate.strftime("%d-%m-%Y %H:%M")
print str(datetime.now())
print str(formatedDate)