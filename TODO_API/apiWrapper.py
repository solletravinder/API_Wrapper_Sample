import requests, json
# from user_agent import generate_user_agent, generate_navigator

BASE_URL = "https://jsonplaceholder.typicode.com"
API_1 = "/todos"

class ApiWrapper:
    def __init__(self, session=None, user_agent="", header=None):
        self.session = session or self.create_session()
        self.user_agent = user_agent or self.get_user_agent()
        self.header = header or self.create_header()
    
    def create_header(self, username="", password="", clientId="", clientSecret=""):
        if username and password:
            self.header= {
                "username": username,
                "password": password,
                "User-Agent": self.user_agent
            }
        elif clientId and clientSecret:
            self.header= {
                "X-Authorization": f"{clientId}:{clientSecret}",
                "User-Agent": self.user_agent
            }
        else:
            self.header= {
                "Content-Type":"application/json",
                "User-Agent": self.user_agent
            }
        return self.header

    def __repr__(self):
        return f"API Wrapper for {id(self):x}"

    def get_particular_data(self, data_id):
        response = self.session.get(url=BASE_URL+API_1+"/"+str(data_id))
        return response.json()

    def post_data(self, data):
        self.create_header()
        response = self.session.post(url=BASE_URL+API_1, json=data,headers=self.header)
        return response.json()

    def put_data(self, data_id, data):
        self.create_header()
        response = self.session.put(url=BASE_URL+API_1+"/"+str(data_id), json=data,headers=self.header)
        return response.json()

    def patch_data(self, data_id, data):
        self.create_header()
        response = self.session.patch(url=BASE_URL+API_1+"/"+str(data_id), json=data,headers=self.header)
        return response.json()

    def delete_data(self, data_id):
        response = self.session.delete(url=BASE_URL+API_1+"/"+str(data_id))
        return response.json()

    def get_list_data(self):
        response = self.session.get(url=BASE_URL+API_1)
        return response.json()

    def create_session(self):
        return requests.Session()

    def get_user_agent(self):
        return "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"

        # generate_user_agent(os=("windows", "linux", "mac"))