# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

import msrest.serialization

from ._storage_cache_management_client_enums import *


class ApiOperation(msrest.serialization.Model):
    """REST API operation description: see https://github.com/Azure/azure-rest-api-specs/blob/master/documentation/openapi-authoring-automated-guidelines.md#r3023-operationsapiimplementation.

    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.storagecache.models.ApiOperationDisplay
    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    """

    _attribute_map = {
        'display': {'key': 'display', 'type': 'ApiOperationDisplay'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        display: Optional["ApiOperationDisplay"] = None,
        name: Optional[str] = None,
        **kwargs
    ):
        super(ApiOperation, self).__init__(**kwargs)
        self.display = display
        self.name = name


class ApiOperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    :param provider: Service provider: Microsoft.StorageCache.
    :type provider: str
    :param resource: Resource on which the operation is performed: Cache, etc.
    :type resource: str
    """

    _attribute_map = {
        'operation': {'key': 'operation', 'type': 'str'},
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        operation: Optional[str] = None,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        **kwargs
    ):
        super(ApiOperationDisplay, self).__init__(**kwargs)
        self.operation = operation
        self.provider = provider
        self.resource = resource


class ApiOperationListResult(msrest.serialization.Model):
    """Result of the request to list Resource Provider operations. It contains a list of operations and a URL link to get the next set of results.

    :param next_link: URL to get the next set of operation list results if there are any.
    :type next_link: str
    :param value: List of Resource Provider operations supported by the Microsoft.StorageCache
     resource provider.
    :type value: list[~azure.mgmt.storagecache.models.ApiOperation]
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[ApiOperation]'},
    }

    def __init__(
        self,
        *,
        next_link: Optional[str] = None,
        value: Optional[List["ApiOperation"]] = None,
        **kwargs
    ):
        super(ApiOperationListResult, self).__init__(**kwargs)
        self.next_link = next_link
        self.value = value


class Cache(msrest.serialization.Model):
    """A Cache instance. Follows Azure Resource Manager standards: https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/resource-api-reference.md.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param tags: A set of tags. ARM tags as name/value pairs.
    :type tags: object
    :ivar id: Resource ID of the Cache.
    :vartype id: str
    :param location: Region name string.
    :type location: str
    :ivar name: Name of Cache.
    :vartype name: str
    :ivar type: Type of the Cache; Microsoft.StorageCache/Cache.
    :vartype type: str
    :param sku: SKU for the Cache.
    :type sku: ~azure.mgmt.storagecache.models.CacheSku
    :param cache_size_gb: The size of this Cache, in GB.
    :type cache_size_gb: int
    :ivar health: Health of the Cache.
    :vartype health: ~azure.mgmt.storagecache.models.CacheHealth
    :ivar mount_addresses: Array of IP addresses that can be used by clients mounting this Cache.
    :vartype mount_addresses: list[str]
    :param provisioning_state: ARM provisioning state, see https://github.com/Azure/azure-resource-
     manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property. Possible values include:
     "Succeeded", "Failed", "Cancelled", "Creating", "Deleting", "Updating".
    :type provisioning_state: str or ~azure.mgmt.storagecache.models.ProvisioningStateType
    :param subnet: Subnet used for the Cache.
    :type subnet: str
    :param upgrade_status: Upgrade status of the Cache.
    :type upgrade_status: ~azure.mgmt.storagecache.models.CacheUpgradeStatus
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True, 'pattern': r'^[-0-9a-zA-Z_]{1,80}$'},
        'type': {'readonly': True},
        'health': {'readonly': True},
        'mount_addresses': {'readonly': True},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'CacheSku'},
        'cache_size_gb': {'key': 'properties.cacheSizeGB', 'type': 'int'},
        'health': {'key': 'properties.health', 'type': 'CacheHealth'},
        'mount_addresses': {'key': 'properties.mountAddresses', 'type': '[str]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'subnet': {'key': 'properties.subnet', 'type': 'str'},
        'upgrade_status': {'key': 'properties.upgradeStatus', 'type': 'CacheUpgradeStatus'},
    }

    def __init__(
        self,
        *,
        tags: Optional[object] = None,
        location: Optional[str] = None,
        sku: Optional["CacheSku"] = None,
        cache_size_gb: Optional[int] = None,
        provisioning_state: Optional[Union[str, "ProvisioningStateType"]] = None,
        subnet: Optional[str] = None,
        upgrade_status: Optional["CacheUpgradeStatus"] = None,
        **kwargs
    ):
        super(Cache, self).__init__(**kwargs)
        self.tags = tags
        self.id = None
        self.location = location
        self.name = None
        self.type = None
        self.sku = sku
        self.cache_size_gb = cache_size_gb
        self.health = None
        self.mount_addresses = None
        self.provisioning_state = provisioning_state
        self.subnet = subnet
        self.upgrade_status = upgrade_status


class CacheHealth(msrest.serialization.Model):
    """An indication of Cache health. Gives more information about health than just that related to provisioning.

    :param state: List of Cache health states. Possible values include: "Unknown", "Healthy",
     "Degraded", "Down", "Transitioning", "Stopping", "Stopped", "Upgrading", "Flushing".
    :type state: str or ~azure.mgmt.storagecache.models.HealthStateType
    :param status_description: Describes explanation of state.
    :type status_description: str
    """

    _attribute_map = {
        'state': {'key': 'state', 'type': 'str'},
        'status_description': {'key': 'statusDescription', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        state: Optional[Union[str, "HealthStateType"]] = None,
        status_description: Optional[str] = None,
        **kwargs
    ):
        super(CacheHealth, self).__init__(**kwargs)
        self.state = state
        self.status_description = status_description


class CacheSku(msrest.serialization.Model):
    """SKU for the Cache.

    :param name: SKU name for this Cache.
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        **kwargs
    ):
        super(CacheSku, self).__init__(**kwargs)
        self.name = name


