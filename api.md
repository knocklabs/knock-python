# Shared

Types:

```python
from knockapi.types import Condition, PageInfo
```

# Recipients

Types:

```python
from knockapi.types import Recipient, RecipientReference, RecipientRequest
```

## Subscriptions

Types:

```python
from knockapi.types.recipients import Subscription
```

## Preferences

Types:

```python
from knockapi.types.recipients import (
    InlinePreferenceSetRequest,
    PreferenceSet,
    PreferenceSetChannelTypeSetting,
    PreferenceSetChannelTypes,
    PreferenceSetRequest,
)
```

## ChannelData

Types:

```python
from knockapi.types.recipients import (
    ChannelData,
    ChannelDataRequest,
    DiscordChannelData,
    InlineChannelDataRequest,
    MsTeamsChannelData,
    OneSignalChannelData,
    PushChannelData,
    SlackChannelData,
)
```

# Users

Types:

```python
from knockapi.types import (
    IdentifyUserRequest,
    InlineIdentifyUserRequest,
    User,
    UserDeleteResponse,
    UserListPreferencesResponse,
    UserUnsetChannelDataResponse,
)
```

Methods:

- <code title="put /v1/users/{user_id}">client.users.<a href="./src/knockapi/resources/users/users.py">update</a>(user_id, \*\*<a href="src/knockapi/types/user_update_params.py">params</a>) -> <a href="./src/knockapi/types/user.py">User</a></code>
- <code title="get /v1/users">client.users.<a href="./src/knockapi/resources/users/users.py">list</a>(\*\*<a href="src/knockapi/types/user_list_params.py">params</a>) -> <a href="./src/knockapi/types/user.py">SyncEntriesCursor[User]</a></code>
- <code title="delete /v1/users/{user_id}">client.users.<a href="./src/knockapi/resources/users/users.py">delete</a>(user_id) -> str</code>
- <code title="get /v1/users/{user_id}">client.users.<a href="./src/knockapi/resources/users/users.py">get</a>(user_id) -> <a href="./src/knockapi/types/user.py">User</a></code>
- <code title="get /v1/users/{user_id}/channel_data/{channel_id}">client.users.<a href="./src/knockapi/resources/users/users.py">get_channel_data</a>(user_id, channel_id) -> <a href="./src/knockapi/types/recipients/channel_data.py">ChannelData</a></code>
- <code title="get /v1/users/{user_id}/preferences/{id}">client.users.<a href="./src/knockapi/resources/users/users.py">get_preferences</a>(user_id, id, \*\*<a href="src/knockapi/types/user_get_preferences_params.py">params</a>) -> <a href="./src/knockapi/types/recipients/preference_set.py">PreferenceSet</a></code>
- <code title="get /v1/users/{user_id}/messages">client.users.<a href="./src/knockapi/resources/users/users.py">list_messages</a>(user_id, \*\*<a href="src/knockapi/types/user_list_messages_params.py">params</a>) -> <a href="./src/knockapi/types/message.py">SyncItemsCursor[Message]</a></code>
- <code title="get /v1/users/{user_id}/preferences">client.users.<a href="./src/knockapi/resources/users/users.py">list_preferences</a>(user_id) -> <a href="./src/knockapi/types/user_list_preferences_response.py">UserListPreferencesResponse</a></code>
- <code title="get /v1/users/{user_id}/schedules">client.users.<a href="./src/knockapi/resources/users/users.py">list_schedules</a>(user_id, \*\*<a href="src/knockapi/types/user_list_schedules_params.py">params</a>) -> <a href="./src/knockapi/types/schedule.py">SyncEntriesCursor[Schedule]</a></code>
- <code title="get /v1/users/{user_id}/subscriptions">client.users.<a href="./src/knockapi/resources/users/users.py">list_subscriptions</a>(user_id, \*\*<a href="src/knockapi/types/user_list_subscriptions_params.py">params</a>) -> <a href="./src/knockapi/types/recipients/subscription.py">SyncEntriesCursor[Subscription]</a></code>
- <code title="post /v1/users/{user_id}/merge">client.users.<a href="./src/knockapi/resources/users/users.py">merge</a>(user_id, \*\*<a href="src/knockapi/types/user_merge_params.py">params</a>) -> <a href="./src/knockapi/types/user.py">User</a></code>
- <code title="put /v1/users/{user_id}/channel_data/{channel_id}">client.users.<a href="./src/knockapi/resources/users/users.py">set_channel_data</a>(user_id, channel_id, \*\*<a href="src/knockapi/types/user_set_channel_data_params.py">params</a>) -> <a href="./src/knockapi/types/recipients/channel_data.py">ChannelData</a></code>
- <code title="put /v1/users/{user_id}/preferences/{id}">client.users.<a href="./src/knockapi/resources/users/users.py">set_preferences</a>(user_id, id, \*\*<a href="src/knockapi/types/user_set_preferences_params.py">params</a>) -> <a href="./src/knockapi/types/recipients/preference_set.py">PreferenceSet</a></code>
- <code title="delete /v1/users/{user_id}/channel_data/{channel_id}">client.users.<a href="./src/knockapi/resources/users/users.py">unset_channel_data</a>(user_id, channel_id) -> str</code>

