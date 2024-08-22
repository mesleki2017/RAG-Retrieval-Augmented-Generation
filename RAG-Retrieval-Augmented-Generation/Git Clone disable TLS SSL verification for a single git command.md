https://stackoverflow.com/questions/11621768/how-can-i-make-git-accept-a-self-signed-certificate

### To disable TLS/SSL verification for a single git command

try passing `-c` to `git` with the proper config variable, or use [Flow's answer](https://stackoverflow.com/a/19363404/194894):

```
git -c http.sslVerify=false clone https://example.com/path/to/git
```

### To disable SSL verification for all repositories

It is possible to globally deactivate ssl verification. It is **highly recommended to NOT do this** but it is mentioned for completeness:

```
git config --global http.sslVerify false # Do NOT do this!
```

---

There are quite a few SSL configuration options in `git`. From the man page of `git config`:

```
http.sslVerify
    Whether to verify the SSL certificate when fetching or pushing over HTTPS.
    Can be overridden by the GIT_SSL_NO_VERIFY environment variable.

http.sslCAInfo
    File containing the certificates to verify the peer with when fetching or pushing
    over HTTPS. Can be overridden by the GIT_SSL_CAINFO environment variable.

http.sslCAPath
    Path containing files with the CA certificates to verify the peer with when
    fetching or pushing over HTTPS.
    Can be overridden by the GIT_SSL_CAPATH environment variable.
```

A few other useful SSL configuration options:

```
http.sslCert
    File containing the SSL certificate when fetching or pushing over HTTPS.
    Can be overridden by the GIT_SSL_CERT environment variable.

http.sslKey
    File containing the SSL private key when fetching or pushing over HTTPS.
    Can be overridden by the GIT_SSL_KEY environment variable.

http.sslCertPasswordProtected
    Enable git's password prompt for the SSL certificate. Otherwise OpenSSL will
    prompt the user, possibly many times, if the certificate or private key is encrypted.
    Can be overridden by the GIT_SSL_CERT_PASSWORD_PROTECTED environment variable.
```