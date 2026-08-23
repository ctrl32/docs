# Intended use

The shortest version: **ctrl32 is a development and learning
environment.** It is not a certified product and it is not sold as one.

This page says plainly where it belongs, where it does not, and why the
distinction matters more than it might seem.

---

## No certification, of any kind

ctrl32 carries no CE marking as a finished product, no functional-safety
rating (no SIL, no PL), no type approval, and no third-party assessment
of any sort.

That is not an oversight to be fixed in the next release. Certification
is a process applied to a **specific device in a specific application**,
with test reports, a technical file and a manufacturer taking legal
responsibility for the result. Software that runs on hardware anybody can
buy, doing whatever the user programmed, cannot be certified in advance
by us.

**What that means in practice:** if your installation needs a certificate
— because a standard requires it, because an inspector will ask, or
because an insurer wrote it into a policy — ctrl32 cannot provide it, and
no amount of careful programming changes that.

---

## What it is for

**Learning.** Ladder, function block diagrams, ST, tags, a real scan
cycle, Modbus, CANopen — the same concepts a professional system uses,
on hardware that costs less than a textbook. A course, a school
laboratory, an apprenticeship, or teaching yourself in the evening.

**Prototyping.** Trying an idea before committing to expensive hardware.
Finding out whether a control strategy works, what the timing looks like,
how a drive behaves — with a full engineering tool, not a breadboard and
a serial monitor.

**Your own projects.** A workshop, a greenhouse, a model railway, a
brewery in a garage, a home automation experiment. Things where you are
the owner, the operator and the person who carries the consequences.

**Development work.** Building and testing logic that will later run
somewhere else, with a simulator, live monitoring and a scope that
records every cycle.

---

## Where it does not belong

!!! danger "Never in a safety function"
    Emergency stop, guards, light curtains, two-hand controls,
    limit switches that prevent damage — all of these are **hard-wired**,
    with certified components, independent of any software.

    This is not a limitation of ctrl32 in particular. It is how safety is
    done everywhere, including on systems that cost a hundred times more.
    Software is what makes things happen; hardware is what stops them.

**Not where people can be hurt.** If a failure of the control could
injure somebody, this is the wrong tool and the honest answer is a
certified controller from a manufacturer who accepts that liability.

**Not where a failure costs somebody else money.** A setup that
somebody else depends on, a process that ruins a batch, equipment that
belongs to a customer. Not because ctrl32 is unreliable, but because when
something does go wrong, "it ran on an uncertified hobby controller" is a
sentence nobody wants to say to an insurer.

**Not in an installation subject to inspection.** Anything an authority
will look at wants documentation ctrl32 does not carry.

**Not on the open internet.** There is no TLS. A board belongs on its own
network — see the network notes in [WEBview](webview.md).

---

## Why we say this so directly

Because the alternative is worse for everybody.

A tool that quietly lets people believe it is more than it is eventually
ends up somewhere it should not be, and the person who put it there had
no way of knowing. Saying it once, clearly, at the front of the
documentation, is cheaper than the conversation that follows the
alternative.

It also lets us build the tool honestly. ctrl32 does real ladder, a real
cycle, real fieldbuses — because that is what makes it worth learning on,
not because we are quietly hoping somebody puts it in a factory.

---

## Where the responsibility sits

You program it, you install it, you decide what it controls. What ctrl32
provides is the environment: an editor, a runtime, and documentation that
tells you the truth about both.

Where the consequences of a failure matter, use a controller certified
for the job. Learn on this one, prototype on this one, build your own
things with it — and be clear-eyed about which of those you are doing.

!!! note "This page is not legal advice"
    It describes what ctrl32 is and how we sell it. What your particular
    installation requires depends on where you are and what it does, and
    that is a question for someone qualified to answer it.
