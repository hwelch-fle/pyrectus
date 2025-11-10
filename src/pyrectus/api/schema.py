from __future__ import annotations

from typing import Any, TypedDict, Literal

# Ported from ..\..\submodules\openapi\openapi\components\schemas

class Activity(TypedDict):
    id: int
    """Unique identifier for the object."""
    
    action: Literal['create', 'update', 'delete', 'login']
    """Action that was performed."""
    
    user: User
    """The user who performed this action. Many-to-one to users."""
    
    timestamp: str
    """When the action happened. (`ISO8601`)"""
    
    ip: str
    """The IP address of the user at the time the action took place. (ipv4)"""
    
    user_agent: str
    """User agent string of the browser the user used when the action took place."""
    
    collection: Collection
    """Collection identifier in which the item resides."""
    
    item: str
    """Unique identifier for the item the action applied to. 
    This is always a string, even for integer primary keys."""
    
    comment: str
    """User comment. 
    This will store the comments that show up in the right sidebar 
    of the item edit page in the admin app."""
    
    origin: str
    """Origin of the request when the action took place. (url)"""
    
    revisions: list[Revision]
    """Any changes that were made in this activity. One-to-many to revisions."""
  
class Collection(TypedDict):
    collection: str
    """Name of the collection. This matches the table name in the database."""
    
    icon: str
    """Icon displayed in the Data Studio when working with this collection."""
    
    note: str
    """Short description displayed in the Data Studio."""
    
    display_template: str
    """How items in this collection should be displayed 
    when viewed relationally in the Data Studio."""
    
    hidden: bool
    """Whether or not this collection is hidden in the Data Studio."""
    
    singleton: bool
    """Whether or not this collection is treated as a singleton."""
    
    translations: list[str]
    """How this collection's name is displayed in the different languages in the Data Studio."""
    
    archive_field: str
    """What field in the collection holds the archived state. (`Field.field`)"""
    
    archive_app_filter: bool
    """No Description Provided"""
    
    archive_value: str
    """What value the archive field should be set to when archiving an item."""
    
    unarchive_value: str
    """What value the archive field should be set to when unarchiving an item."""
    
    sort_field: str
    """What field holds the sort value on the collection. 
    The Data Studio uses this to allow drag-and-drop manual sorting. (`Field.field`)"""
    
    accountability: Literal['all', 'activity']
    """What data is tracked. One of `all`, `activity`."""
    
    item_duplication_fields: list[str]
    """What fields are duplicated during "Save as copy" 
    action of an item in this collection. (`list[Field.field, ...]`)"""
    
    sort: int
    """What sort order of the collection relative to other collections of the same level."""
    
    group: str
    """The name of the parent collection. (`Collection.collection`)"""
    
    collapse: Literal['open', 'closed', 'locked']
    """What is the default behavior of this collection or "folder" collection 
    when it has nested collections. One of `open`, `closed`, `locked`."""
    
    versioning: bool
    """Whether or not Content Versioning is enabled for this collection."""

class Comment(TypedDict):
    
    collection: str
    """Collection identifier in which the item resides. 
    (Collection.id)"""
    
    id: str
    """Unique identifier for the object. 
    (uuid)"""
    
    item: str
    """The item the comment is created for. 
    (Item.id)"""
    
    comment: str
    """User comment. This will store the comments that show up in the 
    right sidebar of the item edit page in the Data Studio."""
    
    date_created: str
    """Timestamp in `ISO8601` when the comment was created."""
    
    date_updated: str
    """Timestamp in `ISO8601` when the comment was last updated. 
    (`ISO8601`)"""
    
    user_created: str
    """The user who created the comment. Many-to-one to users. 
    (`User.user`)"""
    
    user_updated: str
    """The user who last updated the comment. Many-to-one to users. 
    (`User.user`)"""
    
class Dashboard(TypedDict):
    id: str
    """Primary key of the dashboard (uuid)"""
    
    name: str
    """Name of the dashboard."""
    
    icon: str
    """Material icon for dashboard. See: https://fonts.google.com/icons for options"""
    
    note: str
    """Descriptive text about the dashboard."""
    
    date_created: str
    """When the dashboard was created. (ISO8601)"""
    
    user_created: str
    """User that created the dashboard. Many-to-one to users. (`User.id`)"""
    
    color: str
    """Accent color for the dashboard. (hexcode, e.g. #FFFFFF)"""
    
    panels: list[str]
    """Panels that are in this dashboard. One-to-many to panels. (`list[Panel.id]`)"""

