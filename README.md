The datatset used for the project was acquired using a web scraping script for AllRecipes.com, modified by Dr. Jennifer Chang. The repo can be found at <a href="https://github.com/j23414/allrecipes">https://github.com/j23414/allrecipes</a>.

---

<h1>Using phylogenetic methods to investigate the relation between non-genetic based entities: Brief and overly simplistic overview</h1>

<h2>Hypotheses</h2>
Phylogenetic methods can be used to uncover the evolutionary relation between non-genetic entities that share a common ancestor.

<h2>Data</h2>
Any data source that has decomposed the relationship between related objects into a set of discretized/continuous traits can be used. A caveat is that prior knowledge is needed to know if the objects are related from a common ancestor, and if they evolve in a tree like fashion. An additional problem that makes phylogenetic concepts harder to apply to ideas, is that ideas are highly susceptible to horizontal transfer, thus making phylogenetic networks a more appropriate representation.

A few datasets currently exist to this end. Language has been a particular subject of phylogenetic methods, with multiple groups using Bayesian methods to attempt to relate languages based on cognates (1-2). 

Other prior datasets exist related to music, although the journals hosting the articles do not seem as likely to have datasets readily available for follow-up (3).  

One additional dataset may be created based on a cultural aspect. An example of this would be food, where dishes of common origin would be expected to cluster due to use regional ingredients.

<h2>Proposed Methods</h2>

<h3>Testing for hierarchy (treeness)</h3>
The datasets would need to be tested to see how much horizontal transfer occurs. This can be done using SPLITSTREE4 (3). This will give an early indication of how likely tree methods are to work, and can potentially explain errors. In example, two dishes that are very foreign may have converged despite distance from each other. A simple explanation for why this might happen is that there is only so many ways you can fry a chicken.

<h3>Applying parsimony methods to states</h3>
Character states for the taxa can be appropriately formatted, and will be processed using TNT. 

<h3>Using distance methods</h3>
A distance metric would need to be designed to represent how different multiple characters are from each other. After calculating the pairwise distances between all traits, R has a couple of different packages that can build a tree directly from the distance matrix. 

<h3>Maximum likelylihood methods</h3>
Additional research into using maximum likelihood methods for non-genetic trees would need to be researched, and potentially new software written. Although software exists to handle Bayesian analysis on non-genetic data, the complexity of the method makes it difficult gauge the effectiveness in regards to other methods.

<h3>Comparison of methods to know ground truth</h3>
The implementation of each method will be scored based on how close the tree resembles what is believed to be the ground truth. Although some methods may not work as well, it may be implementation dependent and should not be accepted as the end all result.

<h2>References</h2>
<small>
<ol>
<li>Gray, R. D., Drummond, A. J., & Greenhill, S. J. (2009). Language phylogenies reveal expansion pulses and pauses in Pacific settlement. science, 323(5913), 479-483.</li>
<li>Bouckaert, R., Lemey, P., Dunn, M., Greenhill, S. J., Alekseyenko, A. V., Drummond, A. J., ... & Atkinson, Q. D. (2012). Mapping the origins and expansion of the Indo-European language family. Science, 337(6097), 957-960.</li>
<li>Le Bomin, S., Lecointre, G., & Heyer, E. (2016). The evolution of musical diversity: the key role of vertical transmission. PloS one, 11(3), e0151570</li>
</ol>
</small>


