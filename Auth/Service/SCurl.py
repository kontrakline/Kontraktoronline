class SCurl(object) :
    class SCurl(object):

        @classmethod
        def sendRequest(cls, request, url):
            contents = StringIO.StringIO()
            agent = pycurl.Curl()

            agent.setopt(pycurl.POST, True)
            agent.setopt(pycurl.WRITEFUNCTION, contents.write)
            agent.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
            agent.setopt(pycurl.POSTFIELDS, json.dumps(request))
            agent.setopt(pycurl.URL, url)
            agent.setopt(pycurl.VERBOSE, 0)
            agent.perform()

            # contents = StringIO.StringIO()
            # agent.setopt(pycurl.WRITEFUNCTION, contents.write)
            response = contents.getvalue()
            return response