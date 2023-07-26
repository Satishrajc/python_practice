# The Proxy pattern provides a surrogate or placeholder for another object to control access 
# to it or add additional functionality. The proxy object acts as an intermediary between the 
# client and the real subject object, providing additional control or service without altering 
# the subject's interface.

# The key features of the Proxy pattern are:

# A Proxy class that implements the same interface as the real subject.
# A reference to the real subject that the proxy wraps.


class RealSubject:
    def request(self):
        print("RealSubject: Handling request")

class Proxy:
    def __init__(self):
        self._real_subject = RealSubject()

    def request(self):
        # Additional logic before or after forwarding the request to the real subject
        print("Proxy: Logging the request")
        self._real_subject.request()
        print("Proxy: Request handled")

# Usage
proxy = Proxy()
proxy.request()
