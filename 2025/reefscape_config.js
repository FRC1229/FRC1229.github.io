var config_data = `
{
  "dataFormat": "tsv",
  "title": "Scouting PASS 2025",
  "page_title": "REEFSCAPE",
  "checkboxAs": "10",
  "prematch": [
    { "name": "Team #",
      "code": "t",
      "type": "number",
      "min": 1,
      "max": 99999
    },
    { "name": "Scouter Initials",
      "code": "s",
      "type": "scouter",
      "size": 5,
      "maxSize": 5,
      "required": "true"
    },
    
    { "name": "Not Important",
      "code": "e",
      "type": "event",
      "defaultValue": "Not Important",
      "required": "true"
    },
    { "name": "Not Important",
      "code": "l",
      "type": "level",
      "choices": {
        "Not Important": ""
      },
      "defaultValue": "Not Important",
      "required": "true"
    },
    { "name": "Match #",
      "code": "m",
      "type": "number",
      "min": 1,
      "max": 150,
      "required": "true"
    },
    { "name": "Robot",
      "code": "r",
      "type": "robot",
      "choices": {
        "r1": "Red-1",
        "b1": "Blue-1<br>",
        "r2": "Red-2",
        "b2": "Blue-2<br>",
        "r3": "Red-3",
        "b3": "Blue-3"
      },
      "required":"true"
    },
    { "name": "Not Important",
      "code": "r",
      "type": "no",
      "choices": {
        "Not Important": ""
      },
      "defaultValue": "Not Important",
      "required":"true"
    }
  ],
  "auton": [
    { "name": "Starting Position",
  "code": "asp",
  "type": "radio",
  "choices": {
    "f": "far",
    "m": "mid",
    "c": "close"
  },
  "defaultValue": "a"
},
    { "name": "Coral L1",
      "code": "ac1",
      "type": "counter"
    },
    { "name": "Coral L2",
      "code": "ac2",
      "type": "counter"
    },
    { "name": "Coral L3",
      "code": "ac3",
      "type": "counter"
    },
    { "name": "Coral L4",
      "code": "ac4",
      "type": "counter"
    },
    {
    "name": "Leave",
    "code": "alc",
    "type": "checkbox"
    },
    { "name": "Remove Algae #",
      "code": "ara",
      "type": "counter"
    },
    { "name": "Failed Algae #",
      "code": "afa",
      "type": "counter"
    }
  ],
  "teleop": [
    { "name": "Coral L1",
      "code": "tc1",
      "type": "counter"
    },
    { "name": "Coral L2",
      "code": "tc2",
      "type": "counter"
    },
    { "name": "Coral L3",
      "code": "tc3",
      "type": "counter"
    },
    { "name": "Coral L4",
      "code": "tc4",
      "type": "counter"
    },
    {
    "name": "Able to remove algae",
    "code": "tra",
    "type": "checkbox"
    },
    {
    "name": "Attained Coopertition",
    "code": "tac",
    "type": "checkbox"
    },
    { "name": "Processor Score",
      "code": "tps",
      "type": "counter"
    },
    { "name": "Net Score",
      "code": "tns",
      "type": "counter"
    },
    { "name": "Miss #",
      "code": "tmn",
      "type": "counter"
    },
    { "name": "Defense Slider",
      "code": "tds",
      "type": "radio",
      "choices": {
        "n": "none",
        "b": "bad",
        "g": "good"
      },
      "required":"true"
    }
  ],
  "endgame": [
    { "name": "Final Robot Status",
      "code": "efs",
      "type":"radio",
      "choices": {
        "bp": "Parked<br>",
        "ba": "Parked/Failed Climb<br>",
        "bs": "Shallow Cage<br>",
        "bd": "Deep Cage<br>",
        "x": "Not attempted"
      },
      "defaultValue": "x"
    },
    { "name": "Comments",
      "code": "ce",
      "type": "text",
      "size": 15,
      "maxSize": 55,
      "defaultValue": "x"
    }
  ],
  "postmatch": [
    { "name": "Algae Left in Reef",
      "code": "alr",
      "type": "number",
      "min": 0,
      "max": 9,
      "defaultValue": 0
    },
    { "name": "Driver Skill",
      "code": "ds",
      "type": "radio",
      "choices": {
        "n": "Not Effective<br>",
        "a": "Average<br>",
        "v": "Very Effective<br>",
        "x": "Not Observed"
      },
      "defaultValue": "x"
    },
    { "name": "Defense Rating",
      "code": "dr",
      "type": "radio",
      "choices": {
        "b": "Below Average<br>",
        "a": "Average<br>",
        "g": "Good<br>",
        "e": "Excellent<br>",
        "x": "Did not play defense"
      }
    },
    { "name": "Speed Rating",
      "code": "sr",
      "type": "radio",
      "choices": {
        "1": "1 (slow)<br>",
        "2": "2<br>",
        "3": "3<br>",
        "4": "4<br>",
        "5": "5 (fast)"
      }
    },
    { "name": "Died/Immobilized",
      "code": "die",
      "type": "bool"
    },
    { "name": "Tippy<br>(almost tipped over)",
      "code": "tip",
      "type": "bool"
    },
    { "name": "Dropped Coral (>2)",
      "code": "dc",
      "type": "bool"
    },
    { "name": "Dropped Algae (>2)",
      "code": "da",
      "type": "bool"
    },
    { "name": "Comments",
      "code": "co",
      "type": "text",
      "size": 15,
      "maxSize": 55,
      "defaultValue": "x"
    }
  ]
}`;