class CachesListResult(msrest.serialization.Model):
    """Result of the request to list Caches. It contains a list of Caches and a URL link to get the next set of results.

    :param next_link: URL to get the next set of Cache list results, if there are any.
    :type next_link: str
    :param value: List of Caches.
    :type value: list[~azure.mgmt.storagecache.models.Cache]
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[Cache]'},
    }

    def __init__(
        self,
        *,
        next_link: Optional[str] = None,
        value: Optional[List["Cache"]] = None,
        **kwargs
    ):
        super(CachesListResult, self).__init__(**kwargs)
        self.next_link = next_link
        self.value = value


class CacheUpgradeStatus(msrest.serialization.Model):
    """Properties describing the software upgrade state of the Cache.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar current_firmware_version: Version string of the firmware currently installed on this
     Cache.
    :vartype current_firmware_version: str
    :ivar firmware_update_status: True if there is a firmware update ready to install on this
     Cache. The firmware will automatically be installed after firmwareUpdateDeadline if not
     triggered earlier via the upgrade operation. Possible values include: "available",
     "unavailable".
    :vartype firmware_update_status: str or ~azure.mgmt.storagecache.models.FirmwareStatusType
    :ivar firmware_update_deadline: Time at which the pending firmware update will automatically be
     installed on the Cache.
    :vartype firmware_update_deadline: ~datetime.datetime
    :ivar last_firmware_update: Time of the last successful firmware update.
    :vartype last_firmware_update: ~datetime.datetime
    :ivar pending_firmware_version: When firmwareUpdateAvailable is true, this field holds the
     version string for the update.
    :vartype pending_firmware_version: str
    """

    _validation = {
        'current_firmware_version': {'readonly': True},
        'firmware_update_status': {'readonly': True},
        'firmware_update_deadline': {'readonly': True},
        'last_firmware_update': {'readonly': True},
        'pending_firmware_version': {'readonly': True},
    }

    _attribute_map = {
        'current_firmware_version': {'key': 'currentFirmwareVersion', 'type': 'str'},
        'firmware_update_status': {'key': 'firmwareUpdateStatus', 'type': 'str'},
        'firmware_update_deadline': {'key': 'firmwareUpdateDeadline', 'type': 'iso-8601'},
        'last_firmware_update': {'key': 'lastFirmwareUpdate', 'type': 'iso-8601'},
        'pending_firmware_version': {'key': 'pendingFirmwareVersion', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CacheUpgradeStatus, self).__init__(**kwargs)
        self.current_firmware_version = None
        self.firmware_update_status = None
        self.firmware_update_deadline = None
        self.last_firmware_update = None
        self.pending_firmware_version = None


class ClfsTarget(msrest.serialization.Model):
    """Storage container for use as a CLFS Storage Target.

    :param target: Resource ID of storage container.
    :type target: str
    """

    _attribute_map = {
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        target: Optional[str] = None,
        **kwargs
    ):
        super(ClfsTarget, self).__init__(**kwargs)
        self.target = target


class CloudErrorBody(msrest.serialization.Model):
    """An error response.

    :param code: An identifier for the error. Codes are invariant and are intended to be consumed
     programmatically.
    :type code: str
    :param details: A list of additional details about the error.
    :type details: list[~azure.mgmt.storagecache.models.CloudErrorBody]
    :param message: A message describing the error, intended to be suitable for display in a user
     interface.
    :type message: str
    :param target: The target of the particular error. For example, the name of the property in
     error.
    :type target: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CloudErrorBody]'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        details: Optional[List["CloudErrorBody"]] = None,
        message: Optional[str] = None,
        target: Optional[str] = None,
        **kwargs
    ):
        super(CloudErrorBody, self).__init__(**kwargs)
        self.code = code
        self.details = details
        self.message = message
        self.target = target


