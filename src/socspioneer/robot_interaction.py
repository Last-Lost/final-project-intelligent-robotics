# Libraries
import re
import time
import pyaudio
import wave
import speech_recognition as sr
import pyttsx3
from change_angle import changeAngle
import rospy
import random as r
import math
from RobotMovement import RobotMovementThread

r.seed(0)
"""
Explain the class here
"""

# 

import Levenshtein as l

"""
future: when the path is calculated, get the distance and say the number of steps as well.
"""

# rooms = [ "robotics teaching lab","medical imaging lab", "plant room", "gents toilet", "lift", "robotics lab",
        #  "vending machines", "lower ground 21", "lower ground 23", "lower ground 26", "lower ground 30b", "lower ground 3b", "lower ground 3a", "lower ground 4", "mohan's room"]
jargon = ["take", "me", "where", "is", "navigate","to", "the", "can", "you", "please", "show", "way", "guide", "how", "do", "i", "get", "path", "lets", "let's"]
total_coordinates = {
            "robotics teaching lab":((6.90, -10.15), (math.pi/4)),
            "medical imaging lab" : ((10.25,-6.90), (math.pi/4)),
            "plant room":((11.50, -5.00), (math.pi/4)),
            "gents toilet": ((11.75, -3.45),(3*math.pi/4)),
            "lift": ((9.50, -3.50), (3*math.pi/4)),
            "robotics lab": ((5.00, -7.35), (-(3*math.pi/4))),
            "vending manchines":((5.05, -2.70),(math.pi/4)),
            "printer": ((4.05, -0.90),(math.pi/4)),
            "server room": ((2.25, 1.50), (math.pi/4)),
            "water dispenser":((-2.45, 5.35),(math.pi/4)),
            "meeting room": ((-3.40, 9.30),(-(math.pi/4))),
            "ladies toilet":((-3.45, 11.40), (-(math.pi/4))),
            "teaching lab" : ((-6.60, 10.50), (3*math.pi/4))
            }
rooms = list(total_coordinates.keys())
"""
not in rooms list
    - lift
    - gents toilet
    - robotics teaching lab
    - vending machines
    - printer
    - server room
    - water dispenser
    - ladies room
    - meeting room
"""
# temp


def _clean_input(input_text):
    text = [x for x in input_text.strip().lower().split(" ")
            if x not in jargon]

    text = " ".join(text)
    return text


def generate_reply_message(text):
    """
    This function gets the text from the user and generates a reply message.
    """
    # input text after its been cleaned as in removed unnecessary wordings
    clean_text = _clean_input(text)

    # applies levenshtein distance
    def calc_distance(x):
        return l.distance(x, clean_text)

    # calculate the distance between the cleaned text and the rooms
    # clean_text = "plant room" 
    levenshtein_distances = list(map(calc_distance, rooms))

    # getting the index of the smallest distance
    min_val = min(levenshtein_distances)

    if min_val > 2:
        # if the room inputted does not exist this condition is triggered
        return None

    _index = levenshtein_distances.index(min_val)
    room_name = rooms[_index]

    # generates an output message and returns the output message and the room name
    return f"Okay let's head to {room_name}. ", room_name

# 

class RobotInteraction:
    """
    Things to do:
        * Take input from user
        * Analyse it
            * If input is valid
                * Check if room is present in the lab
                * Get coordinates
            * If input is not valid
                * Ask user to repeat
        * Return coordinates
    """

    def __init__(self):
        self._WAVE_OUTPUT_FILENAME = "output.wav"
        self.room_name = ""
        self.engine = pyttsx3.init()

    def _record_audio(self):
        """
        This function records audio for 5 seconds saves it to the file named in _WAVE_OUTPUT_FILE
        """
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        RECORD_SECONDS = 5

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(self._WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    def speech(self, message):
        self.engine.setProperty("voice", "english+f2")
        self.engine.say(message)
        self.engine.runAndWait()
        self.engine.stop()

    def _get_input(self):
        self._record_audio()

        r = sr.Recognizer()

        with sr.AudioFile(self._WAVE_OUTPUT_FILENAME) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            text = None
            # recognize (convert from speech to text)
            try:
                text = r.recognize_google(audio_data)
            except:
                self.speech("Invalid input, try again please.")
            return text

    def get_input(self):
        while True:
            print("listening")
            input = self._get_input()
            if input is not None:
                if generate_reply_message(input) is None:
                    # in case the inputted room does not exist this condition is triggered.
                    self.speech(
                        "The room doesn't exist, try again please.")
                    continue

                output_message, room_name = generate_reply_message(input)
                coordinates = self.get_coordinates(room_name=room_name)

                self.speech(output_message)
                self.room_name = room_name

                return coordinates
            else:
                # while the input is not valid the loop keeps running
                continue

    def get_roomname(self):
        return self.room_name

    def get_coordinates(self, room_name=None):
        if room_name:
            return total_coordinates[room_name]
        return "error inside get_coordinates() - robot_interaction.py - room name does not exist in the file"

        # get coordinates of the room name using room_name from a file and return it
        # coordinates = get_coordinates(room_name)
        # return coordinates``


def main():
    OUTPUT_FILE_NAME = "coodinates.txt"

    rospy.init_node("robot_interaction", anonymous=True)
    ri = RobotInteraction()
    coordinates = ri.get_input()
    room_name = ri.get_roomname()

    # print(coordinates)
    RobotMovementThread_object = RobotMovementThread((2,2), coordinates[0], (-(math.pi/2)), [], False)
    RobotMovementThread_object.move_robot()
    directions = RobotMovementThread_object.getDirections()
    angle = RobotMovementThread_object.getAngle()

    facing_angle = (angle - coordinates[1])
    changeAngle(facing_angle)

    ri.speech(f"Reached {room_name}")

    time.sleep(5)

    ri.speech("Returning Home")

    changeAngle(-(facing_angle))

    return_home_direction = []

    for direction in directions:

        if direction == "t":
            return_home_direction.append("b")
        elif direction == "r":
            return_home_direction.append("l")
        elif direction == "b":
            return_home_direction.append("t")
        elif direction == "l":
            return_home_direction.append("r")

    RobotMovementThread_object2 = RobotMovementThread((coordinates[0]), (2,2), angle, return_home_direction[::-1], True)
    RobotMovementThread_object2.move_robot()
    angle = RobotMovementThread_object2.getAngle()

    # changeAngle((angle - math.pi/2))

    ri.speech("Reached Home")

    # # clear existing coordinates file
    # open(OUTPUT_FILE_NAME,"w").close()

    # # add new coordintes to file
    # with open(OUTPUT_FILE_NAME,"w") as f:
    #     f.write(str(coordinates))
    rospy.spin()
    
if __name__ == "__main__":
    try:
        main()
        # RobotMovement.main()
        rospy.signal_shutdown("* finished")
    except Exception as e:
        rospy.loginfo("Error inside robot_interaction")
        print(e)
