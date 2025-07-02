from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrameRate")


@_attrs_define
class FrameRate:
    """Frame rate expressed as ratio

    Attributes:
        denom (Union[Unset, int]): Denominator Example: 1001.
        num (Union[Unset, int]): Numerator Example: 24000.
    """

    denom: Union[Unset, int] = UNSET
    num: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        denom = self.denom

        num = self.num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if denom is not UNSET:
            field_dict["denom"] = denom
        if num is not UNSET:
            field_dict["num"] = num

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        denom = d.pop("denom", UNSET)

        num = d.pop("num", UNSET)

        frame_rate = cls(
            denom=denom,
            num=num,
        )

        frame_rate.additional_properties = d
        return frame_rate

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
