################################################
Reaction Products Enumeration and Transformation
################################################

.. code::
    :name: rpe-run-and-render
    :hidden:
    
    def loadSdf (sdf_path):
      sdfiterator = indigo.iterateSDFile(sdf_path)
      result = [m.clone() for m in sdfiterator]
      sdfiterator.dispose()
      return result
    
    def performReaction (reaction, mons) :
       indigo.setOption("render-comment", "Input reaction")
       indigoRenderer.renderToFile(reaction, 'result_reaction.png')
       
       indigo.setOption("render-grid-margins", "20, 10")
       indigo.setOption("render-grid-title-offset", "5")
       indigo.setOption("render-grid-title-property", "grid-comment")
       #indigo.setOption("render-comment", "grid-comment")

       idx = 0
       for rct_mons in mons:
          mon_array = indigo.createArray();
          
          alph_idx = 0
          for mon in rct_mons:
              mon.setName(chr(ord('A') + idx) + chr(ord('1') + alph_idx))
              mon.setProperty("grid-comment", mon.name())
              mon_array.arrayAdd(mon)
              alph_idx += 1
              
          idx += 1
          indigo.setOption("render-comment", 'Input monomers for reactant %d' % (idx))
          indigoRenderer.renderGridToFile(mon_array, None, 3, 'result_monomers_%d.png' % (idx))
       
       rpe_reactions = indigo.reactionProductEnumerate(reaction, mons) 
       
       indigo.setOption("render-comment", "Results")
       rxn_array = indigo.createArray();
       for elem in rpe_reactions.iterateArray():
           rxn = elem.clone();
           rxn.setProperty("grid-comment", rxn.name())
           rxn_array.arrayAdd(rxn)
           
       indigoRenderer.renderGridToFile(rxn_array, None, 2, 'result_%d.png' % (idx))


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
    
.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :includecode: rpe-run-and-render
    
    reaction = indigo.loadQueryReactionFromFile('data/rpe/multistep/reaction.rxn')
        
    m1 = loadSdf('data/rpe/multistep/mons1.sdf')
    m2 = loadSdf('data/rpe/multistep/mons2.sdf')
    
    mons = []
    mons.append(m1)
    mons.append(m2)
    
    indigo.setOption("rpe-multistep-reactions", "1")
    indigo.setOption("rpe-max-depth", "2")
    
    performReaction(reaction, mons)

.. indigo_option::
    :name: rpe-mode
    :type: enum (grid, one-tube)
    :default: grid
    :short: Monomers mixing mode

    **grid:**
        different sets of monomers react in different tubes

    **one-tube:**
        reactions take place in one tube

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :includecode: rpe-run-and-render
    
   
    reaction = indigo.loadQueryReactionFromFile('data/rpe/mode/reaction.rxn')
    
    m1 = loadSdf('data/rpe/mode/mons1.sdf')
    m2 = loadSdf('data/rpe/mode/mons2.sdf')
    
    mons = []
    mons.append(m1)
    mons.append(m2)
   
    indigo.setOption("rpe-mode", "grid")
    indigo.setOption("rpe-max-depth", "1")
    
    performReaction(reaction, mons)
   
.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :includecode: rpe-run-and-render
    
           
    reaction = indigo.loadQueryReactionFromFile('data/rpe/mode/reaction.rxn')
    
    m1 = loadSdf('data/rpe/mode/mons1.sdf')
    m2 = loadSdf('data/rpe/mode/mons2.sdf')
    
    indigo.setOption("rpe-mode", "one-tube")
    indigo.setOption("rpe-max-depth", "1")
    
    mons = []
    mons.append(m1)
    mons.append(m2)
    
    performReaction(reaction, mons)
        

.. indigo_option::
    :name: rpe-self-reaction
    :type: boolean
    :default: false
    :short: Enable intramolecular reactions, where one molecule of monomers can play role of two (or more) reactants

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :includecode: rpe-run-and-render

    
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
