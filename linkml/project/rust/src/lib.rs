#![allow(non_camel_case_types)]

#[cfg(feature = "serde")]
mod serde_utils;
pub mod poly;
pub mod poly_containers;
#[cfg(feature = "stubgen")]
pub mod stub_utils;

#[cfg(feature = "serde")]
use serde_yml as _ ;
use chrono::NaiveDate;
#[cfg(feature = "pyo3")]
use pyo3::{FromPyObject,prelude::*};
#[cfg(feature = "stubgen")]
use pyo3_stub_gen::{define_stub_info_gatherer,derive::gen_stub_pyclass,derive::gen_stub_pymethods};
#[cfg(feature = "serde")]
use serde::{Deserialize,Serialize,de::IntoDeserializer};
use serde_value::Value;
#[cfg(feature = "serde")]
use serde_path_to_error;
use std::collections::HashMap;
use std::collections::BTreeMap;

// Types

pub type CronExpression = String;
pub type Metadata = String;
pub type string = String;
pub type integer = String;
pub type boolean = String;
pub type float = f64;
pub type double = f64;
pub type decimal = String;
pub type time = String;
pub type date = String;
pub type datetime = String;
pub type date_or_datetime = String;
pub type uriorcurie = String;
pub type curie = String;
pub type uri = String;
pub type ncname = String;
pub type objectidentifier = String;
pub type nodeidentifier = String;
pub type jsonpointer = String;
pub type jsonpath = String;
pub type sparqlpath = String;

// Slots

pub type nodes = Vec<Node>;
pub type relationships = Vec<Relationship>;
pub type metadata = String;
pub type controls = Control;
pub type flows = Vec<Flow>;
pub type adrs = Vec<String>;
pub type unique_id = String;
pub type node_type = NodeType;
pub type name = String;
pub type description = String;
pub type details = String;
pub type interfaces = Vec<InterfaceDefinition>;
pub type relationship_type = RelationshipType;
pub type protocol = Protocol;
pub type actor = String;
pub type source = NodeInterface;
pub type destination = NodeInterface;
pub type container = String;
pub type requirement_url = String;
pub type config_url = String;
pub type config = String;
pub type control_id = String;
pub type type_ = String;
pub type target = Vec<String>;
pub type applies_to = Vec<String>;
pub type data = String;
pub type evidence = String;
pub type relationship_unique_id = String;
pub type sequence_number = isize;
pub type direction = TransitionDirection;
pub type transitions = Vec<Transition>;
pub type definition_url = String;
pub type node = String;
pub type current_moment = String;
pub type moments = Vec<String>;
pub type valid_from = NaiveDate;
pub type unit = TimeUnitName;
pub type value = f64;
pub type rate = f64;
pub type per = RatePerUnit;
pub type url = String;
pub type control_config_url = String;
pub type evidence_paths = Vec<String>;
pub type decisions = Vec<Decision>;
pub type interacts = InteractsRelationship;
pub type connects = ConnectsRelationship;
pub type deployed_in = DeployedInRelationship;
pub type composed_of = ComposedOfRelationship;
pub type options = Vec<Decision>;
pub type Architecture_nodes = Vec<Node>;
pub type Architecture_relationships = Vec<Relationship>;
pub type Architecture_flows = Vec<Flow>;
pub type Node_interfaces = Vec<InterfaceDefinition>;
pub type Node_description = String;
pub type InteractsRelationship_nodes = Vec<Node>;
pub type DeployedInRelationship_nodes = Vec<Node>;
pub type ComposedOfRelationship_nodes = Vec<Node>;
pub type Decision_nodes = Vec<Node>;
pub type Decision_relationships = Vec<Relationship>;
pub type Decision_description = String;
pub type ControlDetail_requirement_url = String;
pub type ControlRequirement_description = String;
pub type Transition_description = String;
pub type Flow_description = String;
pub type InterfaceDefinition_config = String;
pub type NodeInterface_interfaces = Vec<InterfaceDefinition>;
pub type NodeMoment_details = String;

// Enums

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum Protocol {
    HTTP,
    HTTPS,
    FTP,
    SFTP,
    JDBC,
    WebSocket,
    SocketIO,
    LDAP,
    AMQP,
    TLS,
    MTLS,
    TCP,
}