class Diff(TypedDict):
    hash: str
    """Hash of the diff"""
    
    diff: dict[str, Any]
    """The diff object (collections, fields, relations)"""

class Extension(TypedDict):
    enabled: bool
    """Whether or not the extension is enabled."""
    id: str
    """Unique identifier of the extension. (uuid)"""
    bundle: str
    """Name of the bundle the extension is in."""
    type: Literal['interface', 'display', 'layout', 'module', 'panel', 'hook', 'endpoint', 'operation', 'bundle']
    """Type of the extension. One of `'interface'`, `'display'`, `'layout'`, `'module'`, `'panel'`, `'hook'`, `'endpoint'`, `'operation'`, `'bundle'`."""
    local: bool
    """Whether the extension exists in the local extensions folder or is loaded from `node_modules`."""
    version: str
    """The currently loaded version of the plugin as defined by its `package.json`."""
    partial: bool
    """Whether or not a bundles entries can be individually disabled. This is applicable to bundle type extensions only."""
    
class Field(TypedDict):
    id: int
    """Unique ID of the Field"""
    
    collection: str
    """Unique name of the collection this field is in. (`Collection.collection`)"""
    
    field: str
    """Unique name of the field. Field name is unique within the collection."""
    
    special: list[str]
    """Any special transform flags that apply to this field."""
    
    interface: str
    """The interface used for this field."""
    
    options: Any
    """The interface options configured for this field. The structure is based on the interface used."""
    
    display: str
    """The display used for this field."""
    
    display_options: str
    """The configured options for the used display."""
    
    readonly: bool
    """If the field is considered readonly in the Data Studio."""
    
    hidden: bool
    """If the field is hidden from the edit page in the Data Studio."""
    
    sort: int
    """Where this field is shown on the edit page in the Data Studio."""
    
    width: Literal['half', 'half-left', 'half-right', 'half-space', 'full', 'fill']
    """How wide the interface is rendered on the edit page in the Data Studio. 
    One of `half`, `half-left`, `half-right`, `half-space`, `full`, `fill`."""
    
    translations: list[str]
    """How this field's name is displayed in the different languages in the Data Studio."""
    
    note: str
    """Short description displayed in the Data Studio."""
    
    # conditions: str
    # """REMOVED FROM SCHEMA"""
    
    required: bool
    """Whether or not this field is required"""
    
    group: int
    """Optional field group that this field belongs to (`Field.id` of the Group Field)"""
    
    # validation:
    # """REMOVED FROM SCHEMA"""
    
    validation_message: str
    """Validation message that is displayed to the user"""
    
class File(TypedDict):
    id: str
    """Unique identifier for the file. (uuid)"""
    
    storage: Literal['local', 's3'] | str
    """Where the file is stored. 
    Either `local` for the local filesystem or 
    the name of the storage adapter (for example `s3`)."""
    
    filename_disk: str
    """Name of the file on disk. By default, Directus uses a random hash for the filename."""
    
    filename_download: str
    """How you want to the file to be named when it's being downloaded. (e.g. `file.jpg`)"""
    
    title: str
    """Title for the file. Is extracted from the filename on upload, but can be edited by the user."""
    
    type: str
    """MIME type of the file."""
    
    folder: str
    """Virtual folder where this file resides in. (`Folder.id`)"""
    
    uploaded_by: str
    """Who uploaded the file. (`User.id`)"""
    
    created_on: str
    """When the file was created. (`ISO8601`)"""
    
    modified_by: str
    """Who last modified the file. (`User.id`)"""
    
    modified_on: str
    """When the file was last modified. (`ISO8601`)"""
    
    charset: str
    """Character set of the file."""
    
    filesize: int
    """Size of the file in bytes."""
    
    width: int
    """Width of the file in pixels. Only applies to images."""
    
    height: int
    """Height of the file in pixels. Only applies to images."""
    
    duration: int
    """Duration of the file in seconds. Only applies to audio and video."""
    
    embed: str
    """Where the file was embedded from. (url)"""
    
    description: str
    """Description for the file."""
    
    location: str
    """Where the file was created. 
    Is automatically populated based on Exif data for images."""
    
    tags: list[str]
    """Tags for the file. 
    Is automatically populated based on Exif data for images."""
    
    metadata: Any
    """IPTC, Exif, and ICC metadata extracted from file"""
    
    focal_point_x: int
    """X component of the image focal point from EXIF data"""
    
    focal_point_y: int
    """Y component of the image focal point from EXIF data"""
    
    uploaded_on: str
    """When the file was last uploaded/replaced. (`ISO8601`)"""
      
