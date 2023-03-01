from typing import List, Optional, Any, Union, TypeVar, Callable, Type, cast
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Dbt:
    profile_version: str
    suported_package_versions: Optional[List[str]]

    def __init__(self, profile_version: str, suported_package_versions: Optional[List[str]]) -> None:
        self.profile_version = profile_version
        self.suported_package_versions = suported_package_versions

    @staticmethod
    def from_dict(obj: Any) -> 'Dbt':
        assert isinstance(obj, dict)
        profile_version = from_str(obj.get("profileVersion"))
        suported_package_versions = from_union([lambda x: from_list(from_str, x), from_none], obj.get("suportedPackageVersions"))
        return Dbt(profile_version, suported_package_versions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["profileVersion"] = from_str(self.profile_version)
        if self.suported_package_versions is not None:
            result["suportedPackageVersions"] = from_union([lambda x: from_list(from_str, x), from_none], self.suported_package_versions)
        return result


class FieldType(Enum):
    BOOLEAN = "boolean"
    INTEGER = "integer"
    STRING = "string"


class ProfileFieldElement:
    description: Optional[str]
    display_name: Optional[str]
    field_default: Optional[Union[int, bool, str]]
    field_type: FieldType
    sensitive: Optional[bool]

    def __init__(self, description: Optional[str], display_name: Optional[str], field_default: Optional[Union[int, bool, str]], field_type: FieldType, sensitive: Optional[bool]) -> None:
        self.description = description
        self.display_name = display_name
        self.field_default = field_default
        self.field_type = field_type
        self.sensitive = sensitive

    @staticmethod
    def from_dict(obj: Any) -> 'ProfileFieldElement':
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("description"))
        display_name = from_union([from_str, from_none], obj.get("displayName"))
        field_default = from_union([from_int, from_bool, from_str, from_none], obj.get("fieldDefault"))
        field_type = FieldType(obj.get("fieldType"))
        sensitive = from_union([from_bool, from_none], obj.get("sensitive"))
        return ProfileFieldElement(description, display_name, field_default, field_type, sensitive)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.display_name is not None:
            result["displayName"] = from_union([from_str, from_none], self.display_name)
        if self.field_default is not None:
            result["fieldDefault"] = from_union([from_int, from_bool, from_str, from_none], self.field_default)
        result["fieldType"] = to_enum(FieldType, self.field_type)
        if self.sensitive is not None:
            result["sensitive"] = from_union([from_bool, from_none], self.sensitive)
        return result


class ProfileElement:
    display_name: Optional[str]
    id: Optional[str]
    profile_fields: List[ProfileFieldElement]

    def __init__(self, display_name: Optional[str], id: Optional[str], profile_fields: List[ProfileFieldElement]) -> None:
        self.display_name = display_name
        self.id = id
        self.profile_fields = profile_fields

    @staticmethod
    def from_dict(obj: Any) -> 'ProfileElement':
        assert isinstance(obj, dict)
        display_name = from_union([from_str, from_none], obj.get("displayName"))
        id = from_union([from_str, from_none], obj.get("id"))
        profile_fields = from_list(ProfileFieldElement.from_dict, obj.get("profileFields"))
        return ProfileElement(display_name, id, profile_fields)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.display_name is not None:
            result["displayName"] = from_union([from_str, from_none], self.display_name)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        result["profileFields"] = from_list(lambda x: to_class(ProfileFieldElement, x), self.profile_fields)
        return result


class ProfileSchema:
    """The schema for how dbt plugins describe the profile configuration"""
    dbt_meta: Dbt
    profiles: List[ProfileElement]

    def __init__(self, dbt_meta: Dbt, profiles: List[ProfileElement]) -> None:
        self.dbt_meta = dbt_meta
        self.profiles = profiles

    @staticmethod
    def from_dict(obj: Any) -> 'ProfileSchema':
        assert isinstance(obj, dict)
        dbt_meta = Dbt.from_dict(obj.get("dbtMeta"))
        profiles = from_list(ProfileElement.from_dict, obj.get("profiles"))
        return ProfileSchema(dbt_meta, profiles)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dbtMeta"] = to_class(Dbt, self.dbt_meta)
        result["profiles"] = from_list(lambda x: to_class(ProfileElement, x), self.profiles)
        return result


def profile_schema_from_dict(s: Any) -> ProfileSchema:
    return ProfileSchema.from_dict(s)


def profile_schema_to_dict(x: ProfileSchema) -> Any:
    return to_class(ProfileSchema, x)
