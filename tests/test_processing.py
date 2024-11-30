import pytest

from src.processing import filter_by_state,sort_by_date


@pytest.mark.parametrize(
    "input_data, state, expected_output",
    [
        ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], "EXECUTED",
         [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
        ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], "CANCELED",[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]),
        ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], "CANCELED",
         []),
    ],
)
def test_filter_by_state_with_agr(input_data, state, expected_output):
    assert filter_by_state(input_data,state) == expected_output


@pytest.mark.parametrize(
    "input_data, state, expected_output",
    [
        ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], None,
         [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),  # Результат для "EXECUTED"
        ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], "",
         [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),  # Результат для "EXECUTED"
        ([{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], "",
         []),

    ]
)
def test_filter_by_state_without_arg(input_data, state, expected_output):
    assert filter_by_state(input_data, state) == expected_output


@pytest.mark.parametrize(
    "input_data, sort_by, expected_output",
    [
        ([{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
, "ACS",
         [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
),

        ([{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
         , "DESC",
         [{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

         ),

    ],
)
def test_sort_by_date_with_arg(input_data, sort_by, expected_output):
    assert sort_by_date(input_data, sort_by) == expected_output


@pytest.mark.parametrize(
    "input_data, sort_by, expected_output",
    [
        ([{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
, "",
         [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
),

        ([{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
         , None,
         [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
         ),
        ([{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
         ,"Abracadabra",
         [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
         ),

    ],
)
def test_sort_by_date_without_arg(input_data, sort_by, expected_output):
    assert sort_by_date(input_data, sort_by) == expected_output


@pytest.mark.parametrize("input_data", ([{'id': 939719570, 'state': 'EXECUTED', 'date': '18-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
))
def test_incorrect_date(input_data):
    with pytest.raises(TypeError):
        sort_by_date(input_data)
