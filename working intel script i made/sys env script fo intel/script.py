import subprocess
import re

def ping_and_extract_ip(domain):
    """Ping the given domain and extract the IP address from the output."""
    response = subprocess.run(['ping', '-n', '1', domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if response.returncode == 0:
        print("Ping output:\n", response.stdout)
        match = re.search(r'(?<!\d)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?!\d)', response.stdout)
        if match:
            return match.group(1)
        else:
            print("IP address could not be extracted from the ping output.")
            return None
    else:
        print("Ping failed.")
        return None

def set_environment_variable_setx(name, value):
    """Set a system-wide environment variable permanently using setx with /m option."""
    result = subprocess.run(['setx', name, value, '/m'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print(f"System environment variable {name} set to {value} permanently using setx.")
        return True
    else:
        print(f"Failed to set system environment variable {name} using setx.")
        print(result.stderr)
        return False

def set_environment_variable_powershell(name, value):
    """Set a system-wide environment variable permanently using PowerShell."""
    command = f'[System.Environment]::SetEnvironmentVariable("{name}", "{value}", "Machine")'
    result = subprocess.run(['powershell', '-Command', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print(f"System environment variable {name} set to {value} permanently using PowerShell.")
    else:
        print(f"Failed to set system environment variable {name} using PowerShell.")
        print(result.stderr)

def set_environment_variable(name, value):
    """Try setting system environment variable using setx, fallback to PowerShell if needed."""
    if not set_environment_variable_setx(name, value):
        set_environment_variable_powershell(name, value)

def main():
    domain = "sut_ip" 

    
    ip = ping_and_extract_ip(domain)

    if ip:
        
        set_environment_variable("GALAXY_REMOTE_IP", f"{ip}:50051")
        set_environment_variable("NO_PROXY", f"localhost,127.0.0.1,intel.com,*.intel.com,{ip}")
        print("IP address and other variables set in environment variables.")
    else:
        print("Could not set environment variables because IP extraction failed.")

if __name__ == "__main__":         
    main()
