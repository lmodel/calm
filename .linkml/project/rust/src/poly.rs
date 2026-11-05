#![allow(non_camel_case_types)]

use crate::*;
use crate::poly_containers::*;


pub trait Architecture   {

    fn Architecture_nodes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, NodeOrSubtype>>;
    // fn Architecture_nodes_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, NodeOrSubtype>>;
    // fn set_Architecture_nodes<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Node>;

    fn Architecture_relationships<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Relationship>>;
    // fn Architecture_relationships_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Relationship>>;
    // fn set_Architecture_relationships<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Relationship>;

    fn metadata<'a>(&'a self) -> Option<&'a str>;
    // fn metadata_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_metadata(&mut self, value: Option<&'a str>);

    fn controls<'a>(&'a self) -> Option<&'a crate::Control>;
    // fn controls_mut(&mut self) -> &mut Option<&'a crate::Control>;
    // fn set_controls<E>(&mut self, value: Option<E>) where E: Into<Control>;

    fn Architecture_flows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Flow>>;
    // fn Architecture_flows_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Flow>>;
    // fn set_Architecture_flows<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Flow>;

    fn adrs<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn adrs_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_adrs(&mut self, value: Option<&Vec<String>>);


}

impl Architecture for crate::Architecture {
        fn Architecture_nodes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, NodeOrSubtype>> {
        return self.Architecture_nodes.as_ref();
    }
        fn Architecture_relationships<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Relationship>> {
        return self.Architecture_relationships.as_ref();
    }
        fn metadata<'a>(&'a self) -> Option<&'a str> {
        return self.metadata.as_deref();
    }
        fn controls<'a>(&'a self) -> Option<&'a crate::Control> {
        return self.controls.as_ref();
    }
        fn Architecture_flows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Flow>> {
        return self.Architecture_flows.as_ref();
    }
        fn adrs<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.adrs.as_ref();
    }
}


pub trait Node   {

    fn unique_id<'a>(&'a self) -> &'a str;
    // fn unique_id_mut(&mut self) -> &mut &'a str;
    // fn set_unique_id(&mut self, value: String);

    fn node_type(&self) -> node_utl::node_type_range;
    // fn node_type_mut(&mut self) -> &mut node_utl::node_type_range;
    // fn set_node_type(&mut self, value: node_utl::node_type_range);

    fn name<'a>(&'a self) -> &'a str;
    // fn name_mut(&mut self) -> &mut &'a str;
    // fn set_name(&mut self, value: String);

    fn Node_description<'a>(&'a self) -> &'a str;
    // fn Node_description_mut(&mut self) -> &mut &'a str;
    // fn set_Node_description(&mut self, value: String);

    fn details<'a>(&'a self) -> Option<&'a str>;
    // fn details_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_details(&mut self, value: Option<&'a str>);

    fn Node_interfaces<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InterfaceDefinition>>;
    // fn Node_interfaces_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::InterfaceDefinition>>;
    // fn set_Node_interfaces<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InterfaceDefinition>;

    fn controls<'a>(&'a self) -> Option<&'a crate::Control>;
    // fn controls_mut(&mut self) -> &mut Option<&'a crate::Control>;
    // fn set_controls<E>(&mut self, value: Option<E>) where E: Into<Control>;

    fn metadata<'a>(&'a self) -> Option<&'a str>;
    // fn metadata_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_metadata(&mut self, value: Option<&'a str>);


}

