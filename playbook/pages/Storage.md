# Azure Storage

There are 4 main types of storage on Azure

| Name | Function |
|---|---|
| Blob storage | Storage for very large objects - video and bitmaps for example |
| File storage | File shares that can be accessed and managed like a file server |
| Queue storage | A data store for queuing and reliably delivering messages between apps. MQ service layer for sending messages (less storage more like an AMPQ queue) |
| Table storage | Storage for noSQL data |

These all share the same characteristics:
- **Durable** and highly available with redundancy and replication.
- **Secure** through automatic encryption and RBAC.
- **Scalable** with virtually unlimited storage.
- **Managed**, handling maintenance and any critical problems for you.
- **Accessible** from anywhere in the world over HTTP or HTTPS.