############
APIs
############

.. contents::

home
====

.. automodule:: api.views.home
    :members:
    :private-members:
    :special-members:
    :exclude-members:

.. code-block:: rest

    GET http://<domain>/api/

.. code-block:: json

    {
      "title": "This is Ads On The Run API!",
      "selections": {
        "age": {
          "0": "age0_18",
          "1": "age19_35",
          "2": "age36_55",
          "3": "age56_102"
        },
        "income": {
          "0": "low_income",
          "1": "medium_income",
          "2": "high_income"
        },
        "amenity": {
          "0": "shoes",
          "1": "restaurant",
          "2": "gym",
          "3": "clothes",
          "4": "clinic"
        }
      }
    }

filter
======

.. automodule:: api.views.filter_zip_code
    :members:
    :private-members:
    :special-members:
    :exclude-members:

.. code-block:: rest

    GET http://<domain>/api/filter/<age_range>/<income>/<amenity>/

.. code-block:: json

    {
      "input": [
        "age0_18",
        "low_income",
        "shoes"
      ],
      "top5_zip_code": [
        11220,
        11219,
        11226,
        10032,
        11204
      ],
      "kiosk_lat_lon": [
        [40.63855960867835, -73.95360323811154],
        [40.640666226209724, -73.95592438608668],
        [40.650962, -73.947834],
        [40.8303356348897, -73.94375597248471],
        [40.83074624175121, -73.9434459405358],
        [40.832283000000004, -73.942327]
      ]
    }

kiosk
=====

.. automodule:: api.views.kiosk_zip_code
    :members:
    :private-members:
    :special-members:
    :exclude-members:

.. code-block:: rest

    GET http://<domain>/api/kiosk/<zip_code>/

.. code-block:: json

    {
      "zip_code": "10027",
      "same_cluster_zip_code": [
        11201, 11210, 11215, 10128, 10003,
        10009, 11225, 10011, 10016, 10023,
        10024, 11691, 10031, 10032, 10033
      ],
      "kiosk_lat_lon": [
        [40.688851, -73.980613],
        [40.689026, -73.980862],
        [40.68844943, -73.98247226],
        [40.632134775181385, -73.94678067381743],
        [40.664176, -73.990353],
        [40.665618, -73.989159],
        [40.66355007, -73.99124562],
        [40.779635, -73.953537],
        [40.780782, -73.9524],
        [40.781503, -73.952279],
        [40.72357993, -73.98839009999999],
        [40.72380705, -73.98822418],
        [40.72779351, -73.98532503],
        [40.730496, -73.98076800000001],
        ["..."],
      ]
    }

sports
======

.. automodule:: api.views.sports_detail
    :members:
    :private-members:
    :special-members:
    :exclude-members:

.. code-block:: rest

    GET http://<domain>/api/sports/<zip_code>/

.. code-block:: json

    {
      "input": "10027",
      "val": [
        "Basketball",
        "Football",
        "Soccer",
        "Baseball, softball",
        "Dancing"
      ]
    }