class Flow(TypedDict):
    id: str
    """Unique identifier for the flow. (uuid)"""
    
    name: str
    """The name of the flow."""
    
    icon: str
    """Icon displayed in the Admin App for the flow. See: https://fonts.google.com/icons for options"""
    
    color: str
    """Color of the icon displayed in the Admin App for the flow. (hexcode, e.g. #FFFFFF)"""
    
    description: str
    """User defined description of the flow"""
    
    status: Literal['active', 'inactive']
    """Current status of the flow. 
    One of `active` or `inactive`"""
    
    trigger: Literal['hook', 'webhook', 'operation', 'schedule', 'manual']
    """Type of trigger for the flow. 
    One of `hook`, `webhook`, `operation`, `schedule`, `manual`."""
    
    accountability: Literal['$public', '$trigger', '$full'] | str
    """The permission used during the flow. 
    One of `$public`, `$trigger`, `$full`, or UUID of a role."""
    
    options: Any
    """Options of the selected trigger for the flow."""
    
    operation: str
    """UUID of the operation connected to the trigger in the flow. (`Operation.id`)"""
    
    date_created: str
    """Timestamp in ISO8601 when the flow was created."""
    
    user_created: str
    """The user who created the flow. (`User.id`)"""
    
    operations: list[str]
    """Array of all operations associated with the Flow (`list[Operation.id]`)"""
        
class Folder(TypedDict):
    id: str
    """Unique identifier for the folder. (uuid)"""
    
    name: str
    """Name of the folder."""
    
    parent: str
    """Unique identifier of the parent folder. 
    This allows for nested folders. (Folder.id)"""
    
class Item(TypedDict):
    """Items are Schema dependant, 
    `id` is the only non-user defined field that is guaranteed"""
    id: str
    """Unique ID for the item"""
    
class Notification(TypedDict):
    
    id: int
    """Primary key of the revision."""
    
    timestamp: str
    """Timestamp in ISO8601 when the notification was created."""
    
    status: Literal['inbox', 'archived']
    """Current status of the notification. One of `inbox`, `archived`"""
    
    recipient: str
    """User that received the notification. (`User.id`)"""
    
    sender: str
    """User that sent the notification, if any. (`User.id`)"""
    
    subject: str
    """Subject line of the message."""
    
    message: str
    """Subject line of the message."""
    
    collection: str
    """Collection this notification references. (`Collection.collection`)"""
    
    item: str
    """Primary key of the item this notification references as a string."""
      
class Operation(TypedDict):
    id: str
    """Unique identifier for the operation. (uuid)"""
    
    name: str
    """The name of the operation."""
    
    key: str
    """Key for the operation. Must be unique within a given flow."""
    
    type: Literal['log', 'mail', 'notification', 'create', 'read', 'request', 
                  'sleep', 'transform', 'trigger', 'condition'] | str
    """Type of operation. 
    One of `log`, `mail`, `notification`, `create`, `read`, 
    `request`, `sleep`, `transform`, `trigger`, `condition`, 
    or any type of custom operation extensions."""
    
    position_x: int
    """Position of the operation on the X axis within the flow workspace."""
    
    position_y: int
    """Position of the operation on the Y axis within the flow workspace."""
    
    options: Any
    """Options depending on the type of the operation."""
    
    resolve: str
    """The operation triggered when the current operation succeeds 
    (or `then` logic of a condition operation). (`Operation.id`)"""
    
    reject: str
    """The operation triggered when the current operation fails 
    (or `otherwise` logic of a condition operation). (`Operation.id`)"""
    
    flow: str
    """The parent flow for the operation (uuid) (`Flow.id`)"""
    
    date_created: str
    """Timestamp in ISO8601 when the operation was created."""
    
    user_created: str
    """The user who created the operation. (`User.id`)"""
      
