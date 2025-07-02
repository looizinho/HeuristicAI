from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_parameter import EventParameter
    from ..models.range_parameter import RangeParameter


T = TypeVar("T", bound="TempoController")


@_attrs_define
class TempoController:
    """The controller for various tempo-related aspects of the composition

    Attributes:
        resync (Union[Unset, EventParameter]): A parameter that handles events, but does not contain a value
        tempo (Union[Unset, RangeParameter]): A parameter containing a floating-point value with a minimum and maximum
            allowed value.
        tempo_pull (Union[Unset, EventParameter]): A parameter that handles events, but does not contain a value
        tempo_push (Union[Unset, EventParameter]): A parameter that handles events, but does not contain a value
        tempo_tap (Union[Unset, EventParameter]): A parameter that handles events, but does not contain a value
    """

    resync: Union[Unset, "EventParameter"] = UNSET
    tempo: Union[Unset, "RangeParameter"] = UNSET
    tempo_pull: Union[Unset, "EventParameter"] = UNSET
    tempo_push: Union[Unset, "EventParameter"] = UNSET
    tempo_tap: Union[Unset, "EventParameter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resync: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.resync, Unset):
            resync = self.resync.to_dict()

        tempo: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tempo, Unset):
            tempo = self.tempo.to_dict()

        tempo_pull: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tempo_pull, Unset):
            tempo_pull = self.tempo_pull.to_dict()

        tempo_push: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tempo_push, Unset):
            tempo_push = self.tempo_push.to_dict()

        tempo_tap: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tempo_tap, Unset):
            tempo_tap = self.tempo_tap.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resync is not UNSET:
            field_dict["resync"] = resync
        if tempo is not UNSET:
            field_dict["tempo"] = tempo
        if tempo_pull is not UNSET:
            field_dict["tempo_pull"] = tempo_pull
        if tempo_push is not UNSET:
            field_dict["tempo_push"] = tempo_push
        if tempo_tap is not UNSET:
            field_dict["tempo_tap"] = tempo_tap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_parameter import EventParameter
        from ..models.range_parameter import RangeParameter

        d = dict(src_dict)
        _resync = d.pop("resync", UNSET)
        resync: Union[Unset, EventParameter]
        if isinstance(_resync, Unset):
            resync = UNSET
        else:
            resync = EventParameter.from_dict(_resync)

        _tempo = d.pop("tempo", UNSET)
        tempo: Union[Unset, RangeParameter]
        if isinstance(_tempo, Unset):
            tempo = UNSET
        else:
            tempo = RangeParameter.from_dict(_tempo)

        _tempo_pull = d.pop("tempo_pull", UNSET)
        tempo_pull: Union[Unset, EventParameter]
        if isinstance(_tempo_pull, Unset):
            tempo_pull = UNSET
        else:
            tempo_pull = EventParameter.from_dict(_tempo_pull)

        _tempo_push = d.pop("tempo_push", UNSET)
        tempo_push: Union[Unset, EventParameter]
        if isinstance(_tempo_push, Unset):
            tempo_push = UNSET
        else:
            tempo_push = EventParameter.from_dict(_tempo_push)

        _tempo_tap = d.pop("tempo_tap", UNSET)
        tempo_tap: Union[Unset, EventParameter]
        if isinstance(_tempo_tap, Unset):
            tempo_tap = UNSET
        else:
            tempo_tap = EventParameter.from_dict(_tempo_tap)

        tempo_controller = cls(
            resync=resync,
            tempo=tempo,
            tempo_pull=tempo_pull,
            tempo_push=tempo_push,
            tempo_tap=tempo_tap,
        )

        tempo_controller.additional_properties = d
        return tempo_controller

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
