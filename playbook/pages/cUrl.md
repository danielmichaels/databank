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

## Get Request/Response headers

Two simple ways:
1. `curl -v {URL}`
2. `curl --trace-ascii - {URL}` for stdout or replace `-` with a filename to save the output.

## Follow Redirects

Using the `-L` for Location header will make Curl follow all redirects. Use with `-I` to see just the headers and concatenate both with `-v` to form `-ILv` to get verbose output without the body.

By default Curl will follow 50 redirects before it will error. You can manually override this and set how many times it is allowed to redirect by adding `--max-redirs n` where `n` is the number required. Unlimited redirects can be set with `--max-redirs -1`.