class Panel(TypedDict):
    id: str
    """Primary key of the panel. (uuid)"""
    
    dashboard: str
    """Dashboard where this panel is visible. Many-to-one to dashboards. (`Dashboard.id`)"""
    
    name: str
    """Name of the panel."""
    
    icon: str
    """Material design icon for the panel. See: https://fonts.google.com/icons"""
    
    color: str
    """Accent color of the panel. (hexcode, e.g. #FFFFFF)"""
    
    show_header: bool
    """Whether or not the header should be rendered for this panel."""
    
    note: str
    """Description for the panel."""
    
    type: Literal['bar-chart', 'label', 'line-chart', 'list', 'meter', 
                  'metric-list', 'metric', 'pie-chart', 'relational-variable', 
                  'time-series', 'variable'] | str
    """The panel type used for this panel. 
    One of `bar-chart`, `label`, `line-chart`, `list`, `meter`,
    `metric-list`, `metric`, `pie-chart`, `relational-variable`, 
    `time-series`, `variable`"""
    
    position_x: int
    """The X position on the workspace grid."""
    
    position_y: int
    """The Y position on the workspace grid."""
    
    width: int
    """Width of the panel in number of workspace dots."""
    
    height: int
    """Height of the panel in number of workspace dots."""
    
    options: Any
    """Description for the panel."""
    
    date_created: str
    """When the panel was created (`ISO8601`)"""
    
    user_created: str
    """User that created the panel. Many-to-one to users. (`User.id`)"""

class Permission(TypedDict):
    id: int
    """Unique identifier for the permission."""
    
    collection: str
    """What collection this permission applies to. (`Collection.collection`)"""
    
    action: Literal['create', 'read', 'update', 'delete']
    """What action this permission applies to. 
    One of `create`, `read`, `update`, `delete`"""
    
    permissions: Any
    """JSON structure containing the permissions checks for this permission."""
    
    validation: Any
    """JSON structure containing the validation checks for this permission."""
    
    presets: Any
    """JSON structure containing the preset value for created/updated items."""
    
    fields: list[str]
    """CSV of fields that the user is allowed to interact with. 
    (`Field.field`)"""
    
    policy: str
    """Policy this permission applies to. 
    Many-to-one to policies. (uuid)(`Policy.id`)"""
      
class Policy(TypedDict):
    id: str
    """Primary key of the policy (uuid)"""
    
    name: str
    """Name of the policy."""
    
    icon: str
    """Icon for the policy. Displayed in the Data Studio. 
    See: https://fonts.google.com/icons"""
    
    description: str
    """Description for the policy. Displayed in the Data Studio."""
    
    ip_access: list[str]
    """A CSV of IP addresses that this policy applies to. 
    Allows you to configure an allowlist of IP addresses. 
    If empty, no IP restrictions are applied. (ipv4)"""
    
    enforce_tfa: bool
    """Whether or not Two-Factor Authentication is required 
    for users that have this policy."""
    
    admin_access: bool
    """If this policy grants the user admin access. 
    This means that users with this policy have full 
    permissions to everything."""
    
    app_access: bool
    """Whether or not users with this policy have access 
    to use the Data Studio."""
    
    users: list[str]
    """The users this policy is assigned to directly, 
    this does not include users which receive this policy through a role. 
    It expects and returns data from the directus_access collection. 
    Many-to-many to users via access. (`list[User.id]`)"""
    
    roles: list[str]
    """The roles this policy is assigned to. 
    It expects and returns data from the directus_access collection. 
    Many-to-many to roles via access. (`list[Role.id]`)"""
    
    permissions: list[str]
    """The permissions assigned to this policy. 
    One-to-many to permissions. (`list[Permission.id]`)"""

