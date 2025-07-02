from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frame_rate import FrameRate


T = TypeVar("T", bound="VideoFileInfoType0")


@_attrs_define
class VideoFileInfoType0:
    """Meta information for a video file

    Attributes:
        duration (Union[Unset, str]): Duration of file expressed as hours:seconds:minutes:milliseconds Example:
            00:00:19.06.
        duration_ms (Union[Unset, float]): Duration of file expressed as milliseconds Example: 19269.249999999996.
        exists (Union[Unset, bool]): Whether file is actually present on disk at the given location Example: True.
        framerate (Union[Unset, FrameRate]): Frame rate expressed as ratio
        height (Union[Unset, int]): The number of pixels the video is high Example: 1080.
        path (Union[Unset, str]): The location of the file on disk Example: /Users/Resolume/Videos/Clip1.mov.
        width (Union[Unset, int]): The number of pixels the video is wide Example: 1920.
    """

    duration: Union[Unset, str] = UNSET
    duration_ms: Union[Unset, float] = UNSET
    exists: Union[Unset, bool] = UNSET
    framerate: Union[Unset, "FrameRate"] = UNSET
    height: Union[Unset, int] = UNSET
    path: Union[Unset, str] = UNSET
    width: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration = self.duration

        duration_ms = self.duration_ms

        exists = self.exists

        framerate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.framerate, Unset):
            framerate = self.framerate.to_dict()

        height = self.height

        path = self.path

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration is not UNSET:
            field_dict["duration"] = duration
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if exists is not UNSET:
            field_dict["exists"] = exists
        if framerate is not UNSET:
            field_dict["framerate"] = framerate
        if height is not UNSET:
            field_dict["height"] = height
        if path is not UNSET:
            field_dict["path"] = path
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frame_rate import FrameRate

        d = dict(src_dict)
        duration = d.pop("duration", UNSET)

        duration_ms = d.pop("duration_ms", UNSET)

        exists = d.pop("exists", UNSET)

        _framerate = d.pop("framerate", UNSET)
        framerate: Union[Unset, FrameRate]
        if isinstance(_framerate, Unset):
            framerate = UNSET
        else:
            framerate = FrameRate.from_dict(_framerate)

        height = d.pop("height", UNSET)

        path = d.pop("path", UNSET)

        width = d.pop("width", UNSET)

        video_file_info_type_0 = cls(
            duration=duration,
            duration_ms=duration_ms,
            exists=exists,
            framerate=framerate,
            height=height,
            path=path,
            width=width,
        )

        video_file_info_type_0.additional_properties = d
        return video_file_info_type_0

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
