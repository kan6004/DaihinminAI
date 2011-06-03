import mechanize
from urlparse import urlparse

class PlayerAPIHandler
    """
    Handler class for Daihinmin Player API.
    """
    URL_SUFFIX = {
        "login":"/login",
        "get_hand_json":"/operations/get_hand.json"
        "get_hand_xml":"/operations/get_hand.xml"
        "operation":"/operations"
    }

    def __init__(self, url, username, password, place_id, proxy_url=None, proxy_user=None, proxy_pass=None):
        self.url = url
        self.agent = mechanize.Browser()

        if proxy_url:
            protocol, host = self._parse_url(proxy_url)
            self.agent.set_proxies({protocol:host})
            if proxy_user and proxy_pass:
                self.agent.add_proxy_password(proxy_user, proxy_pass)

        # submit login form
        login_url = self.url + URL_SUFFIX["login"]
        self.agent.open(login_url)
        self.agent.select_form(nr=0)
        self.agent["name"] = username
        self.agent["password"] = password
        self.agent["place_id"] = place_id
        self.agent.submit()

    def get_hand(hand_format="json"):
        """
        Get hand information via Player API.
        Parsing hand (json or xml) is calling module's duty.
        """
        if hand_format == "json":
            get_hand_url = self.url + URL_SUFFIX["get_hand_json"]
            hand = self.agent.get_file(get_hand_url)
        elif hand_format == "xml":
            get_hand_url = self.url + URL_SUFFIX["get_hand_xml"]
            hand = self.agent.get_file(get_hand_url)
        else:
            raise ValueError("Hand format is invalid: %s" % hand_format)
        return hand

    def post_hand(cards):
        """
        Post hand information via Player API.
        """
        ope_url = self.url + URL_SUFFIX["operation"]
        self.agent.open(ope_url)
        self.agent.select_form(nr=0)
        # convert card information format
        self.agent.submit()

    def _parse_url(url):
        """
        Parse url and retuen tuple of ("protocol", "hostname:port")
        """
        parsed = urlparse(url)
        if parsed.scheme:
            protocol = parsed.scheme
        else:
            raise ValueError("Protocol is invalid: %s" % url)
        if parsed.hostname:
            hostname = parsed.hostname
        else:
            raise ValueError("Hostname is invalid: %s" % url)
        if parsed.port:
            port = parsed.port
        else:
            raise ValueError("Port number is invalid: %s" % url)
        return (protocol, hostname + ":" + port)

if __name__ == "__main__":
    p = PlayerAPIHandler("http://urari.dip.jp", "kannos", "1234", "1")
    print p.get_hand()

