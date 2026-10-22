---
title: "OPC UA"
slug: opcua
section: "Protocols"
order: 315
sidebar_position: 315
generator: tools/docs_export.py
---

# OPC UA

OPC UA is how ctrl32 talks to SCADA and to other runtimes. It lives on
**Linux devices** and works
in both directions:

## The device as a server

A Linux runtime serves the project's variables over OPC UA on port
4840 — `Objects/ctrl32`, one node per variable (`ns=1;s=name`). Any
SCADA, historian or test client subscribes and reads; a write is a
**command**, executed only for variables with **rw** access. A
variable can be kept off the server with one checkbox in the variable
list.

The endpoint can run signed and encrypted (Basic256Sha256): the
certificate is managed live from the editor's OPC UA page —
self-signed generated on the device, your own PEM/DER pair, or
encryption off for a closed network.

### Turning the server on

In the devices tree, under the device's **Ethernet**, add **OPC UA**.
Nothing else is configured in the project: the device serves its
variables from the next deploy onwards.

### Addressing

```
opc.tcp://<address>:4840        the endpoint
ns=1;s=<variable name>          the node id of a variable
```

A client finds the variables under **Objects › ctrl32** with their
live values, or takes a node id straight. The node id **is** the
variable's name — there is nothing to map and nothing to name twice.
A variable renamed in the project is renamed on the server at the
next deploy, so a client that addresses it by id has to follow.

![The project's variables: every one of them is a node on the server, under its own name](img/opcua-vars.webp){: .sb-center}

### What a write does

A write from a client goes the same road as a screen's button: it is a
write, not a force. The program owns the variable again on its next
cycle. That separates two kinds of variable:

| Variable | A client writing it |
|:---|:---|
| a **setpoint** (rw, the program only reads it) | the value stays — it is the client's to set |
| an **actual value** (the program computes it) | overwritten on the next cycle — it cannot be held down from outside |
| read-only | refused |

### The device certificate

The **Device certificate** section of the OPC UA page works on the
**running device**, not on the project: type the device's address,
pick a mode and press *Apply to device*. The runtime stores the
choice and restarts, and the page shows what the device answered.

![The certificate section: the address of the running device, the three modes and Apply to device](img/opcua-cert.webp){: .sb-center}

| Mode | When |
|:---|:---|
| **Self-signed (generated on the device)** | the normal choice — the device makes its certificate on first start, a client trusts it once |
| **Own certificate (PEM/DER files)** | a site that issues its certificates centrally |
| **No encryption** | the plain endpoint only, for a closed network nobody else reaches |

The certificate lives with the **device**, not in the project:
deploying one project to two devices does not give them the same
identity, and a new deploy does not change it.

## The editor as a client — variables from another server

The OPC UA page can also **browse a server and import its variables**
into the project (`source: opcua`): pick nodes from the tree, they
become ordinary project variables, and the runtime polls them in.
That is how one runtime reads another — or how a ctrl32 device sits
beside an existing OPC UA installation without touching it. One
server per project.

Setup, node addressing and the certificate modes are described in
detail on [The Linux runtime](/docs/hardware/linux-runtime/).

![The OPC UA page: server state, certificate and the browse-and-import tree](img/opcua-page.webp){: .sb-center}

## When a client gets no answer

| Check | Why |
|:---|:---|
| **Deploy first** | the server starts with the project that declares it; a device running an older project does not serve |
| **Port 4840** reachable | on the device's own network, not through a firewall that only forwards the web port |
| **Address, not name** | a client that connects by host name needs the name the device answers to; the address always works |
| **The project on the device** | a device serves the variables of the project it runs, not of the one open in the editor |
