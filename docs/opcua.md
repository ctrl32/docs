# OPC UA

OPC UA is how ctrl32 talks to SCADA and to other runtimes. It lives on
**Linux devices** — in every version — and works
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

## The editor as a client — variables from another server

The OPC UA page can also **browse a server and import its variables**
into the project (`source: opcua`): pick nodes from the tree, they
become ordinary project variables, and the runtime polls them in.
That is how one runtime reads another — or how a ctrl32 device sits
beside an existing OPC UA installation without touching it. One
server per project.

Setup, node addressing and the certificate modes are described in
detail on [The Linux runtime](linux-runtime.md).

![The OPC UA page: server state, certificate and the browse-and-import tree](img/opcua-page.webp){: .sb-center}