impl Node for crate::Node {
        fn unique_id<'a>(&'a self) -> &'a str {
        return &self.unique_id[..];
    }
        fn node_type(&self) -> node_utl::node_type_range {
            self.node_type.clone()
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn Node_description<'a>(&'a self) -> &'a str {
        return &self.Node_description[..];
    }
        fn details<'a>(&'a self) -> Option<&'a str> {
        return self.details.as_deref();
    }
        fn Node_interfaces<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InterfaceDefinition>> {
        return self.Node_interfaces.as_ref();
    }
        fn controls<'a>(&'a self) -> Option<&'a crate::Control> {
        return self.controls.as_ref();
    }
        fn metadata<'a>(&'a self) -> Option<&'a str> {
        return self.metadata.as_deref();
    }
}
impl Node for crate::NodeMoment {
        fn unique_id<'a>(&'a self) -> &'a str {
        return &self.unique_id[..];
    }
        fn node_type(&self) -> node_utl::node_type_range {
            match &self.node_type {
                node_moment_utl::node_type_range::NodeType(x) => node_utl::node_type_range::NodeType(x.clone()),
                node_moment_utl::node_type_range::String(x) => node_utl::node_type_range::String(x.clone()),
            }
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn Node_description<'a>(&'a self) -> &'a str {
        return &self.Node_description[..];
    }
        fn details<'a>(&'a self) -> Option<&'a str> {
        return Some(&self.details);
    }
        fn Node_interfaces<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InterfaceDefinition>> {
        return self.Node_interfaces.as_ref();
    }
        fn controls<'a>(&'a self) -> Option<&'a crate::Control> {
        return self.controls.as_ref();
    }
        fn metadata<'a>(&'a self) -> Option<&'a str> {
        return self.metadata.as_deref();
    }
}

impl Node for crate::NodeOrSubtype {
        fn unique_id<'a>(&'a self) -> &'a str {
        match self {
                NodeOrSubtype::NodeMoment(val) => val.unique_id(),

        }
    }
        fn node_type(&self) -> node_utl::node_type_range {
        match self {
                NodeOrSubtype::NodeMoment(val) => val.node_type(),

        }
    }
        fn name<'a>(&'a self) -> &'a str {
        match self {
                NodeOrSubtype::NodeMoment(val) => val.name(),

        }
    }
        fn Node_description<'a>(&'a self) -> &'a str {
        match self {
                NodeOrSubtype::NodeMoment(val) => val.Node_description(),

        }
    }
        fn details<'a>(&'a self) -> Option<&'a str> {
        match self {
                NodeOrSubtype::NodeMoment(val) => val.details(),

        }
    }
        fn Node_interfaces<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InterfaceDefinition>> {
        match self {
                NodeOrSubtype::NodeMoment(val) => val.Node_interfaces().map(|x| x.to_any()),

        }
    }
        fn controls<'a>(&'a self) -> Option<&'a crate::Control> {
        match self {
                NodeOrSubtype::NodeMoment(val) => val.controls(),

        }
    }
        fn metadata<'a>(&'a self) -> Option<&'a str> {
        match self {
                NodeOrSubtype::NodeMoment(val) => val.metadata(),

        }
    }
}

pub trait Relationship   {

    fn unique_id<'a>(&'a self) -> &'a str;
    // fn unique_id_mut(&mut self) -> &mut &'a str;
    // fn set_unique_id(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn relationship_type<'a>(&'a self) -> &'a crate::RelationshipType;
    // fn relationship_type_mut(&mut self) -> &mut &'a crate::RelationshipType;
    // fn set_relationship_type<E>(&mut self, value: E) where E: Into<RelationshipType>;

    fn protocol<'a>(&'a self) -> Option<&'a crate::Protocol>;
    // fn protocol_mut(&mut self) -> &mut Option<&'a crate::Protocol>;
    // fn set_protocol(&mut self, value: Option<&'a Protocol>);

    fn metadata<'a>(&'a self) -> Option<&'a str>;
    // fn metadata_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_metadata(&mut self, value: Option<&'a str>);

    fn controls<'a>(&'a self) -> Option<&'a crate::Control>;
    // fn controls_mut(&mut self) -> &mut Option<&'a crate::Control>;
    // fn set_controls<E>(&mut self, value: Option<E>) where E: Into<Control>;


}

