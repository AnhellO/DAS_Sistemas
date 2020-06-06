# Securing Your Containerized Applications with NGINX

1. Benefits of a Reverse Proxy for Security 
2. NGNIX Best Practices for TLS 
3. Running NGNIX in Docker

### Benefits of a Reverse Proxy
HTTP Security is definitely one of the most important thing that you can think about when you're building an application. 

- HTTPS Security and Facade Routing
- TLS Offload 
- Authentication / Authorization Offload

### Complexities of TLS
There's a lot of complexities when you decide that you want to enable TLS that can be somewhat confusing. Especially when you're trying to just focus on designing your application. The first is the ability to do SSL or TLS protocols that backwards compatibility or users may need to access. You also may want to decide to use certain Ciphers over others.
You also may want to know if you want to support SSL sessions or SSL tickets. And then how are you going to manage the certificates and keys. And do you want to enable OCSP stapling. And what kind of performance hit will you see when you're enabling TLS, and how do you monitor vulnerabilities for any open SSL or TLS issues. And how do you do patching or patching life cycles.
- SSL/TLS Protocols
- Ciphers
- Sessions
- Certificate and Key Management
- OCSP 
- Performance Degradation
- Security Vulnerabilities and Patching

So this can get complicated when you do start to enable TLS. Using reverse proxy can help with that. We imagine the same application framework that we have before, where we have our three services running in Docker. And then we have our two virtual servers. 

### Deploying NGINX on Docker 
If we think about it before we've been talking about using NGNIX to sit in front of your dockerized applications and act as a Reverse Proxy. There's no reason why NGNIX can't actually run in Docker. The easiest way to do that is to use Docker Compose. 

1. Configure services you want to communicate thru NGINX using **"expose"**
2. Link your services together with the **"links"** option
3. The publish your NGINX service using the **"ports"** mappging


### Acquired knowledg
How and why NGINX's lightweight and powerfull architecture makes 
it very popular choice for securing containerized applications as a sidecar proxy within containers. 