## Feeds

Types:

```python
from knockapi.types.users import FeedGetSettingsResponse, FeedListItemsResponse
```

Methods:

- <code title="get /v1/users/{user_id}/feeds/{id}/settings">client.users.feeds.<a href="./src/knockapi/resources/users/feeds.py">get_settings</a>(user_id, id) -> <a href="./src/knockapi/types/users/feed_get_settings_response.py">FeedGetSettingsResponse</a></code>
- <code title="get /v1/users/{user_id}/feeds/{id}">client.users.feeds.<a href="./src/knockapi/resources/users/feeds.py">list_items</a>(user_id, id, \*\*<a href="src/knockapi/types/users/feed_list_items_params.py">params</a>) -> <a href="./src/knockapi/types/users/feed_list_items_response.py">SyncEntriesCursor[FeedListItemsResponse]</a></code>

## Guides

Types:

```python
from knockapi.types.users import (
    GuideGetChannelResponse,
    GuideMarkMessageAsArchivedResponse,
    GuideMarkMessageAsInteractedResponse,
    GuideMarkMessageAsSeenResponse,
)
```

Methods:

- <code title="get /v1/users/{user_id}/guides/{channel_id}">client.users.guides.<a href="./src/knockapi/resources/users/guides.py">get_channel</a>(user_id, channel_id, \*\*<a href="src/knockapi/types/users/guide_get_channel_params.py">params</a>) -> <a href="./src/knockapi/types/users/guide_get_channel_response.py">GuideGetChannelResponse</a></code>
- <code title="put /v1/users/{user_id}/guides/messages/{message_id}/archived">client.users.guides.<a href="./src/knockapi/resources/users/guides.py">mark_message_as_archived</a>(user_id, message_id, \*\*<a href="src/knockapi/types/users/guide_mark_message_as_archived_params.py">params</a>) -> <a href="./src/knockapi/types/users/guide_mark_message_as_archived_response.py">GuideMarkMessageAsArchivedResponse</a></code>
- <code title="put /v1/users/{user_id}/guides/messages/{message_id}/interacted">client.users.guides.<a href="./src/knockapi/resources/users/guides.py">mark_message_as_interacted</a>(user_id, message_id, \*\*<a href="src/knockapi/types/users/guide_mark_message_as_interacted_params.py">params</a>) -> <a href="./src/knockapi/types/users/guide_mark_message_as_interacted_response.py">GuideMarkMessageAsInteractedResponse</a></code>
- <code title="put /v1/users/{user_id}/guides/messages/{message_id}/seen">client.users.guides.<a href="./src/knockapi/resources/users/guides.py">mark_message_as_seen</a>(user_id, message_id, \*\*<a href="src/knockapi/types/users/guide_mark_message_as_seen_params.py">params</a>) -> <a href="./src/knockapi/types/users/guide_mark_message_as_seen_response.py">GuideMarkMessageAsSeenResponse</a></code>

## Bulk

Methods:

