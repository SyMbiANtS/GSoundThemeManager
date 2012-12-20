#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path

SOUND_DIR = '/usr/share/sounds'
LOCAL_SOUND_DIR = os.path.join(os.getenv('HOME'), '.local/share/sounds')
DEFAULT_DIR = os.getenv('HOME')

GCONF_FEEDBACK = '/desktop/gnome/sound/input_feedback_sounds'
GCONF_CURRENT_THEME = '/desktop/gnome/sound/theme_name'

# id : label
MAIN_EVENT_SOUNDS = (
('desktop-login', 'Login event'),
('desktop-logout', 'Logout event'),
('dialog-error', 'Error dialog'),
('dialog-warning', 'Warning dialog'),
('dialog-information', 'Information dialog'),
('dialog-question', 'Question dialog'),
('system-ready', 'System ready (GDM startup)')
)

# id : label
EXTRA_EVENT_SOUNDS = (

('complete', 'Complete warning'),
('bell', 'Bell warning'),
('alarm-clock-elapsed', 'Alarm clock'),

None,
('suspend-error', 'Suspend error'),
('trash-empty', 'Empty Trash'),
None,
('message-new-instant', 'Recieve a new instant message'),
('message', 'Incoming mail'),
None,
('window-attention', 'Attention warning'),
('window-question', 'Question warning'),

)
# id : label
SOUND_TEST_EVENT_SOUNDS = (
('audio-test-signal', 'Test signal'),
('audio-volume-change', 'Volume changed'),

('audio-channel-front-center', 'Front center channel'),
('audio-channel-front-left', 'Front left channel'),
('audio-channel-front-right', 'Front right channel'),

('audio-channel-side-left', 'Side left channel'),
('audio-channel-side-right', 'Side right channel'),

('audio-channel-rear-center', 'Rear center channel'),
('audio-channel-rear-left', 'Rear left channel'),
('audio-channel-rear-right', 'Rear right channel'),

)
# id : label
SERVICE_EVENT_SOUNDS = (

('device-added', 'Device added'),
('device-removed', 'Device removed'),

('network-connectivity-established', 'Network connected'),
('network-connectivity-lost', 'Network disconnected'),

('power-plug', 'Power ON'),
('power-unplug', 'Power OFF'),

('phone-incoming-call', 'Incoming VoIP'),
('phone-outgoing-busy', 'VoIP out busy'),
('phone-outgoing-calling', 'VoIP calling'),
)



WARN_EVENT_SOUNDS = (

('camera-shutter', 'Camera shutter'),
('screen-capture', 'Capture screenshot'),

('service-login', 'Service login'),
('service-logout', 'Service logout'),

('window-new', 'Open a new window'),
('window-close', 'Close a window'),

('button-pressed', 'Press a button'),
('button-toggle-on', 'Activate a check button'),
('button-toggle-off', 'Deactivate a check button'),
('menu-click', 'Click a menu'),
('notebook-tab-changed', 'Change a tab'),
)
