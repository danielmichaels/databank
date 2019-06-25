# cUrl

A rad piece of software.

## Send Emails

Curl can send emails, and this is something I have done the STW platform as a workaround for a broken `mailx` config. 

**Syntax**

_curl syntax_
```
curl --url 'smtp://smtp.gmail.com:587' --ssl-reqd \
--mail-from 'me@me.com' --mail-rcpt 'you@you.com' \
--upload-file mail.txt --user 'user@me.com:password' \
--insecure -v
```

_mail.txt_
```
From: "User Name" <me@me.com>
To: "Recv" <you@your.com>
Subject: This is a subject

Please always leave a space between the metadata and here.
I can only accept RFC5322 compliant files
```

Notes:
- Can only upload files, not write to body and subject.
- `--insecure` or `-k` are set when cUrl's certificate is out of date.
