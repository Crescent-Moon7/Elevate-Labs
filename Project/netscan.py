import subprocess
import argparse

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()

def main():
    parser = argparse.ArgumentParser(description='Network Enumeration Script')
    parser.add_argument('-t', '--target', help='Target IP address or hostname', required=True)
    parser.add_argument('-o', '--output', help='Output file to save results', default=None)
    parser.add_argument('--feroxbuster', action='store_true', help='Run FeroxBuster')
    parser.add_argument('--nmap', action='store_true', help='Run Nmap')
    parser.add_argument('--ffuf', action='store_true', help='Run FFUF')

    args = parser.parse_args()

    results = []

    if args.feroxbuster:
        print('Running FeroxBuster...')
        command = f'feroxbuster -u {args.target} -w /usr/share/wordlists/dirb/common.txt'
        stdout, stderr = run_command(command)
        results.append(f'FeroxBuster Results:\n{stdout}\n{stderr}')

    if args.nmap:
        print('Running Nmap...')
        command = f'nmap -sV -O {args.target}'
        stdout, stderr = run_command(command)
        results.append(f'Nmap Results:\n{stdout}\n{stderr}')

    if args.ffuf:
        print('Running FFUF...')
        command = f'ffuf -w /usr/share/wordlists/dirb/common.txt -u {args.target}/FUZZ'
        stdout, stderr = run_command(command)
        results.append(f'FFUF Results:\n{stdout}\n{stderr}')

    if args.output:
        with open(args.output, 'w') as f:
            for result in results:
                f.write(result + '\n')
        print(f'Results saved to {args.output}')
    else:
        for result in results:
            print(result)

if __name__ == '__main__':
    main()