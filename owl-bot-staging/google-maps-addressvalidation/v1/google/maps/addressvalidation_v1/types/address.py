# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.type import postal_address_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.maps.addressvalidation.v1',
    manifest={
        'Address',
        'AddressComponent',
        'ComponentName',
    },
)


class Address(proto.Message):
    r"""Details of the address parsed from the input.

    Attributes:
        formatted_address (str):
            The corrected address, formatted as a
            single-line address following the address
            formatting rules of the region where the address
            is located.
        postal_address (google.type.postal_address_pb2.PostalAddress):
            The validated address represented as a postal
            address.
        address_components (Sequence[google.maps.addressvalidation_v1.types.AddressComponent]):
            The individual address components of the
            formatted and corrected address, along with
            validation information. This provides
            information on the validation status of the
            individual components.
            Address components are not ordered in a
            particular way. DO NOT make any assumptions on
            the ordering of the address components in the
            list.
        missing_component_types (Sequence[str]):
            The types of components that were expected to be present in
            a correctly formatted mailing address but were not found in
            the input AND could not be inferred. Components of this type
            are not present in ``formatted_address``,
            ``postal_address``, or ``address_components``. An example
            might be ``['street_number', 'route']`` for an input like
            "Boulder, Colorado, 80301, USA." The list of possible types
            can be found
            `here <https://developers.google.com/maps/documentation/geocoding/overview#Types>`__.
        unconfirmed_component_types (Sequence[str]):
            The types of the components that are present in the
            ``address_components`` but could not be confirmed to be
            correct. This field is provided for the sake of convenience:
            its contents are equivalent to iterating through the
            ``address_components`` to find the types of all the
            components where the
            [confirmation_level][google.maps.addressvalidation.v1.AddressComponent.confirmation_level]
            is not
            [CONFIRMED][google.maps.addressvalidation.v1.AddressComponent.ConfirmationLevel.CONFIRMED]
            or the
            [inferred][google.maps.addressvalidation.v1.AddressComponent.inferred]
            flag is not set to ``true``.The list of possible types can
            be found
            `here <https://developers.google.com/maps/documentation/geocoding/overview#Types>`__.
        unresolved_tokens (Sequence[str]):
            Any tokens in the input that could not be resolved. This
            might be an input that was not recognized as a valid part of
            an address (for example in an input like "123235253253 Main
            St, San Francisco, CA, 94105", the unresolved tokens may
            look like ``["123235253253"]`` since that does not look like
            a valid street number.
    """

    formatted_address = proto.Field(
        proto.STRING,
        number=2,
    )
    postal_address = proto.Field(
        proto.MESSAGE,
        number=3,
        message=postal_address_pb2.PostalAddress,
    )
    address_components = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message='AddressComponent',
    )
    missing_component_types = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    unconfirmed_component_types = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    unresolved_tokens = proto.RepeatedField(
        proto.STRING,
        number=7,
    )


class AddressComponent(proto.Message):
    r"""Represents an address component, such as a street, city, or
    state.

    Attributes:
        component_name (google.maps.addressvalidation_v1.types.ComponentName):
            The name for this component.
        component_type (str):
            The type of the address component. See `Table 2: Additional
            types returned by the Places
            service <https://developers.google.com/places/web-service/supported_types#table2>`__
            for a list of possible types.
        confirmation_level (google.maps.addressvalidation_v1.types.AddressComponent.ConfirmationLevel):
            Indicates the level of certainty that we have
            that the component is correct.
        inferred (bool):
            Indicates that the component was not part of
            the input, but we inferred it for the address
            location and believe it should be provided for a
            complete address.
        spell_corrected (bool):
            Indicates the spelling of the component name
            was corrected in a minor way, for example by
            switching two characters that appeared in the
            wrong order. This indicates a cosmetic change.
        replaced (bool):
            Indicates the name of the component was
            replaced with a completely different one, for
            example a wrong postal code being replaced with
            one that is correct for the address. This is not
            a cosmetic change, the input component has been
            changed to a different one.
        unexpected (bool):
            Indicates an address component that is not
            expected to be present in a postal address for
            the given region. We have retained it only
            because it was part of the input.
    """
    class ConfirmationLevel(proto.Enum):
        r"""The different possible values for confirmation levels."""
        CONFIRMATION_LEVEL_UNSPECIFIED = 0
        CONFIRMED = 1
        UNCONFIRMED_BUT_PLAUSIBLE = 2
        UNCONFIRMED_AND_SUSPICIOUS = 3

    component_name = proto.Field(
        proto.MESSAGE,
        number=1,
        message='ComponentName',
    )
    component_type = proto.Field(
        proto.STRING,
        number=2,
    )
    confirmation_level = proto.Field(
        proto.ENUM,
        number=3,
        enum=ConfirmationLevel,
    )
    inferred = proto.Field(
        proto.BOOL,
        number=4,
    )
    spell_corrected = proto.Field(
        proto.BOOL,
        number=5,
    )
    replaced = proto.Field(
        proto.BOOL,
        number=6,
    )
    unexpected = proto.Field(
        proto.BOOL,
        number=7,
    )


class ComponentName(proto.Message):
    r"""A wrapper for the name of the component.

    Attributes:
        text (str):
            The name text. For example, "5th Avenue" for
            a street name or "1253" for a street number.
        language_code (str):
            The BCP-47 language code. This will not be
            present if the component name is not associated
            with a language, such as a street number.
    """

    text = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
