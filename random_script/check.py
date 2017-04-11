import urllib.request as urllib2
import urllib

def read_content():
    file = open(r'D:\web developer\files\curseword.txt')
    content = file.read()
    
    content_p = urllib.parse.quote(content)
    
    
    check(content_p)
    file.close()
def check(some_text):
    url = urllib2.urlopen('http://www.wdylike.appspot.com/?q=' + some_text)
    output = url.read().decode('utf-8')
    print(output)
    url.close()

    if output == 'true':
        print('Profane Sentence!')
    elif output == 'false':
        print('Good shit!')
    else:
        print('What the fuck is this!')

    
read_content()
