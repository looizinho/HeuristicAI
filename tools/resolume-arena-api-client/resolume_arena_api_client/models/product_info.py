from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductInfo")


@_attrs_define
class ProductInfo:
    """Generic information about the product serving the api

    Attributes:
        major (Union[Unset, int]): The major version number of the Arena or Avenue instance handling the request.
            Example: 7.
        micro (Union[Unset, int]): The micro version number of the Arena or Avenue instance handling the request.
        minor (Union[Unset, int]): The minor version number of the Arena or Avenue instance handling the request.
            Example: 8.
        name (Union[Unset, str]): The product name. This is either 'Arena' or 'Avenue' Example: Arena.
        revision (Union[Unset, int]): The revision of the Arena or Avenue instance handling the request.
    """

    major: Union[Unset, int] = UNSET
    micro: Union[Unset, int] = UNSET
    minor: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    revision: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        major = self.major

        micro = self.micro

        minor = self.minor

        name = self.name

        revision = self.revision

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if major is not UNSET:
            field_dict["major"] = major
        if micro is not UNSET:
            field_dict["micro"] = micro
        if minor is not UNSET:
            field_dict["minor"] = minor
        if name is not UNSET:
            field_dict["name"] = name
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        major = d.pop("major", UNSET)

        micro = d.pop("micro", UNSET)

        minor = d.pop("minor", UNSET)

        name = d.pop("name", UNSET)

        revision = d.pop("revision", UNSET)

        product_info = cls(
            major=major,
            micro=micro,
            minor=minor,
            name=name,
            revision=revision,
        )

        product_info.additional_properties = d
        return product_info

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
