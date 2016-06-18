GENDER = {
    "male": ["male", "men"],
    "female": ["female", "women"],
    "mixed": ["mixed"]
}

REVERSED_GENDER = {
    k:primary_key for primary_key, keywords in GENDER.items() for k in keywords
}

# men, women, mixed
# team, individual
# meters, kilometers, kg
# steeplechase, relay, hurdles, decathalon, discus throw, high jump, discus throw, javelin throw, long jump, marathon, pole vault, shot put, triple jump
# doubles, singles
# bantam, fly, heavy, light
# keirin, omnium
# backstroke, breaststroke, butterfly, freestyle, marathon

DISCIPLINES = {
    "AR": ["archery"],
    "GA": ["artistic gymnastics"],
    "AT": ["track and field", "athletics"],
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

REVERSED_DISCIPLINES = {
    k:primary_key for primary_key, keywords in DISCIPLINES.items() for k in keywords
}