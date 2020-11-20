from subprocess import Popen, PIPE, TimeoutExpired


# def run_command(cmd, timeout=20):
#     p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     (output, err) = p.communicate(timeout=timeout)
#     return output, err

def run_command(cmd, timeout=5):

    try:
        with Popen(cmd.split(), stdout=PIPE, stderr=PIPE) as ps_process:
            success, _ = ps_process.communicate(timeout=timeout)

    except TimeoutExpired as e:
        print("------" + str(e))
        ps_process.kill()
        success = "Timeout"
    except Exception as e:
        print("------" + str(e))
        ps_process.kill()
        success = "Exception"

    return success
