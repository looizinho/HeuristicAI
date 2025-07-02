from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audio_effect import AudioEffect
    from ..models.range_parameter import RangeParameter


T = TypeVar("T", bound="AudioTrackType0")


@_attrs_define
class AudioTrackType0:
    """An audio track, as part of a clip,layer,group or a composition

    Attributes:
        effects (Union[Unset, list['AudioEffect']]): All the effects that may be applied when the audio track is played
        pan (Union[Unset, RangeParameter]): A parameter containing a floating-point value with a minimum and maximum
            allowed value.
        volume (Union[Unset, RangeParameter]): A parameter containing a floating-point value with a minimum and maximum
            allowed value.
    """

    effects: Union[Unset, list["AudioEffect"]] = UNSET
    pan: Union[Unset, "RangeParameter"] = UNSET
    volume: Union[Unset, "RangeParameter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effects: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.effects, Unset):
            effects = []
            for effects_item_data in self.effects:
                effects_item = effects_item_data.to_dict()
                effects.append(effects_item)

        pan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pan, Unset):
            pan = self.pan.to_dict()

        volume: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.volume, Unset):
            volume = self.volume.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if effects is not UNSET:
            field_dict["effects"] = effects
        if pan is not UNSET:
            field_dict["pan"] = pan
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audio_effect import AudioEffect
        from ..models.range_parameter import RangeParameter

        d = dict(src_dict)
        effects = []
        _effects = d.pop("effects", UNSET)
        for effects_item_data in _effects or []:
            effects_item = AudioEffect.from_dict(effects_item_data)

            effects.append(effects_item)

        _pan = d.pop("pan", UNSET)
        pan: Union[Unset, RangeParameter]
        if isinstance(_pan, Unset):
            pan = UNSET
        else:
            pan = RangeParameter.from_dict(_pan)

        _volume = d.pop("volume", UNSET)
        volume: Union[Unset, RangeParameter]
        if isinstance(_volume, Unset):
            volume = UNSET
        else:
            volume = RangeParameter.from_dict(_volume)

        audio_track_type_0 = cls(
            effects=effects,
            pan=pan,
            volume=volume,
        )

        audio_track_type_0.additional_properties = d
        return audio_track_type_0

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
