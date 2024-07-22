# AWS CloudFormation

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721163600/qQMAeir7CedYq2w0pM_zlw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/0ufBj0fY2GkHj2Sf_xbRG36IUQ7YDUiQP.png)

## Summary

AWS CloudFormation automates and streamlines the task of repeatedly creating and deploying AWS resources in a consistent manner.  With AWS CloudFormation, you can ensure that all of your security and compliance controls are deployed along with your new environment.

To learn more, see [AWS CloudFormation](https://aws.amazon.com/cloudformation/).

## Use

- Create and deploy infrastructure templates for CI/CD automations.
- Infrastructure as Code

Typical CloudFormation flow

- Template > Stack > Physical Resource (Create)
- Stack (Delete) > (Delete) Physical Resource
- v2 Template > Existing Stack > Resources Changed


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
    


## DependsOn

When CloudFormation creates, updates or deletes resources it tries to do it in parrelel (Do as many tasks at a time). However there are times where one action needs to be taken before another, or a resource relies on the prior creation and/or configuration of another resource. 

There are two ways that CloudFormation accomplishes an order of operations.

1.) Intrinsically. By default, it will automatically identify templates that refrence other resources and ensure that they are built prior. 

2.) `DependsOn` statement. With this statement we are explicitly telling CloudFormation that something needs to be done first. This is required in some use-cases where the CloudFormation template does not reference a value from another resource, but the resource still needs to exsist in order to accomplish the task. 

An Example could be creating an Elastic IP (EIP), as it requires an Internet Gateway (IGW) attatched to a VPC in order to work. 

```
wPEIP:
  Type: AWS::EC2::EIP
  DependsOn: InternetGatewayAttachement #A resource mentioned prior
  Properties:
    InstanceId: !Ref WordpressEC2
```

## Wait Condition, Creation Policy, and cfn-signal
When a CloudFormation template is completed, it recieves a notification back notifying it as *Create-Completed*. Although, this may be accurate for some processes, it does not cover the entire completion process. 

Example: A template creates an EC2 instances, and installs software for hosting a web application. The Create-Complete notification would alert you to the fact that the EC2 instance completed being built, but it does not say anything about the processes that took place on the EC2. This is because CloudFormation is only waiting on an AWS signal for completion, and AWS EC2 will not be able to signal regarding things happening inside the instance. Therefore:

- cfn-signal: Is installed on the EC2 instance and can be used for sending signals back to the AWS Console. It can send either success or failure signals.

- Creation Policy: Are used to wait for a series of signals from cfn-signal. It can have a timeout defined, as well as a count of success signals. If a failure signal is recieved, the task will show failed. Creation Policies are most commonly used for EC2 instances and Auto-scaling to verify that all parts of the CloudFormation template passed successfully. 

- Wait Conditions: A WaitCondition is a similar function that can wait for specific data to be returned from the instance before continuing onto another action. Wait Conditions are used to retireve the aditional details of a signal and its response. For instance if there is a failure, we can use !GetAtt WaitCondition.Data to access the data of the received signal and see what caused the data. Once we pull this into an Attribute, you could also then configure automated remediation for certain failure reason (ex. a certificate needs to uploaded error)


## Nested Stack

Nested Stacks allow you to reuse CloudFormation Templates for creating isolated and self contained resources. 

- Used for overcoming the 500 resource limit of one stack
- Modular templates (code reuse) or using lots of potable templates
- Make the installation process easier when everything is lifecycle linked
  - If everything is installed to be used together, work together, until it is deleted together.

## Cross Stack References

Cross Stack References allow you to reuse resorces inside a stack, and share the resources between other stacks.
- Useful for when you want to have a shared VPC 
- Works by outputing inforamtion and resource values, then exporting them, and referencing resources from the export with `!ImportValue SharedVPCID`.
- Service-Oriented & Different Lifecycles & STACK Reuse

## DeletionPolicy

If you delete a logical resource from a template or delete a stack in general, the resulting action will be to delete the associated physical resource as well. 

Although the default is to delete, you can define on a per resource basis what action will be taken. 
- Delete (Default), Retain, or (if supported) Snapshot
  - Snapshot only works on: EBS Volume, ElastiCache, Neptune, RDS, and Redshift.
    - Snapshots will continue past Stack lifetime therefore it is necessary to clean them up after they are no longer needed or they will cost $$ 



## Stack Roles

By default CloudFormation uses the permissions of the user creating the stack. Therefore the user account interacting with CloudFormation needs to have permissions to create and manage all of the resources involved in the CloudFormation Template and the services in the stack. 

CloudFormation can *assume a role* to gain the permissions. Allowing you to implement role seperation in your enviornemnt, and have the identity creating the stack not have resource permissions, just the ability to pass the role into CloudFormation (PassRole).
- This means that the role will be attached to the stack and used for any operations

In this scenario, an AWS admin would create a role that has the permisions to create, update, and delete AWS resources. Then give a user, the permission to Create, update, or delete stacks, **& to pass in a role**. This way the admin, may not even have the permissions to Stack, and the user will not need the permissions to manipulate any resources. 



## Change Sets

When you make a change to a CloudFormation template you can expect the typical/default flow of:

v2 Template > Existing Stack > Resources Changes

This can cause either *no interuption*, *some interuption* (EC2 Reboot = some downtime), or *replacement* (Possible data loss) 

A *Change Set* let you preview changes. 
 - Create a change set is an option in the stack. Using this instead of just simply overwritting it will show additional information about the change prior to taking action. 





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

- Created in an optional *'Conditions'* section of the template. Conditional are either True or False and are processed before resources are created, in order to control whether a logical resources is created or not. They can use AND, EQUALS, IF, NOT, and OR. 

- Example conditions could be how many AZs to create in a resource, or what size of EC2 instance should be created within the stack, dependant on a prior condition*. 

A conditional statement is built of up being in three locations. 

1.) In the parameters section, there multiple options available. This could be through either *Templated Parameters* or *Psuedo Parameters*. The below example uses Templated Parameters, specifically 'AllowedValues'.

```
Parameters:
  EnvType:
    Default: 'dev'
    Type; String
    AllowedValues:
      - 'dev'
      - 'prod'
```

2.) The Conditions block, where we have the conditional statement and the condition name. Below we have the condition 'IsProd' which compares itself to/equals the `!Ref Envtype`

```
Conditions:
  IsProd: !Equals
    - !Ref EnvType
    - 'prod'
```

3.) Next in the template defining the logical resource, we have two logical resources listed. The first is the default, the second contains the conditional statement `IsProd`. If the IsProd condition has been met, the second resource value will be chosen. 

```
Resource:
  Wordpress:
    Type: 'AWS::EC2:Instance'
    Properties:
      ImageID: 'ami-323i3ew239'
   WordpressProd:
    Type: 'AWS::EC2:Instance'
Condition: IsProd
    Properties:
      ImageID: 'ami-323i3ew239'
```




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


