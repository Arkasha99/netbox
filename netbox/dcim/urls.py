from django.urls import path

from extras.views import ObjectChangeLogView, ImageAttachmentEditView
from ipam.views import ServiceCreateView
from secrets.views import secret_add
from . import views
from .models import (
    Cable, ConsolePort, ConsoleServerPort, Device, DeviceRole, DeviceType, FrontPort, Interface, Manufacturer, Platform,
    PowerFeed, PowerPanel, PowerPort, PowerOutlet, Rack, RackGroup, RackReservation, RackRole, RearPort, Region, Site,
    VirtualChassis,
)

app_name = 'dcim'
urlpatterns = [

    # Regions
    path('regions/', views.RegionListView.as_view(), name='region_list'),
    path('regions/add/', views.RegionCreateView.as_view(), name='region_add'),
    path('regions/import/', views.RegionBulkImportView.as_view(), name='region_import'),
    path('regions/delete/', views.RegionBulkDeleteView.as_view(), name='region_bulk_delete'),
    path('regions/<int:pk>/edit/', views.RegionEditView.as_view(), name='region_edit'),
    path('regions/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='region_changelog', kwargs={'model': Region}),

    # Sites
    path('sites/', views.SiteListView.as_view(), name='site_list'),
    path('sites/add/', views.SiteCreateView.as_view(), name='site_add'),
    path('sites/import/', views.SiteBulkImportView.as_view(), name='site_import'),
    path('sites/edit/', views.SiteBulkEditView.as_view(), name='site_bulk_edit'),
    path('sites/delete/', views.SiteBulkDeleteView.as_view(), name='site_bulk_delete'),
    path('sites/<slug:slug>/', views.SiteView.as_view(), name='site'),
    path('sites/<slug:slug>/edit/', views.SiteEditView.as_view(), name='site_edit'),
    path('sites/<slug:slug>/delete/', views.SiteDeleteView.as_view(), name='site_delete'),
    path('sites/<slug:slug>/changelog/', ObjectChangeLogView.as_view(), name='site_changelog', kwargs={'model': Site}),
    path('sites/<int:object_id>/images/add/', ImageAttachmentEditView.as_view(), name='site_add_image', kwargs={'model': Site}),

    # Rack groups
    path('rack-groups/', views.RackGroupListView.as_view(), name='rackgroup_list'),
    path('rack-groups/add/', views.RackGroupCreateView.as_view(), name='rackgroup_add'),
    path('rack-groups/import/', views.RackGroupBulkImportView.as_view(), name='rackgroup_import'),
    path('rack-groups/delete/', views.RackGroupBulkDeleteView.as_view(), name='rackgroup_bulk_delete'),
    path('rack-groups/<int:pk>/edit/', views.RackGroupEditView.as_view(), name='rackgroup_edit'),
    path('rack-groups/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='rackgroup_changelog', kwargs={'model': RackGroup}),

    # Rack roles
    path('rack-roles/', views.RackRoleListView.as_view(), name='rackrole_list'),
    path('rack-roles/add/', views.RackRoleCreateView.as_view(), name='rackrole_add'),
    path('rack-roles/import/', views.RackRoleBulkImportView.as_view(), name='rackrole_import'),
    path('rack-roles/delete/', views.RackRoleBulkDeleteView.as_view(), name='rackrole_bulk_delete'),
    path('rack-roles/<int:pk>/edit/', views.RackRoleEditView.as_view(), name='rackrole_edit'),
    path('rack-roles/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='rackrole_changelog', kwargs={'model': RackRole}),

    # Rack reservations
    path('rack-reservations/', views.RackReservationListView.as_view(), name='rackreservation_list'),
    path('rack-reservations/edit/', views.RackReservationBulkEditView.as_view(), name='rackreservation_bulk_edit'),
    path('rack-reservations/delete/', views.RackReservationBulkDeleteView.as_view(), name='rackreservation_bulk_delete'),
    path('rack-reservations/<int:pk>/edit/', views.RackReservationEditView.as_view(), name='rackreservation_edit'),
    path('rack-reservations/<int:pk>/delete/', views.RackReservationDeleteView.as_view(), name='rackreservation_delete'),
    path('rack-reservations/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='rackreservation_changelog', kwargs={'model': RackReservation}),

    # Racks
    path('racks/', views.RackListView.as_view(), name='rack_list'),
    path('rack-elevations/', views.RackElevationListView.as_view(), name='rack_elevation_list'),
    path('racks/add/', views.RackCreateView.as_view(), name='rack_add'),
    path('racks/import/', views.RackBulkImportView.as_view(), name='rack_import'),
    path('racks/edit/', views.RackBulkEditView.as_view(), name='rack_bulk_edit'),
    path('racks/delete/', views.RackBulkDeleteView.as_view(), name='rack_bulk_delete'),
    path('racks/<int:pk>/', views.RackView.as_view(), name='rack'),
    path('racks/<int:pk>/edit/', views.RackEditView.as_view(), name='rack_edit'),
    path('racks/<int:pk>/delete/', views.RackDeleteView.as_view(), name='rack_delete'),
    path('racks/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='rack_changelog', kwargs={'model': Rack}),
    path('racks/<int:rack>/reservations/add/', views.RackReservationCreateView.as_view(), name='rack_add_reservation'),
    path('racks/<int:object_id>/images/add/', ImageAttachmentEditView.as_view(), name='rack_add_image', kwargs={'model': Rack}),

    # Manufacturers
    path('manufacturers/', views.ManufacturerListView.as_view(), name='manufacturer_list'),
    path('manufacturers/add/', views.ManufacturerCreateView.as_view(), name='manufacturer_add'),
    path('manufacturers/import/', views.ManufacturerBulkImportView.as_view(), name='manufacturer_import'),
    path('manufacturers/delete/', views.ManufacturerBulkDeleteView.as_view(), name='manufacturer_bulk_delete'),
    path('manufacturers/<slug:slug>/edit/', views.ManufacturerEditView.as_view(), name='manufacturer_edit'),
    path('manufacturers/<slug:slug>/changelog/', ObjectChangeLogView.as_view(), name='manufacturer_changelog', kwargs={'model': Manufacturer}),

    # Device types
    path('device-types/', views.DeviceTypeListView.as_view(), name='devicetype_list'),
    path('device-types/add/', views.DeviceTypeCreateView.as_view(), name='devicetype_add'),
    path('device-types/import/', views.DeviceTypeImportView.as_view(), name='devicetype_import'),
    path('device-types/edit/', views.DeviceTypeBulkEditView.as_view(), name='devicetype_bulk_edit'),
    path('device-types/delete/', views.DeviceTypeBulkDeleteView.as_view(), name='devicetype_bulk_delete'),
    path('device-types/<int:pk>/', views.DeviceTypeView.as_view(), name='devicetype'),
    path('device-types/<int:pk>/edit/', views.DeviceTypeEditView.as_view(), name='devicetype_edit'),
    path('device-types/<int:pk>/delete/', views.DeviceTypeDeleteView.as_view(), name='devicetype_delete'),
    path('device-types/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='devicetype_changelog', kwargs={'model': DeviceType}),

    # Console port templates
    path('device-types/<int:pk>/console-ports/add/', views.ConsolePortTemplateCreateView.as_view(), name='devicetype_add_consoleport'),
    path('device-types/<int:pk>/console-ports/delete/', views.ConsolePortTemplateBulkDeleteView.as_view(), name='devicetype_delete_consoleport'),
    path('console-port-templates/<int:pk>/edit/', views.ConsolePortTemplateEditView.as_view(), name='consoleporttemplate_edit'),

    # Console server port templates
    path('device-types/<int:pk>/console-server-ports/add/', views.ConsoleServerPortTemplateCreateView.as_view(), name='devicetype_add_consoleserverport'),
    path('device-types/<int:pk>/console-server-ports/delete/', views.ConsoleServerPortTemplateBulkDeleteView.as_view(), name='devicetype_delete_consoleserverport'),
    path('console-server-port-templates/<int:pk>/edit/', views.ConsoleServerPortTemplateEditView.as_view(), name='consoleserverporttemplate_edit'),

    # Power port templates
    path('device-types/<int:pk>/power-ports/add/', views.PowerPortTemplateCreateView.as_view(), name='devicetype_add_powerport'),
    path('device-types/<int:pk>/power-ports/delete/', views.PowerPortTemplateBulkDeleteView.as_view(), name='devicetype_delete_powerport'),
    path('power-port-templates/<int:pk>/edit/', views.PowerPortTemplateEditView.as_view(), name='powerporttemplate_edit'),

    # Power outlet templates
    path('device-types/<int:pk>/power-outlets/add/', views.PowerOutletTemplateCreateView.as_view(), name='devicetype_add_poweroutlet'),
    path('device-types/<int:pk>/power-outlets/delete/', views.PowerOutletTemplateBulkDeleteView.as_view(), name='devicetype_delete_poweroutlet'),
    path('power-outlet-templates/<int:pk>/edit/', views.PowerOutletTemplateEditView.as_view(), name='poweroutlettemplate_edit'),

    # Interface templates
    path('device-types/<int:pk>/interfaces/add/', views.InterfaceTemplateCreateView.as_view(), name='devicetype_add_interface'),
    path('device-types/<int:pk>/interfaces/edit/', views.InterfaceTemplateBulkEditView.as_view(), name='devicetype_bulkedit_interface'),
    path('device-types/<int:pk>/interfaces/delete/', views.InterfaceTemplateBulkDeleteView.as_view(), name='devicetype_delete_interface'),
    path('interface-templates/<int:pk>/edit/', views.InterfaceTemplateEditView.as_view(), name='interfacetemplate_edit'),

    # Front port templates
    path('device-types/<int:pk>/front-ports/add/', views.FrontPortTemplateCreateView.as_view(), name='devicetype_add_frontport'),
    path('device-types/<int:pk>/front-ports/delete/', views.FrontPortTemplateBulkDeleteView.as_view(), name='devicetype_delete_frontport'),
    path('front-port-templates/<int:pk>/edit/', views.FrontPortTemplateEditView.as_view(), name='frontporttemplate_edit'),

    # Rear port templates
    path('device-types/<int:pk>/rear-ports/add/', views.RearPortTemplateCreateView.as_view(), name='devicetype_add_rearport'),
    path('device-types/<int:pk>/rear-ports/delete/', views.RearPortTemplateBulkDeleteView.as_view(), name='devicetype_delete_rearport'),
    path('rear-port-templates/<int:pk>/edit/', views.RearPortTemplateEditView.as_view(), name='rearporttemplate_edit'),

    # Device bay templates
    path('device-types/<int:pk>/device-bays/add/', views.DeviceBayTemplateCreateView.as_view(), name='devicetype_add_devicebay'),
    path('device-types/<int:pk>/device-bays/delete/', views.DeviceBayTemplateBulkDeleteView.as_view(), name='devicetype_delete_devicebay'),
    path('device-bay-templates/<int:pk>/edit/', views.DeviceBayTemplateEditView.as_view(), name='devicebaytemplate_edit'),

    # Device roles
    path('device-roles/', views.DeviceRoleListView.as_view(), name='devicerole_list'),
    path('device-roles/add/', views.DeviceRoleCreateView.as_view(), name='devicerole_add'),
    path('device-roles/import/', views.DeviceRoleBulkImportView.as_view(), name='devicerole_import'),
    path('device-roles/delete/', views.DeviceRoleBulkDeleteView.as_view(), name='devicerole_bulk_delete'),
    path('device-roles/<slug:slug>/edit/', views.DeviceRoleEditView.as_view(), name='devicerole_edit'),
    path('device-roles/<slug:slug>/changelog/', ObjectChangeLogView.as_view(), name='devicerole_changelog', kwargs={'model': DeviceRole}),

    # Platforms
    path('platforms/', views.PlatformListView.as_view(), name='platform_list'),
    path('platforms/add/', views.PlatformCreateView.as_view(), name='platform_add'),
    path('platforms/import/', views.PlatformBulkImportView.as_view(), name='platform_import'),
    path('platforms/delete/', views.PlatformBulkDeleteView.as_view(), name='platform_bulk_delete'),
    path('platforms/<slug:slug>/edit/', views.PlatformEditView.as_view(), name='platform_edit'),
    path('platforms/<slug:slug>/changelog/', ObjectChangeLogView.as_view(), name='platform_changelog', kwargs={'model': Platform}),

    # Devices
    path('devices/', views.DeviceListView.as_view(), name='device_list'),
    path('devices/add/', views.DeviceCreateView.as_view(), name='device_add'),
    path('devices/import/', views.DeviceBulkImportView.as_view(), name='device_import'),
    path('devices/import/child-devices/', views.ChildDeviceBulkImportView.as_view(), name='device_import_child'),
    path('devices/edit/', views.DeviceBulkEditView.as_view(), name='device_bulk_edit'),
    path('devices/delete/', views.DeviceBulkDeleteView.as_view(), name='device_bulk_delete'),
    path('devices/<int:pk>/', views.DeviceView.as_view(), name='device'),
    path('devices/<int:pk>/edit/', views.DeviceEditView.as_view(), name='device_edit'),
    path('devices/<int:pk>/delete/', views.DeviceDeleteView.as_view(), name='device_delete'),
    path('devices/<int:pk>/config-context/', views.DeviceConfigContextView.as_view(), name='device_configcontext'),
    path('devices/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='device_changelog', kwargs={'model': Device}),
    path('devices/<int:pk>/inventory/', views.DeviceInventoryView.as_view(), name='device_inventory'),
    path('devices/<int:pk>/status/', views.DeviceStatusView.as_view(), name='device_status'),
    path('devices/<int:pk>/lldp-neighbors/', views.DeviceLLDPNeighborsView.as_view(), name='device_lldp_neighbors'),
    path('devices/<int:pk>/config/', views.DeviceConfigView.as_view(), name='device_config'),
    path('devices/<int:pk>/add-secret/', secret_add, name='device_addsecret'),
    path('devices/<int:device>/services/assign/', ServiceCreateView.as_view(), name='device_service_assign'),
    path('devices/<int:object_id>/images/add/', ImageAttachmentEditView.as_view(), name='device_add_image', kwargs={'model': Device}),

    # Console ports
    path('devices/console-ports/add/', views.DeviceBulkAddConsolePortView.as_view(), name='device_bulk_add_consoleport'),
    path('console-ports/', views.ConsolePortListView.as_view(), name='consoleport_list'),
    path('console-ports/add/', views.ConsolePortCreateView.as_view(), name='consoleport_add'),
    path('console-ports/import/', views.ConsolePortBulkImportView.as_view(), name='consoleport_import'),
    # TODO: Bulk edit view for ConsolePorts
    path('console-ports/delete/', views.ConsolePortBulkDeleteView.as_view(), name='consoleport_bulk_delete'),
    path('console-ports/<int:termination_a_id>/connect/<str:termination_b_type>/', views.CableCreateView.as_view(), name='consoleport_connect', kwargs={'termination_a_type': ConsolePort}),
    path('console-ports/<int:pk>/edit/', views.ConsolePortEditView.as_view(), name='consoleport_edit'),
    path('console-ports/<int:pk>/delete/', views.ConsolePortDeleteView.as_view(), name='consoleport_delete'),
    path('console-ports/<int:pk>/trace/', views.CableTraceView.as_view(), name='consoleport_trace', kwargs={'model': ConsolePort}),

    # Console server ports
    path('devices/console-server-ports/add/', views.DeviceBulkAddConsoleServerPortView.as_view(), name='device_bulk_add_consoleserverport'),
    path('console-server-ports/', views.ConsoleServerPortListView.as_view(), name='consoleserverport_list'),
    path('console-server-ports/rename/', views.ConsoleServerPortBulkRenameView.as_view(), name='consoleserverport_bulk_rename'),
    path('console-server-ports/disconnect/', views.ConsoleServerPortBulkDisconnectView.as_view(), name='consoleserverport_bulk_disconnect'),
    path('console-server-ports/add/', views.ConsoleServerPortCreateView.as_view(), name='consoleserverport_add'),
    path('console-server-ports/import/', views.ConsoleServerPortBulkImportView.as_view(), name='consoleserverport_import'),
    path('console-server-ports/edit/', views.ConsoleServerPortBulkEditView.as_view(), name='consoleserverport_bulk_edit'),
    path('console-server-ports/delete/', views.ConsoleServerPortBulkDeleteView.as_view(), name='consoleserverport_bulk_delete'),
    path('console-server-ports/<int:termination_a_id>/connect/<str:termination_b_type>/', views.CableCreateView.as_view(), name='consoleserverport_connect', kwargs={'termination_a_type': ConsoleServerPort}),
    path('console-server-ports/<int:pk>/edit/', views.ConsoleServerPortEditView.as_view(), name='consoleserverport_edit'),
    path('console-server-ports/<int:pk>/delete/', views.ConsoleServerPortDeleteView.as_view(), name='consoleserverport_delete'),
    path('console-server-ports/<int:pk>/trace/', views.CableTraceView.as_view(), name='consoleserverport_trace', kwargs={'model': ConsoleServerPort}),

    # Power ports
    path('devices/power-ports/add/', views.DeviceBulkAddPowerPortView.as_view(), name='device_bulk_add_powerport'),
    path('power-ports/', views.PowerPortListView.as_view(), name='powerport_list'),
    path('power-ports/add/', views.PowerPortCreateView.as_view(), name='powerport_add'),
    path('power-ports/import/', views.PowerPortBulkImportView.as_view(), name='powerport_import'),
    # TODO: Bulk edit view for PowerPorts
    path('power-ports/delete/', views.PowerPortBulkDeleteView.as_view(), name='powerport_bulk_delete'),
    path('power-ports/<int:termination_a_id>/connect/<str:termination_b_type>/', views.CableCreateView.as_view(), name='powerport_connect', kwargs={'termination_a_type': PowerPort}),
    path('power-ports/<int:pk>/edit/', views.PowerPortEditView.as_view(), name='powerport_edit'),
    path('power-ports/<int:pk>/delete/', views.PowerPortDeleteView.as_view(), name='powerport_delete'),
    path('power-ports/<int:pk>/trace/', views.CableTraceView.as_view(), name='powerport_trace', kwargs={'model': PowerPort}),

    # Power outlets
    path('devices/power-outlets/add/', views.DeviceBulkAddPowerOutletView.as_view(), name='device_bulk_add_poweroutlet'),
    path('power-outlets/', views.PowerOutletListView.as_view(), name='poweroutlet_list'),
    path('power-outlets/rename/', views.PowerOutletBulkRenameView.as_view(), name='poweroutlet_bulk_rename'),
    path('power-outlets/disconnect/', views.PowerOutletBulkDisconnectView.as_view(), name='poweroutlet_bulk_disconnect'),
    path('power-outlets/add/', views.PowerOutletCreateView.as_view(), name='poweroutlet_add'),
    path('power-outlets/import/', views.PowerOutletBulkImportView.as_view(), name='poweroutlet_import'),
    path('power-outlets/edit/', views.PowerOutletBulkEditView.as_view(), name='poweroutlet_bulk_edit'),
    path('power-outlets/delete/', views.PowerOutletBulkDeleteView.as_view(), name='poweroutlet_bulk_delete'),
    path('power-outlets/<int:termination_a_id>/connect/<str:termination_b_type>/', views.CableCreateView.as_view(), name='poweroutlet_connect', kwargs={'termination_a_type': PowerOutlet}),
    path('power-outlets/<int:pk>/edit/', views.PowerOutletEditView.as_view(), name='poweroutlet_edit'),
    path('power-outlets/<int:pk>/delete/', views.PowerOutletDeleteView.as_view(), name='poweroutlet_delete'),
    path('power-outlets/<int:pk>/trace/', views.CableTraceView.as_view(), name='poweroutlet_trace', kwargs={'model': PowerOutlet}),

    # Interfaces
    path('devices/interfaces/add/', views.DeviceBulkAddInterfaceView.as_view(), name='device_bulk_add_interface'),
    path('interfaces/', views.InterfaceListView.as_view(), name='interface_list'),
    path('interfaces/rename/', views.InterfaceBulkRenameView.as_view(), name='interface_bulk_rename'),
    path('interfaces/disconnect/', views.InterfaceBulkDisconnectView.as_view(), name='interface_bulk_disconnect'),
    path('interfaces/add/', views.InterfaceCreateView.as_view(), name='interface_add'),
    path('interfaces/import/', views.InterfaceBulkImportView.as_view(), name='interface_import'),
    path('interfaces/edit/', views.InterfaceBulkEditView.as_view(), name='interface_bulk_edit'),
    path('interfaces/delete/', views.InterfaceBulkDeleteView.as_view(), name='interface_bulk_delete'),
    path('interfaces/<int:termination_a_id>/connect/<str:termination_b_type>/', views.CableCreateView.as_view(), name='interface_connect', kwargs={'termination_a_type': Interface}),
    path('interfaces/<int:pk>/', views.InterfaceView.as_view(), name='interface'),
    path('interfaces/<int:pk>/edit/', views.InterfaceEditView.as_view(), name='interface_edit'),
    path('interfaces/<int:pk>/delete/', views.InterfaceDeleteView.as_view(), name='interface_delete'),
    path('interfaces/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='interface_changelog', kwargs={'model': Interface}),
    path('interfaces/<int:pk>/trace/', views.CableTraceView.as_view(), name='interface_trace', kwargs={'model': Interface}),

    # Front ports
    # path('devices/front-ports/add/', views.DeviceBulkAddFrontPortView.as_view(), name='device_bulk_add_frontport'),
    path('front-ports/', views.FrontPortListView.as_view(), name='frontport_list'),
    path('front-ports/rename/', views.FrontPortBulkRenameView.as_view(), name='frontport_bulk_rename'),
    path('front-ports/disconnect/', views.FrontPortBulkDisconnectView.as_view(), name='frontport_bulk_disconnect'),
    path('front-ports/add/', views.FrontPortCreateView.as_view(), name='frontport_add'),
    path('front-ports/import/', views.FrontPortBulkImportView.as_view(), name='frontport_import'),
    path('front-ports/edit/', views.FrontPortBulkEditView.as_view(), name='frontport_bulk_edit'),
    path('front-ports/delete/', views.FrontPortBulkDeleteView.as_view(), name='frontport_bulk_delete'),
    path('front-ports/<int:termination_a_id>/connect/<str:termination_b_type>/', views.CableCreateView.as_view(), name='frontport_connect', kwargs={'termination_a_type': FrontPort}),
    path('front-ports/<int:pk>/edit/', views.FrontPortEditView.as_view(), name='frontport_edit'),
    path('front-ports/<int:pk>/delete/', views.FrontPortDeleteView.as_view(), name='frontport_delete'),
    path('front-ports/<int:pk>/trace/', views.CableTraceView.as_view(), name='frontport_trace', kwargs={'model': FrontPort}),

    # Rear ports
    # path('devices/rear-ports/add/', views.DeviceBulkAddRearPortView.as_view(), name='device_bulk_add_rearport'),
    path('rear-ports/', views.RearPortListView.as_view(), name='rearport_list'),
    path('rear-ports/rename/', views.RearPortBulkRenameView.as_view(), name='rearport_bulk_rename'),
    path('rear-ports/disconnect/', views.RearPortBulkDisconnectView.as_view(), name='rearport_bulk_disconnect'),
    path('rear-ports/add/', views.RearPortCreateView.as_view(), name='rearport_add'),
    path('rear-ports/import/', views.RearPortBulkImportView.as_view(), name='rearport_import'),
    path('rear-ports/edit/', views.RearPortBulkEditView.as_view(), name='rearport_bulk_edit'),
    path('rear-ports/delete/', views.RearPortBulkDeleteView.as_view(), name='rearport_bulk_delete'),
    path('rear-ports/<int:termination_a_id>/connect/<str:termination_b_type>/', views.CableCreateView.as_view(), name='rearport_connect', kwargs={'termination_a_type': RearPort}),
    path('rear-ports/<int:pk>/edit/', views.RearPortEditView.as_view(), name='rearport_edit'),
    path('rear-ports/<int:pk>/delete/', views.RearPortDeleteView.as_view(), name='rearport_delete'),
    path('rear-ports/<int:pk>/trace/', views.CableTraceView.as_view(), name='rearport_trace', kwargs={'model': RearPort}),

    # Device bays
    path('devices/device-bays/add/', views.DeviceBulkAddDeviceBayView.as_view(), name='device_bulk_add_devicebay'),
    path('device-bays/', views.DeviceBayListView.as_view(), name='devicebay_list'),
    path('device-bays/rename/', views.DeviceBayBulkRenameView.as_view(), name='devicebay_bulk_rename'),
    path('device-bays/add/', views.DeviceBayCreateView.as_view(), name='devicebay_add'),
    path('device-bays/import/', views.DeviceBayBulkImportView.as_view(), name='devicebay_import'),
    # TODO: Bulk edit view for DeviceBays
    path('device-bays/delete/', views.DeviceBayBulkDeleteView.as_view(), name='devicebay_bulk_delete'),
    path('device-bays/<int:pk>/edit/', views.DeviceBayEditView.as_view(), name='devicebay_edit'),
    path('device-bays/<int:pk>/delete/', views.DeviceBayDeleteView.as_view(), name='devicebay_delete'),
    path('device-bays/<int:pk>/populate/', views.DeviceBayPopulateView.as_view(), name='devicebay_populate'),
    path('device-bays/<int:pk>/depopulate/', views.DeviceBayDepopulateView.as_view(), name='devicebay_depopulate'),

    # Inventory items
    path('inventory-items/', views.InventoryItemListView.as_view(), name='inventoryitem_list'),
    path('inventory-items/import/', views.InventoryItemBulkImportView.as_view(), name='inventoryitem_import'),
    path('inventory-items/edit/', views.InventoryItemBulkEditView.as_view(), name='inventoryitem_bulk_edit'),
    path('inventory-items/delete/', views.InventoryItemBulkDeleteView.as_view(), name='inventoryitem_bulk_delete'),
    path('inventory-items/<int:pk>/edit/', views.InventoryItemEditView.as_view(), name='inventoryitem_edit'),
    path('inventory-items/<int:pk>/delete/', views.InventoryItemDeleteView.as_view(), name='inventoryitem_delete'),
    # TODO: Replace below with InventoryItemCreateView
    path('devices/<int:device>/inventory-items/add/', views.InventoryItemEditView.as_view(), name='inventoryitem_add'),

    # Cables
    path('cables/', views.CableListView.as_view(), name='cable_list'),
    path('cables/import/', views.CableBulkImportView.as_view(), name='cable_import'),
    path('cables/edit/', views.CableBulkEditView.as_view(), name='cable_bulk_edit'),
    path('cables/delete/', views.CableBulkDeleteView.as_view(), name='cable_bulk_delete'),
    path('cables/<int:pk>/', views.CableView.as_view(), name='cable'),
    path('cables/<int:pk>/edit/', views.CableEditView.as_view(), name='cable_edit'),
    path('cables/<int:pk>/delete/', views.CableDeleteView.as_view(), name='cable_delete'),
    path('cables/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='cable_changelog', kwargs={'model': Cable}),

    # Console/power/interface connections (read-only)
    path('console-connections/', views.ConsoleConnectionsListView.as_view(), name='console_connections_list'),
    path('power-connections/', views.PowerConnectionsListView.as_view(), name='power_connections_list'),
    path('interface-connections/', views.InterfaceConnectionsListView.as_view(), name='interface_connections_list'),

    # Virtual chassis
    path('virtual-chassis/', views.VirtualChassisListView.as_view(), name='virtualchassis_list'),
    path('virtual-chassis/add/', views.VirtualChassisCreateView.as_view(), name='virtualchassis_add'),
    path('virtual-chassis/<int:pk>/edit/', views.VirtualChassisEditView.as_view(), name='virtualchassis_edit'),
    path('virtual-chassis/<int:pk>/delete/', views.VirtualChassisDeleteView.as_view(), name='virtualchassis_delete'),
    path('virtual-chassis/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='virtualchassis_changelog', kwargs={'model': VirtualChassis}),
    path('virtual-chassis/<int:pk>/add-member/', views.VirtualChassisAddMemberView.as_view(), name='virtualchassis_add_member'),
    path('virtual-chassis-members/<int:pk>/delete/', views.VirtualChassisRemoveMemberView.as_view(), name='virtualchassis_remove_member'),

    # Power panels
    path('power-panels/', views.PowerPanelListView.as_view(), name='powerpanel_list'),
    path('power-panels/add/', views.PowerPanelCreateView.as_view(), name='powerpanel_add'),
    path('power-panels/import/', views.PowerPanelBulkImportView.as_view(), name='powerpanel_import'),
    path('power-panels/delete/', views.PowerPanelBulkDeleteView.as_view(), name='powerpanel_bulk_delete'),
    path('power-panels/<int:pk>/', views.PowerPanelView.as_view(), name='powerpanel'),
    path('power-panels/<int:pk>/edit/', views.PowerPanelEditView.as_view(), name='powerpanel_edit'),
    path('power-panels/<int:pk>/delete/', views.PowerPanelDeleteView.as_view(), name='powerpanel_delete'),
    path('power-panels/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='powerpanel_changelog', kwargs={'model': PowerPanel}),

    # Power feeds
    path('power-feeds/', views.PowerFeedListView.as_view(), name='powerfeed_list'),
    path('power-feeds/add/', views.PowerFeedCreateView.as_view(), name='powerfeed_add'),
    path('power-feeds/import/', views.PowerFeedBulkImportView.as_view(), name='powerfeed_import'),
    path('power-feeds/edit/', views.PowerFeedBulkEditView.as_view(), name='powerfeed_bulk_edit'),
    path('power-feeds/delete/', views.PowerFeedBulkDeleteView.as_view(), name='powerfeed_bulk_delete'),
    path('power-feeds/<int:pk>/', views.PowerFeedView.as_view(), name='powerfeed'),
    path('power-feeds/<int:pk>/edit/', views.PowerFeedEditView.as_view(), name='powerfeed_edit'),
    path('power-feeds/<int:pk>/delete/', views.PowerFeedDeleteView.as_view(), name='powerfeed_delete'),
    path('power-feeds/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='powerfeed_changelog', kwargs={'model': PowerFeed}),

]
