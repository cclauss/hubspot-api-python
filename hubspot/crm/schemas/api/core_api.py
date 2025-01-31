# coding: utf-8

"""
    Schemas

    The CRM uses schemas to define how custom objects should store and represent information in the HubSpot CRM. Schemas define details about an object's type, properties, and associations. The schema can be uniquely identified by its **object type ID**.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.schemas.api_client import ApiClient
from hubspot.crm.schemas.exceptions import ApiTypeError, ApiValueError


class CoreApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, object_type, **kwargs):  # noqa: E501
        """Delete a schema  # noqa: E501

        Deletes a schema. Any existing records of this schema must be deleted **first**. Otherwise this call will fail.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive(object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: Fully qualified name or object type ID of your schema. (required)
        :param bool archived: Whether to return only results that have been archived.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.archive_with_http_info(object_type, **kwargs)  # noqa: E501

    def archive_with_http_info(self, object_type, **kwargs):  # noqa: E501
        """Delete a schema  # noqa: E501

        Deletes a schema. Any existing records of this schema must be deleted **first**. Otherwise this call will fail.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_with_http_info(object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: Fully qualified name or object type ID of your schema. (required)
        :param bool archived: Whether to return only results that have been archived.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["object_type", "archived"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method archive" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and ("object_type" not in local_var_params or local_var_params["object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "object_type" in local_var_params:
            path_params["objectType"] = local_var_params["object_type"]  # noqa: E501

        query_params = []
        if "archived" in local_var_params and local_var_params["archived"] is not None:  # noqa: E501
            query_params.append(("archived", local_var_params["archived"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/schemas/{objectType}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def archive_association(self, object_type, association_identifier, **kwargs):  # noqa: E501
        """Remove an association  # noqa: E501

        Removes an existing association from a schema.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_association(object_type, association_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: Fully qualified name or object type ID of your schema. (required)
        :param str association_identifier: Unique ID of the association to remove. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.archive_association_with_http_info(object_type, association_identifier, **kwargs)  # noqa: E501

    def archive_association_with_http_info(self, object_type, association_identifier, **kwargs):  # noqa: E501
        """Remove an association  # noqa: E501

        Removes an existing association from a schema.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_association_with_http_info(object_type, association_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: Fully qualified name or object type ID of your schema. (required)
        :param str association_identifier: Unique ID of the association to remove. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["object_type", "association_identifier"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method archive_association" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and ("object_type" not in local_var_params or local_var_params["object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `archive_association`")  # noqa: E501
        # verify the required parameter 'association_identifier' is set
        if self.api_client.client_side_validation and ("association_identifier" not in local_var_params or local_var_params["association_identifier"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `association_identifier` when calling `archive_association`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "object_type" in local_var_params:
            path_params["objectType"] = local_var_params["object_type"]  # noqa: E501
        if "association_identifier" in local_var_params:
            path_params["associationIdentifier"] = local_var_params["association_identifier"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/schemas/{objectType}/associations/{associationIdentifier}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def create(self, object_schema_egg, **kwargs):  # noqa: E501
        """Create a new schema  # noqa: E501

        Define a new object schema, along with custom properties and associations. The entire object schema, including its object type ID, properties, and associations will be returned in the response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(object_schema_egg, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ObjectSchemaEgg object_schema_egg: Object schema definition, including properties and associations. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ObjectSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.create_with_http_info(object_schema_egg, **kwargs)  # noqa: E501

    def create_with_http_info(self, object_schema_egg, **kwargs):  # noqa: E501
        """Create a new schema  # noqa: E501

        Define a new object schema, along with custom properties and associations. The entire object schema, including its object type ID, properties, and associations will be returned in the response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(object_schema_egg, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ObjectSchemaEgg object_schema_egg: Object schema definition, including properties and associations. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ObjectSchema, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["object_schema_egg"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method create" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'object_schema_egg' is set
        if self.api_client.client_side_validation and ("object_schema_egg" not in local_var_params or local_var_params["object_schema_egg"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_schema_egg` when calling `create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "object_schema_egg" in local_var_params:
            body_params = local_var_params["object_schema_egg"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/schemas",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ObjectSchema",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def create_association(self, object_type, association_definition_egg, **kwargs):  # noqa: E501
        """Create an association  # noqa: E501

        Defines a new association between the primary schema's object type and other object types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_association(object_type, association_definition_egg, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: Fully qualified name or object type ID of your schema. (required)
        :param AssociationDefinitionEgg association_definition_egg: Attributes that define the association. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AssociationDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.create_association_with_http_info(object_type, association_definition_egg, **kwargs)  # noqa: E501

    def create_association_with_http_info(self, object_type, association_definition_egg, **kwargs):  # noqa: E501
        """Create an association  # noqa: E501

        Defines a new association between the primary schema's object type and other object types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_association_with_http_info(object_type, association_definition_egg, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: Fully qualified name or object type ID of your schema. (required)
        :param AssociationDefinitionEgg association_definition_egg: Attributes that define the association. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AssociationDefinition, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["object_type", "association_definition_egg"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method create_association" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and ("object_type" not in local_var_params or local_var_params["object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `create_association`")  # noqa: E501
        # verify the required parameter 'association_definition_egg' is set
        if self.api_client.client_side_validation and ("association_definition_egg" not in local_var_params or local_var_params["association_definition_egg"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `association_definition_egg` when calling `create_association`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "object_type" in local_var_params:
            path_params["objectType"] = local_var_params["object_type"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "association_definition_egg" in local_var_params:
            body_params = local_var_params["association_definition_egg"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/schemas/{objectType}/associations",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="AssociationDefinition",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_all(self, **kwargs):  # noqa: E501
        """Get all schemas  # noqa: E501

        Returns all object schemas that have been defined for your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param bool archived: Whether to return only results that have been archived.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CollectionResponseObjectSchemaNoPaging
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_all_with_http_info(**kwargs)  # noqa: E501

    def get_all_with_http_info(self, **kwargs):  # noqa: E501
        """Get all schemas  # noqa: E501

        Returns all object schemas that have been defined for your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param bool archived: Whether to return only results that have been archived.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CollectionResponseObjectSchemaNoPaging, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["archived"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_all" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "archived" in local_var_params and local_var_params["archived"] is not None:  # noqa: E501
            query_params.append(("archived", local_var_params["archived"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/schemas",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="CollectionResponseObjectSchemaNoPaging",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_by_id(self, object_type, **kwargs):  # noqa: E501
        """Get an existing schema  # noqa: E501

        Returns an existing object schema.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id(object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: Fully qualified name or object type ID of your schema. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ObjectSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_by_id_with_http_info(object_type, **kwargs)  # noqa: E501

    def get_by_id_with_http_info(self, object_type, **kwargs):  # noqa: E501
        """Get an existing schema  # noqa: E501

        Returns an existing object schema.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id_with_http_info(object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: Fully qualified name or object type ID of your schema. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ObjectSchema, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["object_type"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_by_id" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and ("object_type" not in local_var_params or local_var_params["object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `get_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "object_type" in local_var_params:
            path_params["objectType"] = local_var_params["object_type"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/schemas/{objectType}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ObjectSchema",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update(self, object_type, object_type_definition_patch, **kwargs):  # noqa: E501
        """Update a schema  # noqa: E501

        Update the details for an existing object schema.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update(object_type, object_type_definition_patch, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: Fully qualified name or object type ID of your schema. (required)
        :param ObjectTypeDefinitionPatch object_type_definition_patch: Attributes to update in your schema. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ObjectTypeDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.update_with_http_info(object_type, object_type_definition_patch, **kwargs)  # noqa: E501

    def update_with_http_info(self, object_type, object_type_definition_patch, **kwargs):  # noqa: E501
        """Update a schema  # noqa: E501

        Update the details for an existing object schema.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_with_http_info(object_type, object_type_definition_patch, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: Fully qualified name or object type ID of your schema. (required)
        :param ObjectTypeDefinitionPatch object_type_definition_patch: Attributes to update in your schema. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ObjectTypeDefinition, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["object_type", "object_type_definition_patch"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method update" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and ("object_type" not in local_var_params or local_var_params["object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `update`")  # noqa: E501
        # verify the required parameter 'object_type_definition_patch' is set
        if self.api_client.client_side_validation and ("object_type_definition_patch" not in local_var_params or local_var_params["object_type_definition_patch"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type_definition_patch` when calling `update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "object_type" in local_var_params:
            path_params["objectType"] = local_var_params["object_type"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "object_type_definition_patch" in local_var_params:
            body_params = local_var_params["object_type_definition_patch"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/schemas/{objectType}",
            "PATCH",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ObjectTypeDefinition",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
