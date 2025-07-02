from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.boolean_parameter import BooleanParameter
    from ..models.parameter_collection import ParameterCollection


T = TypeVar("T", bound="AudioEffect")


@_attrs_define
class AudioEffect:
    """An audioeffect represents a single effect in a chain of effects to be applied to a source. Properties on the
    audioeffect control how and what is rendered in the effect.

        Attributes:
            bypassed (Union[Unset, BooleanParameter]): A parameter containing a true or false value
            id (Union[Unset, int]): The unique id of the audio effect instance
            name (Union[Unset, str]): The name of the effect Example: Distortion.
            params (Union[Unset, ParameterCollection]): An unstructured collection of parameters. Parameters are presented
                as a map where the key is the name of the parameter and the value is the parameter itself. Parameters may be any
                valid parameter type.
    """

    bypassed: Union[Unset, "BooleanParameter"] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    params: Union[Unset, "ParameterCollection"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bypassed: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bypassed, Unset):
            bypassed = self.bypassed.to_dict()

        id = self.id

        name = self.name

        params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bypassed is not UNSET:
            field_dict["bypassed"] = bypassed
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boolean_parameter import BooleanParameter
        from ..models.parameter_collection import ParameterCollection

        d = dict(src_dict)
        _bypassed = d.pop("bypassed", UNSET)
        bypassed: Union[Unset, BooleanParameter]
        if isinstance(_bypassed, Unset):
            bypassed = UNSET
        else:
            bypassed = BooleanParameter.from_dict(_bypassed)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, ParameterCollection]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = ParameterCollection.from_dict(_params)

        audio_effect = cls(
            bypassed=bypassed,
            id=id,
            name=name,
            params=params,
        )

        audio_effect.additional_properties = d
        return audio_effect

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
