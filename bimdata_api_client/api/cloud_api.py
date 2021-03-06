# coding: utf-8

"""
    BIMData API

    BIMData API documentation  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@bimdata.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from bimdata_api_client.api_client import ApiClient


class CloudApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_cloud_user(self, cloud_pk, data, **kwargs):  # noqa: E501
        """create_cloud_user  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_cloud_user(cloud_pk, data, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cloud_pk: (required)
        :param FosUserWrite data: (required)
        :return: FosUserWrite
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_cloud_user_with_http_info(cloud_pk, data, **kwargs)  # noqa: E501
        else:
            (data) = self.create_cloud_user_with_http_info(cloud_pk, data, **kwargs)  # noqa: E501
            return data

    def create_cloud_user_with_http_info(self, cloud_pk, data, **kwargs):  # noqa: E501
        """create_cloud_user  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_cloud_user_with_http_info(cloud_pk, data, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cloud_pk: (required)
        :param FosUserWrite data: (required)
        :return: FosUserWrite
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cloud_pk', 'data']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_cloud_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_pk' is set
        if ('cloud_pk' not in params or
                params['cloud_pk'] is None):
            raise ValueError("Missing the required parameter `cloud_pk` when calling `create_cloud_user`")  # noqa: E501
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `create_cloud_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_pk' in params:
            path_params['cloud_pk'] = params['cloud_pk']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/cloud/{cloud_pk}/user', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FosUserWrite',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_cloud_user(self, id, cloud_pk, **kwargs):  # noqa: E501
        """delete_cloud_user  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_cloud_user(id, cloud_pk, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param str cloud_pk: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_cloud_user_with_http_info(id, cloud_pk, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_cloud_user_with_http_info(id, cloud_pk, **kwargs)  # noqa: E501
            return data

    def delete_cloud_user_with_http_info(self, id, cloud_pk, **kwargs):  # noqa: E501
        """delete_cloud_user  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_cloud_user_with_http_info(id, cloud_pk, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param str cloud_pk: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cloud_pk']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_cloud_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_cloud_user`")  # noqa: E501
        # verify the required parameter 'cloud_pk' is set
        if ('cloud_pk' not in params or
                params['cloud_pk'] is None):
            raise ValueError("Missing the required parameter `cloud_pk` when calling `delete_cloud_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'cloud_pk' in params:
            path_params['cloud_pk'] = params['cloud_pk']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/cloud/{cloud_pk}/user/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def full_update_cloud_user(self, id, cloud_pk, data, **kwargs):  # noqa: E501
        """full_update_cloud_user  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.full_update_cloud_user(id, cloud_pk, data, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param str cloud_pk: (required)
        :param FosUserWrite data: (required)
        :return: FosUserWrite
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.full_update_cloud_user_with_http_info(id, cloud_pk, data, **kwargs)  # noqa: E501
        else:
            (data) = self.full_update_cloud_user_with_http_info(id, cloud_pk, data, **kwargs)  # noqa: E501
            return data

    def full_update_cloud_user_with_http_info(self, id, cloud_pk, data, **kwargs):  # noqa: E501
        """full_update_cloud_user  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.full_update_cloud_user_with_http_info(id, cloud_pk, data, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param str cloud_pk: (required)
        :param FosUserWrite data: (required)
        :return: FosUserWrite
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cloud_pk', 'data']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method full_update_cloud_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `full_update_cloud_user`")  # noqa: E501
        # verify the required parameter 'cloud_pk' is set
        if ('cloud_pk' not in params or
                params['cloud_pk'] is None):
            raise ValueError("Missing the required parameter `cloud_pk` when calling `full_update_cloud_user`")  # noqa: E501
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `full_update_cloud_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'cloud_pk' in params:
            path_params['cloud_pk'] = params['cloud_pk']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/cloud/{cloud_pk}/user/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FosUserWrite',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cloud(self, id, **kwargs):  # noqa: E501
        """get_cloud  # noqa: E501

        Returns user and his cloud role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cloud(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :return: Cloud
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_cloud_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cloud_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_cloud_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_cloud  # noqa: E501

        Returns user and his cloud role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cloud_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :return: Cloud
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cloud" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_cloud`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/cloud/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Cloud',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cloud_size(self, id, **kwargs):  # noqa: E501
        """get_cloud_size  # noqa: E501

        Returns the size of the cloud in Bytes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cloud_size(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_cloud_size_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cloud_size_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_cloud_size_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_cloud_size  # noqa: E501

        Returns the size of the cloud in Bytes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cloud_size_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cloud_size" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_cloud_size`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/cloud/{id}/size', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cloud_user(self, id, cloud_pk, **kwargs):  # noqa: E501
        """get_cloud_user  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cloud_user(id, cloud_pk, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param str cloud_pk: (required)
        :return: FosUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_cloud_user_with_http_info(id, cloud_pk, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cloud_user_with_http_info(id, cloud_pk, **kwargs)  # noqa: E501
            return data

    def get_cloud_user_with_http_info(self, id, cloud_pk, **kwargs):  # noqa: E501
        """get_cloud_user  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cloud_user_with_http_info(id, cloud_pk, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param str cloud_pk: (required)
        :return: FosUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cloud_pk']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cloud_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_cloud_user`")  # noqa: E501
        # verify the required parameter 'cloud_pk' is set
        if ('cloud_pk' not in params or
                params['cloud_pk'] is None):
            raise ValueError("Missing the required parameter `cloud_pk` when calling `get_cloud_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'cloud_pk' in params:
            path_params['cloud_pk'] = params['cloud_pk']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/cloud/{cloud_pk}/user/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FosUser',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cloud_users(self, cloud_pk, **kwargs):  # noqa: E501
        """get_cloud_users  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cloud_users(cloud_pk, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cloud_pk: (required)
        :return: list[FosUser]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_cloud_users_with_http_info(cloud_pk, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cloud_users_with_http_info(cloud_pk, **kwargs)  # noqa: E501
            return data

    def get_cloud_users_with_http_info(self, cloud_pk, **kwargs):  # noqa: E501
        """get_cloud_users  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cloud_users_with_http_info(cloud_pk, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cloud_pk: (required)
        :return: list[FosUser]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cloud_pk']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cloud_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_pk' is set
        if ('cloud_pk' not in params or
                params['cloud_pk'] is None):
            raise ValueError("Missing the required parameter `cloud_pk` when calling `get_cloud_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_pk' in params:
            path_params['cloud_pk'] = params['cloud_pk']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/cloud/{cloud_pk}/user', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[FosUser]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_clouds(self, **kwargs):  # noqa: E501
        """get_clouds  # noqa: E501

        Returns user's cloud only  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_clouds(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[Cloud]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_clouds_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_clouds_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_clouds_with_http_info(self, **kwargs):  # noqa: E501
        """get_clouds  # noqa: E501

        Returns user's cloud only  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_clouds_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[Cloud]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_clouds" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/cloud', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Cloud]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_cloud_user(self, id, cloud_pk, data, **kwargs):  # noqa: E501
        """update_cloud_user  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_cloud_user(id, cloud_pk, data, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param str cloud_pk: (required)
        :param FosUserWrite data: (required)
        :return: FosUserWrite
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_cloud_user_with_http_info(id, cloud_pk, data, **kwargs)  # noqa: E501
        else:
            (data) = self.update_cloud_user_with_http_info(id, cloud_pk, data, **kwargs)  # noqa: E501
            return data

    def update_cloud_user_with_http_info(self, id, cloud_pk, data, **kwargs):  # noqa: E501
        """update_cloud_user  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_cloud_user_with_http_info(id, cloud_pk, data, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param str cloud_pk: (required)
        :param FosUserWrite data: (required)
        :return: FosUserWrite
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cloud_pk', 'data']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_cloud_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_cloud_user`")  # noqa: E501
        # verify the required parameter 'cloud_pk' is set
        if ('cloud_pk' not in params or
                params['cloud_pk'] is None):
            raise ValueError("Missing the required parameter `cloud_pk` when calling `update_cloud_user`")  # noqa: E501
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `update_cloud_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'cloud_pk' in params:
            path_params['cloud_pk'] = params['cloud_pk']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/cloud/{cloud_pk}/user/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FosUserWrite',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
