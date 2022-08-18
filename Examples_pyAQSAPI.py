# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:14:19 2021

Example of Python tool pyAQSAPI 
by Zuber Farooqui, Ph.D.

"""
from pyAQSAPI import getAQSAPI

# Login Credentials: Key provided by EPA/AQS-API
email       ='***'
key         ='***' 

# L I S T  E X A M P L E S

# Getting State list
endpoint    ='list/states'
state_code  =''
county_code =''
pc_code     =''
aqs = getAQSAPI(email, key, endpoint)
list_states = aqs.get_list(state_code, county_code, pc_code)

# Getting County list in State
endpoint    ='list/countiesByState'
state_code  ='06'
county_code =''
pc_code     =''
aqs = getAQSAPI(email, key, endpoint)
list_county = aqs.get_list(state_code, county_code, pc_code)

# Getting CBSA list
endpoint    ='list/cbsas'
state_code  =''
county_code =''
pc_code     =''
aqs = getAQSAPI(email, key, endpoint)
list_cbsas = aqs.get_list(state_code, county_code, pc_code)

# Getting MA list
endpoint    ='list/mas'
state_code  =''
county_code =''
pc_code     =''
aqs = getAQSAPI(email, key, endpoint)
list_mas = aqs.get_list(state_code, county_code, pc_code)

# Getting PQAO list
endpoint    ='list/pqaos'
state_code  =''
county_code =''
pc_code     =''
aqs = getAQSAPI(email, key, endpoint)
list_pqaos = aqs.get_list(state_code, county_code, pc_code)

# Getting Sites list in County
endpoint    ='list/sitesByCounty'
state_code  ='06'
county_code ='037'
pc_code     =''
aqs = getAQSAPI(email, key, endpoint)
list_sites_county = aqs.get_list(state_code, county_code, pc_code)

# Getting Classes list
endpoint    ='list/classes'
state_code  =''
county_code =''
pc_code     =''
aqs = getAQSAPI(email, key, endpoint)
list_classes = aqs.get_list(state_code, county_code, pc_code)

# Getting Parameters list in a Class (from above class list) (Ex. CRITERIA)
endpoint    ='list/parametersByClass'
state_code  =''
county_code =''
pc_code     ='CRITERIA'
aqs = getAQSAPI(email, key, endpoint)
list_params_class = aqs.get_list(state_code, county_code, pc_code)

# D A T A  E X A M P L E S

# Transaction Sample Data by Site. For others refer pyAQSAPI.py
endpoint    ='transactionsSample/bySite'
cbsa_code   =''
ma_code     =''
state_code  ='06'
county_code ='025'
site_code   ='0005'
param_code  =[88390,88391,88392]
begin_date  =20191227 #YYYYMMDD format for ALL dates variables
end_date    =20191228
cbegin_date =''
cend_date   =''
aqs = getAQSAPI(email, key, endpoint)
trans_site  = aqs.get_data(param_code, begin_date, end_date, cbegin_date, cend_date, state_code, county_code, 
                          site_code, ma_code, cbsa_code)
