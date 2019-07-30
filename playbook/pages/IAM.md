# Identity Access and Management

## TL;DR

- Central control
- Shared access
- Granular permissions
- Identity federation
- Multi-factor authentication
- Password policies
- PCI DSS compliance

Broken into four parts;

1. Users:
   1. end users
2. Groups:
    1. 'A collection of users'
    2. Users in a group inherit the group permission set
3. Policies:
    1. In JSON format
    2. Also in GUI
4. Roles:
    1. Create, delete, edit and assign roles to users and/or groups.

## Generic notes

- IAM is universal, i.e. global in scope
- Root account by default is that which opens an account with AWS, and its a super admin
- New users default to no permissions (must be set once established)
- New users are generated an access key and secret access key (development key) but the key can only be viewed once (on screen) - download the CSV to view it on the local machine
- Always enable MFA
- Do enable a password policy
