from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parameter_view_control_type import ParameterViewControlType
from ..models.parameter_view_display_units import ParameterViewDisplayUnits
from ..types import UNSET, Unset

T = TypeVar("T", bound="ParameterView")


@_attrs_define
class ParameterView:
    """Semantic information on the parameter, contains hints about how best to display the parameter

    Attributes:
        control_type (Union[Unset, ParameterViewControlType]): Which control to show for the parameter
        display_units (Union[Unset, ParameterViewDisplayUnits]): Which units to display.
        multiplier (Union[Unset, float]): Value to multiply with when displaying value. For a parameter with a value
            between 0 and 1 should display as 0 to 100 Example: 1.0.
        step (Union[Unset, float]): Value increments to be used for e.g. sliding or rotary controls Example: 1.0.
        suffix (Union[Unset, str]): The suffix to display for the variable. May be empty Example: %.
    """

    control_type: Union[Unset, ParameterViewControlType] = UNSET
    display_units: Union[Unset, ParameterViewDisplayUnits] = UNSET
    multiplier: Union[Unset, float] = UNSET
    step: Union[Unset, float] = UNSET
    suffix: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        control_type: Union[Unset, str] = UNSET
        if not isinstance(self.control_type, Unset):
            control_type = self.control_type.value

        display_units: Union[Unset, str] = UNSET
        if not isinstance(self.display_units, Unset):
            display_units = self.display_units.value

        multiplier = self.multiplier

        step = self.step

        suffix = self.suffix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_type is not UNSET:
            field_dict["control_type"] = control_type
        if display_units is not UNSET:
            field_dict["display_units"] = display_units
        if multiplier is not UNSET:
            field_dict["multiplier"] = multiplier
        if step is not UNSET:
            field_dict["step"] = step
        if suffix is not UNSET:
            field_dict["suffix"] = suffix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _control_type = d.pop("control_type", UNSET)
        control_type: Union[Unset, ParameterViewControlType]
        if isinstance(_control_type, Unset):
            control_type = UNSET
        else:
            control_type = ParameterViewControlType(_control_type)

        _display_units = d.pop("display_units", UNSET)
        display_units: Union[Unset, ParameterViewDisplayUnits]
        if isinstance(_display_units, Unset):
            display_units = UNSET
        else:
            display_units = ParameterViewDisplayUnits(_display_units)

        multiplier = d.pop("multiplier", UNSET)

        step = d.pop("step", UNSET)

        suffix = d.pop("suffix", UNSET)

        parameter_view = cls(
            control_type=control_type,
            display_units=display_units,
            multiplier=multiplier,
            step=step,
            suffix=suffix,
        )

        parameter_view.additional_properties = d
        return parameter_view

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
