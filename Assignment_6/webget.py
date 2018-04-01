import os
import urllib.request as req
from urllib.parse import urlparse

def download(url, to=None):
    """Download a remote file specified by a URL to a
          local directory.

          :param url: str
              URL pointing to a remote file.

          :param to: str
              Local path, absolute or relative, with a filename
              to the file storing the contents of the remote file.
          """

    # TODO: Implement me!
    filename = os.path.basename(urlparse(url).path)
    if to:
        path = os.path.join(to, filename)
    else:
        path = os.path.join(".", filename)

    if not os.path.isfile(path):
        try:
            req.urlretrieve(url, path)
        except:
            opener = req.build_opener()
            opener.addheaders = [
            ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')]
            req.install_opener(opener)
            req.urlretrieve(url, path)
    return filename