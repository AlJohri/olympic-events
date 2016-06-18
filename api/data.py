def reverse_dict(d):
    return {k:primary_key for primary_key, keywords in d.items() for k in keywords}

GENDERS = {
    "MEN": ["male's", "men's", "man's", "male", "men", "man"],
    "WOMEN": ["female's", "women's", "woman's", "female", "women", "woman"],
    "MIXED": ["mixed"],
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
    "ARCHERY": ["archery"],
    "GYMNASTICS_ARTISTIC": ["artistic gymnastics"],
    "TRACK_AND_FIELD": ["athletics", "track and field", "track"],
    "BADMINTON": ["badminton"],
    "BASKETBALL": ["basketball"],
    "BEACH_VOLLEYBALL": ["beach volleyball"],
    "BOXING": ["boxing"],
    "CANOE_SLALOM": ["canoe slalom"],
    "CANOE_SPRINT": ["canoe sprint"],
    "CYCLING_BMX": ["cycling bmx", "bmx"],
    "CYCLING_MOUNTAIN_BIKE": ["cycling mountain bike", "mountain"],
    "CYCLING_ROAD": ["cycling road"],
    "CYCLING_TRACK": ["cycling track"],
    "DIVING": ["diving"],
    "EQUESTRIAN": ["equestrian"],
    "FENCING": ["fencing"],
    "SOCCER": ["football", "soccer"],
    "GOLF": ["golf"],
    "HANDBALL": ["handball"],
    "FIELD_HOCKEY": ["field hockey", "hockey"],
    "JUDO": ["judo"],
    "MARATHON_SWIMMING": ["marathon swimming"],
    "MODERN_PENTATHALON": ["modern pentathlon"],
    "GYMNASTICS)RYTHMIC": ["rhythmic gymnastics"],
    "ROWING": ["rowing"],
    "RUGBY": ["rugby"],
    "SAILING": ["sailing"],
    "SHOOTING": ["shooting"],
    "SWIWMMING": ["swimming"],
    "SYNCHRONIZED_SWIMMING": ["synchronised swimming", "synchronized swimming"],
    "TABLE_TENNIS": ["table tennis", "ping pong"],
    "TAEKWONDO": ["taekwondo"],
    "TENNIS": ["tennis"],
    "GYMNASTICS_TRAMPOLINE": ["trampoline gymnastics"],
    "TRIATHALON": ["triathlon"],
    "VOLLEYBALL": ["volleyball"],
    "WATER_POLO": ["water polo"],
    "WEIGHTLIFTING": ["weightlifting"],
    "WRESTLING": ["wrestling"],
}

SWIM_EVENTS = {
    "BACKSTROKE": ["backstroke"],
    "BREASTSTROKE": ["breaststroke"],
    "BUTTERFLY": ["butterfly"],
    "FREESTYLE": ["freestyle"],
}

EQUESTRIAN_EVENTS = {
    "DRESSAGE": ["dressage"],
    "EVENTING": ["eventing"],
    "JUMPING": ["jumping"],
}

TRACK_EVENTS = {
    "HURDLES": ["hurdle", "hurdles"],
    "STEEPLECHASE": ["steeplechase"],
    "RELAY": ["relay"],
    "HIGH_JUMP": ["high jump"],
    "LONG_JUMP": ["long jump"],
    "TRIPLE_JUMP": ["triple jump"],
    "JAVELIN_THROW": ["javelin"],
    "DECATHLON": ["decathlon"],
    "HEPTATHLON": ["heptathlon"],
    "DISCUS_THROW": ["discus"],
    "HAMMER_THROW": ["hammer"],
    "MARATHON": ["marathon"],
    "POLE_VAULT": ["pole vault"],
    "SHOT_PUT": ["shot put"],
}

DOUBLES_VS_SINGLES = {
    "DOUBLES": ["doubles", "double"],
    "SINGLES": ["singles", "single"],
}

INDIVIDUAL_VS_TEAM = {
    "INDIVIDUAL": ["individual"],
    "TEAM": ["team"],
}