- <code title="post /v1/users/bulk/delete">client.users.bulk.<a href="./src/knockapi/resources/users/bulk.py">delete</a>(\*\*<a href="src/knockapi/types/users/bulk_delete_params.py">params</a>) -> <a href="./src/knockapi/types/bulk_operation.py">BulkOperation</a></code>
- <code title="post /v1/users/bulk/identify">client.users.bulk.<a href="./src/knockapi/resources/users/bulk.py">identify</a>(\*\*<a href="src/knockapi/types/users/bulk_identify_params.py">params</a>) -> <a href="./src/knockapi/types/bulk_operation.py">BulkOperation</a></code>
- <code title="post /v1/users/bulk/preferences">client.users.bulk.<a href="./src/knockapi/resources/users/bulk.py">set_preferences</a>(\*\*<a href="src/knockapi/types/users/bulk_set_preferences_params.py">params</a>) -> <a href="./src/knockapi/types/bulk_operation.py">BulkOperation</a></code>

# Objects

Types:

```python
from knockapi.types import (
    InlineObjectRequest,
    Object,
    ObjectDeleteResponse,
    ObjectAddSubscriptionsResponse,
    ObjectDeleteSubscriptionsResponse,
    ObjectListPreferencesResponse,
    ObjectUnsetChannelDataResponse,
)
```

Methods:

- <code title="get /v1/objects/{collection}">client.objects.<a href="./src/knockapi/resources/objects/objects.py">list</a>(collection, \*\*<a href="src/knockapi/types/object_list_params.py">params</a>) -> <a href="./src/knockapi/types/object.py">SyncEntriesCursor[Object]</a></code>
- <code title="delete /v1/objects/{collection}/{id}">client.objects.<a href="./src/knockapi/resources/objects/objects.py">delete</a>(collection, id) -> str</code>
- <code title="post /v1/objects/{collection}/{object_id}/subscriptions">client.objects.<a href="./src/knockapi/resources/objects/objects.py">add_subscriptions</a>(collection, object_id, \*\*<a href="src/knockapi/types/object_add_subscriptions_params.py">params</a>) -> <a href="./src/knockapi/types/object_add_subscriptions_response.py">ObjectAddSubscriptionsResponse</a></code>
- <code title="delete /v1/objects/{collection}/{object_id}/subscriptions">client.objects.<a href="./src/knockapi/resources/objects/objects.py">delete_subscriptions</a>(collection, object_id, \*\*<a href="src/knockapi/types/object_delete_subscriptions_params.py">params</a>) -> <a href="./src/knockapi/types/object_delete_subscriptions_response.py">ObjectDeleteSubscriptionsResponse</a></code>
- <code title="get /v1/objects/{collection}/{id}">client.objects.<a href="./src/knockapi/resources/objects/objects.py">get</a>(collection, id) -> <a href="./src/knockapi/types/object.py">Object</a></code>
- <code title="get /v1/objects/{collection}/{object_id}/channel_data/{channel_id}">client.objects.<a href="./src/knockapi/resources/objects/objects.py">get_channel_data</a>(collection, object_id, channel_id) -> <a href="./src/knockapi/types/recipients/channel_data.py">ChannelData</a></code>
- <code title="get /v1/objects/{collection}/{object_id}/preferences/{id}">client.objects.<a href="./src/knockapi/resources/objects/objects.py">get_preferences</a>(collection, object_id, id) -> <a href="./src/knockapi/types/recipients/preference_set.py">PreferenceSet</a></code>
- <code title="get /v1/objects/{collection}/{id}/messages">client.objects.<a href="./src/knockapi/resources/objects/objects.py">list_messages</a>(collection, id, \*\*<a href="src/knockapi/types/object_list_messages_params.py">params</a>) -> <a href="./src/knockapi/types/message.py">SyncItemsCursor[Message]</a></code>
- <code title="get /v1/objects/{collection}/{object_id}/preferences">client.objects.<a href="./src/knockapi/resources/objects/objects.py">list_preferences</a>(collection, object_id) -> <a href="./src/knockapi/types/object_list_preferences_response.py">ObjectListPreferencesResponse</a></code>
- <code title="get /v1/objects/{collection}/{id}/schedules">client.objects.<a href="./src/knockapi/resources/objects/objects.py">list_schedules</a>(collection, id, \*\*<a href="src/knockapi/types/object_list_schedules_params.py">params</a>) -> <a href="./src/knockapi/types/schedule.py">SyncEntriesCursor[Schedule]</a></code>
- <code title="get /v1/objects/{collection}/{object_id}/subscriptions">client.objects.<a href="./src/knockapi/resources/objects/objects.py">list_subscriptions</a>(collection, object_id, \*\*<a href="src/knockapi/types/object_list_subscriptions_params.py">params</a>) -> <a href="./src/knockapi/types/recipients/subscription.py">SyncEntriesCursor[Subscription]</a></code>
- <code title="put /v1/objects/{collection}/{id}">client.objects.<a href="./src/knockapi/resources/objects/objects.py">set</a>(collection, id, \*\*<a href="src/knockapi/types/object_set_params.py">params</a>) -> <a href="./src/knockapi/types/object.py">Object</a></code>
- <code title="put /v1/objects/{collection}/{object_id}/channel_data/{channel_id}">client.objects.<a href="./src/knockapi/resources/objects/objects.py">set_channel_data</a>(collection, object_id, channel_id, \*\*<a href="src/knockapi/types/object_set_channel_data_params.py">params</a>) -> <a href="./src/knockapi/types/recipients/channel_data.py">ChannelData</a></code>
- <code title="put /v1/objects/{collection}/{object_id}/preferences/{id}">client.objects.<a href="./src/knockapi/resources/objects/objects.py">set_preferences</a>(collection, object_id, id, \*\*<a href="src/knockapi/types/object_set_preferences_params.py">params</a>) -> <a href="./src/knockapi/types/recipients/preference_set.py">PreferenceSet</a></code>
- <code title="delete /v1/objects/{collection}/{object_id}/channel_data/{channel_id}">client.objects.<a href="./src/knockapi/resources/objects/objects.py">unset_channel_data</a>(collection, object_id, channel_id) -> str</code>

