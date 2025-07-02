from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.choice_parameter import ChoiceParameter
    from ..models.range_parameter import RangeParameter


T = TypeVar("T", bound="LayerTransition")


@_attrs_define
class LayerTransition:
    """A layer transition describes the transition between clips within the layer

    Attributes:
        blend_mode (Union[Unset, ChoiceParameter]): A multiple-choice parameter
        duration (Union[Unset, RangeParameter]): A parameter containing a floating-point value with a minimum and
            maximum allowed value.
    """

    blend_mode: Union[Unset, "ChoiceParameter"] = UNSET
    duration: Union[Unset, "RangeParameter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blend_mode: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.blend_mode, Unset):
            blend_mode = self.blend_mode.to_dict()

        duration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blend_mode is not UNSET:
            field_dict["blend_mode"] = blend_mode
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.choice_parameter import ChoiceParameter
        from ..models.range_parameter import RangeParameter

        d = dict(src_dict)
        _blend_mode = d.pop("blend_mode", UNSET)
        blend_mode: Union[Unset, ChoiceParameter]
        if isinstance(_blend_mode, Unset):
            blend_mode = UNSET
        else:
            blend_mode = ChoiceParameter.from_dict(_blend_mode)

        _duration = d.pop("duration", UNSET)
        duration: Union[Unset, RangeParameter]
        if isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = RangeParameter.from_dict(_duration)

        layer_transition = cls(
            blend_mode=blend_mode,
            duration=duration,
        )

        layer_transition.additional_properties = d
        return layer_transition

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