class Preset(TypedDict):
    id: int
    """Unique identifier for this single collection preset."""
    
    bookmark: str
    """Name for the bookmark. 
    If this is set, the preset will be considered a bookmark."""
    
    user: str
    """The unique identifier of the user to whom 
    this collection preset applies. (`User.id`)"""
    
    role: str
    """The unique identifier of a role in the platform. If `user` is null, 
    this will be used to apply the collection preset or 
    bookmark for all users in the role. (`Role.id`)"""
    
    collection: str
    """What collection this collection preset is used for. 
    (`Collection.collection`)"""
    
    search: str
    """Search query."""
    
    layout: str
    """Key of the layout that is used."""
    
    layout_query: Any
    """Layout query that's saved per layout type. Controls what data 
    is fetched on load. 
    These follow the same format as the JS SDK parameters."""
    
    layout_options: Any
    """Options of the views. The properties in here are controlled by the layout."""
    
    filters: list[str]
    """A list of filters to apply to the Preset. 
    See: https://directus.io/docs/guides/connect/filter-rules"""
    
class Query(TypedDict):
    fields: list[str]
    """Control what fields are being returned in the object. 
    (`list[Field.field] | * | *.*`)"""
    
    filter: Any
    """A filter to apply to the Query. 
    See: https://directus.io/docs/guides/connect/filter-rules"""
    
    search: str
    """Filter by items that contain the given search query 
    in one of their fields."""
    
    sort: list[str]
    """How to sort the returned items. (`-` prefix for `DESC`)
    
    Example:
        ```
            ['-date_created', 'name']
        ```
    """
    limit: int
    """Set the maximum number of items that will be returned"""
    
    offset: int
    """How many items to skip when fetching data."""
    
    page: int
    """Cursor for use in pagination. Often used in combination with limit."""
    
    deep: Any
    """Deep allows you to set any of the other query parameters 
    on a nested relational dataset.
    
    Example:
        ```
            {'related_articles': _limit: 3}
        ```
    """
    
    backlink: bool
    """Retrieve relational items 
    excluding reverse relations when using wildcard fields."""

class Relation(TypedDict):
    id: int
    """Unique identifier for the relation."""
    
    many_collection: str
    """Collection that has the field that holds the foreign key. 
    (`Collection.collection`)"""
    
    many_field: str
    """Foreign key. 
    Field that holds the primary key of the related collection. (`Field.field`)"""
    
    one_collection: str
    """Collection on the _one_ side of the relationship. 
    (`Collection.collection`)"""
    
    one_field: str
    """Alias column that serves as the _one_ side of the relationship. 
    (`Field.field`)"""
    
    one_collection_field: str
    """Alias column that serves as the _many_ side of the relationship. 
    (`Field.field`)"""
    
    one_allowed_collections: list[str]
    """NO DOC"""
    
    junction_field: str
    """Field on the junction table that holds the many field of the related relation."""
    
    sort_field: str
    """The field to sort the Relationship by 
    (`Field.field`)"""
    
    one_deselect_action: str
    """NO DOC"""

class Revision(TypedDict):
    id: int
    """Unique identifier for the revision."""
    
    activity: int
    """Unique identifier for the activity record. Many-to-one to activity. 
    (`Activity.id`)"""
    
    collection: str
    """Collection of the updated item. 
    (`Collection.collection`)"""
    
    item: str
    """Primary key of updated item as a string"""
    
    data: Any
    """Copy of item state at time of update.
    
    Example:
        ```
        {
            "author": 1,
            "body": "This is my first post",
            "featured_image": 15,
            "id": "168",
            "title": "Hello, World!",
            "type": {...},
            "nullable": true,
        }
        ```
    """
    
    delta: Any
    """Changes between the previous and the current revision.
    
    Example:
        ```
        {
            "title": "Hello, World!",
            "type": {...},
        }
        ```
    """
    
    parent: int
    """If the current item was updated relationally, 
    this is the id of the parent revision record.
    Many-to-one to revisions. (`Revision.id`)"""
    
    version: str
    """Associated version of this revision. Many-to-one to versions. 
    (`Version.key`)"""
    
