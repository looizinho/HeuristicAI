from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.boolean_parameter import BooleanParameter
    from ..models.choice_parameter import ChoiceParameter
    from ..models.integer_parameter import IntegerParameter
    from ..models.string_parameter import StringParameter


T = TypeVar("T", bound="Deck")


@_attrs_define
class Deck:
    """A deck contains a full set of layers and clips. Only the layers and clips of the active deck can be retrieved and
    updated.

        Attributes:
            closed (Union[Unset, bool]): Is this deck closed
            colorid (Union[Unset, ChoiceParameter]): A multiple-choice parameter
            id (Union[Unset, int]): The unique identifier of the deck Example: 1641549604727.
            name (Union[Unset, StringParameter]): A parameter containing string data
            scrollx (Union[Unset, IntegerParameter]): A parameter containing numeric data
            selected (Union[Unset, BooleanParameter]): A parameter containing a true or false value
    """

    closed: Union[Unset, bool] = UNSET
    colorid: Union[Unset, "ChoiceParameter"] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, "StringParameter"] = UNSET
    scrollx: Union[Unset, "IntegerParameter"] = UNSET
    selected: Union[Unset, "BooleanParameter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        closed = self.closed

        colorid: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.colorid, Unset):
            colorid = self.colorid.to_dict()

        id = self.id

        name: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        scrollx: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.scrollx, Unset):
            scrollx = self.scrollx.to_dict()

        selected: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.selected, Unset):
            selected = self.selected.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if closed is not UNSET:
            field_dict["closed"] = closed
        if colorid is not UNSET:
            field_dict["colorid"] = colorid
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if scrollx is not UNSET:
            field_dict["scrollx"] = scrollx
        if selected is not UNSET:
            field_dict["selected"] = selected

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boolean_parameter import BooleanParameter
        from ..models.choice_parameter import ChoiceParameter
        from ..models.integer_parameter import IntegerParameter
        from ..models.string_parameter import StringParameter

        d = dict(src_dict)
        closed = d.pop("closed", UNSET)

        _colorid = d.pop("colorid", UNSET)
        colorid: Union[Unset, ChoiceParameter]
        if isinstance(_colorid, Unset):
            colorid = UNSET
        else:
            colorid = ChoiceParameter.from_dict(_colorid)

        id = d.pop("id", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, StringParameter]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = StringParameter.from_dict(_name)

        _scrollx = d.pop("scrollx", UNSET)
        scrollx: Union[Unset, IntegerParameter]
        if isinstance(_scrollx, Unset):
            scrollx = UNSET
        else:
            scrollx = IntegerParameter.from_dict(_scrollx)

        _selected = d.pop("selected", UNSET)
        selected: Union[Unset, BooleanParameter]
        if isinstance(_selected, Unset):
            selected = UNSET
        else:
            selected = BooleanParameter.from_dict(_selected)

        deck = cls(
            closed=closed,
            colorid=colorid,
            id=id,
            name=name,
            scrollx=scrollx,
            selected=selected,
        )

        deck.additional_properties = d
        return deck

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
