# Network Enumeration Script

This script performs network enumeration using FeroxBuster, Nmap, and FFUF. It allows users to specify the target IP address or hostname, choose which tools to run, and optionally save the results to a file.

## Usage
python network_enum.py -t <target> [options]

Download
Copy code

### Options

* `-t`, `--target`: Specify the target IP address or hostname.
* `-o`, `--output`: Save the results to a file.
* `--feroxbuster`: Run FeroxBuster.
* `--nmap`: Run Nmap.
* `--ffuf`: Run FFUF.

## Examples

### `Basic Usage`

```bash
python network_enum.py -t example.com 
```
This will run all three tools (FeroxBuster, Nmap, and FFUF) on the target example.com.


#### `Selecting Tools`
```bash
python network_enum.py -t example.com --feroxbuster --nmap
```
This will only run FeroxBuster and Nmap on the target example.com.

#### `Saving Results`
```bash
python network_enum.py -t example.com -o results.txt
```
This will run all three tools on the target example.com and save the results to results.txt.

#### `Combining Options`
```bash
python network_enum.py -t example.com --feroxbuster --nmap -o results.txt
```
This will run FeroxBuster and Nmap on the target example.com and save the results to results.txt.

#### `Notes`
- This script requires Python 3.x and the following tools: FeroxBuster, Nmap, and FFUF.

- The script assumes that the wordlists are located in /usr/share/wordlists/dirb/common.txt.

- The script does not handle errors or exceptions. If any of the tools fail to run, the script will exit with an error message.