class Role(TypedDict):
    id: str
    """Unique identifier for the role. (uuid)"""
    
    name: str
    """Name of the role."""
    
    icon: str
    """The role's icon. 
    See: https://fonts.google.com/icons"""
    
    description: str
    """Description of the role."""
    
    parent: str
    """Optional parent role that this role inherits permissions from. 
    Many-to-one to roles. (`Role.id`)"""
    
    children: list[str]
    """Nested child roles that inherit this roles permissions. 
    One-to-many to roles. (`list[Role.id]`)"""
    
    policies: list[str]
    """The policies in this role. 
    Many-to-many to roles. (`list[Policy.id]`)"""
    
    users: list[str]
    """The users in this role. 
    One-to-many to users. (`list[User.id]`)"""

class Schema(TypedDict):
    version: int
    """Schema version identifier"""
    directus: str
    """Directus base URL"""
    vendor: str
    """Vendor Identifier"""
    collections: list[Collection]
    """Schema Collections"""
    fields: list[Field]
    """Schema Fields"""
    relations: list[Relation]
    """Schema Relations"""

class StorageAsset(TypedDict):
    key: str
    """Key for the asset. Used in the assets endpoint."""
    
    fit: Literal['cover', 'contain', 'inside', 'outside']
    """Whether to crop the thumbnail to match the size, 
    or maintain the aspect ratio.
    One of: `cover`, `contain`, `inside`, `outside`"""

    width: int
    """Width of the thumbnail."""

    height: int
    """Height of the thumbnail."""

    withoutEnlargement: bool
    """No image upscale"""

    quality: int
    """Quality of the compression used."""

    format: Literal['jpeg', 'png', 'webp', 'tiff', 'avif']
    """Reformat output image.
    One of: `jpeg`, `png`, `webp`, `tiff`, `avif`"""

    transforms: list[Any]
    """Additional transformations to apply.
    
    See: https://directus.io/docs/guides/files/transform for format
    
    See: https://sharp.pixelplumbing.com/api-operation/ for valid funcs
    """

class Setting(TypedDict):
    id: int
    """Unique identifier for the setting."""
    
    project_name: str
    """Name of the project, shown in the Data Studio."""
    
    project_url: str
    """The url of the project. Link to the (public) website that goes with this project."""
    
    project_color: str
    """The brand color of the project. (herxcode, e.g. #FFFFFF)"""

    project_logo: str
    """The logo of the project. 
    Many-to-one to files (`File.id`)."""

    public_foreground: str
    """The foreground of the project. 
    Many-to-one to files (`File.id`)."""

    public_background: str
    """The background of the project. 
    Many-to-one to files (`File.id`)."""

    public_note: str
    """Note rendered on the public pages of the app."""

    auth_login_attempts: int
    """Allowed authentication login attempts before the user's status is set to blocked."""

    auth_password_policy: str
    """Authentication password policy. 
    What regex passwords must pass in order to be valid."""

    storage_asset_transform: Literal['all', 'none', 'presets']
    """If the transform endpoints are allowed to be used on the assets endpoint. 
    One of `all`, `none` or `presets`."""

    storage_asset_presets: list[StorageAsset]
    """What preset keys exist in the assets endpoint."""
    
    custom_css: str
    """CSS rules to override the App's default styling."""
    
    storage_default_folder: str
    """Folder for uploaded files. Does not affect existing files.
    (`Folder.id`)"""
    
    basemaps: list[str]
    """Custom tiles to overriding the Mapbox defaults.
    (`list[url]`)"""
    
    mapbox_key: str
    """Mapbox Access Token."""
    
    module_bar: list[str]
    """What modules are enabled/added globally."""
    
    project_descriptor: str
    """Descriptor of the project, shown in the Data Studio."""
    
    custom_aspect_ratios: list[float]
    """Custom aspect ratios in the image editor."""
    
    public_favicon: str
    """Favicon for the Data Studio. 
    Many-to-one to files. (`File.id`)"""
    
    default_appearance: Literal['auto', 'light', 'dark']
    """One of `auto`, `light`, `dark`."""
    
    default_theme_light: str
    """Default theme to use in light mode."""
    
    theme_light_overrides: Any
    """Default customization for light theme in use."""
    
    default_theme_dark: str
    """Default theme to use in dark mode."""
    
    theme_dark_overrides: Any
    """Default customization for dark theme in use."""
    
    report_error_url: str
    """Link to the error report page."""
    
    report_bug_url: str
    """Link to the bug report page. (url)"""
    
    report_feature_url: str
    """Link to the feature request page. (url)"""

