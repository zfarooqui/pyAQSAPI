#
"""
Created on Tue Aug 18 14:14:19 2021

Python tool for EPA AQS-API 
by Zuber Farooqui, Ph.D.

"""

import requests
import json
import pandas as pd
import datetime

class getAQSAPI:
    """
    Refer Endpoint, Required Variables, and Optional Variables at 
    https://aqs.epa.gov/aqsweb/documents/data_api.html
    
    For List: Function get_list(*) will get the list from Endpoint in dataframe
        -------------------------------------------------------------
        Endpoint                            Variables required.* 
        -------------------------------------------------------------
        --: *Note: Not required variable(s) for an endpoint must be set to Empty =''
        
        list/states                         --
        list/countiesByState                state
        list/sitesByCounty                  state, county
        list/parametersByClass              class (from list/classes)
        list/classes                        --
        list/cbsas                          --
        list/pqaos                          --
        list/mas                            --
        -------------------------------------------------------------
        
    For Data: Function get_data(*) will get the data from Endpoint in dataframe
        -------------------------------------------------------------
        Endpoint                            Variables required.* 
        -------------------------------------------------------------
        --: *Note: Not required variable(s) for an endpoint must be set to Empty =''
        
        transactionsSample/bySite	        param, bdate, edate, state, county, site    (Optional: cbdate, cedate)
        transactionsSample/byCounty	        param, bdate, edate, state, county          (Optional: cbdate, cedate)
        transactionsSample/byState	        param, bdate, edate, state                  (Optional: cbdate, cedate)
        transactionsSample/byMA	            param, bdate, edate, ma
        
        sampleData/bySite	                param, bdate, edate, state, county, site    (Optional: cbdate, cedate)
        sampleData/byCounty	                param, bdate, edate, state, county          (Optional: cbdate, cedate)
        sampleData/byState	                param, bdate, edate, state                  (Optional: cbdate, cedate)
        sampleData/byCBSA	                param, bdate, edate, cbsa                   (Optional: cbdate, cedate)
        
        dailyData/bySite	                    param, bdate, edate, state, county, site    (Optional: cbdate, cedate)
        dailyData/byCounty	                param, bdate, edate, state, county          (Optional: cbdate, cedate)
        dailyData/byState	                param, bdate, edate, state                  (Optional: cbdate, cedate)
        dailyData/byCBSA	                    param, bdate, edate, cbsa                   (Optional: cbdate, cedate)
        
        annualData/bySite	                param, bdate, edate, state, county, site    (Optional: cbdate, cedate)
        annualData/byCounty	                param, bdate, edate, state, county          (Optional: cbdate, cedate)
        annualData/byState	                param, bdate, edate, state                  (Optional: cbdate, cedate)
        annualData/byCBSA	                param, bdate, edate, cbsa                   (Optional: cbdate, cedate)
    
        monitors/bySite	                    param, bdate, edate, state, county, site
        monitors/byCounty	                param, bdate, edate, state, county
        monitors/byState	                    param, bdate, edate, state
        monitors/byCBSA	                    param, bdate, edate, cbsa
        -------------------------------------------------------------
    """

    def __init__(self,email,key,endpoint):
        """
        The class constructor.
        """
        api_url='https://aqs.epa.gov/data/api/'
        
        self.email = email
        self.key = key
        self.endpoint = endpoint
        self.api_url = api_url
        self.stub = f'{self.endpoint}?email={self.email}&key={self.key}'
    
    def get_list(self,state_code,county_code,pc_code):
        """
        Gets a list of below endpoints and their associated codes that can be used to
        construct additional queries.
        """
        
        self.state  = state_code
        self.county = county_code
        self.pc     = pc_code
        
        # Setting URL
        url = self.api_url + self.stub
        if (len(str(self.state)) > 0):
            url += f'&state={self.state}'
        if (len(str(self.county)) > 0):
            url += f'&county={self.county}'
        if (len(str(self.pc)) > 0):
            url += f'&pc={self.pc}'
        
        response = requests.get(url)
        try:
            assert response.status_code == requests.codes.ok
            
            # Getting data
            json_data = json.loads(response.content)['Data']
            df = pd.DataFrame.from_records(json_data)
            
            # Status message
            json_header = json.loads(response.content)['Header']
            if (json_header[0]['status'] == 'Failed'):
                print('---: Job Status: %s; Error: %s :---' % (json_header[0]['status'],json_header[0]['error']))
            else:
                print('---: Job Status: %s; Rows: %s :---' % (json_header[0]['status'],json_header[0]['rows']))
            
            #
            return df

        except AssertionError:
            print('Bad URL!')
    
    def get_data(self,param_code,begin_date,end_date,cbegin_date,cend_date,state_code,county_code,site_code,ma_code,cbsa_code):
        """
        Gets data of endpoints based on associated codes
        
        More information in endpoints and variables can be found at __doc__.
        """
        
        self.param  = param_code
        self.state  = state_code
        self.county = county_code
        self.site   = site_code
        self.bdate  = begin_date
        self.edate  = end_date
        self.cbdate = cbegin_date
        self.cedate = cend_date
        self.ma     = ma_code
        self.cbsa   = cbsa_code

        # Setting URL
        search_params = ''
        if (len(str(self.param)) > 0):
            search_params = '&param='
            for p in param_code:
                search_params += str(p)
                search_params += ','
            search_params = search_params[:-1]
        if (len(str(self.state)) > 0):
            search_params += f'&state={self.state}'
        if (len(str(self.county)) > 0):
            search_params += f'&county={self.county}'
        if (len(str(self.cbsa)) > 0):
            search_params += f'&cbsa={self.cbsa}'
        if (len(str(self.ma)) > 0):
            search_params += f'&ma={self.ma}'
        if (len(str(self.bdate)) > 0):
            search_params += (f'&bdate={self.bdate}' + f'&edate={self.edate}') 
        if (len(str(self.cbdate)) > 0):
            search_params += (f'&cbdate={self.cbdate}' + f'&cedate={self.cedate}') 
        if (len(str(self.site)) > 0):    
            search_params += f'&site={self.site}'
        url = self.api_url + self.stub + search_params

        response = requests.get(url)
        try:
            assert response.status_code == requests.codes.ok
            #print(url)
            
            # Getting data
            json_data = json.loads(response.content)['Data']
            df = pd.DataFrame.from_records(json_data)
            
            # Including downlaod datetime
            datenow = datetime.datetime.now()
            datenow = datenow.strftime("%Y-%m-%d %H:%M:%S")
            df['download_datetime'] = datenow
            
            # Status message
            json_header = json.loads(response.content)['Header']
            if (json_header[0]['status'] == 'Failed'):
                print('---: Job Status: %s; Error: %s :---' % (json_header[0]['status'],json_header[0]['error']))
            else:
                print('---: Job Status: %s; Rows: %s :---' % (json_header[0]['status'],json_header[0]['rows']))
            
            #
            return df

        except AssertionError:
            print('Bad URL!')
