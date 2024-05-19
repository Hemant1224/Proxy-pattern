# Proxy-pattern

The Proxy Design Pattern is a structural design pattern that provides an object representing another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object. This can be useful for various reasons, such as controlling access, reducing cost, enhancing security, or adding extra functionality.

Types of Proxies
Virtual Proxy: Controls access to a resource that is expensive to create. It creates the resource on demand.
Remote Proxy: Manages interaction between a client and a remote object.
Protection Proxy: Controls access to the original object based on access rights.
Smart Proxy: Adds additional behavior when accessing the object, such as reference counting, logging, etc.
