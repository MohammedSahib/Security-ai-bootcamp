# TCP Port Scanner

A simple command-line TCP port scanner written in Python.

The scanner attempts TCP connections to a range of ports on a target host and reports which ports are open.

## Features

- Scan a custom range of TCP ports
- Accept IP addresses or hostnames
- Resolve hostnames to IPv4 addresses
- Detect open TCP ports
- Validate port ranges
- Socket timeout to prevent long connection waits
- Measure total scan time
- Automatic socket cleanup using context managers

## Usage

Run the scanner by providing a target:

```bash
python scanner.py <host>
```

By default, the scanner checks ports 1 through 100.

Example:

```bash
python scanner.py 127.0.0.1
```

Specify a custom port range using `--start` and `--end`:

```bash
python scanner.py 127.0.0.1 --start 20 --end 500
```

You can also provide a hostname:

```bash
python scanner.py localhost --start 1 --end 100
```

## Example Output

```text
Scanning 127.0.0.1 (127.0.0.1) from port 7995 to 8005...
Port 8000 is OPEN
Scan completed in 0.02 seconds.
```

## Testing

A known open port can be created locally using Python's built-in HTTP server:

```bash
python -m http.server 8000
```

Then scan the surrounding range:

```bash
python scanner.py 127.0.0.1 --start 7995 --end 8005
```

The scanner should report port `8000` as open.

## Technologies

- Python
- `socket`
- `argparse`
- `time`
- Git / GitHub

## What I Learned

This project was built to practice:

- TCP sockets and connection attempts
- IPv4 addressing and ports
- Blocking socket operations and timeouts
- Hostname resolution
- Command-line argument parsing
- Input validation and error handling
- Python context managers
- Measuring program execution time

## Note

Only scan systems you own or have permission to test.
