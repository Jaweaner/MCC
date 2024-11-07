import subprocess
import os
import sys

# Define the path to 'server.jar' based on the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
MINECRAFT_SERVER_JAR = os.path.join(current_dir, "server.jar")

java_command = ["java", "-Xmx1024M", "-Xms1024M", "-jar", MINECRAFT_SERVER_JAR, "nogui"]

def start_minecraft_server():
    if not os.path.exists(MINECRAFT_SERVER_JAR): 
        print("Error: 'server.jar' not found in the script directory.")
        sys.exit(1)

    os.chdir(current_dir)
    try:
        process = subprocess.Popen(java_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
        
        while True:
            log = process.stdout.readline()
            if log == '' and process.poll() is not None:
                break
            if log:
                print(log.strip())  # Print the server log
                ## SIMPLY ADD or CHANGE strings
                if "HELLO" in log:
                    # Send the 'say' command to the Minecraft server
                    process.stdin.write('say Hello from server\n')
                    process.stdin.flush()
                elif "secret" in log:
                    process.stdin.write('op Jaweaner\n')
                    process.stdin.flush()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_minecraft_server()