class NamespaceJunction(msrest.serialization.Model):
    """A namespace junction.

    :param namespace_path: Namespace path on a Cache for a Storage Target.
    :type namespace_path: str
    :param target_path: Path in Storage Target to which namespacePath points.
    :type target_path: str
    :param nfs_export: NFS export where targetPath exists.
    :type nfs_export: str
    """

    _attribute_map = {
        'namespace_path': {'key': 'namespacePath', 'type': 'str'},
        'target_path': {'key': 'targetPath', 'type': 'str'},
        'nfs_export': {'key': 'nfsExport', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        namespace_path: Optional[str] = None,
        target_path: Optional[str] = None,
        nfs_export: Optional[str] = None,
        **kwargs
    ):
        super(NamespaceJunction, self).__init__(**kwargs)
        self.namespace_path = namespace_path
        self.target_path = target_path
        self.nfs_export = nfs_export


class Nfs3Target(msrest.serialization.Model):
    """An NFSv3 mount point for use as a Storage Target.

    :param target: IP address or host name of an NFSv3 host (e.g., 10.0.44.44).
    :type target: str
    :param usage_model: Identifies the primary usage model to be used for this Storage Target. Get
     choices from .../usageModels.
    :type usage_model: str
    """

    _validation = {
        'target': {'pattern': r'^[-.0-9a-zA-Z]+$'},
    }

    _attribute_map = {
        'target': {'key': 'target', 'type': 'str'},
        'usage_model': {'key': 'usageModel', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        target: Optional[str] = None,
        usage_model: Optional[str] = None,
        **kwargs
    ):
        super(Nfs3Target, self).__init__(**kwargs)
        self.target = target
        self.usage_model = usage_model


class ResourceSku(msrest.serialization.Model):
    """A resource SKU.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar resource_type: The type of resource the SKU applies to.
    :vartype resource_type: str
    :param capabilities: A list of capabilities of this SKU, such as throughput or ops/sec.
    :type capabilities: list[~azure.mgmt.storagecache.models.ResourceSkuCapabilities]
    :ivar locations: The set of locations that the SKU is available. This will be supported and
     registered Azure Geo Regions (e.g., West US, East US, Southeast Asia, etc.).
    :vartype locations: list[str]
    :param location_info: The set of locations that the SKU is available.
    :type location_info: list[~azure.mgmt.storagecache.models.ResourceSkuLocationInfo]
    :param name: The name of this SKU.
    :type name: str
    :param restrictions: The restrictions preventing this SKU from being used. This is empty if
     there are no restrictions.
    :type restrictions: list[~azure.mgmt.storagecache.models.Restriction]
    """

    _validation = {
        'resource_type': {'readonly': True},
        'locations': {'readonly': True},
    }

    _attribute_map = {
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'capabilities': {'key': 'capabilities', 'type': '[ResourceSkuCapabilities]'},
        'locations': {'key': 'locations', 'type': '[str]'},
        'location_info': {'key': 'locationInfo', 'type': '[ResourceSkuLocationInfo]'},
        'name': {'key': 'name', 'type': 'str'},
        'restrictions': {'key': 'restrictions', 'type': '[Restriction]'},
    }

    def __init__(
        self,
        *,
        capabilities: Optional[List["ResourceSkuCapabilities"]] = None,
        location_info: Optional[List["ResourceSkuLocationInfo"]] = None,
        name: Optional[str] = None,
        restrictions: Optional[List["Restriction"]] = None,
        **kwargs
    ):
        super(ResourceSku, self).__init__(**kwargs)
        self.resource_type = None
        self.capabilities = capabilities
        self.locations = None
        self.location_info = location_info
        self.name = name
        self.restrictions = restrictions


class ResourceSkuCapabilities(msrest.serialization.Model):
    """A resource SKU capability.

    :param name: Name of a capability, such as ops/sec.
    :type name: str
    :param value: Quantity, if the capability is measured by quantity.
    :type value: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        value: Optional[str] = None,
        **kwargs
    ):
        super(ResourceSkuCapabilities, self).__init__(**kwargs)
        self.name = name
        self.value = value


class ResourceSkuLocationInfo(msrest.serialization.Model):
    """Resource SKU location information.

    :param location: Location where this SKU is available.
    :type location: str
    :param zones: Zones if any.
    :type zones: list[str]
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'zones': {'key': 'zones', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        zones: Optional[List[str]] = None,
        **kwargs
    ):
        super(ResourceSkuLocationInfo, self).__init__(**kwargs)
        self.location = location
        self.zones = zones


class ResourceSkusResult(msrest.serialization.Model):
    """The response from the List Cache SKUs operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param next_link: The URI to fetch the next page of Cache SKUs.
    :type next_link: str
    :ivar value: The list of SKUs available for the subscription.
    :vartype value: list[~azure.mgmt.storagecache.models.ResourceSku]
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[ResourceSku]'},
    }

    def __init__(
        self,
        *,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ResourceSkusResult, self).__init__(**kwargs)
        self.next_link = next_link
        self.value = None


class Restriction(msrest.serialization.Model):
    """The restrictions preventing this SKU from being used.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The type of restrictions. In this version, the only possible value for this is
     location.
    :vartype type: str
    :ivar values: The value of restrictions. If the restriction type is set to location, then this
     would be the different locations where the SKU is restricted.
    :vartype values: list[str]
    :param reason_code: The reason for the restriction. As of now this can be "QuotaId" or
     "NotAvailableForSubscription". "QuotaId" is set when the SKU has requiredQuotas parameter as
     the subscription does not belong to that quota. "NotAvailableForSubscription" is related to
     capacity at the datacenter. Possible values include: "QuotaId", "NotAvailableForSubscription".
    :type reason_code: str or ~azure.mgmt.storagecache.models.ReasonCode
    """

    _validation = {
        'type': {'readonly': True},
        'values': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'values': {'key': 'values', 'type': '[str]'},
        'reason_code': {'key': 'reasonCode', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        reason_code: Optional[Union[str, "ReasonCode"]] = None,
        **kwargs
    ):
        super(Restriction, self).__init__(**kwargs)
        self.type = None
        self.values = None
        self.reason_code = reason_code


class StorageTarget(msrest.serialization.Model):
    """A storage system being cached by a Cache.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Name of the Storage Target.
    :vartype name: str
    :ivar id: Resource ID of the Storage Target.
    :vartype id: str
    :ivar type: Type of the Storage Target; Microsoft.StorageCache/Cache/StorageTarget.
    :vartype type: str
    :param junctions: List of Cache namespace junctions to target for namespace associations.
    :type junctions: list[~azure.mgmt.storagecache.models.NamespaceJunction]
    :param target_type: Type of the Storage Target. Possible values include: "nfs3", "clfs",
     "unknown".
    :type target_type: str or ~azure.mgmt.storagecache.models.StorageTargetType
    :param provisioning_state: ARM provisioning state, see https://github.com/Azure/azure-resource-
     manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property. Possible values include:
     "Succeeded", "Failed", "Cancelled", "Creating", "Deleting", "Updating".
    :type provisioning_state: str or ~azure.mgmt.storagecache.models.ProvisioningStateType
    :param nfs3: Properties when targetType is nfs3.
    :type nfs3: ~azure.mgmt.storagecache.models.Nfs3Target
    :param clfs: Properties when targetType is clfs.
    :type clfs: ~azure.mgmt.storagecache.models.ClfsTarget
    :param unknown: Properties when targetType is unknown.
    :type unknown: ~azure.mgmt.storagecache.models.UnknownTarget
    """

    _validation = {
        'name': {'readonly': True, 'pattern': r'^[-0-9a-zA-Z_]{1,80}$'},
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'junctions': {'key': 'properties.junctions', 'type': '[NamespaceJunction]'},
        'target_type': {'key': 'properties.targetType', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'nfs3': {'key': 'properties.nfs3', 'type': 'Nfs3Target'},
        'clfs': {'key': 'properties.clfs', 'type': 'ClfsTarget'},
        'unknown': {'key': 'properties.unknown', 'type': 'UnknownTarget'},
    }

    def __init__(
        self,
        *,
        junctions: Optional[List["NamespaceJunction"]] = None,
        target_type: Optional[Union[str, "StorageTargetType"]] = None,
        provisioning_state: Optional[Union[str, "ProvisioningStateType"]] = None,
        nfs3: Optional["Nfs3Target"] = None,
        clfs: Optional["ClfsTarget"] = None,
        unknown: Optional["UnknownTarget"] = None,
        **kwargs
    ):
        super(StorageTarget, self).__init__(**kwargs)
        self.name = None
        self.id = None
        self.type = None
        self.junctions = junctions
        self.target_type = target_type
        self.provisioning_state = provisioning_state
        self.nfs3 = nfs3
        self.clfs = clfs
        self.unknown = unknown


class StorageTargetsResult(msrest.serialization.Model):
    """A list of Storage Targets.

    :param next_link: The URI to fetch the next page of Storage Targets.
    :type next_link: str
    :param value: The list of Storage Targets defined for the Cache.
    :type value: list[~azure.mgmt.storagecache.models.StorageTarget]
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[StorageTarget]'},
    }

    def __init__(
        self,
        *,
        next_link: Optional[str] = None,
        value: Optional[List["StorageTarget"]] = None,
        **kwargs
    ):
        super(StorageTargetsResult, self).__init__(**kwargs)
        self.next_link = next_link
        self.value = value


class UnknownTarget(msrest.serialization.Model):
    """Storage container for use as an Unknown Storage Target.

    :param unknown_map: Dictionary of string->string pairs containing information about the Storage
     Target.
    :type unknown_map: dict[str, str]
    """

    _attribute_map = {
        'unknown_map': {'key': 'unknownMap', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        unknown_map: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(UnknownTarget, self).__init__(**kwargs)
        self.unknown_map = unknown_map


class UsageModel(msrest.serialization.Model):
    """A usage model.

    :param display: Localized information describing this usage model.
    :type display: ~azure.mgmt.storagecache.models.UsageModelDisplay
    :param model_name: Non-localized keyword name for this usage model.
    :type model_name: str
    :param target_type: The type of Storage Target to which this model is applicable (only nfs3 as
     of this version).
    :type target_type: str
    """

    _attribute_map = {
        'display': {'key': 'display', 'type': 'UsageModelDisplay'},
        'model_name': {'key': 'modelName', 'type': 'str'},
        'target_type': {'key': 'targetType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        display: Optional["UsageModelDisplay"] = None,
        model_name: Optional[str] = None,
        target_type: Optional[str] = None,
        **kwargs
    ):
        super(UsageModel, self).__init__(**kwargs)
        self.display = display
        self.model_name = model_name
        self.target_type = target_type


class UsageModelDisplay(msrest.serialization.Model):
    """Localized information describing this usage model.

    :param description: String to display for this usage model.
    :type description: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        description: Optional[str] = None,
        **kwargs
    ):
        super(UsageModelDisplay, self).__init__(**kwargs)
        self.description = description


class UsageModelsResult(msrest.serialization.Model):
    """A list of Cache usage models.

    :param next_link: The URI to fetch the next page of Cache usage models.
    :type next_link: str
    :param value: The list of usage models available for the subscription.
    :type value: list[~azure.mgmt.storagecache.models.UsageModel]
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[UsageModel]'},
    }

    def __init__(
        self,
        *,
        next_link: Optional[str] = None,
        value: Optional[List["UsageModel"]] = None,
        **kwargs
    ):
        super(UsageModelsResult, self).__init__(**kwargs)
        self.next_link = next_link
        self.value = value
