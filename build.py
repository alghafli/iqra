import subprocess
import os
import sys

package = 'iqra'

cwd = os.getcwd()
try:
    os.chdir('{}/docs'.format(package))
    subprocess.check_call(['make', 'html'])
except Exception as e:
    print('error while making docs:', e, file=sys.stderr)
finally:
    os.chdir(cwd)

try:
    doc_text = open('{}/__init__.py'.format(package)).read().split("'''", 2)[1]
    tutorial_text = f'''
    --------
    Tutorial
    --------
    Check out iqra tutorial at http://{package}.readthedocs.io/
    '''

    readme_text = doc_text.lstrip() # + tutorial_text

    with open('README.txt', 'w') as f:
        print(readme_text, file=f)
except Exception as e:
    print('error while writing README.txt:', e, file=sys.stderr)

subprocess.check_call(['python3', 'setup.py', 'sdist'])
