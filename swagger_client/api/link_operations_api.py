# coding: utf-8

"""
    DCNM Postman Collection

    # Cisco Datacenter Network Manager (DCNM) API Postman Collection  This repository contains the a Postman collection and environment variable file to leverage the REST API on DCNM.  This collection was tested and built using DCNM 11.5(1) within the DevNet Sandbox infrastructure.  As such, some variables will need to be reset if used outside of this testbed.  ## Cisco DCNM Background  DCNM is a network management platform for all NX-OS-centric network deployments.  DCNM has several different installation personas, including LAN Fabric (BGP-EVPN with VXLAN), LAN Management (classic layer-2/layer-3 architecture), IP Fabric for Media (IPFM) and storage networking (SAN), however this collection covers the LAN fabric deployment model supporting an EVPN-VXLAN fabric backed by Nexus 9000-series switching.  APIs for other personas, while potentially overlapping, are not covered as part of this collection.  ## Additional Resources - [DCNM Sandbox on DevNet](https://devnetsandbox.cisco.com/RM/Diagram/Index/4b6f511a-4d7c-4764-927b-0fc591a661c6?diagramType=Topology) - REST API documentation is available off-box [here](https://developer.cisco.com/docs/data-center-network-manager/11-5-1/) - REST API documentation also available directly on the DCNM at `http://DCNM.IP.ADDRESS/api-docs`  ## Covered APIs  - DCNM administration - L4-L7 service operations - Fabric, Network, Interface, VRF, and Link top-down operations - LAN credential management - Policy and Template operations - Physical switch roles and discovery  ## Notes about the included ENV variables  Prior to using any requests, please ensure you gather the token from your DCNM instance using the included API call `dcnm login - gather token`.  This call will log you into the DCNM (using credentials stored in the environment) and automatically store the key for use with every other request in the collection.  In order to keep the environment variables to a reasonable number, reuse was included.  While I made attempts to include commonly reused variables (fabric names, VRF names, etc), the variables may require a bit of context parsing to ensure the correct usage within a particular environment.  In some instances, variables are defined within the payload, but not inside of the environment file to discern that the specific variable should be replaced.  As a final note, for any API or payload referencing a device serial number -- please ensure correct serial numbers are inserted as appropriate.  _In some instances, Javascript tests have been included as part of the API request to populate another variable that would be used somewhere else in that folder of requests (VRF IDs, VLAN IDs, etc).  These can be overridden in the environment settings, but have been included for automated tasks (like using Runner)_  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class LinkOperationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def rest_control_links_fabrics_fabric_get(self, fabric, **kwargs):  # noqa: E501
        """get all links in fabric  # noqa: E501

        Gathers detailed information for all links within the fabric named within the URI  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_control_links_fabrics_fabric_get(fabric, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fabric: (required)
        :param str dcnm_token:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_control_links_fabrics_fabric_get_with_http_info(fabric, **kwargs)  # noqa: E501
        else:
            (data) = self.rest_control_links_fabrics_fabric_get_with_http_info(fabric, **kwargs)  # noqa: E501
            return data

    def rest_control_links_fabrics_fabric_get_with_http_info(self, fabric, **kwargs):  # noqa: E501
        """get all links in fabric  # noqa: E501

        Gathers detailed information for all links within the fabric named within the URI  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_control_links_fabrics_fabric_get_with_http_info(fabric, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fabric: (required)
        :param str dcnm_token:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fabric', 'dcnm_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_control_links_fabrics_fabric_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fabric' is set
        if ('fabric' not in params or
                params['fabric'] is None):
            raise ValueError("Missing the required parameter `fabric` when calling `rest_control_links_fabrics_fabric_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fabric' in params:
            path_params['fabric'] = params['fabric']  # noqa: E501

        query_params = []

        header_params = {}
        if 'dcnm_token' in params:
            header_params['dcnm-token'] = params['dcnm_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/control/links/fabrics/{fabric}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rest_control_links_get(self, **kwargs):  # noqa: E501
        """get all links  # noqa: E501

        Used to list all of the links within DCNM  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_control_links_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dcnm_token:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_control_links_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.rest_control_links_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def rest_control_links_get_with_http_info(self, **kwargs):  # noqa: E501
        """get all links  # noqa: E501

        Used to list all of the links within DCNM  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_control_links_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dcnm_token:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dcnm_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_control_links_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'dcnm_token' in params:
            header_params['dcnm-token'] = params['dcnm_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/control/links', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rest_control_links_linkuuid57500_delete(self, **kwargs):  # noqa: E501
        """delete link  # noqa: E501

        Deletes the link named by the UUID given in the URI  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_control_links_linkuuid57500_delete(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dcnm_token:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_control_links_linkuuid57500_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.rest_control_links_linkuuid57500_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def rest_control_links_linkuuid57500_delete_with_http_info(self, **kwargs):  # noqa: E501
        """delete link  # noqa: E501

        Deletes the link named by the UUID given in the URI  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_control_links_linkuuid57500_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dcnm_token:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dcnm_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_control_links_linkuuid57500_delete" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'dcnm_token' in params:
            header_params['dcnm-token'] = params['dcnm_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/control/links/LINK-UUID-57500', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rest_control_links_linkuuid57500_put(self, **kwargs):  # noqa: E501
        """modify link  # noqa: E501

        Modifies the parameters of an existing link through details given within the payload.  Payload can be retrieved from one of the `GET` operations listed within this folder  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_control_links_linkuuid57500_put(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :param str dcnm_token:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_control_links_linkuuid57500_put_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.rest_control_links_linkuuid57500_put_with_http_info(**kwargs)  # noqa: E501
            return data

    def rest_control_links_linkuuid57500_put_with_http_info(self, **kwargs):  # noqa: E501
        """modify link  # noqa: E501

        Modifies the parameters of an existing link through details given within the payload.  Payload can be retrieved from one of the `GET` operations listed within this folder  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_control_links_linkuuid57500_put_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :param str dcnm_token:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'dcnm_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_control_links_linkuuid57500_put" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'dcnm_token' in params:
            header_params['dcnm-token'] = params['dcnm_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/control/links/LINK-UUID-57500', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rest_control_links_linkuuid88310_get(self, **kwargs):  # noqa: E501
        """get link info by uuid  # noqa: E501

        Gathers the link details for a given link defined by the UUID within the URI  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_control_links_linkuuid88310_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dcnm_token:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_control_links_linkuuid88310_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.rest_control_links_linkuuid88310_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def rest_control_links_linkuuid88310_get_with_http_info(self, **kwargs):  # noqa: E501
        """get link info by uuid  # noqa: E501

        Gathers the link details for a given link defined by the UUID within the URI  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_control_links_linkuuid88310_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dcnm_token:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dcnm_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_control_links_linkuuid88310_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'dcnm_token' in params:
            header_params['dcnm-token'] = params['dcnm_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/rest/control/links/LINK-UUID-88310', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
