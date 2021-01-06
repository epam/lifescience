################################################
Reaction Products Enumeration and Transformation
################################################


.. indigo_option::
    :name: rpe-max-depth
    :type: int
    :default: 2
    :short: Maximum level of representing product like a monomer (works only with ``rpe-multistep-reactions enabled``).

.. indigo_option::
    :name: rpe-multistep-reactions
    :type: boolean
    :default: false
    :short: Enable multistep reactions (Products of the reaction can take part in further reactions)
    
.. code-block:: python
    
    reaction = indigo.loadQueryReactionFromFile('data/rpe/multistep/reaction.rxn')
        
    m1 = loadSdf('data/rpe/multistep/mons1.sdf')
    m2 = loadSdf('data/rpe/multistep/mons2.sdf')
    
    mons = []
    mons.append(m1)
    mons.append(m2)
    
    indigo.setOption("rpe-multistep-reactions", "1")
    indigo.setOption("rpe-max-depth", "2")
    
    performReaction(reaction, mons)

.. image:: ../../assets/indigo/render/indigorenderer_1a61f4d79f7235f339f19077ab30d5f4991ee7fareaction.svg
    :scale: 25

.. image:: ../../assets/indigo/render/indigorenderer_1a61f4d79f7235f339f19077ab30d5f4991ee7famonomers_1.svg
    :scale: 25

.. image:: ../../assets/indigo/render/indigorenderer_1a61f4d79f7235f339f19077ab30d5f4991ee7famonomers_2.svg
    :scale: 25

.. image:: ../../assets/indigo/render/indigorenderer_1a61f4d79f7235f339f19077ab30d5f4991ee7fa2.svg
    :scale: 25

.. indigo_option::
    :name: rpe-mode
    :type: enum (grid, one-tube)
    :default: grid
    :short: Monomers mixing mode

    **grid:**
        different sets of monomers react in different tubes

    **one-tube:**
        reactions take place in one tube

.. code-block:: python

    reaction = indigo.loadQueryReactionFromFile('data/rpe/mode/reaction.rxn')
    
    m1 = loadSdf('data/rpe/mode/mons1.sdf')
    m2 = loadSdf('data/rpe/mode/mons2.sdf')
    
    mons = []
    mons.append(m1)
    mons.append(m2)
   
    indigo.setOption("rpe-mode", "grid")
    indigo.setOption("rpe-max-depth", "1")
    
    performReaction(reaction, mons)

.. image:: ../../assets/indigo/render/indigorenderer_7834e1712f1fb80a558b8e476aef20a9b6d77854reaction.svg
    :scale: 25

.. image:: ../../assets/indigo/render/indigorenderer_7834e1712f1fb80a558b8e476aef20a9b6d77854monomers_1.svg
    :scale: 25

.. image:: ../../assets/indigo/render/indigorenderer_7834e1712f1fb80a558b8e476aef20a9b6d77854monomers_2.svg
    :scale: 25

.. image:: ../../assets/indigo/render/indigorenderer_7834e1712f1fb80a558b8e476aef20a9b6d778542.svg
    :scale: 25
   
.. code-block:: python
       
    reaction = indigo.loadQueryReactionFromFile('data/rpe/mode/reaction.rxn')
    
    m1 = loadSdf('data/rpe/mode/mons1.sdf')
    m2 = loadSdf('data/rpe/mode/mons2.sdf')
    
    indigo.setOption("rpe-mode", "one-tube")
    indigo.setOption("rpe-max-depth", "1")
    
    mons = []
    mons.append(m1)
    mons.append(m2)
    
    performReaction(reaction, mons)

.. image:: ../../assets/indigo/render/indigorenderer_e429ea8e132ac97d7659820fd3a254ebb383d2a4reaction.svg
    :scale: 25

.. image:: ../../assets/indigo/render/indigorenderer_e429ea8e132ac97d7659820fd3a254ebb383d2a4monomers_1.svg
    :scale: 25

.. image:: ../../assets/indigo/render/indigorenderer_e429ea8e132ac97d7659820fd3a254ebb383d2a4monomers_2.svg
    :scale: 25

.. image:: ../../assets/indigo/render/indigorenderer_e429ea8e132ac97d7659820fd3a254ebb383d2a42.svg
    :scale: 25

.. indigo_option::
    :name: rpe-self-reaction
    :type: boolean
    :default: false
    :short: Enable intramolecular reactions, where one molecule of monomers can play role of two (or more) reactants

.. code-block:: python

    reaction = indigo.loadQueryReactionFromFile('data/rpe/self_reaction/reaction.rxn')
    
    m1 = loadSdf('data/rpe/self_reaction/mons1.sdf')
    m2 = loadSdf('data/rpe/self_reaction/mons2.sdf')
    
    indigo.setOption("rpe-mode", "one-tube")
    indigo.setOption("rpe-self-reaction", "1")
    indigo.setOption("rpe-max-depth", "1")
    
    mons = []
    mons.append(m1)
    mons.append(m2)
    
    performReaction(reaction, mons)

.. image:: ../../assets/indigo/render/indigorenderer_c1233cd3aa11ecd6fef27d2aa4434a4a96d964d8reaction.svg
    :scale: 25

.. image:: ../../assets/indigo/render/indigorenderer_c1233cd3aa11ecd6fef27d2aa4434a4a96d964d8monomers_1.svg
    :scale: 25

.. image:: ../../assets/indigo/render/indigorenderer_c1233cd3aa11ecd6fef27d2aa4434a4a96d964d8monomers_2.svg
    :scale: 25

.. image:: ../../assets/indigo/render/indigorenderer_c1233cd3aa11ecd6fef27d2aa4434a4a96d964d82.svg
    :scale: 25

.. indigo_option::
    :name: rpe-max-products-count
    :type: int
    :default: 1000
    :short: Maximum amount of generated products.

.. indigo_option::
    :name: rpe-layout
    :type: boolean
    :default: true
    :short: Enable layout after product enumeration
    
.. indigo_option::
    :name: transform-layout
    :type: boolean
    :default: true
    :short: Enable layout after transformation.