## Bulk

Methods:

- <code title="post /v1/objects/{collection}/bulk/delete">client.objects.bulk.<a href="./src/knockapi/resources/objects/bulk.py">delete</a>(collection, \*\*<a href="src/knockapi/types/objects/bulk_delete_params.py">params</a>) -> <a href="./src/knockapi/types/bulk_operation.py">BulkOperation</a></code>
- <code title="post /v1/objects/{collection}/bulk/subscriptions/add">client.objects.bulk.<a href="./src/knockapi/resources/objects/bulk.py">add_subscriptions</a>(collection, \*\*<a href="src/knockapi/types/objects/bulk_add_subscriptions_params.py">params</a>) -> <a href="./src/knockapi/types/bulk_operation.py">BulkOperation</a></code>
- <code title="post /v1/objects/{collection}/bulk/set">client.objects.bulk.<a href="./src/knockapi/resources/objects/bulk.py">set</a>(collection, \*\*<a href="src/knockapi/types/objects/bulk_set_params.py">params</a>) -> <a href="./src/knockapi/types/bulk_operation.py">BulkOperation</a></code>

# Tenants

Types:

```python
from knockapi.types import InlineTenantRequest, Tenant, TenantRequest, TenantDeleteResponse
```

Methods:

- <code title="get /v1/tenants">client.tenants.<a href="./src/knockapi/resources/tenants/tenants.py">list</a>(\*\*<a href="src/knockapi/types/tenant_list_params.py">params</a>) -> <a href="./src/knockapi/types/tenant.py">SyncEntriesCursor[Tenant]</a></code>
- <code title="delete /v1/tenants/{id}">client.tenants.<a href="./src/knockapi/resources/tenants/tenants.py">delete</a>(id) -> str</code>
- <code title="get /v1/tenants/{id}">client.tenants.<a href="./src/knockapi/resources/tenants/tenants.py">get</a>(id) -> <a href="./src/knockapi/types/tenant.py">Tenant</a></code>
- <code title="put /v1/tenants/{id}">client.tenants.<a href="./src/knockapi/resources/tenants/tenants.py">set</a>(id, \*\*<a href="src/knockapi/types/tenant_set_params.py">params</a>) -> <a href="./src/knockapi/types/tenant.py">Tenant</a></code>

## Bulk

Methods:

