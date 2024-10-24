# layer 7 load balancer


Things to install:

- Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Verify that Homebrew is installed by running: 

```bash
brew --version
```

- HAProxy

Use Homebrew to install HAProxy by running the following command: 

```bash
brew install haproxy
```

Verify that HAProxy was installed correctly: 

```bash
haproxy -v
```
 

To start HAProxy server:

```bash
haproxy -f haproxy/haproxy.cfg
```

To check if HAProxy server is running on port 5009:

```bash
 lsof -i :5009 -P
```

To kill the HAProxy server --> kill <PID> of HAProxy process from above command