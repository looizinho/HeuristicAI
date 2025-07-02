from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.choice_parameter import ChoiceParameter


T = TypeVar("T", bound="AutoPilotType0")


@_attrs_define
class AutoPilotType0:
    """AutoPilot options to control automatic clip transitions

    Attributes:
        target (Union[Unset, ChoiceParameter]): A multiple-choice parameter
    """

    target: Union[Unset, "ChoiceParameter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.choice_parameter import ChoiceParameter

        d = dict(src_dict)
        _target = d.pop("target", UNSET)
        target: Union[Unset, ChoiceParameter]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = ChoiceParameter.from_dict(_target)

        auto_pilot_type_0 = cls(
            target=target,
        )

        auto_pilot_type_0.additional_properties = d
        return auto_pilot_type_0

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
