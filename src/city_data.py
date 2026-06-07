graph = {
    "Airport": [
        ("BusStation", 4),
        ("Mall", 2)
    ],

    "BusStation": [
        ("Airport", 4),
        ("RailwayStation", 5)
    ],

    "Mall": [
        ("Airport", 2),
        ("RailwayStation", 8),
        ("University", 10)
    ],

    "RailwayStation": [
        ("BusStation", 5),
        ("Mall", 8),
        ("University", 2)
    ],

    "University": [
        ("Mall", 10),
        ("RailwayStation", 2)
    ]
}