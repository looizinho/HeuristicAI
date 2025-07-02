from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AudioFileInfoType0")


@_attrs_define
class AudioFileInfoType0:
    """Meta information for an audio file

    Attributes:
        bpm (Union[Unset, float]): Bpm rate expressed in beats
        duration (Union[Unset, str]): Duration of file expressed as hours:seconds:minutes:milliseconds Example:
            00:12:08.085.
        duration_ms (Union[Unset, float]): Duration of file expressed as milliseconds Example: 728084.8979591837.
        exists (Union[Unset, bool]): Whether file is actully present on disk at the given location Example: True.
        num_channels (Union[Unset, int]): Number of audio channels Example: 2.
        path (Union[Unset, str]): The location of the file on disk Example: /Users/Resolume/Music/Track1.wav.
        sample_rate (Union[Unset, float]): Sample rate expressed in Hertz Example: 44100.
    """

    bpm: Union[Unset, float] = UNSET
    duration: Union[Unset, str] = UNSET
    duration_ms: Union[Unset, float] = UNSET
    exists: Union[Unset, bool] = UNSET
    num_channels: Union[Unset, int] = UNSET
    path: Union[Unset, str] = UNSET
    sample_rate: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bpm = self.bpm

        duration = self.duration

        duration_ms = self.duration_ms

        exists = self.exists

        num_channels = self.num_channels

        path = self.path

        sample_rate = self.sample_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bpm is not UNSET:
            field_dict["bpm"] = bpm
        if duration is not UNSET:
            field_dict["duration"] = duration
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if exists is not UNSET:
            field_dict["exists"] = exists
        if num_channels is not UNSET:
            field_dict["num_channels"] = num_channels
        if path is not UNSET:
            field_dict["path"] = path
        if sample_rate is not UNSET:
            field_dict["sample_rate"] = sample_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bpm = d.pop("bpm", UNSET)

        duration = d.pop("duration", UNSET)

        duration_ms = d.pop("duration_ms", UNSET)

        exists = d.pop("exists", UNSET)

        num_channels = d.pop("num_channels", UNSET)

        path = d.pop("path", UNSET)

        sample_rate = d.pop("sample_rate", UNSET)

        audio_file_info_type_0 = cls(
            bpm=bpm,
            duration=duration,
            duration_ms=duration_ms,
            exists=exists,
            num_channels=num_channels,
            path=path,
            sample_rate=sample_rate,
        )

        audio_file_info_type_0.additional_properties = d
        return audio_file_info_type_0

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
