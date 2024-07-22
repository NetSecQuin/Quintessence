# AWS CloudFormation

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721163600/qQMAeir7CedYq2w0pM_zlw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/0ufBj0fY2GkHj2Sf_xbRG36IUQ7YDUiQP.png)

## Summary

AWS CloudFormation automates and streamlines the task of repeatedly creating and deploying AWS resources in a consistent manner.  With AWS CloudFormation, you can ensure that all of your security and compliance controls are deployed along with your new environment.

To learn more, see [AWS CloudFormation](https://aws.amazon.com/cloudformation/).

## Use

- Create and deploy infrastructure templates for CI/CD automations.
- Infrastructure as Code




## Physical & Logic Resources

CloudFormation Templates are YAML or JSON and contain logical resources (the "WHAT")
Templates are used to create stacks. Stacks create physical resources from the logical resoureces. 
A CloudFormation Stack contains multiple CloudFormation templates?
Stacks are synched. If a stacks template is changes, the physical resoureces are changes. If a stack is deleted, then the resources are deleated. 

## Template Parameters & Psuedo Parameters

Paramets accept variable input, whether entered externally or through AWS itself. 

#### Template Parameters

Template Parameters accept external (human) input when a stack is created or updated via the Console, CLI, or an API.

The values for the parameter can be defined in the Template within a logic resource. This allows you to influence the physical resource and/or configuration instead of leaving configuration entirely open-ended.
  - Preset types consist of: *configure defaults*, *allowed values*, *min or max length*, and *allowed patterns*.
  - You can also enable *NoEcho* for hidden values like passwords
  - Each parameter can have a type. Simple ones like String, Int, and List. Or AWS ones like a specific item from a list like a VPC or subnets.
 
Example of Template Parameter where end-user would be queried for an EC2 instance size:
```
Parameters:
  InstanceType:
    Type: String
    Default: 't3.micro'
    AllowedValues:
    - 't3.micro'
    - 't3.medium'
    - 't3.large'
  Description: 'Pick a supported InstanceType.'
InstanceAmiID:
  Type: String
  Description: 'AMI ID for Instances.'
```  

#### Psuedo Parameters
Psuedo Parameters are defined in a CLoudFormation template but unlike template parameters, the values are filled in by AWS. These parameters are defined/based upon the enviornment when creating the stack. 

- Psuedo Parameters follow the syntax of ```AWS::FIELD```

For example, if you were to run a stack in *us-east-1* with the psuedo parameter `AWS::Region`, AWS would fill the region parameter with the region the stack is being run. Other examples could be **AWS::StackName**, **AWS::StackId**, or **AWS::AccountID**. 

## Mappings

Mappings can contain a number of key to value pairs that allow for lookups within an template. They are used to improve template portability. The Mappings template shows a variety of options then mappings use the !FindInMap Intrinsic function in order to lookup the value inside a mapping. 

An Example Mapping would be 

```
Mappings:
  RegionMap:
    us-east-1:
      HVM64: "ami-0932eh921383s"
      HVMG2: "ami-0932js832kds9"
   us-west1:
      HVM64: "ami-0723dsjf83kws1"
      HVMG2: "ami-08232dsi219323"
   eu-east-1:
      HVM64: "ami-9328sfad234231a"
      HVMG2: "ami-28193sjkri9810p"
```

They can contain either one key, or top and second level keys. In the following Mapping we have a toplevel and a secondlevel key. 
The Syntax for a "!FindInMap function is:

``` !FindInMap [ MapName, TopLevelKey, SecondLevelKey ] ```

Where in this example, we are Mapping to the `MapName` "RegionMap". The `TopLevelKey` we are pulling from the AWS region the template was launched in, and the `SecondLevelKey` "HVM64".

``` !FindInMap ["RegionMap", !Ref 'AWS::Region', "HVM64" ] ```

## Outputs

Optional within a template, not many have them, but sometimes useful. Allows you to declare outputs in the CLI, Console, and accesible from a parent stack when nesting. 

Example output: would output a description string and the value. 

```
Outputs:
  WordpressURL:
    Description: "Instance WebURL"
    Value: !Join [ '', [ 'https://', !GetAtt Instance.DNSname ] ]
```
    





## Intrinsic Functions

Allow you to make decisions or pick attributes due to a run-time descision or finding. 

Intrinsic Functions follow the following syntax inside a CloudFormation template. Additionally there are numerous types of Intrinsic Functions as seen below. 

```
Instance:
  Type: AWS::EC2::Instance
  Properties:
    ImageID: !Ref LatestAmiID #Ref Intrinsic Function
    InstanceType: "t3.micro"
    KayName: "A4L"
    AvailabilityZone: !Select [ 0, !GetAZs ''] # Get AZs and Select Function
```

#### `Ref` & `Fn::GetATT` - Reference a value from a logical resource or parameter in another Cloudformation Template. (Template1 makes a VPC, template 2 references VPC name in Template1)
  - Whenever an action is prefrormed a value is returned. For instance when creating an EC2 with a logical resource, an instanceID is returned. When you want to reference the returned value, we use `!Ref Instance`.
  - Additionally there may be sub-attributes associated with the returned value. When the same EC2 instance is created, in addition to the resourceID, we also get additional details about the instance (PublicIP, DNSname, etc.) These values can be retrieved with `Fn:: !GetAtt LogicalResource.Attribute`

#### `Fn::Join` & `Fn:Split` - Join strings together or split them up. (If you create a EC2 with an IPv4 address, you could use join to add the IP to a url)
  - `!Split` lets us take in a single string and split it into a series of list values. For example if we have `!Split ["|" , "hippy|dippy|doopy|daa"]` the output list would be `["hippy", "dippy", "doopy", "daa"]` as it was deliminitated by `|`
  - `!join` concats a list into a single string value. `!Join [ '', [ 'https://', !GetAtt Instance.DNSname ] ]`

#### `Fn:GetAZs` & `Fn::Select` - Get a list of AZs in a region. Select an item in a list. (Get a list of AZs, select an AZ from the list)
 - Commonly used together, but 'select' will select an option from a retrieved list of results. For example if we want to get the availibility zones thare are availabile in a region, we may use `!GetAZs "us-east-1"` or `!GetAZs ""` (current region). This will return a list of all AZs in that region.
 - Next we will want to select an AZ and have its value returned to the logical reference. This can be down with `!Select [ 0, !GetAZs '' ]` which will choose the first item in the returned list.

#### Conditions: `Fn::IF, AND, Equals, Not & Or` - Provision resources based on a condition (IF a certain parameter is set to prod, provision *big* instances)

#### `Fn::Base64` & `Fn::Sub` - Accepts non-encoded text and outputs Bases64. Substitute things within text based on runtime information
  - Used for when the external function requires an input of Base64.
  - `!Sub` Substitutes variable in the input (could be the pre-base64 text) with their actual runtime values. Examples of this could be `${Parameter}`, `${LogicalResource}` , `${LogicalResource.AttributeName}`


#### `Fn::Cidr` - Build CIDR blocks for networking
  - Used for generating a number of smaller CIDR ranges for subnets from a larger VPC range.
  - In the following example we want to create **16** subnets, and have **12** bits per CIDR. This gives us a **/20** range.
```
VPC:
  Type: AWS::EC2::VPC
  Properties:
    CidrBlock: "10.16.0.0/16
Subnet1:
  Type: AWS::EC2:Subnet
  Properties:
    CidrBlock: !Select [ "0", !Cidr [Cidr [!GetAtt VPC.CidrBlock, "16", "12" ]]
    VpcId: !Ref VPC
Subnet2:
  Type: AWS::EC2:Subnet
  Properties:
    CidrBlock: !Select [ "1", !Cidr [Cidr [!GetAtt VPC.CidrBlock, "16", "12" ]]
    VpcId: !Ref VPC
```
#### `Fn:ImportValue`
#### `Fn::FindInMap`

Review the ["Mappings" section above.](##Mappings)

#### `Fn::Transform`


