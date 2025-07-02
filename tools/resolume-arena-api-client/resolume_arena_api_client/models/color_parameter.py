from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parameter_view import ParameterView


T = TypeVar("T", bound="ColorParameter")


@_attrs_define
class ColorParameter:
    """A parameter containing color data

    Attributes:
        id (Union[Unset, int]): The unique identifier of the parameter Example: 1682459812085.
        palette (Union[Unset, list[str]]): Array of colors Example: ['#ffffff', '#ff00ff', '#000'].
        value (Union[Unset, str]): The color value. This always starts with a '#', followed by a number of hexadecimal
            values representing rgb and - optionally - the alpha channel. Each channel may be either represented by a single
            character - in which case the values are from 0 to 15 - or by two characters - allowing a range from 0 to 255
            per channel. Example: #ffffff.
        valuetype (Union[Unset, str]): The parameter type. This is "ParamColor" for this type Example: ParamColor.
        view (Union[Unset, ParameterView]): Semantic information on the parameter, contains hints about how best to
            display the parameter
    """

    id: Union[Unset, int] = UNSET
    palette: Union[Unset, list[str]] = UNSET
    value: Union[Unset, str] = UNSET
    valuetype: Union[Unset, str] = UNSET
    view: Union[Unset, "ParameterView"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        palette: Union[Unset, list[str]] = UNSET
        if not isinstance(self.palette, Unset):
            palette = self.palette

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
        if palette is not UNSET:
            field_dict["palette"] = palette
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

        palette = cast(list[str], d.pop("palette", UNSET))

        value = d.pop("value", UNSET)

        valuetype = d.pop("valuetype", UNSET)

        _view = d.pop("view", UNSET)
        view: Union[Unset, ParameterView]
        if isinstance(_view, Unset):
            view = UNSET
        else:
            view = ParameterView.from_dict(_view)

        color_parameter = cls(
            id=id,
            palette=palette,
            value=value,
            valuetype=valuetype,
            view=view,
        )

        color_parameter.additional_properties = d
        return color_parameter

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
