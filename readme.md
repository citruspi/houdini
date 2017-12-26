![](https://user-images.githubusercontent.com/2125849/34342959-c8822054-e9b8-11e7-844d-8accd6e9d9da.png)

<br/>

### Table of Contents

- [Overview](#overview)
- [SSH](#ssh) (Linux/Unix hosts)
- [Setup](#setup)
- [Usage](#usage)

<br>

## Overview

Houdini runs on [AWS Lambda][0] and executes commands on remote hosts
- over SSH using [Paramiko][1]
- over WinRM using [pywinrm][6]

### Sample Use Cases

- Executing commands on hosts from other Lambda functions
- Executing commands on hosts from other hosts in other VPCs/network configurations (e.g. deploy a copy of the Lambda to each network environment)
- Cron-as-a-Service; schedule commands to run on hosts using [scheduled events][4]

<br>

## SSH

### Security Considerations

- Current policy for unknown host keys is [`AutoAdd`][5]

### Limitations

- Requires an RSA private key

### Todo

- Accept DSS, ECDSA, and Ed25519 private keys
- Support private keys secured with a password
- Support use of PTYs (pseudo-terminals)
- Support a timeout for (1) connecting to the host (2) executing the command
- Allow for a stricter host key checking and for the user to specify the expected host key
- Return the command's exit code

<br>

## Setup

1. Create new KMS key
2. Base64 encode your private key:
```
$ cat ~/.ssh/id_rsa | base64
LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb3dJQkFBS0NBUUVBdXRweFdCSDM0QWdadUtqR2ZaV1NnZHNDcVc3UXR5MXlhQlROazJ4b1VYVE9GNjRqCjBWQVgwVEFSTVpVNlJBZzdaVXVUWCtzV2pzT0VaQS9kUzRFTnp2NkJlUklZZ1Z6TnVYRDY2cnlFWjJuYnR0d20KRTBQem5QRnNad2RrdStnTzlsZEVVT0M2VDNBUi9iZVZUM0E3ZXcyWlpPazhNNTNrK0I0V00vMFc1enUyZi9WNQprSUN1RnJFZG1rNklZNnFkc08zQ2ptM2lxZEdyUXBlOUVIdTJrWVdqNHN5Ly9Qd0xHL1dkSnl5aWFua2hjQnoyCmFOUkFjTFdxcUV2bkNLcGR2WWNHWkxKd0dQaHQ3Z20waUpsdCtLUVZvOUdta0NkMjBjV1hHQlVXTlNvY0JiaE4KVzRjYkQvazFxTlpZdEJFZVhKaEJWU3FwY0laQmVLNnNUbFNlTndJREFRQUJBb0lCQURPWXVHMjZZSGxEbzE2agpkRlFmWmxwblVML2FzdFd5UGdKUnBFYk9TNndhbGdKaCt0QUV6dDdiNkJPS0FwSGd1QTRMcFlGNkdEdUo3OWYxCnJZVDQrUWdzclRIeWRrUGFqWkJraTFVZ2cydFBCdlhpcXJ6dEthc3YyMkJENFdRbCsyTzR5MHVPRXNSMnpQRUQKcmI1RzNwWG5ObkZ3R2tpaWxDU1Rva3Z1MmxFMWFpNUpOWWY3c1g4OXNFbC9icWlvWHpYOHJneWs3RTVNQlZVdwpDdUVRWlFkanlZU2ZQV1hUeHZRVnVkdU11c3NYOS9rMytZRlpMcFlWNzk2Wksvc09hQ2JaUnIzUVYxZTJsVkowCnZpaXFaWFFkcGRaSkhTd2wrUmpsVGhtMDNQbExueGZPOEVmenZNTXpxL1dQdDhvSEM3RzhVQUdkbCt5cnozV2kKS0hYMzhQa0NnWUVBM1lSQmF1aEV2eE5OVU14MXZGeEZ1MUllYU9JNEtQa3Z5bzkvbnpSODV0TExwL0pFRkpESwpCb0duRHc0TlloQkkzOHlzQnpvb1JtU2QxN1RPdytwODUrYzhwOHpXQUdCZThzOWFkMTU1eDhsQzFGbFpnc1daCmFyS3Y1blpTa0Q5U1R1OUFuZ2pkdlVLeVpQSTk0aXk3TXlEWkpDY0NMM0RKZ1JHb3NZOHZMWU1DZ1lFQTEvRE8KTC84ZG1ReUtLQTZuVTRTVjdpWWRSN0JGS01vYXlldnRiKzdSM2szbWt0ZmQzdUtDamVDZDhYU25DSzBaL1ZwawpXU2pWZTJUM0JTWE9Ocnd5YkMrV2pTeTMya2cxNzJLYzF5YnJOVkkwdGNGNjd5b1lSMHZFSnd3OHZDcGZiV21QCmhRT0hWYzlyc1EwZDlDbXRadERiL1ZhMHlITHE3N2JwUXdSSlFqMENnWUErbVJsRGRNKzRqMlBSNlhWNy9UZFgKY0NWWHpsWEFmbXFhKzJJOVF6L29tcmtpaEx2b2MrSWpaSkFwR1BkL05zcmhNNTJKalUzRVZycWtNbHdiMFMvcQorTldUTmJkajg5ZmhGZWVpdy9mMkZWSGxZRHFEVWdQQXV5NHFHbFhLblpwTTVCK0dpVXJnS1BEd3hlUG0vbTBJClRjZ1BCMWIrd1Fpd2lLVDdTRk0wc1FLQmdRQzZrUFN6aHlqZFNIWTg4WndqamxPek0vN3NKeUU1Z3BQdWpRWFIKUlhiUktHRGowZG1CYmhYNTJtemJaanZDUlR4RkprbTR0b3pyVldvT2FvRmx6T2VMalBuMzh3RE5lTUlRbHhTRwoxcnMwa0ZlMkNQbmJsSFR4ZEVaK3JoWHpSSEM2S1ErMGpqM3BKNUlWb0EyWEhFTVNwN1RKaHBZZThScUdEWFF2ClVJNnl5UUtCZ0FXSFJUVUwrOGRET1VHOGFvRHBLZGU0anRpeElIQWxlelRYOERSNFRubGYwMW1hN0p0cHBLdWwKVll1b1BnL25DK05ldG5kSFNWZ0N5cmRCTzkxMlNQcjZFaHFWTUErdFhJQm9XcDFqVWcyV0RqeXVZR01xSkZjego1dGh4K0kzMlBYd0RpQVlYUTFsakNyNWFHMWdSbGlCYzhIZXdMVVdFWFF6c1JMcExwQTM0Ci0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0tCg==
```
3. Create a new parameter in SSM Parameter store with the following settings:

| Name | Value | Type | KMS Key ID |
|:-|:-|:-|:-|
| `ssh-private-key-{private_key_name}` | Output from step 2 | Secure String | Key ID from step 1 |

4. Create a new Lambda function with the desired network configuration and set the function handler to `houdini.lambda_handler`
5. Update your Lambda's IAM Role to provide it with the following IAM permission(s):
```
- ssm:GetParameter
```
6. Build the Lambda package using the vendored dependencies and upload `package.zip` to the Lambda function
```
$ make
``` 
7. Update the KMS key created in step 1 to allow for the IAM role in use by the Lambda from the previous step to decrypt data

<br/>

## Usage

Invoke the Lambda function with a payload e.g.

```json
{
    "mode": "ssh",
    "address": "127.0.0.1",
    "command": "uptime",
    "username": "ec2-user,
    "private-key": "production"
}
```

and expect a response e.g.

```json
{
    "stdin": null,
    "stdout": " 10:05:47 up  4:57,  1 user,  load average: 0.01, 0.01, 0.00\n",
    "stderr": ""
}
```

### Example

```python
$ python
>>> import json
>>> import boto3
>>> lambda_ = boto3.client('lambda')
>>> payload = {
...     'mode': 'ssh',
...     'address': 'foobar.somedomain.com',
...     'command': 'ps aux',
...     'username': 'ec2-user',
...     'private-key': 'myprivatekey'
... }
>>> resp = lambda_.invoke(FunctionName='houdini', Payload=json.dumps(payload))
>>> resp_payload = json.load(resp['Payload'])
>>> print(resp_payload['stdout'])
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.5  19648  2548 ?        Ss   05:08   0:00 /sbin/init
root      2223  0.0  2.6 362348 13292 ?        Ssl  05:08   0:02 /usr/bin/amazon-ssm-agent
root      2233  0.0  0.4  52960  2148 ?        S<sl 05:08   0:00 auditd
root      2262  0.0  0.5 247388  2804 ?        Sl   05:08   0:00 /sbin/rsyslogd -i /var/run/syslogd.pid -c 5
root      2284  0.0  0.0   6476    96 ?        Ss   05:08   0:00 rngd --no-tpm=1 --quiet
rpc       2302  0.0  0.4  35320  2232 ?        Ss   05:08   0:00 rpcbind
rpcuser   2323  0.0  0.6  39888  3244 ?        Ss   05:08   0:00 rpc.statd
dbus      2354  0.0  0.0  21800   228 ?        Ss   05:08   0:00 dbus-daemon --system
root      2389  0.0  0.2   4352  1440 ?        Ss   05:08   0:00 /usr/sbin/acpid
root      2536  0.0  0.6  80492  3092 ?        Ss   05:08   0:00 /usr/sbin/sshd
ntp       2546  0.0  0.8  29772  4272 ?        Ss   05:08   0:00 ntpd -u ntp:ntp -p /var/run/ntpd.pid -g
root      2566  0.0  0.9  89532  4556 ?        Ss   05:08   0:00 sendmail: accepting connections
smmsp     2575  0.0  0.8  80992  4072 ?        Ss   05:08   0:00 sendmail: Queue runner@01:00:00 for /var/spool/clientmqueue
root      2587  0.0  0.4 121604  2472 ?        Ss   05:08   0:00 crond
root      2601  0.0  0.0  19144   168 ?        Ss   05:08   0:00 /usr/sbin/atd
root      2634  0.0  0.3   6464  1652 ttyS0    Ss+  05:08   0:00 /sbin/agetty ttyS0 9600 vt100-nav
root      2637  0.0  0.2   4316  1456 tty1     Ss+  05:08   0:00 /sbin/mingetty /dev/tty1
root      2640  0.0  0.2   4316  1452 tty2     Ss+  05:08   0:00 /sbin/mingetty /dev/tty2
root      2650  0.0  0.3  10880  1600 ?        S    05:08   0:00 /sbin/udevd -d
root     23661  0.0  1.4 117872  7120 ?        Ss   08:19   0:00 sshd: ec2-user [priv]
ec2-user 23663  0.0  0.7 117872  3700 ?        S    08:19   0:00 sshd: ec2-user@pts/0
ec2-user 23664  0.0  0.6 115360  3436 pts/0    Ss   08:19   0:00 -bash
root     23700  0.0  0.0      0     0 ?        S    08:20   0:00 [kworker/u30:2]
mongod   23940  0.3 10.1 782536 50992 ?        Sl   08:58   0:17 /usr/bin/mongod -f /etc/mongod.conf
root     24356  0.0  0.4   9368  2320 ?        Ss   08:59   0:00 /sbin/dhclient -H localhost -q -lf /var/lib/dhclient/dhclient-eth0.leases -pf /var
/run/dhclient-eth0.pid eth0
root     24452  0.0  0.3   9368  1996 ?        Ss   08:59   0:00 /sbin/dhclient -6 -nw -lf /var/lib/dhclient/dhclient6-eth0.leases -pf /var/run/dhc
lient6-eth0.pid -H localhost eth0
ec2-user 24499  0.0  5.1 211924 25636 pts/0    Sl+  08:59   0:00 mongo
root     24742  0.0  1.3 117872  6992 ?        Ss   10:20   0:00 sshd: ec2-user [priv]
ec2-user 24744  0.0  0.8 117872  4012 ?        S    10:20   0:00 sshd: ec2-user@notty
root     24758  0.0  1.4 117872  7108 ?        Ss   10:21   0:00 sshd: ec2-user [priv]
ec2-user 24760  0.0  0.7 117872  3940 ?        S    10:21   0:00 sshd: ec2-user@notty
root     24841  0.0  1.4 117872  7044 ?        Ss   10:27   0:00 sshd: ec2-user [priv]
ec2-user 24843  0.0  0.7 117872  3948 ?        S    10:27   0:00 sshd: ec2-user@notty
ec2-user 24844  0.0  0.4 117216  2380 ?        Rs   10:27   0:00 ps aux

>>>
```

[0]: https://aws.amazon.com/lambda/
[1]: http://www.paramiko.org
[2]: https://aws.amazon.com/kms/
[3]: https://aws.amazon.com/systems-manager/features/#Parameter_Store
[4]: http://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html
[5]: http://docs.paramiko.org/en/2.4/api/client.html?#paramiko.client.AutoAddPolicy
[6]: https://github.com/diyan/pywinrm