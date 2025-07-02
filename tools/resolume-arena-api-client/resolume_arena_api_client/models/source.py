from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_presets_item import SourcePresetsItem


T = TypeVar("T", bound="Source")


@_attrs_define
class Source:
    """A source to be used in a clip

    Attributes:
        idstring (Union[Unset, str]): The unique identifier for the source Example: A401.
        name (Union[Unset, str]): The descriptive name of the source Example: Gradient.
        presets (Union[Unset, list['SourcePresetsItem']]): All the presets for this source
    """

    idstring: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    presets: Union[Unset, list["SourcePresetsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idstring = self.idstring

        name = self.name

        presets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.presets, Unset):
            presets = []
            for presets_item_data in self.presets:
                presets_item = presets_item_data.to_dict()
                presets.append(presets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idstring is not UNSET:
            field_dict["idstring"] = idstring
        if name is not UNSET:
            field_dict["name"] = name
        if presets is not UNSET:
            field_dict["presets"] = presets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_presets_item import SourcePresetsItem

        d = dict(src_dict)
        idstring = d.pop("idstring", UNSET)

        name = d.pop("name", UNSET)

        presets = []
        _presets = d.pop("presets", UNSET)
        for presets_item_data in _presets or []:
            presets_item = SourcePresetsItem.from_dict(presets_item_data)

            presets.append(presets_item)

        source = cls(
            idstring=idstring,
            name=name,
            presets=presets,
        )

        source.additional_properties = d
        return source

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
