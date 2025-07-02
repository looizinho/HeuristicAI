from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parameter_collection import ParameterCollection
    from ..models.video_effect_bypassed import VideoEffectBypassed


T = TypeVar("T", bound="VideoEffect")


@_attrs_define
class VideoEffect:
    """A videoeffect represents a single effect in a chain of effects to be applied to a source. Properties on the
    videoeffect control how and what is rendered in the effect.

        Attributes:
            bypassed (Union[Unset, VideoEffectBypassed]):
            display_name (Union[Unset, str]): The name to show the user Example: ChromaKey.
            effect (Union[Unset, ParameterCollection]): An unstructured collection of parameters. Parameters are presented
                as a map where the key is the name of the parameter and the value is the parameter itself. Parameters may be any
                valid parameter type.
            id (Union[Unset, int]): The unique id of the video effect instance Example: 1723069642348.
            mixer (Union[Unset, ParameterCollection]): An unstructured collection of parameters. Parameters are presented as
                a map where the key is the name of the parameter and the value is the parameter itself. Parameters may be any
                valid parameter type.
            name (Union[Unset, str]): The unique name of the key Example: ChromaKey.
            params (Union[Unset, ParameterCollection]): An unstructured collection of parameters. Parameters are presented
                as a map where the key is the name of the parameter and the value is the parameter itself. Parameters may be any
                valid parameter type.
    """

    bypassed: Union[Unset, "VideoEffectBypassed"] = UNSET
    display_name: Union[Unset, str] = UNSET
    effect: Union[Unset, "ParameterCollection"] = UNSET
    id: Union[Unset, int] = UNSET
    mixer: Union[Unset, "ParameterCollection"] = UNSET
    name: Union[Unset, str] = UNSET
    params: Union[Unset, "ParameterCollection"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bypassed: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bypassed, Unset):
            bypassed = self.bypassed.to_dict()

        display_name = self.display_name

        effect: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.effect, Unset):
            effect = self.effect.to_dict()

        id = self.id

        mixer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mixer, Unset):
            mixer = self.mixer.to_dict()

        name = self.name

        params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bypassed is not UNSET:
            field_dict["bypassed"] = bypassed
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if effect is not UNSET:
            field_dict["effect"] = effect
        if id is not UNSET:
            field_dict["id"] = id
        if mixer is not UNSET:
            field_dict["mixer"] = mixer
        if name is not UNSET:
            field_dict["name"] = name
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parameter_collection import ParameterCollection
        from ..models.video_effect_bypassed import VideoEffectBypassed

        d = dict(src_dict)
        _bypassed = d.pop("bypassed", UNSET)
        bypassed: Union[Unset, VideoEffectBypassed]
        if isinstance(_bypassed, Unset):
            bypassed = UNSET
        else:
            bypassed = VideoEffectBypassed.from_dict(_bypassed)

        display_name = d.pop("display_name", UNSET)

        _effect = d.pop("effect", UNSET)
        effect: Union[Unset, ParameterCollection]
        if isinstance(_effect, Unset):
            effect = UNSET
        else:
            effect = ParameterCollection.from_dict(_effect)

        id = d.pop("id", UNSET)

        _mixer = d.pop("mixer", UNSET)
        mixer: Union[Unset, ParameterCollection]
        if isinstance(_mixer, Unset):
            mixer = UNSET
        else:
            mixer = ParameterCollection.from_dict(_mixer)

        name = d.pop("name", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, ParameterCollection]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = ParameterCollection.from_dict(_params)

        video_effect = cls(
            bypassed=bypassed,
            display_name=display_name,
            effect=effect,
            id=id,
            mixer=mixer,
            name=name,
            params=params,
        )

        video_effect.additional_properties = d
        return video_effect

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
