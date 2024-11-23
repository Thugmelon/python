'''
Lab 12 didn't say anything about type hinting and 
there wasn't much of a point to it (not really any params),
so I just put line comments instead.
(Also this note is before watching lab hints vid, just as I'm reading instructions)
'''
class Television: 
    # Constants / Class vars
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        #Instance vars
        self.status = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL

    def power(self):
        # Change TV power status
        self.status = not self.status

    def mute(self):
        # Toggle mute status
        if self.status:
            self.muted = not self.muted

    def channel_up(self):
        # Increase channel (ONLY IF TV ON)
        if self.status:
            if self.channel == Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            else:
                self.channel += 1
    
    def channel_down(self):
        #Decrease channel (ONLY IF TV IS ON AS WELL)
        if self.status:
            if self.channel == Television.MIN_CHANNEL:
                self.channel = Television.MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self):
        #Increase volume (if tv on & unmute if it is muted as well)
        if self.status:
            if self.muted:
                self.muted = False
            if self.volume < Television.MAX_VOLUME: #(Cannot exceed max volume)
                self.volume += 1

    def volume_down(self):
        #Same as volume_up functionality except only decrease if greater than min volume
        if self.status:
            if self.muted:
                self.muted = False
            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1
        
    def __str__(self):
        #Return power status of TV & Muted status, channel & volume status, etc.
        power_status = "On" if self.status else "Off"
        volume_status = "Muted" if self.muted else str(self.volume)
        return f'Power = [{power_status}], Channel = [{self.channel}], Volume = [{volume_status}]'

    
tv = Television()
tv.power()