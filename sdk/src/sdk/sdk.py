"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .burger import Burger
from .order import Order
from .sdkconfiguration import SDKConfiguration
from sdk import utils

class SDK:
    r"""Apitizing Burger API: A simple API to manage burgers and orders
    This API is used to manage burgers and orders in a restaurant
    """
    burger: Burger
    r"""Operations related to burgers
    https://en.wikipedia.org/wiki/Hamburger - Burger external docs
    """
    order: Order
    r"""Operations related to orders"""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        if client is None:
            client = requests_http.Session()
        
        security_client = client
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security_client, server_url, server_idx)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.burger = Burger(self.sdk_configuration)
        self.order = Order(self.sdk_configuration)
    