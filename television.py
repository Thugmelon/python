class Television: 
    # Constants / Class vars
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        '''
        status: Indicate if TV is on
        muted: indicate if TV is muted
        volume: Represents current volume
        channel: Represents channel
        
        '''
        #Instance vars
        self.status: bool = False
        self.muted: bool = False
        self.volume: int = Television.MIN_VOLUME
        self.channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        # Change TV power status
        self.status = not self.status

    def mute(self) -> None:
        # Toggle mute status
        if self.status:
            self.muted = not self.muted

    def channel_up(self) -> None:
        # Increase channel (ONLY IF TV ON)
        if self.status:
            if self.channel == Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            else:
                self.channel += 1
    
    def channel_down(self) -> None:
        #Decrease channel (ONLY IF TV IS ON AS WELL)
        if self.status:
            if self.channel == Television.MIN_CHANNEL:
                self.channel = Television.MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self) -> None:
        #Increase volume (if tv on & unmute if it is muted as well)
        if self.status:
            if self.muted:
                self.muted = False
            if self.volume < Television.MAX_VOLUME: #(Cannot exceed max volume)
                self.volume += 1

    def volume_down(self) -> None:
        #Same as volume_up functionality except only decrease if greater than min volume
        if self.status:
            if self.muted:
                self.muted = False
            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1
        
    def __str__(self) -> str:
        #Return power status of TV & Muted status, channel & volume status, etc.
        power_status = "On" if self.status else "Off"
        volume_status = "Muted" if self.muted else str(self.volume)
        return f'Power = [{power_status}], Channel = [{self.channel}], Volume = [{volume_status}]'