impl Relationship for crate::Relationship {
        fn unique_id<'a>(&'a self) -> &'a str {
        return &self.unique_id[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn relationship_type<'a>(&'a self) -> &'a crate::RelationshipType {
        return self.relationship_type.as_deref();
    }
        fn protocol<'a>(&'a self) -> Option<&'a crate::Protocol> {
        return self.protocol.as_ref();
    }
        fn metadata<'a>(&'a self) -> Option<&'a str> {
        return self.metadata.as_deref();
    }
        fn controls<'a>(&'a self) -> Option<&'a crate::Control> {
        return self.controls.as_ref();
    }
}


pub trait InteractsRelationship   {

    fn actor<'a>(&'a self) -> &'a str;
    // fn actor_mut(&mut self) -> &mut &'a str;
    // fn set_actor(&mut self, value: String);

    fn InteractsRelationship_nodes<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String>;
    // fn InteractsRelationship_nodes_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, String>;
    // fn set_InteractsRelationship_nodes<E>(&mut self, value: &Vec<String>) where E: Into<String>;


}

impl InteractsRelationship for crate::InteractsRelationship {
        fn actor<'a>(&'a self) -> &'a str {
        return &self.actor[..];
    }
        fn InteractsRelationship_nodes<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String> {
        return &self.InteractsRelationship_nodes;
    }
}


pub trait ConnectsRelationship   {

    fn source<'a>(&'a self) -> &'a crate::NodeInterface;
    // fn source_mut(&mut self) -> &mut &'a crate::NodeInterface;
    // fn set_source<E>(&mut self, value: E) where E: Into<NodeInterface>;

    fn destination<'a>(&'a self) -> &'a crate::NodeInterface;
    // fn destination_mut(&mut self) -> &mut &'a crate::NodeInterface;
    // fn set_destination<E>(&mut self, value: E) where E: Into<NodeInterface>;


}

impl ConnectsRelationship for crate::ConnectsRelationship {
        fn source<'a>(&'a self) -> &'a crate::NodeInterface {
        return &self.source;
    }
        fn destination<'a>(&'a self) -> &'a crate::NodeInterface {
        return &self.destination;
    }
}


pub trait DeployedInRelationship   {

    fn container<'a>(&'a self) -> &'a str;
    // fn container_mut(&mut self) -> &mut &'a str;
    // fn set_container(&mut self, value: String);

    fn DeployedInRelationship_nodes<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String>;
    // fn DeployedInRelationship_nodes_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, String>;
    // fn set_DeployedInRelationship_nodes<E>(&mut self, value: &Vec<String>) where E: Into<String>;


}

impl DeployedInRelationship for crate::DeployedInRelationship {
        fn container<'a>(&'a self) -> &'a str {
        return &self.container[..];
    }
        fn DeployedInRelationship_nodes<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String> {
        return &self.DeployedInRelationship_nodes;
    }
}


pub trait ComposedOfRelationship   {

    fn container<'a>(&'a self) -> &'a str;
    // fn container_mut(&mut self) -> &mut &'a str;
    // fn set_container(&mut self, value: String);

    fn ComposedOfRelationship_nodes<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String>;
    // fn ComposedOfRelationship_nodes_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, String>;
    // fn set_ComposedOfRelationship_nodes<E>(&mut self, value: &Vec<String>) where E: Into<String>;


}

impl ComposedOfRelationship for crate::ComposedOfRelationship {
        fn container<'a>(&'a self) -> &'a str {
        return &self.container[..];
    }
        fn ComposedOfRelationship_nodes<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String> {
        return &self.ComposedOfRelationship_nodes;
    }
}


pub trait Decision   {

