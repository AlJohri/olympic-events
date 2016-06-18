def reverse_dict(d):
    return {k:primary_key for primary_key, keywords in d.items() for k in keywords}

MALE_GENDER = ["male", "men", "man"]
FEMALE_GENDER = ["female", "women", "woman"]
MIXED_GENDER = ["mixed"]

GENDER = {
    "men": [x+"'s" for x in MALE_GENDER] + MALE_GENDER,
    "women": [x+"'s" for x in FEMALE_GENDER] + FEMALE_GENDER,
    "mixed": MIXED_GENDER,
}

# [r"(?<!wo)man", r"(?<!wo)men"]

# men, women, mixed
# team, individual
# meters, kilometers, kg
# doubles, singles
# bantam, fly, heavy, light
# keirin, omnium
# backstroke, breaststroke, butterfly, freestyle, marathon

DISCIPLINES = {
    "AR": ["archery"],
    "GA": ["artistic gymnastics"],
    "AT": ["athletics", "track and field"],
    "BD": ["badminton"],
    "BK": ["basketball"],
    "BV": ["beach volleyball"],
    "BX": ["boxing"],
    "CS": ["canoe slalom"],
    "CF": ["canoe sprint"],
    "CB": ["cycling bmx"],
    "CM": ["cycling mountain bike"],
    "CR": ["cycling road"],
    "CT": ["cycling track"],
    "DV": ["diving"],
    "EQ": ["equestrian"],
    "FE": ["fencing"],
    "FB": ["football"],
    "GO": ["golf"],
    "HB": ["handball"],
    "HO": ["hockey"],
    "JU": ["judo"],
    "OW": ["marathon swimming"],
    "MP": ["modern pentathlon"],
    "GR": ["rhythmic gymnastics"],
    "RO": ["rowing"],
    "RU": ["rugby"],
    "SA": ["sailing"],
    "SH": ["shooting"],
    "SW": ["swimming"],
    "SY": ["synchronised swimming"],
    "TT": ["table tennis"],
    "TK": ["taekwondo"],
    "TE": ["tennis"],
    "GT": ["trampoline gymnastics"],
    "TR": ["triathlon"],
    "VO": ["volleyball"],
    "WP": ["water polo"],
    "WL": ["weightlifting"],
    "WR": ["wrestling"],
}

SWIM_EVENTS = {
    "backstroke": ["backstroke"],
    "breaststroke": ["breaststroke"],
    "butterfly": ["butterfly"],
    "freestyle": ["freestyle"],
}

EQUESTRIAN_EVENTS = {
    "dressage": ["dressage"],
    "eventing": ["eventing"],
    "jumping": ["jumping"],
}

TRACK_EVENTS = {
    "hurdles": ["hurdles"],
    "steeplechase": ["steeplechase"],
    "relay": ["relay"],
    "high jump": ["high jump"],
    "long jump": ["long jump"],
    "triple jump": ["triple jump"],
    "javelin throw": ["javelin throw"],
    "decathlon": ["decathlon"],
    "heptathalon": ["heptathalon"],
    "discus throw": ["discus throw"],
    "hammer throw": ["hammer throw"],
    "marathon": ["marathon"],
    "pole vault": ["pole vault"],
    "shot put": ["shot put"],
}

DOUBLES_VS_SINGLES = {
    "doubles": ["doubles", "double"],
    "singles": ["singles", "single"],
}

INDIVIDUAL_VS_TEAM = {
    "individual": ["individual"],
    "team": ["team"],
}
