import re

t=re.match(r'^/crm/(.*?\..*?)/$','/crm/index/house_type_list.html/').group(1)
print t