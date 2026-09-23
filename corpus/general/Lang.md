---
provenance: "docs/original/Lang.htm#overview"
unit_type: "general"
title: "Vision Language Basics"
ingested: "2026-09-22"
---

## Overview

The Vision language is designed around the concept of communicating objects. Objects interact with one another via a process known as ["sending a message".](Fund/4.md) A message is a request for an object to carry out one of its operations. In the example:

      universe select: [ score > 10]

the message *select:* is sent to the object named *universe*. Some messages require parameters. For example, to send the *select:* message, you provide a parameter that represents your selection criteria. In the example, the *select:* parameter is *\[score \> 10\]*.

All requests in Vision conform to this object/message pattern known as a **Message Expression**. Message expressions always produce an object as a result. In the preceding example, the expression produces a new object which represents the list of companies that satisfied the criteria.

The general form for a message expression is:

      object message

A message expression includes a recipient object, a selector, and possibly some parameters. The **Recipient** is the object to which the message is sent. The **Selector** is the name of the message. A **Parameter** or **Argument** is an extra piece of information needed to execute the message. Messages can have any number of parameters (including none).

------------------------------------------------------------------------