impl core::fmt::Display for Protocol {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            Protocol::HTTP => f.write_str("HTTP"),
            Protocol::HTTPS => f.write_str("HTTPS"),
            Protocol::FTP => f.write_str("FTP"),
            Protocol::SFTP => f.write_str("SFTP"),
            Protocol::JDBC => f.write_str("JDBC"),
            Protocol::WebSocket => f.write_str("WebSocket"),
            Protocol::SocketIO => f.write_str("SocketIO"),
            Protocol::LDAP => f.write_str("LDAP"),
            Protocol::AMQP => f.write_str("AMQP"),
            Protocol::TLS => f.write_str("TLS"),
            Protocol::MTLS => f.write_str("mTLS"),
            Protocol::TCP => f.write_str("TCP"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Protocol {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            Protocol::HTTP => "HTTP",
            Protocol::HTTPS => "HTTPS",
            Protocol::FTP => "FTP",
            Protocol::SFTP => "SFTP",
            Protocol::JDBC => "JDBC",
            Protocol::WebSocket => "WebSocket",
            Protocol::SocketIO => "SocketIO",
            Protocol::LDAP => "LDAP",
            Protocol::AMQP => "AMQP",
            Protocol::TLS => "TLS",
            Protocol::MTLS => "mTLS",
            Protocol::TCP => "TCP",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Protocol {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "HTTP" => Ok(Protocol::HTTP),
                "HTTPS" => Ok(Protocol::HTTPS),
                "FTP" => Ok(Protocol::FTP),
                "SFTP" => Ok(Protocol::SFTP),
                "JDBC" => Ok(Protocol::JDBC),
                "WebSocket" => Ok(Protocol::WebSocket),
                "SocketIO" => Ok(Protocol::SocketIO),
                "LDAP" => Ok(Protocol::LDAP),
                "AMQP" => Ok(Protocol::AMQP),
                "TLS" => Ok(Protocol::TLS),
                "mTLS" | "MTLS" => Ok(Protocol::MTLS),
                "TCP" => Ok(Protocol::TCP),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for Protocol: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(Protocol)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for Protocol {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['HTTP', 'HTTPS', 'FTP', 'SFTP', 'JDBC', 'WebSocket', 'SocketIO', 'LDAP', 'AMQP', 'TLS', 'mTLS', 'TCP']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum NodeType {
    Actor,
    Ecosystem,
    System,
    Service,
    Database,
    Network,
    Ldap,
    Webclient,
    DataAsset,
}

impl core::fmt::Display for NodeType {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            NodeType::Actor => f.write_str("actor"),
            NodeType::Ecosystem => f.write_str("ecosystem"),
            NodeType::System => f.write_str("system"),
            NodeType::Service => f.write_str("service"),
            NodeType::Database => f.write_str("database"),
            NodeType::Network => f.write_str("network"),
            NodeType::Ldap => f.write_str("ldap"),
            NodeType::Webclient => f.write_str("webclient"),
            NodeType::DataAsset => f.write_str("data_asset"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for NodeType {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            NodeType::Actor => "actor",
            NodeType::Ecosystem => "ecosystem",
            NodeType::System => "system",
            NodeType::Service => "service",
            NodeType::Database => "database",
            NodeType::Network => "network",
            NodeType::Ldap => "ldap",
            NodeType::Webclient => "webclient",
            NodeType::DataAsset => "data_asset",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for NodeType {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "actor" | "Actor" => Ok(NodeType::Actor),
                "ecosystem" | "Ecosystem" => Ok(NodeType::Ecosystem),
                "system" | "System" => Ok(NodeType::System),
                "service" | "Service" => Ok(NodeType::Service),
                "database" | "Database" => Ok(NodeType::Database),
                "network" | "Network" => Ok(NodeType::Network),
                "ldap" | "Ldap" => Ok(NodeType::Ldap),
                "webclient" | "Webclient" => Ok(NodeType::Webclient),
                "data_asset" | "DataAsset" => Ok(NodeType::DataAsset),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for NodeType: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(NodeType)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for NodeType {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['actor', 'ecosystem', 'system', 'service', 'database', 'network', 'ldap', 'webclient', 'data_asset']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum TimeUnitName {
    Nanoseconds,
    Microseconds,
    Milliseconds,
    Seconds,
    Minutes,
    Hours,
    Days,
    Weeks,
    Months,
    Quarters,
    Years,
}

impl core::fmt::Display for TimeUnitName {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            TimeUnitName::Nanoseconds => f.write_str("nanoseconds"),
            TimeUnitName::Microseconds => f.write_str("microseconds"),
            TimeUnitName::Milliseconds => f.write_str("milliseconds"),
            TimeUnitName::Seconds => f.write_str("seconds"),
            TimeUnitName::Minutes => f.write_str("minutes"),
            TimeUnitName::Hours => f.write_str("hours"),
            TimeUnitName::Days => f.write_str("days"),
            TimeUnitName::Weeks => f.write_str("weeks"),
            TimeUnitName::Months => f.write_str("months"),
            TimeUnitName::Quarters => f.write_str("quarters"),
            TimeUnitName::Years => f.write_str("years"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for TimeUnitName {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            TimeUnitName::Nanoseconds => "nanoseconds",
            TimeUnitName::Microseconds => "microseconds",
            TimeUnitName::Milliseconds => "milliseconds",
            TimeUnitName::Seconds => "seconds",
            TimeUnitName::Minutes => "minutes",
            TimeUnitName::Hours => "hours",
            TimeUnitName::Days => "days",
            TimeUnitName::Weeks => "weeks",
            TimeUnitName::Months => "months",
            TimeUnitName::Quarters => "quarters",
            TimeUnitName::Years => "years",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for TimeUnitName {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "nanoseconds" | "Nanoseconds" => Ok(TimeUnitName::Nanoseconds),
                "microseconds" | "Microseconds" => Ok(TimeUnitName::Microseconds),
                "milliseconds" | "Milliseconds" => Ok(TimeUnitName::Milliseconds),
                "seconds" | "Seconds" => Ok(TimeUnitName::Seconds),
                "minutes" | "Minutes" => Ok(TimeUnitName::Minutes),
                "hours" | "Hours" => Ok(TimeUnitName::Hours),
                "days" | "Days" => Ok(TimeUnitName::Days),
                "weeks" | "Weeks" => Ok(TimeUnitName::Weeks),
                "months" | "Months" => Ok(TimeUnitName::Months),
                "quarters" | "Quarters" => Ok(TimeUnitName::Quarters),
                "years" | "Years" => Ok(TimeUnitName::Years),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for TimeUnitName: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(TimeUnitName)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for TimeUnitName {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['nanoseconds', 'microseconds', 'milliseconds', 'seconds', 'minutes', 'hours', 'days', 'weeks', 'months', 'quarters', 'years']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum RatePerUnit {
    Nanosecond,
    Microsecond,
    Millisecond,
    Second,
    Minute,
    Hour,
    Day,
    Week,
    Month,
    Quarter,
    Year,
}

impl core::fmt::Display for RatePerUnit {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            RatePerUnit::Nanosecond => f.write_str("nanosecond"),
            RatePerUnit::Microsecond => f.write_str("microsecond"),
            RatePerUnit::Millisecond => f.write_str("millisecond"),
            RatePerUnit::Second => f.write_str("second"),
            RatePerUnit::Minute => f.write_str("minute"),
            RatePerUnit::Hour => f.write_str("hour"),
            RatePerUnit::Day => f.write_str("day"),
            RatePerUnit::Week => f.write_str("week"),
            RatePerUnit::Month => f.write_str("month"),
            RatePerUnit::Quarter => f.write_str("quarter"),
            RatePerUnit::Year => f.write_str("year"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for RatePerUnit {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            RatePerUnit::Nanosecond => "nanosecond",
            RatePerUnit::Microsecond => "microsecond",
            RatePerUnit::Millisecond => "millisecond",
            RatePerUnit::Second => "second",
            RatePerUnit::Minute => "minute",
            RatePerUnit::Hour => "hour",
            RatePerUnit::Day => "day",
            RatePerUnit::Week => "week",
            RatePerUnit::Month => "month",
            RatePerUnit::Quarter => "quarter",
            RatePerUnit::Year => "year",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for RatePerUnit {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "nanosecond" | "Nanosecond" => Ok(RatePerUnit::Nanosecond),
                "microsecond" | "Microsecond" => Ok(RatePerUnit::Microsecond),
                "millisecond" | "Millisecond" => Ok(RatePerUnit::Millisecond),
                "second" | "Second" => Ok(RatePerUnit::Second),
                "minute" | "Minute" => Ok(RatePerUnit::Minute),
                "hour" | "Hour" => Ok(RatePerUnit::Hour),
                "day" | "Day" => Ok(RatePerUnit::Day),
                "week" | "Week" => Ok(RatePerUnit::Week),
                "month" | "Month" => Ok(RatePerUnit::Month),
                "quarter" | "Quarter" => Ok(RatePerUnit::Quarter),
                "year" | "Year" => Ok(RatePerUnit::Year),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for RatePerUnit: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(RatePerUnit)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for RatePerUnit {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['nanosecond', 'microsecond', 'millisecond', 'second', 'minute', 'hour', 'day', 'week', 'month', 'quarter', 'year']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum TransitionDirection {
    SourceToDestination,
    DestinationToSource,
}

impl core::fmt::Display for TransitionDirection {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            TransitionDirection::SourceToDestination => f.write_str("source_to_destination"),
            TransitionDirection::DestinationToSource => f.write_str("destination_to_source"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for TransitionDirection {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            TransitionDirection::SourceToDestination => "source_to_destination",
            TransitionDirection::DestinationToSource => "destination_to_source",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for TransitionDirection {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "source_to_destination" | "SourceToDestination" => Ok(TransitionDirection::SourceToDestination),
                "destination_to_source" | "DestinationToSource" => Ok(TransitionDirection::DestinationToSource),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for TransitionDirection: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(TransitionDirection)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for TransitionDirection {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['source_to_destination', 'destination_to_source']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum RelationshipKind {
    Interacts,
    Connects,
    DeployedIn,
    ComposedOf,
    Options,
}

impl core::fmt::Display for RelationshipKind {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            RelationshipKind::Interacts => f.write_str("interacts"),
            RelationshipKind::Connects => f.write_str("connects"),
            RelationshipKind::DeployedIn => f.write_str("deployed_in"),
            RelationshipKind::ComposedOf => f.write_str("composed_of"),
            RelationshipKind::Options => f.write_str("options"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for RelationshipKind {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            RelationshipKind::Interacts => "interacts",
            RelationshipKind::Connects => "connects",
            RelationshipKind::DeployedIn => "deployed_in",
            RelationshipKind::ComposedOf => "composed_of",
            RelationshipKind::Options => "options",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for RelationshipKind {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "interacts" | "Interacts" => Ok(RelationshipKind::Interacts),
                "connects" | "Connects" => Ok(RelationshipKind::Connects),
                "deployed_in" | "DeployedIn" => Ok(RelationshipKind::DeployedIn),
                "composed_of" | "ComposedOf" => Ok(RelationshipKind::ComposedOf),
                "options" | "Options" => Ok(RelationshipKind::Options),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for RelationshipKind: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(RelationshipKind)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for RelationshipKind {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['interacts', 'connects', 'deployed_in', 'composed_of', 'options']",
            "typing".into(),
        )
    }
}

// Classes

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Architecture {
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(alias = "nodes"))]
    pub Architecture_nodes: Option<Vec<NodeOrSubtype>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(alias = "relationships"))]
    pub Architecture_relationships: Option<Vec<Relationship>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub metadata: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub controls: Option<Control>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(alias = "flows"))]
    pub Architecture_flows: Option<Vec<Flow>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub adrs: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Architecture {
    #[new]
    #[pyo3(signature = (Architecture_nodes=None, Architecture_relationships=None, metadata=None, controls=None, Architecture_flows=None, adrs=None))]
    pub fn new(Architecture_nodes: Option<serde_utils::PyValue<Vec<NodeOrSubtype>>>, Architecture_relationships: Option<serde_utils::PyValue<Vec<Relationship>>>, metadata: Option<String>, controls: Option<serde_utils::PyValue<Control>>, Architecture_flows: Option<serde_utils::PyValue<Vec<Flow>>>, adrs: Option<Vec<String>>) -> Self {
        let Architecture_nodes = Architecture_nodes.map(|v| v.into_inner());
        let Architecture_relationships = Architecture_relationships.map(|v| v.into_inner());
        let controls = controls.map(|v| v.into_inner());
        let Architecture_flows = Architecture_flows.map(|v| v.into_inner());
        Architecture{Architecture_nodes, Architecture_relationships, metadata, controls, Architecture_flows, adrs}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Architecture>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Architecture> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Architecture>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Architecture",
        ))
    }
}



pub mod node_utl {
    use super::*;
    #[derive(Debug, Clone, PartialEq)]
    #[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
    pub enum node_type_range {
        NodeType(NodeType),
        String(String)    }

    #[cfg(feature = "pyo3")]
    impl<'py> FromPyObject<'py> for node_type_range {
        fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
            if let Ok(val) = ob.extract::<NodeType>() {
                return Ok(node_type_range::NodeType(val));
            }            if let Ok(val) = ob.extract::<String>() {
                return Ok(node_type_range::String(val));
            }Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                "invalid node_type",
            ))
        }
    }

    #[cfg(feature = "pyo3")]
    impl<'py> IntoPyObject<'py> for node_type_range {
        type Target = PyAny;
        type Output = Bound<'py, Self::Target>;
        type Error = PyErr;

        fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
            match self {
                node_type_range::NodeType(val) => Ok(val.into_pyobject(py).map(move |b| <pyo3::Bound<'_, _> as Clone>::clone(&b).into_any())?),
                node_type_range::String(val) => Ok(val.into_pyobject(py).map(move |b| <pyo3::Bound<'_, _> as Clone>::clone(&b).into_any())?),
            }
        }
    }


    #[cfg(feature = "pyo3")]
    impl<'py> IntoPyObject<'py> for Box<node_type_range>
    {
        type Target = PyAny;
        type Output = Bound<'py, Self::Target>;
        type Error = PyErr;
        fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
            (*self).into_pyobject(py).map(move |x| x.into_any())
        }
    }

    #[cfg(feature = "pyo3")]
    impl<'py> FromPyObject<'py> for Box<node_type_range> {
        fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
            if let Ok(val) = ob.extract::<node_type_range>() {
                return Ok(Box::new(val));
            }
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                "invalid node_type",
            ))
        }
    }

    #[cfg(feature = "stubgen")]
    ::pyo3_stub_gen::impl_stub_type!(node_type_range = NodeType | String);
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Node {
    pub unique_id: String,
    pub node_type: node_utl::node_type_range,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(alias = "description"))]
    pub Node_description: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub details: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(alias = "interfaces"))]
    pub Node_interfaces: Option<Vec<InterfaceDefinition>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub controls: Option<Control>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub metadata: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Node {
    #[new]
    #[pyo3(signature = (unique_id, node_type, name, Node_description, details=None, Node_interfaces=None, controls=None, metadata=None))]
    pub fn new(unique_id: String, node_type: node_utl::node_type_range, name: String, Node_description: String, details: Option<String>, Node_interfaces: Option<serde_utils::PyValue<Vec<InterfaceDefinition>>>, controls: Option<serde_utils::PyValue<Control>>, metadata: Option<String>) -> Self {
        let Node_interfaces = Node_interfaces.map(|v| v.into_inner());
        let controls = controls.map(|v| v.into_inner());
        Node{unique_id, node_type, name, Node_description, details, Node_interfaces, controls, metadata}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Node>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Node> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Node>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Node",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for Node {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.unique_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("unique_id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a Node from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("unique_id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature="serde", serde(untagged))]
pub enum NodeOrSubtype {    NodeMoment(NodeMoment)}

impl From<NodeMoment>   for NodeOrSubtype { fn from(x: NodeMoment)   -> Self { Self::NodeMoment(x) } }

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for NodeOrSubtype {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<NodeMoment>() {
            return Ok(NodeOrSubtype::NodeMoment(val));
        }Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid NodeOrSubtype",
        ))
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for NodeOrSubtype {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;

    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        match self {
            NodeOrSubtype::NodeMoment(val) => val.into_pyobject(py).map(move |b| b.into_any()),
        }
    }
}


#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<NodeOrSubtype>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<NodeOrSubtype> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<NodeOrSubtype>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid NodeOrSubtype",
        ))
    }
}

#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for NodeOrSubtype {
    type Key       = String;
    type Value     = serde_value::Value;
    type Error     = String;

    fn from_pair_mapping(k: Self::Key, v: Self::Value) -> Result<Self, Self::Error> {
        if let Ok(x) = NodeMoment::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(NodeOrSubtype::NodeMoment(x));
        }
        Err("none of the variants matched the mapping form".into())
    }

    fn from_pair_simple(k: Self::Key, v: Self::Value) -> Result<Self, Self::Error> {
        if let Ok(x) = NodeMoment::from_pair_simple(k.clone(), v.clone()) {
            return Ok(NodeOrSubtype::NodeMoment(x));
        }
        Err("none of the variants support the primitive form".into())
    }

    fn extract_key(&self) -> &Self::Key {
        match self {
            NodeOrSubtype::NodeMoment(inner) => inner.extract_key(),
        }
    }
}

#[cfg(feature = "stubgen")]
::pyo3_stub_gen::impl_stub_type!(NodeOrSubtype = NodeMoment);

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Relationship {
    pub unique_id: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    pub relationship_type: Box<RelationshipType>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub protocol: Option<Protocol>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub metadata: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub controls: Option<Control>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Relationship {
    #[new]
    #[pyo3(signature = (unique_id, relationship_type, description=None, protocol=None, metadata=None, controls=None))]
    pub fn new(unique_id: String, relationship_type: serde_utils::PyValue<Box<RelationshipType>>, description: Option<String>, protocol: Option<Protocol>, metadata: Option<String>, controls: Option<serde_utils::PyValue<Control>>) -> Self {
        let relationship_type = relationship_type.into_inner();
        let controls = controls.map(|v| v.into_inner());
        Relationship{unique_id, relationship_type, description, protocol, metadata, controls}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Relationship>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Relationship> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Relationship>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Relationship",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for Relationship {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.unique_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("unique_id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a Relationship from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("unique_id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InteractsRelationship {
    pub actor: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(alias = "nodes"))]
    pub InteractsRelationship_nodes: Vec<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InteractsRelationship {
    #[new]
    #[pyo3(signature = (actor, InteractsRelationship_nodes))]
    pub fn new(actor: String, InteractsRelationship_nodes: Vec<String>) -> Self {
        InteractsRelationship{actor, InteractsRelationship_nodes}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InteractsRelationship>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InteractsRelationship> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InteractsRelationship>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InteractsRelationship",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct ConnectsRelationship {
    pub source: NodeInterface,
    pub destination: NodeInterface
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl ConnectsRelationship {
    #[new]
    #[pyo3(signature = (source, destination))]
    pub fn new(source: serde_utils::PyValue<NodeInterface>, destination: serde_utils::PyValue<NodeInterface>) -> Self {
        let source = source.into_inner();
        let destination = destination.into_inner();
        ConnectsRelationship{source, destination}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ConnectsRelationship>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ConnectsRelationship> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ConnectsRelationship>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ConnectsRelationship",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct DeployedInRelationship {
    pub container: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(alias = "nodes"))]
    pub DeployedInRelationship_nodes: Vec<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl DeployedInRelationship {
    #[new]
    #[pyo3(signature = (container, DeployedInRelationship_nodes))]
    pub fn new(container: String, DeployedInRelationship_nodes: Vec<String>) -> Self {
        DeployedInRelationship{container, DeployedInRelationship_nodes}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<DeployedInRelationship>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<DeployedInRelationship> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<DeployedInRelationship>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid DeployedInRelationship",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct ComposedOfRelationship {
    pub container: String,
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(alias = "nodes"))]
    pub ComposedOfRelationship_nodes: Vec<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl ComposedOfRelationship {
    #[new]
    #[pyo3(signature = (container, ComposedOfRelationship_nodes))]
    pub fn new(container: String, ComposedOfRelationship_nodes: Vec<String>) -> Self {
        ComposedOfRelationship{container, ComposedOfRelationship_nodes}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ComposedOfRelationship>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ComposedOfRelationship> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ComposedOfRelationship>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ComposedOfRelationship",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Decision {
    #[cfg_attr(feature = "serde", serde(alias = "description"))]
    pub Decision_description: String,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list",
        serialize_with = "serde_utils::serialize_inlined_dict_list"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(alias = "nodes"))]
    pub Decision_nodes: Vec<NodeOrSubtype>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list",
        serialize_with = "serde_utils::serialize_inlined_dict_list"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(alias = "relationships"))]
    pub Decision_relationships: Vec<Box<Relationship>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub controls: Option<Control>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Decision {
    #[new]
    #[pyo3(signature = (Decision_description, Decision_nodes, Decision_relationships, controls=None))]
    pub fn new(Decision_description: String, Decision_nodes: serde_utils::PyValue<Vec<NodeOrSubtype>>, Decision_relationships: serde_utils::PyValue<Vec<Box<Relationship>>>, controls: Option<serde_utils::PyValue<Control>>) -> Self {
        let Decision_nodes = Decision_nodes.into_inner();
        let Decision_relationships = Decision_relationships.into_inner();
        let controls = controls.map(|v| v.into_inner());
        Decision{Decision_description, Decision_nodes, Decision_relationships, controls}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Decision>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Decision> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Decision>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Decision",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct ControlDetail {
    #[cfg_attr(feature = "serde", serde(alias = "requirement_url"))]
    pub ControlDetail_requirement_url: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub config_url: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub config: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl ControlDetail {
    #[new]
    #[pyo3(signature = (ControlDetail_requirement_url, config_url=None, config=None))]
    pub fn new(ControlDetail_requirement_url: String, config_url: Option<String>, config: Option<String>) -> Self {
        ControlDetail{ControlDetail_requirement_url, config_url, config}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ControlDetail>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ControlDetail> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ControlDetail>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ControlDetail",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Control {
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct ControlRequirement {
    pub control_id: String,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(alias = "description"))]
    pub ControlRequirement_description: String
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl ControlRequirement {
    #[new]
    #[pyo3(signature = (control_id, name, ControlRequirement_description))]
    pub fn new(control_id: String, name: String, ControlRequirement_description: String) -> Self {
        ControlRequirement{control_id, name, ControlRequirement_description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ControlRequirement>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ControlRequirement> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ControlRequirement>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ControlRequirement",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for ControlRequirement {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.control_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("control_id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a ControlRequirement from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("control_id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Decorator {
    pub unique_id: String,
    pub type_: String,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub target: Vec<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub applies_to: Vec<String>,
    pub data: String
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Decorator {
    #[new]
    #[pyo3(signature = (unique_id, type_, target, applies_to, data))]
    pub fn new(unique_id: String, type_: String, target: Vec<String>, applies_to: Vec<String>, data: String) -> Self {
        Decorator{unique_id, type_, target, applies_to, data}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Decorator>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Decorator> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Decorator>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Decorator",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for Decorator {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.unique_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("unique_id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a Decorator from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("unique_id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct EvidenceDocument {
    pub evidence: String
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl EvidenceDocument {
    #[new]
    #[pyo3(signature = (evidence))]
    pub fn new(evidence: String) -> Self {
        EvidenceDocument{evidence}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<EvidenceDocument>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<EvidenceDocument> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<EvidenceDocument>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid EvidenceDocument",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Transition {
    pub relationship_unique_id: String,
    pub sequence_number: isize,
    #[cfg_attr(feature = "serde", serde(alias = "description"))]
    pub Transition_description: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub direction: Option<TransitionDirection>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Transition {
    #[new]
    #[pyo3(signature = (relationship_unique_id, sequence_number, Transition_description, direction=None))]
    pub fn new(relationship_unique_id: String, sequence_number: isize, Transition_description: String, direction: Option<TransitionDirection>) -> Self {
        Transition{relationship_unique_id, sequence_number, Transition_description, direction}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Transition>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Transition> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Transition>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Transition",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Flow {
    pub unique_id: String,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(alias = "description"))]
    pub Flow_description: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub requirement_url: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub transitions: Vec<Transition>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub controls: Option<Control>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub metadata: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Flow {
    #[new]
    #[pyo3(signature = (unique_id, name, Flow_description, transitions, requirement_url=None, controls=None, metadata=None))]
    pub fn new(unique_id: String, name: String, Flow_description: String, transitions: serde_utils::PyValue<Vec<Transition>>, requirement_url: Option<String>, controls: Option<serde_utils::PyValue<Control>>, metadata: Option<String>) -> Self {
        let transitions = transitions.into_inner();
        let controls = controls.map(|v| v.into_inner());
        Flow{unique_id, name, Flow_description, transitions, requirement_url, controls, metadata}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Flow>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Flow> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Flow>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Flow",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for Flow {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.unique_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("unique_id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a Flow from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("unique_id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InterfaceDefinition {
    pub unique_id: String,
    pub definition_url: String,
    #[cfg_attr(feature = "serde", serde(alias = "config"))]
    pub InterfaceDefinition_config: String
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InterfaceDefinition {
    #[new]
    #[pyo3(signature = (unique_id, definition_url, InterfaceDefinition_config))]
    pub fn new(unique_id: String, definition_url: String, InterfaceDefinition_config: String) -> Self {
        InterfaceDefinition{unique_id, definition_url, InterfaceDefinition_config}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InterfaceDefinition>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InterfaceDefinition> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InterfaceDefinition>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InterfaceDefinition",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for InterfaceDefinition {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.unique_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("unique_id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a InterfaceDefinition from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("unique_id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InterfaceType {
    pub unique_id: String
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InterfaceType {
    #[new]
    #[pyo3(signature = (unique_id))]
    pub fn new(unique_id: String) -> Self {
        InterfaceType{unique_id}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InterfaceType>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InterfaceType> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InterfaceType>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InterfaceType",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct NodeInterface {
    pub node: String,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(alias = "interfaces"))]
    pub NodeInterface_interfaces: Option<Vec<InterfaceDefinition>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl NodeInterface {
    #[new]
    #[pyo3(signature = (node, NodeInterface_interfaces=None))]
    pub fn new(node: String, NodeInterface_interfaces: Option<serde_utils::PyValue<Vec<InterfaceDefinition>>>) -> Self {
        let NodeInterface_interfaces = NodeInterface_interfaces.map(|v| v.into_inner());
        NodeInterface{node, NodeInterface_interfaces}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<NodeInterface>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<NodeInterface> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<NodeInterface>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid NodeInterface",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Timeline {
    #[cfg_attr(feature = "serde", serde(default))]
    pub current_moment: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub moments: Vec<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub metadata: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Timeline {
    #[new]
    #[pyo3(signature = (moments, current_moment=None, metadata=None))]
    pub fn new(moments: Vec<String>, current_moment: Option<String>, metadata: Option<String>) -> Self {
        Timeline{moments, current_moment, metadata}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Timeline>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Timeline> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Timeline>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Timeline",
        ))
    }
}



pub mod node_moment_utl {
    use super::*;
    #[derive(Debug, Clone, PartialEq)]
    #[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
    pub enum node_type_range {
        NodeType(NodeType),
        String(String)    }

    #[cfg(feature = "pyo3")]
    impl<'py> FromPyObject<'py> for node_type_range {
        fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
            if let Ok(val) = ob.extract::<NodeType>() {
                return Ok(node_type_range::NodeType(val));
            }            if let Ok(val) = ob.extract::<String>() {
                return Ok(node_type_range::String(val));
            }Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                "invalid node_type",
            ))
        }
    }

    #[cfg(feature = "pyo3")]
    impl<'py> IntoPyObject<'py> for node_type_range {
        type Target = PyAny;
        type Output = Bound<'py, Self::Target>;
        type Error = PyErr;

        fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
            match self {
                node_type_range::NodeType(val) => Ok(val.into_pyobject(py).map(move |b| <pyo3::Bound<'_, _> as Clone>::clone(&b).into_any())?),
                node_type_range::String(val) => Ok(val.into_pyobject(py).map(move |b| <pyo3::Bound<'_, _> as Clone>::clone(&b).into_any())?),
            }
        }
    }


    #[cfg(feature = "pyo3")]
    impl<'py> IntoPyObject<'py> for Box<node_type_range>
    {
        type Target = PyAny;
        type Output = Bound<'py, Self::Target>;
        type Error = PyErr;
        fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
            (*self).into_pyobject(py).map(move |x| x.into_any())
        }
    }

    #[cfg(feature = "pyo3")]
    impl<'py> FromPyObject<'py> for Box<node_type_range> {
        fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
            if let Ok(val) = ob.extract::<node_type_range>() {
                return Ok(Box::new(val));
            }
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                "invalid node_type",
            ))
        }
    }

    #[cfg(feature = "stubgen")]
    ::pyo3_stub_gen::impl_stub_type!(node_type_range = NodeType | String);
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct NodeMoment {
    pub unique_id: String,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(alias = "description"))]
    pub Node_description: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub controls: Option<Control>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub metadata: Option<String>,
    pub node_type: node_moment_utl::node_type_range,
    #[cfg_attr(feature = "serde", serde(default))]
    pub valid_from: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub adrs: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub interfaces: Option<Vec<InterfaceDefinition>>,
    #[cfg_attr(feature = "serde", serde(alias = "details"))]
    pub NodeMoment_details: String,
    pub details: String,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    #[cfg_attr(feature = "serde", serde(alias = "interfaces"))]
    pub Node_interfaces: Option<Vec<InterfaceDefinition>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl NodeMoment {
    #[new]
    #[pyo3(signature = (unique_id, name, Node_description, node_type, NodeMoment_details, details, controls=None, metadata=None, valid_from=None, adrs=None, interfaces=None, Node_interfaces=None))]
    pub fn new(unique_id: String, name: String, Node_description: String, node_type: node_moment_utl::node_type_range, NodeMoment_details: String, details: String, controls: Option<serde_utils::PyValue<Control>>, metadata: Option<String>, valid_from: Option<NaiveDate>, adrs: Option<Vec<String>>, interfaces: Option<serde_utils::PyValue<Vec<InterfaceDefinition>>>, Node_interfaces: Option<serde_utils::PyValue<Vec<InterfaceDefinition>>>) -> Self {
        let controls = controls.map(|v| v.into_inner());
        let interfaces = interfaces.map(|v| v.into_inner());
        let Node_interfaces = Node_interfaces.map(|v| v.into_inner());
        NodeMoment{unique_id, name, Node_description, node_type, NodeMoment_details, details, controls, metadata, valid_from, adrs, interfaces, Node_interfaces}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<NodeMoment>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<NodeMoment> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<NodeMoment>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid NodeMoment",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for NodeMoment {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.unique_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("unique_id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a NodeMoment from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("unique_id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TimeUnit {
    pub unit: TimeUnitName,
    pub value: f64
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TimeUnit {
    #[new]
    #[pyo3(signature = (unit, value))]
    pub fn new(unit: TimeUnitName, value: f64) -> Self {
        TimeUnit{unit, value}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TimeUnit>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TimeUnit> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TimeUnit>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TimeUnit",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct RateUnit {
    pub rate: f64,
    pub per: RatePerUnit
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl RateUnit {
    #[new]
    #[pyo3(signature = (rate, per))]
    pub fn new(rate: f64, per: RatePerUnit) -> Self {
        RateUnit{rate, per}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<RateUnit>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<RateUnit> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<RateUnit>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid RateUnit",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct OptionList {
    #[cfg_attr(feature = "serde", serde(default))]
    pub decisions: Option<Vec<Decision>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl OptionList {
    #[new]
    #[pyo3(signature = (decisions=None))]
    pub fn new(decisions: Option<serde_utils::PyValue<Vec<Decision>>>) -> Self {
        let decisions = decisions.map(|v| v.into_inner());
        OptionList{decisions}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<OptionList>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<OptionList> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<OptionList>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid OptionList",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct RelationshipType {
    #[cfg_attr(feature = "serde", serde(default))]
    pub interacts: Option<InteractsRelationship>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub connects: Option<ConnectsRelationship>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub deployed_in: Option<DeployedInRelationship>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub composed_of: Option<ComposedOfRelationship>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub options: Option<Vec<Box<Decision>>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl RelationshipType {
    #[new]
    #[pyo3(signature = (interacts=None, connects=None, deployed_in=None, composed_of=None, options=None))]
    pub fn new(interacts: Option<serde_utils::PyValue<InteractsRelationship>>, connects: Option<serde_utils::PyValue<ConnectsRelationship>>, deployed_in: Option<serde_utils::PyValue<DeployedInRelationship>>, composed_of: Option<serde_utils::PyValue<ComposedOfRelationship>>, options: Option<serde_utils::PyValue<Vec<Box<Decision>>>>) -> Self {
        let interacts = interacts.map(|v| v.into_inner());
        let connects = connects.map(|v| v.into_inner());
        let deployed_in = deployed_in.map(|v| v.into_inner());
        let composed_of = composed_of.map(|v| v.into_inner());
        let options = options.map(|v| v.into_inner());
        RelationshipType{interacts, connects, deployed_in, composed_of, options}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<RelationshipType>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<RelationshipType> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<RelationshipType>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid RelationshipType",
        ))
    }
}






#[cfg(feature = "stubgen")]
define_stub_info_gatherer!(stub_info);
