# Hugo 

Some Hugo snippets and memory joggers.

## Table of Contents

Currently Hugo does not support TOC, or rather it renders it poorly. Do not use.

## Bind Address

To get a bind address for serving locally run the following:

`hugo server --bind=<host_ip OR "0.0.0.0"> --baseUrl="<host_ip>:<port>`

example:

`hugo server --bind=0.0.0.0 --baseUrl="10.0.0.1:1313"`

Also works with Ngrok.
