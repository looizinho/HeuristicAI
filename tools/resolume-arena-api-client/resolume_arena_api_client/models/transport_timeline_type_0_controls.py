from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.choice_parameter import ChoiceParameter
    from ..models.range_parameter import RangeParameter


T = TypeVar("T", bound="TransportTimelineType0Controls")


@_attrs_define
class TransportTimelineType0Controls:
    """Timeline controls

    Attributes:
        duration (Union[Unset, RangeParameter]): A parameter containing a floating-point value with a minimum and
            maximum allowed value.
        playdirection (Union[Unset, ChoiceParameter]): A multiple-choice parameter
        playmode (Union[Unset, ChoiceParameter]): A multiple-choice parameter
        playmodeaway (Union[Unset, ChoiceParameter]): A multiple-choice parameter
        speed (Union[Unset, RangeParameter]): A parameter containing a floating-point value with a minimum and maximum
            allowed value.
    """

    duration: Union[Unset, "RangeParameter"] = UNSET
    playdirection: Union[Unset, "ChoiceParameter"] = UNSET
    playmode: Union[Unset, "ChoiceParameter"] = UNSET
    playmodeaway: Union[Unset, "ChoiceParameter"] = UNSET
    speed: Union[Unset, "RangeParameter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.to_dict()

        playdirection: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.playdirection, Unset):
            playdirection = self.playdirection.to_dict()

        playmode: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.playmode, Unset):
            playmode = self.playmode.to_dict()

        playmodeaway: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.playmodeaway, Unset):
            playmodeaway = self.playmodeaway.to_dict()

        speed: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.speed, Unset):
            speed = self.speed.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration is not UNSET:
            field_dict["duration"] = duration
        if playdirection is not UNSET:
            field_dict["playdirection"] = playdirection
        if playmode is not UNSET:
            field_dict["playmode"] = playmode
        if playmodeaway is not UNSET:
            field_dict["playmodeaway"] = playmodeaway
        if speed is not UNSET:
            field_dict["speed"] = speed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.choice_parameter import ChoiceParameter
        from ..models.range_parameter import RangeParameter

        d = dict(src_dict)
        _duration = d.pop("duration", UNSET)
        duration: Union[Unset, RangeParameter]
        if isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = RangeParameter.from_dict(_duration)

        _playdirection = d.pop("playdirection", UNSET)
        playdirection: Union[Unset, ChoiceParameter]
        if isinstance(_playdirection, Unset):
            playdirection = UNSET
        else:
            playdirection = ChoiceParameter.from_dict(_playdirection)

        _playmode = d.pop("playmode", UNSET)
        playmode: Union[Unset, ChoiceParameter]
        if isinstance(_playmode, Unset):
            playmode = UNSET
        else:
            playmode = ChoiceParameter.from_dict(_playmode)

        _playmodeaway = d.pop("playmodeaway", UNSET)
        playmodeaway: Union[Unset, ChoiceParameter]
        if isinstance(_playmodeaway, Unset):
            playmodeaway = UNSET
        else:
            playmodeaway = ChoiceParameter.from_dict(_playmodeaway)

        _speed = d.pop("speed", UNSET)
        speed: Union[Unset, RangeParameter]
        if isinstance(_speed, Unset):
            speed = UNSET
        else:
            speed = RangeParameter.from_dict(_speed)

        transport_timeline_type_0_controls = cls(
            duration=duration,
            playdirection=playdirection,
            playmode=playmode,
            playmodeaway=playmodeaway,
            speed=speed,
        )

        transport_timeline_type_0_controls.additional_properties = d
        return transport_timeline_type_0_controls

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