class Share(TypedDict):
    id: str
    """Primary key of the share (uuid)"""

    name: str
    """Custom (optional) name for the share."""

    collection: str
    """Collection in which the current item is shared. 
    Many-to-one to Collections. (`Collection.collection`)"""

    item: str
    """Primary key of the item that's shared in string format"""

    role: str
    """Role of which the share will inherit the permissions. 
    Many-to-one to shares. (`Role.id`)"""

    password: str
    """Optional password that's required to view this shared item.
    (hash)"""

    user_created: str
    """Reference to the user who created this share. 
    Many-to-one to Users. (`User.id`)"""

    date_created: str
    """When the share was created.
    (`ISO8601`)"""

    date_start: str
    """Optional timestamp that controls from what date/time the shared item can be viewed.
    (`ISO8601`)"""
        
    date_end: str
    """Optional timestamp that controls until what date/time the shared item can be viewed.
    (`ISO8601`)"""
    
    times_used: int
    """The number of times the shared item has been viewed."""
    
    max_uses: int
    """The maximum number of times the shared item can be viewed."""
    
class Translation(TypedDict):
    id: str
    """Primary key of the translations."""

    key: str
    """The translation key."""

    language:str
    """The language code of the translation. (e.g. `en-US`)"""

    string: str
    """The translation value."""
    
class User(TypedDict):
    id: str
    """Unique identifier for the user."""

    first_name: str
    """First name of the user."""

    last_name: str
    """Last name of the user."""

    email: str
    """Unique email address for the user."""

    password: str
    """Password of the user."""

    location: str
    """The user's location."""

    title: str
    """The user's title."""

    description: str
    """The user's description."""

    tags: list[str]
    """The user's tags."""

    avatar: str
    """The user's avatar. 
    Many-to-one to files. (`File.id`)"""

    language: str
    """The user's language used in Directus. 
    Language the Data Studio is rendered in. 
    See Directus Crowdin page for all available languages and translations."""

    tfa_secret: str
    """The 2FA secret string that's used to generate one time passwords."""

    status: Literal['active', 'invited', 'draft', 'suspended', 'deleted']
    """Status of the user.
    One of: `active`, `invited`, `draft`, `suspended`, `deleted`"""

    role: str
    """Unique identifier of the role of this user. 
    Many-to-one to roles. (`Role.id`)"""

    token: str
    """Static token for the user."""

    policies: str
    """The policies associated with this user. 
    Many-to-many to policies. (`Policy.id`)"""

    last_access: str
    """When this user used the API last.
    (`ISO8601`)"""

    last_page: str
    """Last page that the user was on. 
    Relative to base URL (e.g. /project/settings/...)"""

    provider: str
    """What auth provider was used to register this user."""

    external_identifier: str
    """Primary key of the user in the third party authentication provider, if used."""

    auth_data: Any
    """Required data about the user as provided by the third party auth provider, if used."""

    email_notifications: bool
    """When this is enabled, the user will receive emails for notifications."""

    appearance: Literal['auto', 'light', 'dark']
    """One of `auto`, `light`, `dark`."""

    theme_dark: str
    """Theme to use in dark mode."""

    theme_light: str
    """Theme to use in light mode."""

    theme_light_overrides: Any
    """Customization for light theme in use."""

    theme_dark_overrides: Any
    """Customization for dark theme in use."""

class Version(TypedDict):
    id: str
    """Primary key of the Content Version."""

    key: str
    """Key of the Content Version, used as the value for the "version" query parameter."""

    name: str
    """Descriptive name of the Content Version."""

    collection: str
    """Name of the collection the Content Version is created on.
    (`Collection.collection`)"""

    item: str
    """The item the Content Version is created on. 
    Many-to-one to items. (`Item.id`)"""
        
    hash: str
    """Version hash/checksum"""

    date_created: str
    """When the Content Version was created.
    (`ISO8601`)"""

    date_updated: str
    """When the Content Version was updated.
    (`ISO8601`)"""

    user_created: str
    """User that created the Content Version. 
    Many-to-one to users. (`User.id`)"""

    user_updated: str
    """User that updated the Content Version. 
    Many-to-one to users. (`User.id`)"""

    delta: Any
    """The current changes compared to the main version of the item."""
