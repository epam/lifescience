##############
Layout options
##############

.. indigo_option::
    :name: layout-max-iterations
    :type: int
    :default: 0
    :short: The maximum number of iterations allowed for the layout procedure to run

    The maximum number of iterations allowed for the layout procedure to run (the number is internally multiplied by 10000). If the limit is reached, an exception is thrown. Zero value means no limit.


.. indigo_option::
    :name: smart-layout
    :type: boolean
    :default: false
    :short: whether to use "smart" layout or "simple"

    "Smart" layout is some slower then "simple" but much better. See exsamples.


