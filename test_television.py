import pytest
from television import Television

class TestTelevision:
    def setup_method(self):
        """Set up a Television instance before each test."""
        self.tv = Television()

    def teardown_method(self):
        """Clean up after each test."""
        del self.tv

    def test_init(self):
        """Test the initialization of a Television instance."""
        assert not self.tv.get_status()
        assert self.tv.get_volume() == Television.MIN_VOLUME
        assert self.tv.get_channel() == Television.MIN_CHANNEL
        assert not self.tv.get_muted()

    def test_power(self):
        """Test toggling the power of the Television."""
        assert not self.tv.get_status()
        self.tv.power()
        assert self.tv.get_status()
        self.tv.power()
        assert not self.tv.get_status()

    def test_mute(self):
        """Test muting and unmuting the Television."""
        self.tv.power()
        self.tv.mute()
        assert self.tv.get_muted()
        self.tv.mute()
        assert not self.tv.get_muted()

    def test_channel_up(self):
        """Test increasing the channel with looping behavior."""
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.get_channel() == 1
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.get_channel() == Television.MIN_CHANNEL

    def test_channel_down(self):
        """Test decreasing the channel with looping behavior."""
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.get_channel() == Television.MAX_CHANNEL
        self.tv.channel_down()
        assert self.tv.get_channel() == Television.MAX_CHANNEL - 1

    def test_volume_up(self):
        """Test increasing the volume, including unmuting."""
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.get_volume() == 1
        self.tv.volume_up()
        assert self.tv.get_volume() == 2
        self.tv.volume_up()  # Exceeding MAX_VOLUME
        assert self.tv.get_volume() == 2

    def test_volume_down(self):
        """Test decreasing the volume, including unmuting."""
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.get_volume() == 0
        self.tv.volume_down()  # Below MIN_VOLUME
        assert self.tv.get_volume() == 0