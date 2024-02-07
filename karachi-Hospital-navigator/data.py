hospitals = [
    'dow_hospital',
    'universal_pharmacy',
    'darul_sehat_hospital',
    'pob_eye_hospital',
    'dow_dental_hospital'
]


graph = {
    "dow_hospital": {
        "mosamiyat": 2
    },
    "johar_block_7": {
        "mosamiyat": 6,
        "safoora": 8
    },
    "mosamiyat": {
        "dow_hospital": 2,
        "johar_block_7": 6,
        "safoora": 9,
        "sheikh_zayed_college": 3,
        "johar_block_10": 5,
        "johar_block_4": 1,
        "johar_block_5": 4,
        "kamran_chowrangi": 8
    },
    "safoora": {
        "johar_block_7": 8,
        "mosamiyat": 9,
        "memon_hospital": 4,
        "check_post_5": 5,
        "check_post_6": 7,
        "universal_pharmacy": 6
    },
    "memon_hospital": {
        "safoora": 4
    },
    "check_post_5": {
        "safoora": 2,
        "check_post_6": 6
    },
    "check_post_6": {
        "universal_pharmacy": 7,
        "check_post_5": 3,
        "safoora": 6
    },
    "universal_pharmacy": {
        "safoora": 6,
        "check_post_6": 7
    },
    "sheikh_zayed_college": {
        "karachi_university": 2,
        "university_road": 1,
        "mosamiyat": 3
    },
    "karachi_university": {
        "sheikh_zayed_college": 2,
        "ned_university": 3,
        "university_road": 1
    },
    "ned_university": {
        "samama": 3,
        "karachi_university": 2,
        "dow_dental_hospital": 4,
        "university_road": 1
    },
    "samama": {
        "johar_block_15": 6,
        "johar_block_16": 5,
        "johar_block_1": 2,
        "johar_chowrangi": 9,
        "ned_university": 3,
        "university_road": 1
    },
    "dow_dental_hospital": {
        "ned_university": 3,
        "johar_block_1": 2,
        "university_road": 1
    },
    "university_road": {
        "karachi_university": 2,
        "ned_university": 1,
        "samama": 3,
        "sheikh_zayed_college": 4,
        "dow_dental_hospital": 5,
        "johar_block_1": 6,
        "johar_block_2": 7,
        "johar_block_4": 8
    },
    "johar_block_1": {
        "samama": 3,
        "johar_block_2": 2,
        "university_road": 1,
        "dow_dental_hospital": 4
    },
    "johar_block_2": {
        "johar_block_1": 3,
        "university_road": 1,
        "johar_block_4": 2,
        "johar_block_3": 5
    },
    "johar_block_4": {
        "johar_block_2": 2,
        "university_road": 1,
        "mosamiyat": 3,
        "kamran_chowrangi": 6
    },
    "johar_block_5": {
        "kamran_chowrangi": 7,
        "mosamiyat": 4,
        "johar_block_6": 5,
        "johar_block_10": 3
    },
    "johar_block_6": {
        "johar_block_5": 2
    },
    "johar_block_10": {
        "johar_block_5": 4,
        "mosamiyat": 5,
        "kamran_chowrangi": 3
    },
    "kamran_chowrangi": {
        "johar_block_5": 7,
        "johar_block_4": 6,
        "johar_block_10": 3,
        "mosamiyat": 8,
        "munawar_chowrangi": 10
    },
    "munawar_chowrangi": {
        "rado_bakery": 2,
        "johar_block_3": 4,
        "johar_block_14": 5,
        "pob_eye_hospital": 3,
        "kamran_chowrangi": 10
    },
    "pob_eye_hospital": {
        "munawar_chowrangi": 3
    },
    "johar_block_3": {
        "johar_block_2": 5,
        "munawar_chowrangi": 4
    },
    "rado_bakery": {
        "johar_block_14": 3,
        "munawar_chowrangi": 4,
        "darul_sehat_hospital": 3
    },
    "johar_block_14": {
        "johar_block_15": 2,
        "darul_sehat_hospital": 3,
        "rado_bakery": 4,
        "pob_eye_hospital": 5
    },
    "darul_sehat_hospital": {
        "johar_block_14": 3,
        "johar_block_15": 4,
        "johar_chowrangi": 2,
        "rado_bakery": 1
    },
    "johar_chowrangi": {
        "darul_sehat_hospital": 2,
        "johar_block_13": 6,
        "johar_block_15": 4,
        "johar_block_16": 5,
        "johar_block_17": 1,
        "johar_block_18": 3,
        "samama": 9,
        "habib_university": 7
    },
    "johar_block_13": {
        "habib_university": 4,
        "johar_chowrangi": 3
    },
    "johar_block_18": {
        "johar_chowrangi": 3,
        "habib_university": 4
    },
    "johar_block_9": {
        "habib_university": 9
    },
    "habib_university": {
        "johar_block_9": 9,
        "johar_block_13": 5,
        "johar_block_18": 4,
        "johar_chowrangi": 7
    },
    "johar_block_15": {
        "johar_block_14": 3,
        "samama": 6,
        "darul_sehat_hospital": 5,
        "johar_chowrangi": 4
    },
    "johar_block_16": {
        "johar_block_17": 4,
        "samama": 6,
        "johar_chowrangi": 5
    },
    "johar_block_17": {
        "johar_block_16": 3,
        "johar_chowrangi": 4
    }
}
