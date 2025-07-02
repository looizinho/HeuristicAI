from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parameter_collection import ParameterCollection
    from ..models.range_parameter import RangeParameter
    from ..models.video_effect import VideoEffect


T = TypeVar("T", bound="VideoTrackType0")


@_attrs_define
class VideoTrackType0:
    """A video track, as part of a clip,layer,group or a composition

    Attributes:
        effects (Union[Unset, list['VideoEffect']]): All the effects that may be applied when the video track is played
        height (Union[Unset, RangeParameter]): A parameter containing a floating-point value with a minimum and maximum
            allowed value.
        mixer (Union[Unset, ParameterCollection]): An unstructured collection of parameters. Parameters are presented as
            a map where the key is the name of the parameter and the value is the parameter itself. Parameters may be any
            valid parameter type.
        opacity (Union[Unset, RangeParameter]): A parameter containing a floating-point value with a minimum and maximum
            allowed value.
        width (Union[Unset, RangeParameter]): A parameter containing a floating-point value with a minimum and maximum
            allowed value.
    """

    effects: Union[Unset, list["VideoEffect"]] = UNSET
    height: Union[Unset, "RangeParameter"] = UNSET
    mixer: Union[Unset, "ParameterCollection"] = UNSET
    opacity: Union[Unset, "RangeParameter"] = UNSET
    width: Union[Unset, "RangeParameter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effects: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.effects, Unset):
            effects = []
            for effects_item_data in self.effects:
                effects_item = effects_item_data.to_dict()
                effects.append(effects_item)

        height: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.height, Unset):
            height = self.height.to_dict()

        mixer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mixer, Unset):
            mixer = self.mixer.to_dict()

        opacity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.opacity, Unset):
            opacity = self.opacity.to_dict()

        width: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.width, Unset):
            width = self.width.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if effects is not UNSET:
            field_dict["effects"] = effects
        if height is not UNSET:
            field_dict["height"] = height
        if mixer is not UNSET:
            field_dict["mixer"] = mixer
        if opacity is not UNSET:
            field_dict["opacity"] = opacity
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parameter_collection import ParameterCollection
        from ..models.range_parameter import RangeParameter
        from ..models.video_effect import VideoEffect

        d = dict(src_dict)
        effects = []
        _effects = d.pop("effects", UNSET)
        for effects_item_data in _effects or []:
            effects_item = VideoEffect.from_dict(effects_item_data)

            effects.append(effects_item)

        _height = d.pop("height", UNSET)
        height: Union[Unset, RangeParameter]
        if isinstance(_height, Unset):
            height = UNSET
        else:
            height = RangeParameter.from_dict(_height)

        _mixer = d.pop("mixer", UNSET)
        mixer: Union[Unset, ParameterCollection]
        if isinstance(_mixer, Unset):
            mixer = UNSET
        else:
            mixer = ParameterCollection.from_dict(_mixer)

        _opacity = d.pop("opacity", UNSET)
        opacity: Union[Unset, RangeParameter]
        if isinstance(_opacity, Unset):
            opacity = UNSET
        else:
            opacity = RangeParameter.from_dict(_opacity)

        _width = d.pop("width", UNSET)
        width: Union[Unset, RangeParameter]
        if isinstance(_width, Unset):
            width = UNSET
        else:
            width = RangeParameter.from_dict(_width)

        video_track_type_0 = cls(
            effects=effects,
            height=height,
            mixer=mixer,
            opacity=opacity,
            width=width,
        )

        video_track_type_0.additional_properties = d
        return video_track_type_0

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
