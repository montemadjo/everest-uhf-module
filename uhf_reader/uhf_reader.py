import socket
import sys
import os
from uhf_reader.constants import GET_FIRMWARE_VERSION, CLEAR_READER_BUFFER, SCAN_FOR_TAGS, GET_TAG_DATA, SET_OUT0_HIGH, SET_OUT0_LOW, SET_OUT1_HIGH, SET_OUT1_LOW, SET_RELEY_HIGH, SET_RELEY_LOW


class UHFReader:
    """
    UHF reader MR6211E
    """
    buffer_size = 1024
    connection = None
    timeout = 5.0
    port = 100
    host = None

    def __init__(self, host, port):
        self.port = port
        self.host = host
        self.count = 200
        self.count_locker = True
        self.activate_output_0_flag = False
        self.activate_output_1_flag = False
        self.activate_output_2_flag = False
        self.blinker_0_counter = 10
        self.blinker_1_counter = 10
        self.blinker_2_counter = 10
        self.is_0_lit = False
        self.is_1_lit = False
        self.is_2_lit = False

    def connect(self) -> None:
        try:
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.settimeout(self.timeout)
            self.connection.connect((self.host, self.port))
        except:
            print("Cannot process command connect")
            os._exit(1)

    def disconnect(self) -> None:
        """
        Close connection to the reader
        """
        try:
            self.connection.close()
        except:
            print("Cannot process command disconnect")
            os._exit(1)

    def get_firmware_version(self) -> bytes:
        try:
            message = bytes.fromhex(GET_FIRMWARE_VERSION)
            self.connection.send(message)
            data = self.connection.recv(self.buffer_size)
            return data
        except:
            print("Cannot process command get_firmware_version")
            os._exit(1)

    def clear_reader_buffer(self) -> bytes:
        try:
            message = bytes.fromhex(CLEAR_READER_BUFFER)
            self.connection.send(message)
            data = self.connection.recv(self.buffer_size)
            return data
        except:
            print("Cannot process command clear_reader_buffer")
            os._exit(1)

    def scan_for_tags(self) -> bytes:
        try:
            message = bytes.fromhex(SCAN_FOR_TAGS)
            self.connection.send(message)
            data = self.connection.recv(self.buffer_size)
            segment = data[5:6]
            return segment
        except:
            print("Cannot process command scan_for_tags")
            os._exit(1)

    def get_tag_data(self) -> bytes:
        try:
            message = bytes.fromhex((GET_TAG_DATA))
            self.connection.send(message)
            data = self.connection.recv(self.buffer_size)
            segment = data[7:19]
            return segment
        except:
            print("Cannot process command get_tag_data")
            os._exit(1)

    def set_output0(self, level) -> bytes:
        try:
            if level is False:
                # if deactivate:
                self.is_0_lit = False
                message = bytes.fromhex((SET_OUT0_LOW))
                self.connection.send(message)
                data = self.connection.recv(self.buffer_size)
                return data
            else:
                self.is_0_lit = True
                message = bytes.fromhex((SET_OUT0_HIGH))
                self.connection.send(message)
                data = self.connection.recv(self.buffer_size)
                return data
        except:
            print("Cannot process command set_output0")
            os._exit(1)

    def set_output1(self, level) -> bytes:
        try:
            if level is False:
                # if deactivate:
                self.is_1_lit = False
                message = bytes.fromhex((SET_OUT1_LOW))
                self.connection.send(message)
                data = self.connection.recv(self.buffer_size)
                return data
            else:
                self.is_1_lit = True
                message = bytes.fromhex((SET_OUT1_HIGH))
                self.connection.send(message)
                data = self.connection.recv(self.buffer_size)
                return data
        except:
            print("Cannot process command set_output1")
            os._exit(1)

    def set_output2(self, level) -> bytes:
        try:
            if level is False:
                # if deactivate:
                self.is_2_lit = False
                message = bytes.fromhex((SET_RELEY_LOW))
                self.connection.send(message)
                data = self.connection.recv(self.buffer_size)
                return data
            else:
                self.is_2_lit = True
                message = bytes.fromhex((SET_RELEY_HIGH))
                self.connection.send(message)
                data = self.connection.recv(self.buffer_size)
                return data
        except:
            print("Cannot process command set_output2")
            os._exit(1)

    def blink_output0(self, dark, light) -> None:
        self.blinker_0_counter -= 1
        if self.blinker_0_counter == 0:
            self.blinker_0_counter = dark + light

        if self.blinker_0_counter >= light:
            self.set_output0(False)
        else:
            self.set_output0(True)

    def blink_output1(self, dark, light) -> None:
        self.blinker_1_counter -= 1
        if self.blinker_1_counter == 0:
            self.blinker_1_counter = dark + light

        if self.blinker_1_counter >= light:
            self.set_output1(False)
        else:
            self.set_output1(True)

    def blink_output2(self, dark, light) -> None:
        self.blinker_2_counter -= 1
        if self.blinker_2_counter == 0:
            self.blinker_2_counter = dark + light

        if self.blinker_2_counter >= light:
            self.set_output2(False)
        else:
            self.set_output2(True)
