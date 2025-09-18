# EDITABLE SETTING
# Choose whether or not to use named discs or named boxes
# Using unnamed discs will reduce schematic size and
# Possibly reduce lag due to less NBT data
# Options: True, False (it's case-sensitive,
# so make sure it's written with a capital first letter and
# all other letters lowercase)
NAME_DISCS = False
NAME_BOXES = True

# EDITABLE SETTING
# Choose whether or not to use ONLY discs that are farmable in survival
# This assigns shears to the silence and replaces the last disc with water bottles
SURVIVAL_FARMABLE = True

# EDITABLE SETTING
# The number of full modules (2 half-modules) of each instrument
# in the physical machine. Can be set to 0 if the module does not exist.
# NOTE: These settings are configured for the machine in the world download.
CHORD_MAX_SIZES = {
  'piano': 3,
  'double bass': 1,
  'bass drum': 1,
  'snare drum': 1,
  'click': 1,
  'guitar': 3,
  'flute': 3,
  'bell': 1,
  'chime': 1,
  'xylophone': 1,
  'iron xylophone': 1,
  'cow bell': 1,
  'digeridoo': 1,
  'bit': 1,
  'banjo': 1,
  'pling': 3,
}

# EDITABLE SETTING
# Whether you want to keep the lowest or highest notes in chords that are too large
# 'l' means keep the low notes; 'h' means keep the high notes.
KEEP_NOTES_BY_INSTRUMENT = {
  'piano': 'h',
  'double bass': 'l',
  'bass drum': 'l',
  'snare drum': 'l',
  'click': 'l',
  'guitar': 'l',
  'flute': 'h',
  'bell': 'l',
  'chime': 'l',
  'xylophone': 'l',
  'iron xylophone': 'l',
  'cow bell': 'l',
  'digeridoo': 'l',
  'bit': 'l',
  'banjo': 'l',
  'pling': 'h',
}

# EDITABLE SETTING
# The default directory to place the formatted files
DEFAULT_FORMATTED_DIRECTORY = "out/formatted"

# EDITABLE SETTING
# The default directory to place the schematic files
DEFAULT_SCHEM_DIRECTORY = "out/schem"


# DO NOT EDIT
# The maximum length of a song, dictated by the capacity of a double chest
MAX_SONG_LENGTH = 1457

# DO NOT EDIT
# The minimum fill of the last shulker box so that the machine doesn't break
CHEST_MIN_FILL = 4

# DO NOT EDIT
# The instrument names in order
INSTRUMENTS = [
  'piano',
  'double bass',
  'bass drum',
  'snare drum',
  'click',
  'guitar',
  'flute',
  'bell',
  'chime',
  'xylophone',
  'iron xylophone',
  'cow bell',
  'digeridoo',
  'bit',
  'banjo',
  'pling',
]

# DO NOT EDIT
# The range of .nbs notes that a vanilla note block can play
INSTRUMENT_RANGE = (33, 57)

# DO NOT EDIT
# List of music discs in order
NOTES_TO_DISCS_UNNAMED = [
  '"minecraft:music_disc_13"',  # Silence
  '"minecraft:music_disc_cat"',
  '"minecraft:music_disc_blocks"',
  '"minecraft:music_disc_chirp"',
  '"minecraft:music_disc_far"',
  '"minecraft:music_disc_mall"',
  '"minecraft:music_disc_mellohi"',
  '"minecraft:music_disc_stal"',
  '"minecraft:music_disc_strad"',
  '"minecraft:music_disc_ward"',
  '"minecraft:music_disc_11"',
  '"minecraft:music_disc_wait"',
  '"minecraft:music_disc_pigstep"',
  '"minecraft:music_disc_otherside"',
]

# DO NOT EDIT
# List of music discs in order, but named
NOTES_TO_DISCS_NAMED = [
  '"minecraft:music_disc_13",tag:{display:{Name:\'{"text":"Silence"}\'}}', # Silence
  '"minecraft:music_disc_cat",tag:{display:{Name:\'{"text":"F#"}\'}}',
  '"minecraft:music_disc_blocks",tag:{display:{Name:\'{"text":"G"}\'}}',
  '"minecraft:music_disc_chirp",tag:{display:{Name:\'{"text":"G#"}\'}}',
  '"minecraft:music_disc_far",tag:{display:{Name:\'{"text":"A"}\'}}',
  '"minecraft:music_disc_mall",tag:{display:{Name:\'{"text":"A#"}\'}}',
  '"minecraft:music_disc_mellohi",tag:{display:{Name:\'{"text":"B"}\'}}',
  '"minecraft:music_disc_stal",tag:{display:{Name:\'{"text":"C"}\'}}',
  '"minecraft:music_disc_strad",tag:{display:{Name:\'{"text":"C#"}\'}}',
  '"minecraft:music_disc_ward",tag:{display:{Name:\'{"text":"D"}\'}}',
  '"minecraft:music_disc_11",tag:{display:{Name:\'{"text":"D#"}\'}}',
  '"minecraft:music_disc_wait",tag:{display:{Name:\'{"text":"E"}\'}}',
  '"minecraft:music_disc_pigstep",tag:{display:{Name:\'{"text":"F"}\'}}',
  '"minecraft:music_disc_otherside",tag:{display:{Name:\'{"text":"F#"}\'}}',
]

# DO NOT EDIT
# List of music discs in order, but obtainable in survival 
NOTES_TO_DISCS_SURVIVAL = [
  '"minecraft:shears"',   # Silence
  '"minecraft:music_disc_13"',
  '"minecraft:music_disc_cat"',
  '"minecraft:music_disc_blocks"',
  '"minecraft:music_disc_chirp"',
  '"minecraft:music_disc_far"',
  '"minecraft:music_disc_mall"',
  '"minecraft:music_disc_mellohi"',
  '"minecraft:music_disc_stal"',
  '"minecraft:music_disc_strad"',
  '"minecraft:music_disc_ward"',
  '"minecraft:music_disc_11"',
  '"minecraft:music_disc_wait"',
  '"minecraft:potion"',
]

COLORED_SHULKER_BOXES = [
  '"minecraft:black_shulker_box"',
  '"minecraft:blue_shulker_box"',
  '"minecraft:brown_shulker_box"',
  '"minecraft:cyan_shulker_box"',
  '"minecraft:gray_shulker_box"',
  '"minecraft:green_shulker_box"',
  '"minecraft:light_blue_shulker_box"',
  '"minecraft:light_gray_shulker_box"',
  '"minecraft:lime_shulker_box"',
  '"minecraft:magenta_shulker_box"',
  '"minecraft:orange_shulker_box"',
  '"minecraft:pink_shulker_box"',
  '"minecraft:purple_shulker_box"',
  '"minecraft:red_shulker_box"',
  '"minecraft:shulker_box"',
  '"minecraft:white_shulker_box"',
  '"minecraft:yellow_shulker_box"',
]
