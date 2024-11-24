class Television: 
    '''
    Class created to simulate a TV with basic functions. Ex. Power toggle,
    channel adjustment, volume control and muting.


    Attributes:
        MIN_VOLUME (int): Min volume level.
        MAX_VOLUME (int): Max volume level.
        MIN_CHANNEL (int): Minimum channel num.
        MAX_CHANNEL (int): Max channel num.
    '''

    # Constants / Class vars
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        '''
        __status (bool): False, Indicates if TV is powered on.
        __muted (bool): False, Indicates if TV is muted.
        __volume (int): Set to MIN_VOLUME, Current volume level.
        __channel (int): Set to MIN_Channel, Current channel num.
        '''
        #Instance vars
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        '''
        Toggle the power status for the Television.

        Changes value of private var __status:

        If __status is False, set to True (Turn TV ON)
        If _-status if True, set to False (turn TV off)

        '''
        self.__status = not self.__status

    def mute(self) -> None:
        '''
        toggle the mute status of the TV

        Changes value of private var __muted:
        If __status is True & TV is on, toggle __muted.
        (True for muted, false for unmute)
        If TV is off, no changes made.
        '''
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        '''
        Decrease the TV channel by 1.

        Adjusts the private var __channel:

        If __status is True & TV is on, increment __channel by 1.
        If __channel reaches MAX_Channel, loops back to Min_Channel
        If TV is off, no changes made.
        
        '''
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
    
    def channel_down(self) -> None:
        '''
        Decrease TV channel by 1

        Adjust private var __channel

        If __status is True & TV on, decrement __channel by 1.
        IF __channel reaches __MIN_CHANNEL, loop back to MAX_CHANNEL
        If TV is off, no changes made.
        '''
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        '''
        Increase volume by 1.

        Adjusts the private vars __volume & __muted

        If __status is True & TV on:
            If __muted is true, sets __muted to False (unmutes the TV)
            If __volume is less than Max_volume, increments __volume by 1.
        If the TV is off, no changes made.
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME: #(Cannot exceed max volume)
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Decrease volume by 1

        If __status is True & TV on:
            If __muted is true, sets __muted to False (unmutes the TV)
            If __volume is greater than MIN_VOLUME, decrements __volume by 1.
        If the TV is off, no changes made.
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
        
    def __str__(self) -> str:
        '''
        Return string representation of TV's current status.

        Constructs a string using private variables:

        __status: Indicates whether TV is "On" or "Off"
        __channel: Indicates the current channel #
        __volume: Displays either the volume level or "Muted" based on __muted

        Returns:
            str: A string in the format
            "Power = True/False, Channel = X, Volume = X"
        '''
        return (f'Power = {self.__status}, '
                f'Channel = {self.__channel}, '
                f'Volume = {self.__volume}')