- <code title="post /v1/tenants/bulk/delete">client.tenants.bulk.<a href="./src/knockapi/resources/tenants/bulk.py">delete</a>(\*\*<a href="src/knockapi/types/tenants/bulk_delete_params.py">params</a>) -> <a href="./src/knockapi/types/bulk_operation.py">BulkOperation</a></code>
- <code title="post /v1/tenants/bulk/set">client.tenants.bulk.<a href="./src/knockapi/resources/tenants/bulk.py">set</a>(\*\*<a href="src/knockapi/types/tenants/bulk_set_params.py">params</a>) -> <a href="./src/knockapi/types/bulk_operation.py">BulkOperation</a></code>

# BulkOperations

Types:

```python
from knockapi.types import BulkOperation
```

Methods:

- <code title="get /v1/bulk_operations/{id}">client.bulk_operations.<a href="./src/knockapi/resources/bulk_operations.py">get</a>(id) -> <a href="./src/knockapi/types/bulk_operation.py">BulkOperation</a></code>

# Messages

Types:

```python
from knockapi.types import (
    Activity,
    Message,
    MessageDeliveryLog,
    MessageEvent,
    MessageGetContentResponse,
)
```

Methods:

- <code title="get /v1/messages">client.messages.<a href="./src/knockapi/resources/messages/messages.py">list</a>(\*\*<a href="src/knockapi/types/message_list_params.py">params</a>) -> <a href="./src/knockapi/types/message.py">SyncItemsCursor[Message]</a></code>
- <code title="put /v1/messages/{message_id}/archived">client.messages.<a href="./src/knockapi/resources/messages/messages.py">archive</a>(message_id) -> <a href="./src/knockapi/types/message.py">Message</a></code>
- <code title="get /v1/messages/{message_id}">client.messages.<a href="./src/knockapi/resources/messages/messages.py">get</a>(message_id) -> <a href="./src/knockapi/types/message.py">Message</a></code>
- <code title="get /v1/messages/{message_id}/content">client.messages.<a href="./src/knockapi/resources/messages/messages.py">get_content</a>(message_id) -> <a href="./src/knockapi/types/message_get_content_response.py">MessageGetContentResponse</a></code>
- <code title="get /v1/messages/{message_id}/activities">client.messages.<a href="./src/knockapi/resources/messages/messages.py">list_activities</a>(message_id, \*\*<a href="src/knockapi/types/message_list_activities_params.py">params</a>) -> <a href="./src/knockapi/types/activity.py">SyncItemsCursor[Activity]</a></code>
- <code title="get /v1/messages/{message_id}/delivery_logs">client.messages.<a href="./src/knockapi/resources/messages/messages.py">list_delivery_logs</a>(message_id, \*\*<a href="src/knockapi/types/message_list_delivery_logs_params.py">params</a>) -> <a href="./src/knockapi/types/message_delivery_log.py">SyncItemsCursor[MessageDeliveryLog]</a></code>
- <code title="get /v1/messages/{message_id}/events">client.messages.<a href="./src/knockapi/resources/messages/messages.py">list_events</a>(message_id, \*\*<a href="src/knockapi/types/message_list_events_params.py">params</a>) -> <a href="./src/knockapi/types/message_event.py">SyncItemsCursor[MessageEvent]</a></code>
- <code title="put /v1/messages/{message_id}/interacted">client.messages.<a href="./src/knockapi/resources/messages/messages.py">mark_as_interacted</a>(message_id, \*\*<a href="src/knockapi/types/message_mark_as_interacted_params.py">params</a>) -> <a href="./src/knockapi/types/message.py">Message</a></code>
- <code title="put /v1/messages/{message_id}/read">client.messages.<a href="./src/knockapi/resources/messages/messages.py">mark_as_read</a>(message_id) -> <a href="./src/knockapi/types/message.py">Message</a></code>
- <code title="put /v1/messages/{message_id}/seen">client.messages.<a href="./src/knockapi/resources/messages/messages.py">mark_as_seen</a>(message_id) -> <a href="./src/knockapi/types/message.py">Message</a></code>
- <code title="delete /v1/messages/{message_id}/read">client.messages.<a href="./src/knockapi/resources/messages/messages.py">mark_as_unread</a>(message_id) -> <a href="./src/knockapi/types/message.py">Message</a></code>
- <code title="delete /v1/messages/{message_id}/seen">client.messages.<a href="./src/knockapi/resources/messages/messages.py">mark_as_unseen</a>(message_id) -> <a href="./src/knockapi/types/message.py">Message</a></code>
- <code title="delete /v1/messages/{message_id}/archived">client.messages.<a href="./src/knockapi/resources/messages/messages.py">unarchive</a>(message_id) -> <a href="./src/knockapi/types/message.py">Message</a></code>

