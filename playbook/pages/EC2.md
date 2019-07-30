# EC2


<!-- vim-markdown-toc GFM -->

* [EBS](#ebs)
* [Logins](#logins)

<!-- vim-markdown-toc -->

## EBS

API codes:
| api name   | name                     | description                                                                                         | use cases                                   | volume size      | max IOPS |
| ---------- | --------------------     | ---------------                                                                                     | --------                                    | -                | -        |
| `gp2`      | General Purpose SSD      | Gen. purposed SSD that balances price and performance for a wide variety of transactional workloads | Most work loads                             | 1 Gib - 16 TiB   | 16,000   |
| `io1`      | Provioned IOPS SSD       | Highest performance SSD designed for mission critical applications                                  | Databases                                   | 4 GiB - 16 TiB   | 64,000   |
| `st1`      | Throughput Optimised HDD | Low cost HDD designed for frequently accessed, throughput intensive loads                           | Big Data & Data warehouses                  | 500 GiB - 16 TiB | 500      |
| `sc1`      | Cold HDD                 | Lowest cost HDD for less frequently accessed workloads                                              | File Servers                                | 500 GiB - 16 TiB | 250      |
| `standard` | EBS Magnetic             | Previous Gen. HDD                                                                                   | Workloads where data is access infrequently | 1 GiB - 1 TiB    | 40-200   |


## Logins

- Ubuntu:
  - `ubuntu@<ip or dns>`
- AMI:
  - `ec2-user@<ip or dns>`
