from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResetParameter")


@_attrs_define
class ResetParameter:
    """Options for resetting a parameter, should only the value be reset, or should animations also be reset

    Attributes:
        resetanimation (Union[Unset, bool]): If set to true, animations are also reset
    """

    resetanimation: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resetanimation = self.resetanimation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resetanimation is not UNSET:
            field_dict["resetanimation"] = resetanimation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resetanimation = d.pop("resetanimation", UNSET)

        reset_parameter = cls(
            resetanimation=resetanimation,
        )

        reset_parameter.additional_properties = d
        return reset_parameter

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