## Batch

Types:

```python
from knockapi.types.messages import (
    BatchArchiveResponse,
    BatchGetContentResponse,
    BatchMarkAsInteractedResponse,
    BatchMarkAsReadResponse,
    BatchMarkAsSeenResponse,
    BatchMarkAsUnreadResponse,
    BatchMarkAsUnseenResponse,
    BatchUnarchiveResponse,
)
```

Methods:

- <code title="post /v1/messages/batch/archived">client.messages.batch.<a href="./src/knockapi/resources/messages/batch.py">archive</a>(\*\*<a href="src/knockapi/types/messages/batch_archive_params.py">params</a>) -> <a href="./src/knockapi/types/messages/batch_archive_response.py">BatchArchiveResponse</a></code>
- <code title="get /v1/messages/batch/content">client.messages.batch.<a href="./src/knockapi/resources/messages/batch.py">get_content</a>(\*\*<a href="src/knockapi/types/messages/batch_get_content_params.py">params</a>) -> <a href="./src/knockapi/types/messages/batch_get_content_response.py">BatchGetContentResponse</a></code>
- <code title="post /v1/messages/batch/interacted">client.messages.batch.<a href="./src/knockapi/resources/messages/batch.py">mark_as_interacted</a>(\*\*<a href="src/knockapi/types/messages/batch_mark_as_interacted_params.py">params</a>) -> <a href="./src/knockapi/types/messages/batch_mark_as_interacted_response.py">BatchMarkAsInteractedResponse</a></code>
- <code title="post /v1/messages/batch/read">client.messages.batch.<a href="./src/knockapi/resources/messages/batch.py">mark_as_read</a>(\*\*<a href="src/knockapi/types/messages/batch_mark_as_read_params.py">params</a>) -> <a href="./src/knockapi/types/messages/batch_mark_as_read_response.py">BatchMarkAsReadResponse</a></code>
- <code title="post /v1/messages/batch/seen">client.messages.batch.<a href="./src/knockapi/resources/messages/batch.py">mark_as_seen</a>(\*\*<a href="src/knockapi/types/messages/batch_mark_as_seen_params.py">params</a>) -> <a href="./src/knockapi/types/messages/batch_mark_as_seen_response.py">BatchMarkAsSeenResponse</a></code>
- <code title="post /v1/messages/batch/unread">client.messages.batch.<a href="./src/knockapi/resources/messages/batch.py">mark_as_unread</a>(\*\*<a href="src/knockapi/types/messages/batch_mark_as_unread_params.py">params</a>) -> <a href="./src/knockapi/types/messages/batch_mark_as_unread_response.py">BatchMarkAsUnreadResponse</a></code>
- <code title="post /v1/messages/batch/unseen">client.messages.batch.<a href="./src/knockapi/resources/messages/batch.py">mark_as_unseen</a>(\*\*<a href="src/knockapi/types/messages/batch_mark_as_unseen_params.py">params</a>) -> <a href="./src/knockapi/types/messages/batch_mark_as_unseen_response.py">BatchMarkAsUnseenResponse</a></code>
- <code title="post /v1/messages/batch/unarchived">client.messages.batch.<a href="./src/knockapi/resources/messages/batch.py">unarchive</a>(\*\*<a href="src/knockapi/types/messages/batch_unarchive_params.py">params</a>) -> <a href="./src/knockapi/types/messages/batch_unarchive_response.py">BatchUnarchiveResponse</a></code>

# Providers

## Slack

Types:

```python
from knockapi.types.providers import (
    SlackCheckAuthResponse,
    SlackListChannelsResponse,
    SlackRevokeAccessResponse,
)
```

