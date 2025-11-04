# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import TypeAlias

from .slack_channel_data_param import SlackChannelDataParam
from .discord_channel_data_param import DiscordChannelDataParam
from .ms_teams_channel_data_param import MsTeamsChannelDataParam
from .push_channel_data_tokens_only_param import PushChannelDataTokensOnlyParam
from .push_channel_data_devices_only_param import PushChannelDataDevicesOnlyParam
from .aws_sns_push_channel_data_devices_only_param import AwsSnsPushChannelDataDevicesOnlyParam
from .one_signal_channel_data_player_ids_only_param import OneSignalChannelDataPlayerIDsOnlyParam
from .aws_sns_push_channel_data_target_arns_only_param import AwsSnsPushChannelDataTargetArnsOnlyParam

__all__ = ["InlineChannelDataRequestParam", "InlineChannelDataRequestParamItem"]

InlineChannelDataRequestParamItem: TypeAlias = Union[
    PushChannelDataTokensOnlyParam,
    PushChannelDataDevicesOnlyParam,
    AwsSnsPushChannelDataTargetArnsOnlyParam,
    AwsSnsPushChannelDataDevicesOnlyParam,
    OneSignalChannelDataPlayerIDsOnlyParam,
    SlackChannelDataParam,
    MsTeamsChannelDataParam,
    DiscordChannelDataParam,
]

InlineChannelDataRequestParam: TypeAlias = Dict[str, InlineChannelDataRequestParamItem]
