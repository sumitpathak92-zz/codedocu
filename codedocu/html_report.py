import os
import dominate
from dominate.tags import *
from __init__ import first



def main():
    doc = dominate.document(title='ALPS Code Documentation')
    module_name = 'Content Gap Analysis' #TODO fetch it dynamically
    print first()
    try:
        api_name = first()[2]
    except:
        api_name = 'Some Dummy Name'
    api_comment = ''
    print api_comment

    with doc.head:
        link(rel='stylesheet', href='style.css')
        script(type='text/javascript', src='script.js')

    with doc:
        with div():
            attr(id='header')
            p('ALPS Code Documentation - VERSION-0.4.5')
            p(module_name)
            br()

        with div():
            p(api_name) 
            p(api_comment)

        with div():
            attr(cls='body')
            p('Lorem Ipsum..')
    try:
        os.remove('/home/sumit/personal files/codedocu/codedocu/doc.html')
    except:
        print "no such file"
    with open('/home/sumit/personal files/codedocu/codedocu/doc.html', 'w+') as f:
        f.write(str(doc))
    print str(doc)

if __name__=='__main__':
    main()
