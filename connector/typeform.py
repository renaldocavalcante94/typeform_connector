import requests
from connector.base import BaseAPI
import os

TYPEFORM_ACCESS_TOKEN = os.getenv('TYPEFORM_ACCESS_TOKEN')

class TypeformAPI(BaseAPI):
    base_url = "https://api.typeform.com/"
    token = TYPEFORM_ACCESS_TOKEN
    headers = {'Authorization': f"Bearer {TYPEFORM_ACCESS_TOKEN}"}

    def me(self):
        uri = self.base_url + "me"

        result = requests.get(uri,headers=self.headers)

        return result

    def list_forms(self,page_size=200,page=None):
        #TODO This must be capable of process more than 200 pages.
        uri = self.base_url + "forms"
        params = {'page_size':page_size}
        
        if page != None:
            params.update({'page':page})

        result = requests.get(uri,headers=self.headers,params=params)

        return result.json()

    def list_all_forms(self):
        result = self.list_forms()
        page_count = result['page_count']
        items = result['items']
        page = 1

        while int(page_count) > page:
            
            page += 1
            result = self.list_forms(page=page)
            page_count = result['page_count']
            items += result['items']

        return items


    def get_form(self,form_id):
        uri = self.base_url + f"forms/{form_id}"

        result = requests.get(uri,headers=self.headers)

        return result.json()


    def get_responses(self,form_id,page_size=1000,completed=True,before=None):
        uri = self.base_url + f"forms/{form_id}/responses"
        
        if before != None:
            params = {'page_size': page_size, 'completed': completed, 'before':before}             
        else:
            params = {'page_size': page_size, 'completed': completed}

        result = requests.get(uri,headers=self.headers,params=params)

        return result.json()


    def get_all_responses(self,form_id,completed=True):
        result = self.get_responses(form_id,completed=completed)
        page_count = result['page_count']
        items = result['items']

        while int(page_count) > 1:
            before_token = items[-1]['landing_id']

            result = self.get_responses(form_id,completed=completed,before=before_token)
            page_count = result['page_count']
            items += result['items']

        return items




        

