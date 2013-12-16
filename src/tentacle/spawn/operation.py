import sys
import StringIO
import contextlib

from tentacle.shared.screed import Screed

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

'''
Runs the funcrion and returns the output as text
'''
def run_fn(snippet):
    
    with stdoutIO() as s:
        exec snippet    
    return s.getvalue()
        
'''
Processes all the steps of the screed
'''
def run_screed(screed_json):
    
    screed = Screed()
    screed.load(screed_json)
        
    for idx, step in enumerate(screed.steps()):
        for key in step:
            text = run_fn(step[key])
            screed.add_fn(idx, key, text)
    
    return screed.to_json()