    fn Decision_description<'a>(&'a self) -> &'a str;
    // fn Decision_description_mut(&mut self) -> &mut &'a str;
    // fn set_Decision_description(&mut self, value: String);

    fn Decision_nodes<'a>(&'a self) -> impl poly_containers::SeqRef<'a, NodeOrSubtype>;
    // fn Decision_nodes_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, NodeOrSubtype>;
    // fn set_Decision_nodes<E>(&mut self, value: &Vec<E>) where E: Into<Node>;

    fn Decision_relationships<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::Relationship>;
    // fn Decision_relationships_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::Relationship>;
    // fn set_Decision_relationships<E>(&mut self, value: &Vec<E>) where E: Into<Relationship>;

    fn controls<'a>(&'a self) -> Option<&'a crate::Control>;
    // fn controls_mut(&mut self) -> &mut Option<&'a crate::Control>;
    // fn set_controls<E>(&mut self, value: Option<E>) where E: Into<Control>;


}

impl Decision for crate::Decision {
        fn Decision_description<'a>(&'a self) -> &'a str {
        return &self.Decision_description[..];
    }
        fn Decision_nodes<'a>(&'a self) -> impl poly_containers::SeqRef<'a, NodeOrSubtype> {
        return &self.Decision_nodes;
    }
        fn Decision_relationships<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::Relationship> {
        return poly_containers::ListView::new(&self.Decision_relationships);
    }
        fn controls<'a>(&'a self) -> Option<&'a crate::Control> {
        return self.controls.as_ref();
    }
}


pub trait ControlDetail   {

    fn ControlDetail_requirement_url<'a>(&'a self) -> &'a str;
    // fn ControlDetail_requirement_url_mut(&mut self) -> &mut &'a str;
    // fn set_ControlDetail_requirement_url(&mut self, value: String);

    fn config_url<'a>(&'a self) -> Option<&'a str>;
    // fn config_url_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_config_url(&mut self, value: Option<&'a str>);

    fn config<'a>(&'a self) -> Option<&'a str>;
    // fn config_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_config(&mut self, value: Option<&'a str>);


}

impl ControlDetail for crate::ControlDetail {
        fn ControlDetail_requirement_url<'a>(&'a self) -> &'a str {
        return &self.ControlDetail_requirement_url[..];
    }
        fn config_url<'a>(&'a self) -> Option<&'a str> {
        return self.config_url.as_deref();
    }
        fn config<'a>(&'a self) -> Option<&'a str> {
        return self.config.as_deref();
    }
}


pub trait Control   {


}

impl Control for crate::Control {
}


pub trait ControlRequirement   {

    fn control_id<'a>(&'a self) -> &'a str;
    // fn control_id_mut(&mut self) -> &mut &'a str;
    // fn set_control_id(&mut self, value: String);

    fn name<'a>(&'a self) -> &'a str;
    // fn name_mut(&mut self) -> &mut &'a str;
    // fn set_name(&mut self, value: String);

    fn ControlRequirement_description<'a>(&'a self) -> &'a str;
    // fn ControlRequirement_description_mut(&mut self) -> &mut &'a str;
    // fn set_ControlRequirement_description(&mut self, value: String);


}

impl ControlRequirement for crate::ControlRequirement {
        fn control_id<'a>(&'a self) -> &'a str {
        return &self.control_id[..];
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn ControlRequirement_description<'a>(&'a self) -> &'a str {
        return &self.ControlRequirement_description[..];
    }
}


pub trait Decorator   {

    fn unique_id<'a>(&'a self) -> &'a str;
    // fn unique_id_mut(&mut self) -> &mut &'a str;
    // fn set_unique_id(&mut self, value: String);

    fn type_<'a>(&'a self) -> &'a str;
    // fn type__mut(&mut self) -> &mut &'a str;
    // fn set_type_(&mut self, value: String);

    fn target<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String>;
    // fn target_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, String>;
    // fn set_target(&mut self, value: &Vec<String>);

    fn applies_to<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String>;
    // fn applies_to_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, String>;
    // fn set_applies_to(&mut self, value: &Vec<String>);

    fn data<'a>(&'a self) -> &'a str;
    // fn data_mut(&mut self) -> &mut &'a str;
    // fn set_data(&mut self, value: String);


}

