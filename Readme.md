# Introduction to NGINX

### Lesson 1 (Getting Started with NGINX Web Server)
- Installing and Serving Websites.
- Configuring NGINX Reverse Proxy.
- Managing Multiple Applications.
- Understanding and Configuring Logs.

### Lesson 2 (Securing Your NGINX Server)
- Password Protecting Applications.
- Implementing Rate Limiting.
- Blocking Malicious Traffic.
- Enabling HTTPS Security.

### Lesson 3 (Load Balancing and Performance Tuning)
- Implementing Basic Load Balancing.
- Advanced Load Balancing Strategies.
- Caching Responses for Performance.
- Enabling Gzip Compression.

### Lesson 4 (Advanced NGINX Configuration and Monitoring)
- URL Rewriting and Redirects.
- Creating Custom Error Pages.
- Implementing Health Checks.


## Notes on Lesson 3
__Important Consideration on cache validity.__
* Lower the cache validity time, so updates appear sooner at the cost of    more frequent backend requests.
* Use cache purging to manually remove outdated entries when data changes on the backend.
* Implement cache revalidation, so NGINX checks with the backend (using conditional requests with ETags or Last-Modified headers) before serving cached content.

### Variables in Lesson 3
- $scheme: Whether the request used HTTP or HTTPS.
- $proxy_host: The target hostname being proxied to.
- $request_uri: The full path and query string of the request.
- $is_args: A question mark if query arguments exist, empty otherwise.
- $args: The actual query string parameters.
- $upstream_cache_status variable contains values like HIT (served from cache), MISS (fetched from backend), EXPIRED (cache entry was stale), or BYPASS (caching was intentionally bypassed). 
- always parameter ensures the header appears even in error responses, which is useful for debugging.
- error: When an error occurs connecting to the backend.
- timeout: When the backend doesn't respond in time.
- updating: While a cache entry is being refreshed in the background.

## Notes on Lesson 4
__Redirects__ tell the client's browser to make a new request to a different URL, which is visible to the user.
__Rewrites__ happen internally on the server, transforming one URL pattern into another without the client knowing.