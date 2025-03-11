# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["SlackListChannelsResponse"]


class SlackListChannelsResponse(BaseModel):
    id: str

    context_team_id: str

    is_im: bool

    is_private: bool

    name: str
