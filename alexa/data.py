# -*- coding: utf-8 -*-

WELCOME_MSG = "Welcome to the Arsenal Fan Chants. You can say, start chanting, to begin chanting with the best team in the world!"
WELCOME_REPROMPT_MSG = "You can say, play chants, to begin."
WELCOME_PLAYBACK_MSG = "You were listening to {}. Would you like to resume?"
WELCOME_PLAYBACK_REPROMPT_MSG = "You can say yes to resume or no to play from the top"
DEVICE_NOT_SUPPORTED = "Sorry, this skill is not supported on this device"
LOOP_ON_MSG = "Loop turned on."
LOOP_OFF_MSG = "Loop turned off."
HELP_MSG = WELCOME_MSG
HELP_PLAYBACK_MSG = WELCOME_PLAYBACK_MSG
HELP_DURING_PLAY_MSG = "You are listening to the Arsenal Fan Chants. You can say, Next or Previous to navigate through the playlist. At any time, you can say Pause to pause the audio and Resume to resume."
STOP_MSG = "Goodbye."
EXCEPTION_MSG = "Sorry, this is not a valid command. Please say help, to hear what you can say."
PLAYBACK_PLAY = "This is {}"
PLAYBACK_PLAY_CARD = "Playing {}"
PLAYBACK_NEXT_END = "You have reached the end of the playlist"
PLAYBACK_PREVIOUS_END = "You have reached the start of the playlist"

DYNAMODB_TABLE_NAME = "Fan-Chants-Multi-Stream"

AUDIO_DATA = [
    {
        "title": "Arsenal The Greatest Team.",
        "url": "https://fanchantsbucket.s3.us-east-2.amazonaws.com/190930_07_f_f-fanchants-free.mp3",  
    },
    {
        "title": "Come On Arsenal.",
        "url": "https://fanchantsbucket.s3.us-east-2.amazonaws.com/come-on-arsenal-fanchants-free.mp3",
    },
    {
        "title": "Good Old Arsenal.",
        "url": "https://fanchantsbucket.s3.us-east-2.amazonaws.com/good-old-arsenal-fanchants-free.mp3", 
    },
    {
        "title": "Hello, Hello, We are the Arsenal Boys.",
        "url": "https://fanchantsbucket.s3.us-east-2.amazonaws.com/hello-hello-4-fanchants-free.mp3",
    },
    {
       "title": "Red Army.",
       "url": "https://fanchantsbucket.s3.us-east-2.amazonaws.com/red-army-arsenal-fanchants-free.mp3",
    },
    {
        "title": "Arsenal Till I Die.",
        "url": "https://fanchantsbucket.s3.us-east-2.amazonaws.com/arsenal-till-i-die-3418-fanchants-free.mp3",
    },
    {
        "title": "Standup for the Arsenal.",
        "url": "https://fanchantsbucket.s3.us-east-2.amazonaws.com/stand-arsenal-gooners-fanchants-free.mp3",
    },
    {
        "title": "If You Hate Tottenham.",
        "url": "https://fanchantsbucket.s3.us-east-2.amazonaws.com/if-you-hate-tottenham-hotspur-fanchants-free.mp3",
    },
    {
        "title": "We all follow the Arsenal.",
        "url": "https://fanchantsbucket.s3.us-east-2.amazonaws.com/we-all-follow-the-arsenal-fanchants-free.mp3",
    },
    {
        "title": "Oh! When the Spurs go marching down.",
        "url": "https://fanchantsbucket.s3.us-east-2.amazonaws.com/stand-arsenal-gooners-fanchants-free.mp3",
    },
    {
        "title": "We've got Ozil.",
        "url": "https://fanchantsbucket.s3.us-east-2.amazonaws.com/weve-got-ozil-mesut-ozil-fanchants-free.mp3",
    },
    {
        "title": "What do you think of Tottenham?",
        "url": "https://fanchantsbucket.s3.us-east-2.amazonaws.com/190105_02_b_f-fanchants-free.mp3",
    },
    {
        "title": "We're not going Home.",
        "url": "https://fanchantsbucket.s3.us-east-2.amazonaws.com/were-not-going-home-fanchants-free.mp3",
    },
    {
        "title": "We won the league in Manchester",
        "url": "https://fanchantsbucket.s3.us-east-2.amazonaws.com/we-won-the-league-in-fanchants-free.mp3",
    },
    {
        "title": "Aubameyang",
        "url": "https://fanchantsbucket.s3.us-east-2.amazonaws.com/190930_01_k_f-fanchants-free.mp3",
    }
]