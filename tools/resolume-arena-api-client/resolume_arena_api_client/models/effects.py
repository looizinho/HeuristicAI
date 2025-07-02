from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.effect import Effect


T = TypeVar("T", bound="Effects")


@_attrs_define
class Effects:
    """The available effects for clips, layer (group)s and the composition

    Attributes:
        video (Union[Unset, list['Effect']]): The available video effects
    """

    video: Union[Unset, list["Effect"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        video: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.video, Unset):
            video = []
            for video_item_data in self.video:
                video_item = video_item_data.to_dict()
                video.append(video_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if video is not UNSET:
            field_dict["video"] = video

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.effect import Effect

        d = dict(src_dict)
        video = []
        _video = d.pop("video", UNSET)
        for video_item_data in _video or []:
            video_item = Effect.from_dict(video_item_data)

            video.append(video_item)

        effects = cls(
            video=video,
        )

        effects.additional_properties = d
        return effects

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
