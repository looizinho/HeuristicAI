from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.boolean_parameter import BooleanParameter
    from ..models.choice_parameter import ChoiceParameter
    from ..models.color_parameter import ColorParameter
    from ..models.integer_parameter import IntegerParameter
    from ..models.range_parameter import RangeParameter
    from ..models.string_parameter import StringParameter
    from ..models.text_parameter import TextParameter


T = TypeVar("T", bound="ParameterCollection")


@_attrs_define
class ParameterCollection:
    """An unstructured collection of parameters. Parameters are presented as a map where the key is the name of the
    parameter and the value is the parameter itself. Parameters may be any valid parameter type.

    """

    additional_properties: dict[
        str,
        Union[
            "BooleanParameter",
            "ChoiceParameter",
            "ColorParameter",
            "IntegerParameter",
            "RangeParameter",
            "StringParameter",
            "TextParameter",
        ],
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.boolean_parameter import BooleanParameter
        from ..models.color_parameter import ColorParameter
        from ..models.integer_parameter import IntegerParameter
        from ..models.range_parameter import RangeParameter
        from ..models.string_parameter import StringParameter
        from ..models.text_parameter import TextParameter

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, StringParameter):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, TextParameter):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, BooleanParameter):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, IntegerParameter):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ColorParameter):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, RangeParameter):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boolean_parameter import BooleanParameter
        from ..models.choice_parameter import ChoiceParameter
        from ..models.color_parameter import ColorParameter
        from ..models.integer_parameter import IntegerParameter
        from ..models.range_parameter import RangeParameter
        from ..models.string_parameter import StringParameter
        from ..models.text_parameter import TextParameter

        d = dict(src_dict)
        parameter_collection = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> Union[
                "BooleanParameter",
                "ChoiceParameter",
                "ColorParameter",
                "IntegerParameter",
                "RangeParameter",
                "StringParameter",
                "TextParameter",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = StringParameter.from_dict(data)

                    return additional_property_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_1 = TextParameter.from_dict(data)

                    return additional_property_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_2 = BooleanParameter.from_dict(data)

                    return additional_property_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_3 = IntegerParameter.from_dict(data)

                    return additional_property_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_4 = ColorParameter.from_dict(data)

                    return additional_property_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_5 = RangeParameter.from_dict(data)

                    return additional_property_type_5
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_6 = ChoiceParameter.from_dict(data)

                return additional_property_type_6

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        parameter_collection.additional_properties = additional_properties
        return parameter_collection

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> Union[
        "BooleanParameter",
        "ChoiceParameter",
        "ColorParameter",
        "IntegerParameter",
        "RangeParameter",
        "StringParameter",
        "TextParameter",
    ]:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: Union[
            "BooleanParameter",
            "ChoiceParameter",
            "ColorParameter",
            "IntegerParameter",
            "RangeParameter",
            "StringParameter",
            "TextParameter",
        ],
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
