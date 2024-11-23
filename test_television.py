import pytest
from television import Television

def test_init():
    tv = Television()
    assert not tv.status
    assert tv.volume == Television.MIN_VOLUME
    assert tv.channel == Television.MIN_CHANNEL
    assert not tv.muted

def test_power():
    tv = Television()
    assert not tv.status
    tv.power()
    assert tv.status
    tv.power()
    assert not tv.status

def test_mute():
    tv = Television()
    tv.power()
    tv.mute()
    assert tv.muted is True
    tv.mute()
    assert tv.muted is False

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert tv.channel == Television.MAX_CHANNEL
    tv.channel = 1
    tv.channel_down()
    assert tv.channel == 0

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert tv.volume == 1
    tv.volume = Television.MAX_VOLUME
    tv.volume_up()
    assert tv.volume == Television.MAX_VOLUME

def test_volume_down():
    tv = Television()
    tv.power()

    tv.volume = Television.MAX_VOLUME
    tv.volume_down()
    assert tv.volume == Television.MAX_VOLUME - 1

    tv.volume = Television.MIN_VOLUME
    tv.volume_down()
    assert tv.volume == Television.MIN_VOLUME

def test_volume_up_unmutes():
    tv = Television()
    tv.power()
    tv.mute()
    tv.volume_up()
    assert not tv.muted
    assert tv.volume == 1

def test_volume_down_unmutes():
    tv = Television()
    tv.power()
    tv.mute()
    tv.volume_down()
    assert not tv.muted
    assert tv.volume == Television.MIN_VOLUME
