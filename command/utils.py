import subprocess


def run_command(cmd, timeout=20):
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, err) = p.communicate(timeout=timeout)
    return output, err
