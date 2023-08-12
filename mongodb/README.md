# MongoDB

## Rule of Thumb

- Data that is accessed together, should be stored together.

# Transactions

- Distributed ACID Transactions
- A query that allows to add/update data in multiple collections and they both either succeed/fails
- To use transactions, the DB must be set as **Replica Set** or **Sharded cluster**
- Not supported on standalone deployments
- Transactions should be linked to a session at the time of creation

## ACID

- A = Atomicity
- B = Consistency
- C = Isolation
- D = Durability

# Change Streams (Real-time)

- Change streams allow you to receive notifications about changes made to your MongoDB databases and collections.
- Uses NodeJS EventEmitter on functionality.
- Uses an aggregation pipeline to filter data for output
- Change streams can be resumed with change stream token.

## Ways to use

1. Monitor using EventEmitted's on() class
2. Monitor using ChangeStreams's hasNext() (using while loop)
3. Monitor using NodeJS Stream API
4. Monitor using Atlas triggers

# Cluster

- A group of servers that store your data

# Replica set

- Few connected MongoDB instances that store the same data
- An instance is a single machine (locally or in a cloud) running a certain software

# Triggers (by Atlas)

- Don't have to program change streams
- No server management
- Configuration UI (less code to write)

# Improve Performance

- Increase poolSize (recommended 10)
- Break Up One Slow Operation Into Many Fast Operations
- Indexing (For lookup fields)
- maxTimeMS

# Security

- MongoDB provides both client and cluster authentication for security

## Authentication

- Verifies the identity of a user
- Who are you?

## Available Machanisms

- SCRAM (default)
- X.509

### MongoDB Enterprise Only

- LDAP
- KERBEROS

## Authorization

- Role Based Access Control
- Verifies the privileges of a user
- What do you have access to?
