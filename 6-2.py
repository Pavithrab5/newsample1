1. YANG Code

module ultraconfig-interfaces {

  yang-version 1.1;

  namespace
    "http://ultraconfig.com.au/ns/yang/ultraconfig-interfaces";

  prefix if;

  organization
    "Ultra Config Pty Ltd";

  contact
    "Support: <https://ultraconfig.com.au/contact/>";

  description
    "This YANG module has been created for the purpose of a tutorial.
      It defines the model for a basic ethernet interface";

  revision "2020-01-03" {
    description
      "Initial Revision";
    reference
      "Learn YANG - Full Tutorial for Beginners";
  }

  typedef dotted-quad {
    type string {
      pattern
        '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}'
          + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])';
    }
    description
      "Four octets written as decimal numbers and
       separated with the '.' (full stop) character.";
  }

  container interfaces {
    list interface {
      key "name";
      leaf name {
        type string;
        mandatory "true";
        description
          "Interface name. Example value: GigabitEthernet 0/0/0";
      }
      leaf address {
        type dotted-quad;
        mandatory "true";
        description
          "Interface IP address. Example value: 10.10.10.1";
      }
      leaf subnet-mask {
        type dotted-quad;
        mandatory "true";
        description
          "Interface subnet mask. Example value: 255.255.255.0";
      }
      leaf enabled {
        type boolean;
        default "false";
        description
          "Enable or disable the interface. Example value: true";
      }
    }
    list interface-state {
      config false;
      key "name";
      leaf name {
        type string;
        description
          "Interface name. Example value: GigabitEthernet 0/0/0";
      }
      leaf oper-status {
        type enumeration {
          enum up;
          enum down;
        }
        mandatory "true";
        description
          "Describes whether the interface is physically up or down";
      }
    }
  }
}

2. Respond to [hello]

<?xml version="1.0" encoding="UTF-8"?>
<hello
xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <capabilities>
<capability>urn:ietf:params:netconf:base:1.0</capability>
</capabilities></hello> ]]>]]>

3. Check Config Details

<?xml version="1.0" encoding="UTF-8"?>
<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<get-config>
<source>
<running/>
</source>
</get-config>
</rpc>]]>]]>

4. IP

<?xml version="1.0" encoding="UTF-8"?>
<nc:rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<nc:get>
<nc:filter type="subtree">
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<interface>
<GigabitEthernet>
<name>GigabitEthernet1</name>
<description></description>
<ip></ip>
</GigabitEthernet>
<interface>
</native>
</nc:filter>
</nc:get>
</nc:rpc>
]]>]]>
