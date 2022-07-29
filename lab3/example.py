import requests
from jinja2 import Environment, FileSystemLoader
from pprint import PrettyPrinter

# disable warnings about self-signed certs
import urllib3
urllib3.disable_warnings()

CVP_IP = "192.168.0.5"
              
# USE YOUR CREDENTIALS
USERNAME = ''
PASSWORD = ''

if __name__ == '__main__':
    pp = PrettyPrinter()
    env = Environment(loader=FileSystemLoader("/home/coder/project/labfiles/day1/lab3/"))
    template = env.get_template("pretty.j2")

    with open('/home/coder/project/labfiles/day1/lab3/this.will.not.work.for.you') as infile:
        access_token = infile.read()

    s = requests.session(verify=False)
    s.verify = False
    s.cookies.set("access_token", access_token)

    r = s.get('https://{}/imageurl'.format(CVP_IP))
    response = r.json()
    
    r = s.get('https://{}/containerurl'.format(CVP_IP))
    response = r.json()

    # pass the data you collected above to your jinja tempalte
    print(template.render(kwargs=kwargs))