Methods:

- <code title="get /v1/providers/slack/{channel_id}/auth_check">client.providers.slack.<a href="./src/knockapi/resources/providers/slack.py">check_auth</a>(channel_id, \*\*<a href="src/knockapi/types/providers/slack_check_auth_params.py">params</a>) -> <a href="./src/knockapi/types/providers/slack_check_auth_response.py">SlackCheckAuthResponse</a></code>
- <code title="get /v1/providers/slack/{channel_id}/channels">client.providers.slack.<a href="./src/knockapi/resources/providers/slack.py">list_channels</a>(channel_id, \*\*<a href="src/knockapi/types/providers/slack_list_channels_params.py">params</a>) -> <a href="./src/knockapi/types/providers/slack_list_channels_response.py">SyncSlackChannelsCursor[SlackListChannelsResponse]</a></code>
- <code title="put /v1/providers/slack/{channel_id}/revoke_access">client.providers.slack.<a href="./src/knockapi/resources/providers/slack.py">revoke_access</a>(channel_id, \*\*<a href="src/knockapi/types/providers/slack_revoke_access_params.py">params</a>) -> <a href="./src/knockapi/types/providers/slack_revoke_access_response.py">SlackRevokeAccessResponse</a></code>

## MsTeams

Types:

```python
from knockapi.types.providers import (
    MsTeamCheckAuthResponse,
    MsTeamListChannelsResponse,
    MsTeamListTeamsResponse,
    MsTeamRevokeAccessResponse,
)
```

Methods:

- <code title="get /v1/providers/ms-teams/{channel_id}/auth_check">client.providers.ms_teams.<a href="./src/knockapi/resources/providers/ms_teams.py">check_auth</a>(channel_id, \*\*<a href="src/knockapi/types/providers/ms_team_check_auth_params.py">params</a>) -> <a href="./src/knockapi/types/providers/ms_team_check_auth_response.py">MsTeamCheckAuthResponse</a></code>
- <code title="get /v1/providers/ms-teams/{channel_id}/channels">client.providers.ms_teams.<a href="./src/knockapi/resources/providers/ms_teams.py">list_channels</a>(channel_id, \*\*<a href="src/knockapi/types/providers/ms_team_list_channels_params.py">params</a>) -> <a href="./src/knockapi/types/providers/ms_team_list_channels_response.py">MsTeamListChannelsResponse</a></code>
- <code title="get /v1/providers/ms-teams/{channel_id}/teams">client.providers.ms_teams.<a href="./src/knockapi/resources/providers/ms_teams.py">list_teams</a>(channel_id, \*\*<a href="src/knockapi/types/providers/ms_team_list_teams_params.py">params</a>) -> <a href="./src/knockapi/types/providers/ms_team_list_teams_response.py">SyncMsTeamsPagination[MsTeamListTeamsResponse]</a></code>
- <code title="put /v1/providers/ms-teams/{channel_id}/revoke_access">client.providers.ms_teams.<a href="./src/knockapi/resources/providers/ms_teams.py">revoke_access</a>(channel_id, \*\*<a href="src/knockapi/types/providers/ms_team_revoke_access_params.py">params</a>) -> <a href="./src/knockapi/types/providers/ms_team_revoke_access_response.py">MsTeamRevokeAccessResponse</a></code>

# Integrations

## Census

Types:

```python
from knockapi.types.integrations import CensusCustomDestinationResponse
```

Methods:

- <code title="post /v1/integrations/census/custom-destination">client.integrations.census.<a href="./src/knockapi/resources/integrations/census.py">custom_destination</a>(\*\*<a href="src/knockapi/types/integrations/census_custom_destination_params.py">params</a>) -> <a href="./src/knockapi/types/integrations/census_custom_destination_response.py">CensusCustomDestinationResponse</a></code>

## Hightouch

Types:

```python
from knockapi.types.integrations import HightouchEmbeddedDestinationResponse
```

Methods:

- <code title="post /v1/integrations/hightouch/embedded-destination">client.integrations.hightouch.<a href="./src/knockapi/resources/integrations/hightouch.py">embedded_destination</a>(\*\*<a href="src/knockapi/types/integrations/hightouch_embedded_destination_params.py">params</a>) -> <a href="./src/knockapi/types/integrations/hightouch_embedded_destination_response.py">HightouchEmbeddedDestinationResponse</a></code>

