# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "EntriesCursorPageInfo",
    "SyncEntriesCursor",
    "AsyncEntriesCursor",
    "ItemsCursorPageInfo",
    "SyncItemsCursor",
    "AsyncItemsCursor",
    "SyncSlackChannelsCursor",
    "AsyncSlackChannelsCursor",
    "SyncMsTeamsPagination",
    "AsyncMsTeamsPagination",
]

_T = TypeVar("_T")


class EntriesCursorPageInfo(BaseModel):
    after: Optional[str] = None


class SyncEntriesCursor(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    entries: List[_T]
    page_info: Optional[EntriesCursorPageInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        entries = self.entries
        if not entries:
            return []
        return entries

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        after = None
        if self.page_info is not None:
            if self.page_info.after is not None:
                after = self.page_info.after
        if not after:
            return None

        return PageInfo(params={"after": after})


class AsyncEntriesCursor(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    entries: List[_T]
    page_info: Optional[EntriesCursorPageInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        entries = self.entries
        if not entries:
            return []
        return entries

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        after = None
        if self.page_info is not None:
            if self.page_info.after is not None:
                after = self.page_info.after
        if not after:
            return None

        return PageInfo(params={"after": after})


class ItemsCursorPageInfo(BaseModel):
    after: Optional[str] = None


class SyncItemsCursor(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    page_info: Optional[ItemsCursorPageInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        after = None
        if self.page_info is not None:
            if self.page_info.after is not None:
                after = self.page_info.after
        if not after:
            return None

        return PageInfo(params={"after": after})


class AsyncItemsCursor(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    page_info: Optional[ItemsCursorPageInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        after = None
        if self.page_info is not None:
            if self.page_info.after is not None:
                after = self.page_info.after
        if not after:
            return None

        return PageInfo(params={"after": after})


class SyncSlackChannelsCursor(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    next_cursor: Optional[str] = None
    slack_channels: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        slack_channels = self.slack_channels
        if not slack_channels:
            return []
        return slack_channels

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"query_options.cursor": next_cursor})


class AsyncSlackChannelsCursor(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    next_cursor: Optional[str] = None
    slack_channels: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        slack_channels = self.slack_channels
        if not slack_channels:
            return []
        return slack_channels

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"query_options.cursor": next_cursor})


class SyncMsTeamsPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    skip_token: Optional[str] = None
    ms_teams_teams: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        ms_teams_teams = self.ms_teams_teams
        if not ms_teams_teams:
            return []
        return ms_teams_teams

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        skip_token = self.skip_token
        if not skip_token:
            return None

        return PageInfo(params={"query_options.$skiptoken": skip_token})


class AsyncMsTeamsPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    skip_token: Optional[str] = None
    ms_teams_teams: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        ms_teams_teams = self.ms_teams_teams
        if not ms_teams_teams:
            return []
        return ms_teams_teams

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        skip_token = self.skip_token
        if not skip_token:
            return None

        return PageInfo(params={"query_options.$skiptoken": skip_token})
