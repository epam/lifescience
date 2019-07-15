Research and Development
========================

..  raw:: html

    <link rel="stylesheet" href="../_static/css/bio-custom.css"/>


Unique optimization of isosurface rendering algorithm
-----------------------------------------------------

Sergey Belyaev, Pavel Smirnov, Vladislav Shubnikov and Natalia Smirnova,
*"An Adaptive Algorithm for Accelerating Direct Isosurface Rendering on GPU"*,
JOURNAL OF ELECTRONIC SCIENCE AND TECHNOLOGY.


Approach
~~~~~~~~

One of the methods for medical data visualization is direct isosurface volume rendering. It is based on the search of
the intersection points between the rays corresponding to pixels on the screen and the isosurface. This article
describes a two-pass algorithm for accelerating the runtime of this method on a GPU. On the first pass, it finds the
intersections with the isosurface only for a small number of rays; it works by rendering into a lower-resolution
texture. On the second pass, the algorithm uses the obtained information to efficiently calculate the intersection
points of all the rays when rendering into the frame buffer.

..  image:: ../assets/mri/mri-adapt.png
    :align: center


Result
~~~~~~

New approach allows **to significantly speed up isosuface visualization without quality loss**
(depends on data being visualized, 6 to 12 times for the optimal texture resolution ratio).
