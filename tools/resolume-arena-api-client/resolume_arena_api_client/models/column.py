from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.boolean_parameter import BooleanParameter
    from ..models.choice_parameter import ChoiceParameter
    from ..models.string_parameter import StringParameter


T = TypeVar("T", bound="Column")


@_attrs_define
class Column:
    """A column within a deck

    Attributes:
        colorid (Union[Unset, ChoiceParameter]): A multiple-choice parameter
        connected (Union[Unset, ChoiceParameter]): A multiple-choice parameter
        id (Union[Unset, int]): The unique identifier of the column Example: 1641549605447.
        name (Union[Unset, StringParameter]): A parameter containing string data
        selected (Union[Unset, BooleanParameter]): A parameter containing a true or false value
    """

    colorid: Union[Unset, "ChoiceParameter"] = UNSET
    connected: Union[Unset, "ChoiceParameter"] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, "StringParameter"] = UNSET
    selected: Union[Unset, "BooleanParameter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        colorid: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.colorid, Unset):
            colorid = self.colorid.to_dict()

        connected: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.connected, Unset):
            connected = self.connected.to_dict()

        id = self.id

        name: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        selected: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.selected, Unset):
            selected = self.selected.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if colorid is not UNSET:
            field_dict["colorid"] = colorid
        if connected is not UNSET:
            field_dict["connected"] = connected
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if selected is not UNSET:
            field_dict["selected"] = selected

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boolean_parameter import BooleanParameter
        from ..models.choice_parameter import ChoiceParameter
        from ..models.string_parameter import StringParameter

        d = dict(src_dict)
        _colorid = d.pop("colorid", UNSET)
        colorid: Union[Unset, ChoiceParameter]
        if isinstance(_colorid, Unset):
            colorid = UNSET
        else:
            colorid = ChoiceParameter.from_dict(_colorid)

        _connected = d.pop("connected", UNSET)
        connected: Union[Unset, ChoiceParameter]
        if isinstance(_connected, Unset):
            connected = UNSET
        else:
            connected = ChoiceParameter.from_dict(_connected)

        id = d.pop("id", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, StringParameter]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = StringParameter.from_dict(_name)

        _selected = d.pop("selected", UNSET)
        selected: Union[Unset, BooleanParameter]
        if isinstance(_selected, Unset):
            selected = UNSET
        else:
            selected = BooleanParameter.from_dict(_selected)

        column = cls(
            colorid=colorid,
            connected=connected,
            id=id,
            name=name,
            selected=selected,
        )

        column.additional_properties = d
        return column

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
