from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parameter_view import ParameterView


T = TypeVar("T", bound="RangeParameter")


@_attrs_define
class RangeParameter:
    """A parameter containing a floating-point value with a minimum and maximum allowed value.

    Attributes:
        id (Union[Unset, int]): The unique identifier of the parameter Example: 1824357891293.
        in_ (Union[Unset, float]): The lowest value we clamped the range to, inclusive Example: 25.0.
        max_ (Union[Unset, float]): The highest allowed value for the parameter, inclusive Example: 100.0.
        min_ (Union[Unset, float]): The lowest allowed value for the parameter, inclusive
        out (Union[Unset, float]): The highest value we clamped the range to, inclusive Example: 75.0.
        value (Union[Unset, float]): The value for the parameter Example: 50.0.
        valuetype (Union[Unset, str]): The parameter type. This is "ParamRange" for this type Example: ParamRange.
        view (Union[Unset, ParameterView]): Semantic information on the parameter, contains hints about how best to
            display the parameter
    """

    id: Union[Unset, int] = UNSET
    in_: Union[Unset, float] = UNSET
    max_: Union[Unset, float] = UNSET
    min_: Union[Unset, float] = UNSET
    out: Union[Unset, float] = UNSET
    value: Union[Unset, float] = UNSET
    valuetype: Union[Unset, str] = UNSET
    view: Union[Unset, "ParameterView"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        in_ = self.in_

        max_ = self.max_

        min_ = self.min_

        out = self.out

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
        if in_ is not UNSET:
            field_dict["in"] = in_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if out is not UNSET:
            field_dict["out"] = out
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

        in_ = d.pop("in", UNSET)

        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        out = d.pop("out", UNSET)

        value = d.pop("value", UNSET)

        valuetype = d.pop("valuetype", UNSET)

        _view = d.pop("view", UNSET)
        view: Union[Unset, ParameterView]
        if isinstance(_view, Unset):
            view = UNSET
        else:
            view = ParameterView.from_dict(_view)

        range_parameter = cls(
            id=id,
            in_=in_,
            max_=max_,
            min_=min_,
            out=out,
            value=value,
            valuetype=valuetype,
            view=view,
        )

        range_parameter.additional_properties = d
        return range_parameter

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
