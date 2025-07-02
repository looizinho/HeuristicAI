from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parameter_view import ParameterView


T = TypeVar("T", bound="TextParameter")


@_attrs_define
class TextParameter:
    """A parameter containing string data, possibly multiline

    Attributes:
        id (Union[Unset, int]): The unique identifier of the parameter Example: 1638334400287.
        value (Union[Unset, Any]): The value for the parameter Example: Some
            Multiline
            String
            .
        valuetype (Union[Unset, str]): The parameter type. This is "ParamText" for this type Example: ParamText.
        view (Union[Unset, ParameterView]): Semantic information on the parameter, contains hints about how best to
            display the parameter
    """

    id: Union[Unset, int] = UNSET
    value: Union[Unset, Any] = UNSET
    valuetype: Union[Unset, str] = UNSET
    view: Union[Unset, "ParameterView"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        value = self.value

        valuetype = self.valuetype

        view: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.view, Unset):
            view = self.view.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value
        if valuetype is not UNSET:
            field_dict["valuetype"] = valuetype
        if view is not UNSET:
            field_dict["view"] = view

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parameter_view import ParameterView

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        valuetype = d.pop("valuetype", UNSET)

        _view = d.pop("view", UNSET)
        view: Union[Unset, ParameterView]
        if isinstance(_view, Unset):
            view = UNSET
        else:
            view = ParameterView.from_dict(_view)

        text_parameter = cls(
            id=id,
            value=value,
            valuetype=valuetype,
            view=view,
        )

        text_parameter.additional_properties = d
        return text_parameter

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
