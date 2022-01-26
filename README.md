# CVE-2022-23967

> In TightVNC 1.3.10, there is an integer signedness error and resultant
> heap-based buffer overflow in InitialiseRFBConnection in rfbproto.c
> (for the vncviewer component). There is no check on the size given to
> malloc, e.g., -1 is accepted. This allocates a chunk of size zero,
> which will give a heap pointer. However, one can send 0xffffffff bytes
> of data, which can have a DoS impact or lead to remote code execution.
> 
> ------------------------------------------
> 
> [Vulnerability Type]
> Buffer Overflow
>
> ------------------------------------------
>
> [Vendor of Product]
> TightVNC
>
> ------------------------------------------
>
> [Affected Product Code Base]
> vncviewer - 1.3.10
>
> ------------------------------------------
>
> [Affected Component]
> file : rfbproto.c, function : InitialiseRFBConnection , line of code : 307
>
> ------------------------------------------
>
> [Attack Type]
> Remote
>
> ------------------------------------------
>
> [Impact Denial of Service]
> true
>
> ------------------------------------------
>
> [Attack Vectors]
> You just need to setup a fake server, to interact with the vulnerable client.
>
> ------------------------------------------
>
> [Discoverer]
> Maher Azzouzi
>
> ------------------------------------------
>
> [Reference]
> https://www.tightvnc.com/licensing-server-x11.php

Use CVE-2022-23967.
