# Imports the Google Cloud client library
from google.cloud import datastore
import pdb
import shutil
import os
from jinja2 import FileSystemLoader, Environment

def render_from_template(directory, template_name, **kwargs):
    loader = FileSystemLoader(directory)
    env = Environment(loader=loader)
    template = env.get_template(template_name)
    return template.render(**kwargs)

# Delete the old comments directory (read clean every time)
try:
    shutil.rmtree('comments')
except:
    pass

# Instantiates a client
client = datastore.Client()
query = client.query(kind='Message')
all_data = list(query.fetch())

# grab the list of urls and map them to a filename
filenames = set(map(lambda x: x['url'], all_data))

def add_spaces_to_comment(msg):
    out = []
    for line in msg.split('\n'):
        out.append('    ' + line)
    return '\n'.join(out)

# recreate the comments folder
os.mkdir('comments')
for filename in filenames:
    jsonified_data = []
    counter = 0
    for msg in sorted(filter(lambda x: x['url'] == filename, all_data), key=lambda x: x['time']):
        if msg['approved']:
            counter += 1
            jsonified_data.append({
                'author': msg['author'],
                'count': counter,
                'msg': add_spaces_to_comment(msg['msg'])
            })
 
    # construct the file here
    to_write = render_from_template('.', 'comments_template.html', comments=jsonified_data)
    with open(os.path.join('comments', "{}.md".format(filename)), 'w') as f:
        f.write(to_write)
