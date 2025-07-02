from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.choice_parameter import ChoiceParameter
    from ..models.event_parameter import EventParameter
    from ..models.parameter_collection import ParameterCollection
    from ..models.range_parameter import RangeParameter


T = TypeVar("T", bound="CrossFader")


@_attrs_define
class CrossFader:
    """Cross fade between two clips

    Attributes:
        behaviour (Union[Unset, ChoiceParameter]): A multiple-choice parameter
        curve (Union[Unset, ChoiceParameter]): A multiple-choice parameter
        id (Union[Unset, int]): The unique identifier of the cross fader Example: 1.
        mixer (Union[Unset, ParameterCollection]): An unstructured collection of parameters. Parameters are presented as
            a map where the key is the name of the parameter and the value is the parameter itself. Parameters may be any
            valid parameter type.
        phase (Union[Unset, RangeParameter]): A parameter containing a floating-point value with a minimum and maximum
            allowed value.
        sidea (Union[Unset, EventParameter]): A parameter that handles events, but does not contain a value
        sideb (Union[Unset, EventParameter]): A parameter that handles events, but does not contain a value
    """

    behaviour: Union[Unset, "ChoiceParameter"] = UNSET
    curve: Union[Unset, "ChoiceParameter"] = UNSET
    id: Union[Unset, int] = UNSET
    mixer: Union[Unset, "ParameterCollection"] = UNSET
    phase: Union[Unset, "RangeParameter"] = UNSET
    sidea: Union[Unset, "EventParameter"] = UNSET
    sideb: Union[Unset, "EventParameter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        behaviour: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.behaviour, Unset):
            behaviour = self.behaviour.to_dict()

        curve: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.curve, Unset):
            curve = self.curve.to_dict()

        id = self.id

        mixer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mixer, Unset):
            mixer = self.mixer.to_dict()

        phase: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase.to_dict()

        sidea: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sidea, Unset):
            sidea = self.sidea.to_dict()

        sideb: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sideb, Unset):
            sideb = self.sideb.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if behaviour is not UNSET:
            field_dict["behaviour"] = behaviour
        if curve is not UNSET:
            field_dict["curve"] = curve
        if id is not UNSET:
            field_dict["id"] = id
        if mixer is not UNSET:
            field_dict["mixer"] = mixer
        if phase is not UNSET:
            field_dict["phase"] = phase
        if sidea is not UNSET:
            field_dict["sidea"] = sidea
        if sideb is not UNSET:
            field_dict["sideb"] = sideb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.choice_parameter import ChoiceParameter
        from ..models.event_parameter import EventParameter
        from ..models.parameter_collection import ParameterCollection
        from ..models.range_parameter import RangeParameter

        d = dict(src_dict)
        _behaviour = d.pop("behaviour", UNSET)
        behaviour: Union[Unset, ChoiceParameter]
        if isinstance(_behaviour, Unset):
            behaviour = UNSET
        else:
            behaviour = ChoiceParameter.from_dict(_behaviour)

        _curve = d.pop("curve", UNSET)
        curve: Union[Unset, ChoiceParameter]
        if isinstance(_curve, Unset):
            curve = UNSET
        else:
            curve = ChoiceParameter.from_dict(_curve)

        id = d.pop("id", UNSET)

        _mixer = d.pop("mixer", UNSET)
        mixer: Union[Unset, ParameterCollection]
        if isinstance(_mixer, Unset):
            mixer = UNSET
        else:
            mixer = ParameterCollection.from_dict(_mixer)

        _phase = d.pop("phase", UNSET)
        phase: Union[Unset, RangeParameter]
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = RangeParameter.from_dict(_phase)

        _sidea = d.pop("sidea", UNSET)
        sidea: Union[Unset, EventParameter]
        if isinstance(_sidea, Unset):
            sidea = UNSET
        else:
            sidea = EventParameter.from_dict(_sidea)

        _sideb = d.pop("sideb", UNSET)
        sideb: Union[Unset, EventParameter]
        if isinstance(_sideb, Unset):
            sideb = UNSET
        else:
            sideb = EventParameter.from_dict(_sideb)

        cross_fader = cls(
            behaviour=behaviour,
            curve=curve,
            id=id,
            mixer=mixer,
            phase=phase,
            sidea=sidea,
            sideb=sideb,
        )

        cross_fader.additional_properties = d
        return cross_fader

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
