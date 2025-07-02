from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parameter_view import ParameterView


T = TypeVar("T", bound="ChoiceParameter")


@_attrs_define
class ChoiceParameter:
    """A multiple-choice parameter

    Attributes:
        id (Union[Unset, int]): The unique identifier of the parameter Example: 1673448923421.
        index (Union[Unset, int]): The index of the selected option within the options
        options (Union[Unset, list[str]]): The list of available options for the parameter Example: ['Option 1', 'Option
            2', 'Option 3'].
        value (Union[Unset, str]): The value of the selected option Example: Option 1.
        valuetype (Union[Unset, str]): The parameter type. This is "ParamChoice" or "ParamState" for this type Example:
            ParamChoice.
        view (Union[Unset, ParameterView]): Semantic information on the parameter, contains hints about how best to
            display the parameter
    """

    id: Union[Unset, int] = UNSET
    index: Union[Unset, int] = UNSET
    options: Union[Unset, list[str]] = UNSET
    value: Union[Unset, str] = UNSET
    valuetype: Union[Unset, str] = UNSET
    view: Union[Unset, "ParameterView"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        index = self.index

        options: Union[Unset, list[str]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

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
        if index is not UNSET:
            field_dict["index"] = index
        if options is not UNSET:
            field_dict["options"] = options
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

        index = d.pop("index", UNSET)

        options = cast(list[str], d.pop("options", UNSET))

        value = d.pop("value", UNSET)

        valuetype = d.pop("valuetype", UNSET)

        _view = d.pop("view", UNSET)
        view: Union[Unset, ParameterView]
        if isinstance(_view, Unset):
            view = UNSET
        else:
            view = ParameterView.from_dict(_view)

        choice_parameter = cls(
            id=id,
            index=index,
            options=options,
            value=value,
            valuetype=valuetype,
            view=view,
        )

        choice_parameter.additional_properties = d
        return choice_parameter

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
