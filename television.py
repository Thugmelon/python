class Television:
    '''
    Class created to simulate a TV with basic functions. Ex. Power toggle,
    channel adjustment, volume control, and muting.

    Attributes:
        MIN_VOLUME (int): Minimum volume level.
        MAX_VOLUME (int): Maximum volume level.
        MIN_CHANNEL (int): Minimum channel number.
        MAX_CHANNEL (int): Maximum channel number.
    '''

    # Constants / Class vars
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        '''
        Initialize the Television instance.

        Private Variables:
            __status (bool): Indicates if the TV is powered on (default: False).
            __muted (bool): Indicates if the TV is muted (default: False).
            __volume (int): Current volume level (default: MIN_VOLUME).
            __channel (int): Current channel number (default: MIN_CHANNEL).
        '''
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

# Getters
    def get_status(self) -> bool:
        """
        Return the power status of the TV.
        
        Returns:
            bool: True if the TV is powered on, False otherwise.
        """
        return self.__status

    def get_muted(self) -> bool:
        """
        Return the mute status of the TV.
        
        Returns:
            bool: True if the TV is muted, False otherwise.
        """
        return self.__muted

    def get_volume(self) -> int:
        """
        Return the current volume level of the TV.
        
        Returns:
            int: The current volume level.
        """
        return self.__volume

    def get_channel(self) -> int:
        """
        Return the current channel number of the TV.
        
        Returns:
            int: The current channel number.
        """
        return self.__channel
    
    def power(self) -> None:
        '''
        Toggle the power status for the Television.

        If the TV is off, turn it on. If the TV is on, turn it off.

        Changes:
            __status: True (on) or False (off).
        '''
        self.__status = not self.__status

    def mute(self) -> None:
        '''
        Toggle the mute status of the TV.

        If the TV is powered on, mute or unmute the TV. No changes are made
        if the TV is powered off.

        Changes:
            __muted: True (muted) or False (unmuted).
        '''
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        '''
        Increase the TV channel by 1.

        If the TV is powered on, increment the channel by 1. If the channel
        reaches MAX_CHANNEL, loop back to MIN_CHANNEL. No changes are made
        if the TV is powered off.

        Changes:
            __channel: Incremented by 1 or reset to MIN_CHANNEL.
        '''
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        '''
        Decrease the TV channel by 1.

        If the TV is powered on, decrement the channel by 1. If the channel
        reaches MIN_CHANNEL, loop back to MAX_CHANNEL. No changes are made
        if the TV is powered off.

        Changes:
            __channel: Decremented by 1 or reset to MAX_CHANNEL.
        '''
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        '''
        Increase the volume by 1.

        If the TV is powered on, unmute the TV if it is muted, then increment
        the volume by 1 (up to MAX_VOLUME). No changes are made if the TV is
        powered off.

        Changes:
            __volume: Incremented by 1 or stays at MAX_VOLUME.
            __muted: Set to False if previously muted.
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Decrease the volume by 1.

        If the TV is powered on, unmute the TV if it is muted, then decrement
        the volume by 1 (down to MIN_VOLUME). No changes are made if the TV is
        powered off.

        Changes:
            __volume: Decremented by 1 or stays at MIN_VOLUME.
            __muted: Set to False if previously muted.
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Return string representation of TV's current status.

        Format:
            "Power = True/False, Channel = X, Volume = X/Muted"

        Returns:
            str: The TV's current power, channel, and volume status.
        '''
        power_status = self.__status  # Use True/False directly
        volume_status = "0" if self.__muted else self.__volume
        return f"Power = {power_status}, Channel = {self.__channel}, Volume = {volume_status}"