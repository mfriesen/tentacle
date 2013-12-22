import StringIO
import sys

from tentacle.shared.screed import Screed

'''
Runs the funcrion and returns the output as text
'''
def run_fn(snippet):
    backup = sys.stdout
   
    try:
        sys.stdout = StringIO.StringIO()
        exec snippet
    
        out = sys.stdout.getvalue()
        sys.stdout.close()
    except Exception as e:
        out = str(e)
    finally:
        sys.stdout = backup
    
    return out
        
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