impl Decorator for crate::Decorator {
        fn unique_id<'a>(&'a self) -> &'a str {
        return &self.unique_id[..];
    }
        fn type_<'a>(&'a self) -> &'a str {
        return &self.type_[..];
    }
        fn target<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String> {
        return &self.target;
    }
        fn applies_to<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String> {
        return &self.applies_to;
    }
        fn data<'a>(&'a self) -> &'a str {
        return &self.data[..];
    }
}


pub trait EvidenceDocument   {

    fn evidence<'a>(&'a self) -> &'a str;
    // fn evidence_mut(&mut self) -> &mut &'a str;
    // fn set_evidence(&mut self, value: String);


}

impl EvidenceDocument for crate::EvidenceDocument {
        fn evidence<'a>(&'a self) -> &'a str {
        return &self.evidence[..];
    }
}


pub trait Transition   {

    fn relationship_unique_id<'a>(&'a self) -> &'a str;
    // fn relationship_unique_id_mut(&mut self) -> &mut &'a str;
    // fn set_relationship_unique_id(&mut self, value: String);

    fn sequence_number(&self) -> isize;
    // fn sequence_number_mut(&mut self) -> &mut isize;
    // fn set_sequence_number(&mut self, value: isize);

    fn Transition_description<'a>(&'a self) -> &'a str;
    // fn Transition_description_mut(&mut self) -> &mut &'a str;
    // fn set_Transition_description(&mut self, value: String);

    fn direction<'a>(&'a self) -> Option<&'a crate::TransitionDirection>;
    // fn direction_mut(&mut self) -> &mut Option<&'a crate::TransitionDirection>;
    // fn set_direction(&mut self, value: Option<&'a TransitionDirection>);


}

impl Transition for crate::Transition {
        fn relationship_unique_id<'a>(&'a self) -> &'a str {
        return &self.relationship_unique_id[..];
    }
        fn sequence_number(&self) -> isize {
        return self.sequence_number;
    }
        fn Transition_description<'a>(&'a self) -> &'a str {
        return &self.Transition_description[..];
    }
        fn direction<'a>(&'a self) -> Option<&'a crate::TransitionDirection> {
        return self.direction.as_ref();
    }
}


pub trait Flow   {

    fn unique_id<'a>(&'a self) -> &'a str;
    // fn unique_id_mut(&mut self) -> &mut &'a str;
    // fn set_unique_id(&mut self, value: String);

    fn name<'a>(&'a self) -> &'a str;
    // fn name_mut(&mut self) -> &mut &'a str;
    // fn set_name(&mut self, value: String);

    fn Flow_description<'a>(&'a self) -> &'a str;
    // fn Flow_description_mut(&mut self) -> &mut &'a str;
    // fn set_Flow_description(&mut self, value: String);

    fn requirement_url<'a>(&'a self) -> Option<&'a str>;
    // fn requirement_url_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_requirement_url(&mut self, value: Option<&'a str>);

    fn transitions<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::Transition>;
    // fn transitions_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::Transition>;
    // fn set_transitions<E>(&mut self, value: &Vec<E>) where E: Into<Transition>;

    fn controls<'a>(&'a self) -> Option<&'a crate::Control>;
    // fn controls_mut(&mut self) -> &mut Option<&'a crate::Control>;
    // fn set_controls<E>(&mut self, value: Option<E>) where E: Into<Control>;

    fn metadata<'a>(&'a self) -> Option<&'a str>;
    // fn metadata_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_metadata(&mut self, value: Option<&'a str>);


}

impl Flow for crate::Flow {
        fn unique_id<'a>(&'a self) -> &'a str {
        return &self.unique_id[..];
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn Flow_description<'a>(&'a self) -> &'a str {
        return &self.Flow_description[..];
    }
        fn requirement_url<'a>(&'a self) -> Option<&'a str> {
        return self.requirement_url.as_deref();
    }
        fn transitions<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::Transition> {
        return &self.transitions;
    }
        fn controls<'a>(&'a self) -> Option<&'a crate::Control> {
        return self.controls.as_ref();
    }
        fn metadata<'a>(&'a self) -> Option<&'a str> {
        return self.metadata.as_deref();
    }
}


