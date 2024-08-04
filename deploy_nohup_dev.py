import subprocess
import time
import signal

def echo_at_cmd(text):
    echo_command = "echo " + text
    echo_process = subprocess.Popen(echo_command, shell=True)
    echo_process.wait()


# START OF SCRIPT
target_py = "manage.py runserver 9996"
nohup_output_folder = "deploy/nohup_output.txt"
# nohup_output_folder = "nohup.out"

# Execute pgrep -a java
pgrep_command = "pgrep -a python3"
pgrep_process = subprocess.Popen(pgrep_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
pgrep_output, pgrep_error = pgrep_process.communicate()

# Print pgrep output
output = pgrep_output.decode()
echo_at_cmd("pgrep -a python3 output:")
echo_at_cmd(output)

# Check if the output contains target/saas-backend-1.0.0.jar
if target_py in pgrep_output.decode():

    # Execute pkill -f "Python -jar target/hapy-backend-1.0.0.jar"
    pkill_command = "pkill -f \"python3 " + target_py + "\""
    echo_at_cmd("Python process " + target_py + " is running, killing it with : " + pkill_command)
    pkill_process = subprocess.Popen(pkill_command, shell=True)
    pkill_process.wait()
    echo_at_cmd("Python3 process " + target_py + " has been killed.")

    # Wait for a few seconds to ensure the Pkill process has finsihed
    echo_at_cmd("Waiting for 10 seconds to ensure the Pkill process has finsihed...")
    time.sleep(10)

else:
    echo_at_cmd(target_py + " not present in python3 process is not running or has a different name.")


# Execute nohup python -jar target-dev/hapy-backend-1.0.0.jar > deploy/nohup_output.txt &
nohup_command = "nohup python3 " + target_py + " > " + nohup_output_folder + " &"
# nohup_command = "nohup python3 " + target_py + " &"
echo_at_cmd("Starting new Python3 process " + target_py + " with : " + nohup_command)
nohup_process = subprocess.Popen(nohup_command, shell=True)
nohup_process.wait()

# Wait for a few seconds to ensure the Python process has started
echo_at_cmd("Waiting for 10 seconds to ensure the Python process has started...")
time.sleep(10)

# Execute cat nohup.out
cat_command = "cat " + nohup_output_folder
cat_process = subprocess.Popen(cat_command, shell=True)
cat_process.wait()

# Print the end
echo_at_cmd("End of script !!!")
