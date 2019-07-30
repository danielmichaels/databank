# HTTP 101

## General Notes

*What happens when: you type an address into the search bar and hit enter*

1. The browser extracts the domain name from the search bar
2. The hosts DNS cache is queried, if not found a DNS request is sent via your configured DNS server.
3. After getting the IP address via DNS, the host will initiate a TCP connection with that address.
4. If the connection is setup a response will be sent from that server and its data will be rendered.

## HTTP

HTTP is a standard and browsers will conform to it. HTTP has the following methods:

### **GET**

The most common request, it broadly asks the remote host to send the requested data. In general, GET requests will retrieve the data from a Uniform Request Identified (URI).

### **HEAD**

Very similar to the *GET* request except that it only retrieves the header information. All body content is omitted.

### **POST**

The client will invoke a *POST* request such as adding a new user, or piece of information which will a function on the servers side. This function will then act on the *POST* and make changes on the servers side. It is up to the  server to validate and check the request, and does not need to action the *POST* request.

### **PUT**

Similar to a *POST* request, a *PUT* references an already existing entity, and requests a update to it. Again, the server must verify, and is not obligated to action the request.

### **DELETE**

A request to the server to call a function capable of deleting a specified entity. Server side is responsible for checking.

### **TRACE**

An uncommon request that is often seen during diagnostics such as Traceroute. Can see what the server was delivered.

### **CONNECT**

For use with a proxy to initiate the connection.

### **OPTIONS**

A utility call that asks the server which HTTP methods are supported.