pub trait InterfaceDefinition   {

    fn unique_id<'a>(&'a self) -> &'a str;
    // fn unique_id_mut(&mut self) -> &mut &'a str;
    // fn set_unique_id(&mut self, value: String);

    fn definition_url<'a>(&'a self) -> &'a str;
    // fn definition_url_mut(&mut self) -> &mut &'a str;
    // fn set_definition_url(&mut self, value: String);

    fn InterfaceDefinition_config<'a>(&'a self) -> &'a str;
    // fn InterfaceDefinition_config_mut(&mut self) -> &mut &'a str;
    // fn set_InterfaceDefinition_config(&mut self, value: String);


}

impl InterfaceDefinition for crate::InterfaceDefinition {
        fn unique_id<'a>(&'a self) -> &'a str {
        return &self.unique_id[..];
    }
        fn definition_url<'a>(&'a self) -> &'a str {
        return &self.definition_url[..];
    }
        fn InterfaceDefinition_config<'a>(&'a self) -> &'a str {
        return &self.InterfaceDefinition_config[..];
    }
}


pub trait InterfaceType   {

    fn unique_id<'a>(&'a self) -> &'a str;
    // fn unique_id_mut(&mut self) -> &mut &'a str;
    // fn set_unique_id(&mut self, value: String);


}

impl InterfaceType for crate::InterfaceType {
        fn unique_id<'a>(&'a self) -> &'a str {
        return &self.unique_id[..];
    }
}


pub trait NodeInterface   {

    fn node<'a>(&'a self) -> &'a str;
    // fn node_mut(&mut self) -> &mut &'a str;
    // fn set_node(&mut self, value: String);

    fn NodeInterface_interfaces<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InterfaceDefinition>>;
    // fn NodeInterface_interfaces_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::InterfaceDefinition>>;
    // fn set_NodeInterface_interfaces<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InterfaceDefinition>;


}

impl NodeInterface for crate::NodeInterface {
        fn node<'a>(&'a self) -> &'a str {
        return &self.node[..];
    }
        fn NodeInterface_interfaces<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InterfaceDefinition>> {
        return self.NodeInterface_interfaces.as_ref();
    }
}


pub trait Timeline   {

    fn current_moment<'a>(&'a self) -> Option<&'a str>;
    // fn current_moment_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_current_moment(&mut self, value: Option<&'a str>);

    fn moments<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String>;
    // fn moments_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, String>;
    // fn set_moments(&mut self, value: &Vec<String>);

    fn metadata<'a>(&'a self) -> Option<&'a str>;
    // fn metadata_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_metadata(&mut self, value: Option<&'a str>);


}

impl Timeline for crate::Timeline {
        fn current_moment<'a>(&'a self) -> Option<&'a str> {
        return self.current_moment.as_deref();
    }
        fn moments<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String> {
        return &self.moments;
    }
        fn metadata<'a>(&'a self) -> Option<&'a str> {
        return self.metadata.as_deref();
    }
}


pub trait NodeMoment : Node   {

    fn valid_from<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn valid_from_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_valid_from(&mut self, value: Option<&'a NaiveDate>);

    fn adrs<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn adrs_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_adrs(&mut self, value: Option<&Vec<String>>);

    fn interfaces<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InterfaceDefinition>>;
    // fn interfaces_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::InterfaceDefinition>>;
    // fn set_interfaces<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InterfaceDefinition>;

    fn NodeMoment_details<'a>(&'a self) -> &'a str;
    // fn NodeMoment_details_mut(&mut self) -> &mut &'a str;
    // fn set_NodeMoment_details(&mut self, value: String);


}