# Workflows

Types:

```python
from knockapi.types import WorkflowCancelResponse, WorkflowTriggerResponse
```

Methods:

- <code title="post /v1/workflows/{key}/cancel">client.workflows.<a href="./src/knockapi/resources/workflows.py">cancel</a>(key, \*\*<a href="src/knockapi/types/workflow_cancel_params.py">params</a>) -> str</code>
- <code title="post /v1/workflows/{key}/trigger">client.workflows.<a href="./src/knockapi/resources/workflows.py">trigger</a>(key, \*\*<a href="src/knockapi/types/workflow_trigger_params.py">params</a>) -> <a href="./src/knockapi/types/workflow_trigger_response.py">WorkflowTriggerResponse</a></code>

# Schedules

Types:

```python
from knockapi.types import (
    Schedule,
    ScheduleRepeatRule,
    ScheduleCreateResponse,
    ScheduleUpdateResponse,
    ScheduleDeleteResponse,
)
```

Methods:

- <code title="post /v1/schedules">client.schedules.<a href="./src/knockapi/resources/schedules/schedules.py">create</a>(\*\*<a href="src/knockapi/types/schedule_create_params.py">params</a>) -> <a href="./src/knockapi/types/schedule_create_response.py">ScheduleCreateResponse</a></code>
- <code title="put /v1/schedules">client.schedules.<a href="./src/knockapi/resources/schedules/schedules.py">update</a>(\*\*<a href="src/knockapi/types/schedule_update_params.py">params</a>) -> <a href="./src/knockapi/types/schedule_update_response.py">ScheduleUpdateResponse</a></code>
- <code title="get /v1/schedules">client.schedules.<a href="./src/knockapi/resources/schedules/schedules.py">list</a>(\*\*<a href="src/knockapi/types/schedule_list_params.py">params</a>) -> <a href="./src/knockapi/types/schedule.py">SyncEntriesCursor[Schedule]</a></code>
- <code title="delete /v1/schedules">client.schedules.<a href="./src/knockapi/resources/schedules/schedules.py">delete</a>(\*\*<a href="src/knockapi/types/schedule_delete_params.py">params</a>) -> <a href="./src/knockapi/types/schedule_delete_response.py">ScheduleDeleteResponse</a></code>

## Bulk

Methods:

- <code title="post /v1/schedules/bulk/create">client.schedules.bulk.<a href="./src/knockapi/resources/schedules/bulk.py">create</a>(\*\*<a href="src/knockapi/types/schedules/bulk_create_params.py">params</a>) -> <a href="./src/knockapi/types/bulk_operation.py">BulkOperation</a></code>

# Channels

## Bulk

Methods:

- <code title="post /v1/channels/{channel_id}/messages/bulk/{action}">client.channels.bulk.<a href="./src/knockapi/resources/channels/bulk.py">update_message_status</a>(channel_id, action, \*\*<a href="src/knockapi/types/channels/bulk_update_message_status_params.py">params</a>) -> <a href="./src/knockapi/types/bulk_operation.py">BulkOperation</a></code>

# Audiences

Types:

```python
from knockapi.types import (
    AudienceMember,
    AudienceAddMembersResponse,
    AudienceListMembersResponse,
    AudienceRemoveMembersResponse,
)
```

Methods:

- <code title="post /v1/audiences/{key}/members">client.audiences.<a href="./src/knockapi/resources/audiences.py">add_members</a>(key, \*\*<a href="src/knockapi/types/audience_add_members_params.py">params</a>) -> str</code>
- <code title="get /v1/audiences/{key}/members">client.audiences.<a href="./src/knockapi/resources/audiences.py">list_members</a>(key) -> <a href="./src/knockapi/types/audience_list_members_response.py">AudienceListMembersResponse</a></code>
- <code title="delete /v1/audiences/{key}/members">client.audiences.<a href="./src/knockapi/resources/audiences.py">remove_members</a>(key, \*\*<a href="src/knockapi/types/audience_remove_members_params.py">params</a>) -> str</code>
