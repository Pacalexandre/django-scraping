import urllib.request

x = urllib.request.urlopen('https://hideout.co/watch.php?v=444363&p=6740')
html = bytes.decode(x.read())
print(html)