impl NodeMoment for crate::NodeMoment {
        fn valid_from<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.valid_from.as_ref();
    }
        fn adrs<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.adrs.as_ref();
    }
        fn interfaces<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InterfaceDefinition>> {
        return self.interfaces.as_ref();
    }
        fn NodeMoment_details<'a>(&'a self) -> &'a str {
        return &self.NodeMoment_details[..];
    }
}


pub trait TimeUnit   {

    fn unit<'a>(&'a self) -> &'a crate::TimeUnitName;
    // fn unit_mut(&mut self) -> &mut &'a crate::TimeUnitName;
    // fn set_unit(&mut self, value: TimeUnitName);

    fn value(&self) -> f64;
    // fn value_mut(&mut self) -> &mut f64;
    // fn set_value(&mut self, value: f64);


}

impl TimeUnit for crate::TimeUnit {
        fn unit<'a>(&'a self) -> &'a crate::TimeUnitName {
        return &self.unit;
    }
        fn value(&self) -> f64 {
        return self.value;
    }
}


pub trait RateUnit   {

    fn rate(&self) -> f64;
    // fn rate_mut(&mut self) -> &mut f64;
    // fn set_rate(&mut self, value: f64);

    fn per<'a>(&'a self) -> &'a crate::RatePerUnit;
    // fn per_mut(&mut self) -> &mut &'a crate::RatePerUnit;
    // fn set_per(&mut self, value: RatePerUnit);


}

impl RateUnit for crate::RateUnit {
        fn rate(&self) -> f64 {
        return self.rate;
    }
        fn per<'a>(&'a self) -> &'a crate::RatePerUnit {
        return &self.per;
    }
}


pub trait OptionList   {

    fn decisions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Decision>>;
    // fn decisions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Decision>>;
    // fn set_decisions<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Decision>;


}

impl OptionList for crate::OptionList {
        fn decisions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Decision>> {
        return self.decisions.as_ref();
    }
}


pub trait RelationshipType   {

    fn interacts<'a>(&'a self) -> Option<&'a crate::InteractsRelationship>;
    // fn interacts_mut(&mut self) -> &mut Option<&'a crate::InteractsRelationship>;
    // fn set_interacts<E>(&mut self, value: Option<E>) where E: Into<InteractsRelationship>;

    fn connects<'a>(&'a self) -> Option<&'a crate::ConnectsRelationship>;
    // fn connects_mut(&mut self) -> &mut Option<&'a crate::ConnectsRelationship>;
    // fn set_connects<E>(&mut self, value: Option<E>) where E: Into<ConnectsRelationship>;

    fn deployed_in<'a>(&'a self) -> Option<&'a crate::DeployedInRelationship>;
    // fn deployed_in_mut(&mut self) -> &mut Option<&'a crate::DeployedInRelationship>;
    // fn set_deployed_in<E>(&mut self, value: Option<E>) where E: Into<DeployedInRelationship>;

    fn composed_of<'a>(&'a self) -> Option<&'a crate::ComposedOfRelationship>;
    // fn composed_of_mut(&mut self) -> &mut Option<&'a crate::ComposedOfRelationship>;
    // fn set_composed_of<E>(&mut self, value: Option<E>) where E: Into<ComposedOfRelationship>;

    fn options<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Decision>>;
    // fn options_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Decision>>;
    // fn set_options<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Decision>;


}

impl RelationshipType for crate::RelationshipType {
        fn interacts<'a>(&'a self) -> Option<&'a crate::InteractsRelationship> {
        return self.interacts.as_ref();
    }
        fn connects<'a>(&'a self) -> Option<&'a crate::ConnectsRelationship> {
        return self.connects.as_ref();
    }
        fn deployed_in<'a>(&'a self) -> Option<&'a crate::DeployedInRelationship> {
        return self.deployed_in.as_ref();
    }
        fn composed_of<'a>(&'a self) -> Option<&'a crate::ComposedOfRelationship> {
        return self.composed_of.as_ref();
    }
        fn options<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Decision>> {
        return self.options.as_ref().map(|x| poly_containers::ListView::new(x));
    }
}
