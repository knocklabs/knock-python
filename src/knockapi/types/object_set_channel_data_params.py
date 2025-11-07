# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .recipients.slack_channel_data_param import SlackChannelDataParam
from .recipients.discord_channel_data_param import DiscordChannelDataParam
from .recipients.ms_teams_channel_data_param import MsTeamsChannelDataParam
from .recipients.push_channel_data_tokens_only_param import PushChannelDataTokensOnlyParam
from .recipients.push_channel_data_devices_only_param import PushChannelDataDevicesOnlyParam
from .recipients.aws_sns_push_channel_data_devices_only_param import AwsSnsPushChannelDataDevicesOnlyParam
from .recipients.one_signal_channel_data_player_ids_only_param import OneSignalChannelDataPlayerIDsOnlyParam
from .recipients.aws_sns_push_channel_data_target_arns_only_param import AwsSnsPushChannelDataTargetArnsOnlyParam

__all__ = ["ObjectSetChannelDataParams", "Data"]


class ObjectSetChannelDataParams(TypedDict, total=False):
    data: Required[Data]
    """Channel data for a given channel type."""


Data: TypeAlias = Union[
    PushChannelDataTokensOnlyParam,
    PushChannelDataDevicesOnlyParam,
    AwsSnsPushChannelDataTargetArnsOnlyParam,
    AwsSnsPushChannelDataDevicesOnlyParam,
    OneSignalChannelDataPlayerIDsOnlyParam,
    SlackChannelDataParam,
    MsTeamsChannelDataParam,
    DiscordChannelDataParam,
]
