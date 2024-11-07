# MCC - Minecraft Chat Control

<img src="https://pngimg.com/uploads/minecraft/minecraft_PNG39.png" width="700px" height="280px">


**Minecraft Chat Control (MCC)** is a simple Python script that reads chat inputs from a local Minecraft server and takes automated actions based on them. It’s especially useful for hosting a Minecraft server on your PC for friends. MCC automates responses, triggers events, and provides a way to learn Python and Minecraft server management.

## Features
- Responds automatically to specific chat keywords (e.g., sends "Hello from server" when "HELLO" is detected).
- Enables command automation (e.g., grants "op" privileges when "secret" is detected).
- Helps users practice Python and server control.

## Requirements
- **Minecraft Server**: Download the server .jar file from [Minecraft’s official website](https://www.minecraft.net/en-us/download/server).
- **Java**: Ensure Java is installed and in your system's PATH.
- **Python**: Uses Python’s subprocess module.

## Setup
1. Download server.jar and place it where desired. Update the MINECRAFT_SERVER_JAR path in the script.
2. Verify Java installation.
3. Run the script using Python:

## Run

Navigate to the directory where your server.jar is located. For example:

```bash
cd /Your Directory/
```
Run script

```bash
python mcc.py

```


##
> [!NOTE]  
> If there was an error saying you need to accept EULA, please go to the directory where all the files are located `mcc.py` and `server.jar`, then open EULA.txt file and change `eula=false` to ```eula=true```
 ##


> [!TIP]
> You can contact me here: https://www.youtube.com/@jaweaner



