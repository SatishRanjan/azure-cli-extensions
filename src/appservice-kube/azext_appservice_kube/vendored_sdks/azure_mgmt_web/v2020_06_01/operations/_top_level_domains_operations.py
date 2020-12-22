# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class TopLevelDomainsOperations(object):
    """TopLevelDomainsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: API Version. Constant value: "2020-06-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-06-01"

        self.config = config

    def list(
            self, custom_headers=None, raw=False, **operation_config):
        """Get all top-level domains supported for registration.

        Description for Get all top-level domains supported for registration.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of TopLevelDomain
        :rtype:
         ~azure.mgmt.web.v2020_06_01.models.TopLevelDomainPaged[~azure.mgmt.web.v2020_06_01.models.TopLevelDomain]
        :raises:
         :class:`DefaultErrorResponseException<azure.mgmt.web.v2020_06_01.models.DefaultErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.DefaultErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.TopLevelDomainPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains'}

    def get(
            self, name, custom_headers=None, raw=False, **operation_config):
        """Get details of a top-level domain.

        Description for Get details of a top-level domain.

        :param name: Name of the top-level domain.
        :type name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: TopLevelDomain or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.web.v2020_06_01.models.TopLevelDomain or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`DefaultErrorResponseException<azure.mgmt.web.v2020_06_01.models.DefaultErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.DefaultErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('TopLevelDomain', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains/{name}'}

    def list_agreements(
            self, name, include_privacy=None, for_transfer=None, custom_headers=None, raw=False, **operation_config):
        """Gets all legal agreements that user needs to accept before purchasing a
        domain.

        Description for Gets all legal agreements that user needs to accept
        before purchasing a domain.

        :param name: Name of the top-level domain.
        :type name: str
        :param include_privacy: If <code>true</code>, then the list of
         agreements will include agreements for domain privacy as well;
         otherwise, <code>false</code>.
        :type include_privacy: bool
        :param for_transfer: If <code>true</code>, then the list of agreements
         will include agreements for domain transfer as well; otherwise,
         <code>false</code>.
        :type for_transfer: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of TldLegalAgreement
        :rtype:
         ~azure.mgmt.web.v2020_06_01.models.TldLegalAgreementPaged[~azure.mgmt.web.v2020_06_01.models.TldLegalAgreement]
        :raises:
         :class:`DefaultErrorResponseException<azure.mgmt.web.v2020_06_01.models.DefaultErrorResponseException>`
        """
        agreement_option = models.TopLevelDomainAgreementOption(include_privacy=include_privacy, for_transfer=for_transfer)

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_agreements.metadata['url']
                path_format_arguments = {
                    'name': self._serialize.url("name", name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct body
            body_content = self._serialize.body(agreement_option, 'TopLevelDomainAgreementOption')

            # Construct and send request
            request = self._client.post(url, query_parameters, header_parameters, body_content)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.DefaultErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.TldLegalAgreementPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_agreements.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains/{name}/listAgreements'}
